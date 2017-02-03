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
  stateManagerLast = state_manager.StateManager(lastState)
  stateManagerCurrent = state_manager.StateManager(currentState)
  
  """variables pertinent to creating a reward from each state"""
  #Stocks
  lastStocks1 = lastState.players[0].stocks
  currentStocks1 = currentState.players[0].stocks
  
  lastStocks2 = lastState.players[0].stocks
  currentStocks2 = currentState.players[0].stocks
  
  #Percentages
  lastPercent1 = lastState.players[0].percent
  currentPercent1 = currentState.players[0].percent
  
  lastPercent2 = lastState.players[0].percent
  currentPercent2 = currentState.players[0].percent
  return botReward
  