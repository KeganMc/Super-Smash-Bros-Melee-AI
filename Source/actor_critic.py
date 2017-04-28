import tensorflow as tf
import numpy as np

class ActorCriticNetwork(object):
	def __init__(self, act_size, opt, global_ep_tensor, summary_writer):
		self.state = tf.placeholder(tf.float32, [None, 1, 78])
		self.action_size = act_size
		self.optimizer = opt
		self.global_episodes = global_ep_tensor
		self.summary_writer = summary_writer
		self.fc1, self.fc1_b = self.fc_layer([78, 128])
		self.fc2, self.fc2_b = self.fc_layer([128, 128])
		self.fc3, self.fc3_b = self.fc_layer([128, act_size])
		self.fc4, self.fc4_b = self.fc_layer([128, 1])
		h_fc1 = tf.nn.relu(tf.matmul(tf.reshape(self.state, [-1, 78]), self.fc1) + self.fc1_b)
		h_fc2 = tf.nn.relu(tf.matmul(h_fc1, self.fc2) + self.fc2_b)
		h_fc3 = tf.nn.relu(tf.matmul(h_fc2, self.fc3) + self.fc3_b)
		self.policy_out = tf.nn.softmax(tf.nn.relu(tf.matmul(h_fc2, self.fc3) + self.fc3_b))
		val = tf.matmul(h_fc2, self.fc4) + self.fc4_b
		self.value = tf.reshape(val, [-1])

	def set_up_loss(self, entropy_var):
		self.a = tf.placeholder(tf.float32, [None, self.action_size])
		self.diff = tf.placeholder(tf.float32, [None])
		log_policy = tf.log(tf.clip_by_value(self.policy_out, 1e-15, 1.0))
		self.entropy = -tf.reduce_sum(self.policy_out * log_policy, reduction_indices=1)
		policy_loss = -tf.reduce_sum(tf.reduce_sum(tf.multiply(log_policy, self.a), reduction_indices=1) * self.diff + self.entropy * entropy_var)
		self.reward = tf.placeholder(tf.float32, [None])
		value_loss = 0.5 * tf.nn.l2_loss(self.reward - self.value)
		self.total_loss = policy_loss + value_loss
		self.gradients = tf.gradients(self.total_loss, self.get_vars())

	def set_up_apply_grads(self, learning_rate_tensor, global_vars):
		self.learning_rate = learning_rate_tensor
		self.var_norms = tf.global_norm(self.get_vars())
		grads, self.grad_norms = tf.clip_by_global_norm(self.gradients, 40.0)
		self.apply_gradients = self.optimizer.apply_gradients(zip(grads, global_vars))
		self.add_eps = self.global_episodes.assign_add(1)

	def set_up_sync_weights(self, global_vars):
		local_vars = self.get_vars()
		self.sync = []
		for(local, globl) in zip(local_vars, global_vars):
			self.sync.append(local.assign(globl))

	def apply_grads(self, sess, a_batch, r_batch, s_batch, reward_val_diff_batch, lr):
		feed_dic={self.state: s_batch,
			self.a: a_batch,
			self.diff: reward_val_diff_batch,
			self.reward: r_batch,
			self.learning_rate: lr}
		sess.run(self.apply_gradients, feed_dict=feed_dic)
		if self.summary_writer is None:
			return
		mean_reward = np.mean(r_batch)
		loss = sess.run(self.total_loss, feed_dict=feed_dic)
		entropy = sess.run(self.entropy, feed_dict=feed_dic)
		episode = sess.run(self.global_episodes)
		summary = tf.Summary()
		summary.value.add(tag='Perf/Reward', simple_value=float(mean_reward))
		summary.value.add(tag='Losses/Total Loss', simple_value=float(loss))
		summary.value.add(tag='Losses/Entropy', simple_value=float(np.sum(entropy)))
		self.summary_writer.add_summary(summary, episode)
		self.summary_writer.flush()
		sess.run(self.add_eps)

	def sync_weights(self, sess):
		sess.run(self.sync)

	def fc_layer(self, shapes):
		inputs = shapes[0]
		outputs = shapes[1]
		bias_shape = [outputs]
		initial = tf.random_normal(shapes, stddev=1.0)
		norms = tf.sqrt(tf.reduce_sum(tf.square(initial), list(range(len(shapes)-1))))
		initial /= norms
		weights = tf.Variable(initial)
		biases = tf.Variable(tf.truncated_normal(bias_shape, stddev=0.1))
		return weights, biases

	def run_policy_and_value(self, sess, state):
		policy_out, value_out = sess.run([self.policy_out, self.value],
						feed_dict={self.state:[state]})
		return(policy_out[0], value_out[0])

	def run_policy(self, sess, state):
		policy_out = sess.run(self.policy_out, feed_dict={self.state:[state]})
		return policy_out[0]

	def run_value(self, sess, state):
		value = sess.run(self.value, feed_dict={self.state:[state]})
		return value[0]

	def get_vars(self):
		return [self.fc1, self.fc1_b,
			self.fc2, self.fc2_b,
			self.fc3, self.fc3_b,
			self.fc4, self.fc4_b]
