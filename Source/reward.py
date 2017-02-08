import state
import state_manager

"""
Input: The current and previous states our bot had been in (is in)
    characters = A list containing character information. The index of each element in the
    list reflects the id number for each character and the value reflects the character allegiance.
        0 = Does not exist in game
        1 = Our Bot
        2 = Opponent
        3 = Ally
Process: Past and current state variables such as player stocks and percentages are
    examined and a reward is assigned to our bot based off the differences in those variables
Output: Reward to be given to our bot
"""
def reward(lastState, currentState, characters):
  botReward = 0
  
  """variables pertinent to creating a reward from each state"""
  #Stocks
  opponentStockLast = lastState.players[0].stocks
  opponentStockCurrent = currentState.players[0].stocks
  
  botStockLast = lastState.players[1].stocks
  botStockCurrent = currentState.players[1].stocks
  
  #Percentages
  opponentPercentLast = lastState.players[0].percent
  opponentPercentCurrent = currentState.players[0].percent
  
  botPercentLast = lastState.players[1].percent
  botPercentCurrent = currentState.players[1].percent
  
  #Dying
  opponentPrevDying = lastState.players[0].action_state.value <= 0xA
  opponentNowDying = currentState.players[0].action_state.value <= 0xA
  
  botPrevDying = lastState.players[1].action_state.value <= 0xA
  botNowDying = currentState.players[1].action_state.value <= 0xA

  #Determine Reward
  if (not opponentPrevDying and opponentNowDying) and (not botPrevDying and botNowDying):
    return 0
  elif (not opponentPrevDying and opponentNowDying):
    return 1
  elif (not botPrevDying and botNowDying):
    return -1

  # Don't give negative reward for the opponent respawning.
  opponentPercentReward = 0
  if not (opponentPercentCurrent == 0 and opponentPercentLast > 0):
    opponentPercentReward = opponentPercentCurrent - opponentPercentLast

  allyPercentPenalty = 0
  if not (botPercentCurrent == 0 and botPercentLast > 0):
    allyPercentPenalty = botPercentCurrent - botPercentLast

  botReward = opponentPercentReward - allyPercentPenalty
  return (botReward*0.01)
  
