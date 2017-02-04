import state
import state_manager

"""
Input: The current and previous states our bot had been in (is in)
Process: Past and current state variables such as player stocks and percentages are
    examined and a reward is assigned to our bot based off the differences in those variables
Output: Reward to be given to our bot
"""
def reward(lastState, currentState):
  botReward = 0
  
  """variables pertinent to creating a reward from each state"""
  #Stocks
  lastStocks1 = lastState.players[0].stocks
  currentStocks1 = currentState.players[0].stocks
  
  lastStocks2 = lastState.players[1].stocks
  currentStocks2 = currentState.players[1].stocks
  
  #Percentages
  lastPercent1 = lastState.players[0].percent
  currentPercent1 = currentState.players[0].percent
  
  lastPercent2 = lastState.players[1].percent
  currentPercent2 = currentState.players[1].percent
  
  #Dying
  prevDying1 = lastState.players[0].action_state.value <= 0xA
  prevDying2 = lastState.players[1].action_state.value <= 0xA
  nowDying1 = currentState.players[0].action_state.value <= 0xA
  nowDying2 = currentState.players[1].action_state.value <= 0xA

  #Determine Reward
  if (not prevDying1 and nowDying1) and (not prevDying2 and nowDying2):
    return 0
  elif (not prevDying1 and nowDying1):
    return 100
  elif (not prevDying2 and nowDying2):
    return -100

  # Don't give negative reward for the opponent respawning.
  opponentPercentReward = 0
  if not (currentPercent1 == 0 and lastPercent1 > 0):
    opponentPercentReward = currentPercent1 - lastPercent1

  allyPercentPenalty = 0
  if not (currentPercent2 == 0 and lastPercent2 > 0):
    allyPercentPenalty = currentPercent2 - lastPercent2

  botReward = opponentPercentReward - allyPercentPenalty
  return botReward
  
