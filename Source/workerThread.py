import tensorflow as tf
import numpy as np

class workerThread(object):
    def _init_(self, arg):
        self.actorCritic = arg

    def apply(self, sess, a_batch, r_batch, s_batch, reward_val_diff_batch, lr):
		actorCritic.apply_grads(sess, a_batch, r_batch, s_batch, reward_val_diff_batch, lr)
