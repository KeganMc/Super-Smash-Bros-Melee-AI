import tensorflow as tf
import numpy as np
from threading import Thread

class workerThread(Thread):
    def _init_(self, function, *args):
        self.function = function
        self.args = args
        Thread._init_(self)

    def run(self):
        self.function(*self.args)
