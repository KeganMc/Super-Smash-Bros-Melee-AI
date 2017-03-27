class playerData(object):
  def __init__(self):
    self.percent = None
    self.action_state = None

  def __init__(self, player):
    self.percent = player.percent
    self.action_state = player.action_state

class RewardData(object):
  def __init__(self):
    self.players = []
    for id in range(4):
      self.players.append(playerData)

  def __init__(self, state):
    self.players = []
    for player in state.players:
      pData = playerData(player)
      self.players.append(pData)
