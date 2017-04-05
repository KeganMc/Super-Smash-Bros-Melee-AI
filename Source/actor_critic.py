import tensorflow as tf
import numpy as np

class ActorCriticNetwork(object):
	def __init__(self, act_size, opt):
		self.state = tf.placeholder(tf.float32, [None, 1, 78])
		self.action_size = act_size
		self.optimizer = opt
		self.fc1, self.fc1_b = self.fc_layer([78, 256])
		self.fc2, self.fc2_b = self.fc_layer([256, 256])
		self.fc3, self.fc3_b = self.fc_layer([256, act_size])
		#self.fc4, self.fc4_b = self.fc_layer([64, act_size])
		self.fc4, self.fc4_b = self.fc_layer([256, 1])
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
		self.log_policy = tf.log(tf.clip_by_value(self.policy_out, 1e-15, 1.0))
		entropy = -tf.reduce_sum(self.policy_out * log_policy, reduction_indices=1)
		self.entropy = -tf.reduce_sum(self.policy_out * log_policy, reduction_indices=1)
		self.policy_loss = -tf.reduce_sum(tf.reduce_sum(tf.multiply(log_policy, self.a), reduction_indices=1) * self.diff + entropy * entropy_var)
		self.debug_stuff = -tf.reduce_sum(tf.reduce_sum(tf.multiply(log_policy, self.a), reduction_indices=1) * self.diff)
		self.more_debug = -tf.reduce_sum(entropy * entropy_var)
		policy_loss = -tf.reduce_sum(tf.reduce_sum(tf.multiply(log_policy, self.a), reduction_indices=1) * self.diff + entropy * entropy_var)
		self.reward = tf.placeholder(tf.float32, [None])
		value_loss = 0.5 * tf.nn.l2_loss(self.reward - self.value)
		self.value_loss = 0.5 * tf.nn.l2_loss(self.reward - self.value)
		self.total_loss = policy_loss + value_loss
		self.gradients = tf.gradients(self.total_loss, self.get_vars())

	def run_loss_debug(self, sess, a_batch, r_batch, s_batch, reward_val_diff_batch, lr):
		return sess.run([self.policy_loss, self.debug_stuff, self.more_debug], feed_dict={self.state: s_batch,
							self.a: a_batch,
							self.diff: reward_val_diff_batch,
							self.reward: r_batch,
							self.learning_rate: lr})

	def set_up_apply_grads(self, learning_rate_tensor, global_vars):
		self.learning_rate = learning_rate_tensor
		self.var_norms = tf.global_norm(self.get_vars())
		grads, self.grad_norms = tf.clip_by_global_norm(self.gradients, 40.0)
		self.apply_gradients = self.optimizer.apply_gradients(zip(grads, global_vars))

	def set_up_sync_weights(self, global_vars):
		local_vars = self.get_vars()
		self.sync = []
		for(local, globl) in zip(local_vars, global_vars):
			self.sync.append(local.assign(globl))

	def apply_grads(self, sess, a_batch, r_batch, s_batch, reward_val_diff_batch, lr):
		sess.run(self.apply_gradients, feed_dict={self.state: s_batch,
							self.a: a_batch,
							self.diff: reward_val_diff_batch,
							self.reward: r_batch,
							self.learning_rate: lr})

	def sync_weights(self, sess):
		sess.run(self.sync)

	def fc_layer(self, shapes):
		inputs = shapes[0]
		outputs = shapes[1]
		bias_shape = [outputs]
		tmp = 1.0/np.sqrt(inputs)
		weights = tf.Variable(tf.random_uniform(shapes, minval=-tmp, maxval=tmp))
		biases = tf.Variable(tf.random_uniform(bias_shape, minval=-tmp, maxval=tmp))
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
			#self.fc5, self.fc5_b]
