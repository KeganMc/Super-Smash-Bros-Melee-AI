class StateStore(object):
  def __init__(self, memoryWatcher):
    self.mw = memoryWatcher
    self.state = None

  def getNextState(self):
    res = next(self.mw)
    while res is not None:
      self.state = res
      res = next(self.mw)
    return self.state
