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
  
  #Percentages
  
  return botReward
  