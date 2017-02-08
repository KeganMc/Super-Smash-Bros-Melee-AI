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
  
  #Bot Pleyer Number
  bot = characters.index(1)
  
  #Opponent Player Numbers
  opponents = []
  [opponents.insert(i) for i, j in enumerate(characters) if j == 2]
  
  #Ally Player Numbers
  allies = []
  [allies.insert(i) for i, j in enumerate(characters) if j == 3]
  
  """variables pertinent to creating a reward from each state"""
  #Stocks 
  botStockLast = lastState.players[bot].stocks
  botStockCurrent = currentState.players[bot].stocks
  
  for i in opponents:
    opponentStockLast[i] = lastState.players[opponents[i]].stocks
    opponentStockCurrent[i] = currentState.players[opponents[i]].stocks
    
  for i in allies:
    allyStockLast[i] = lastState.players[allies[i]].stocks
    allyStockCurrent[i] = currentState.players[allies[i]].stocks
  
  #Percentages
  botPercentLast = lastState.players[bot].percent
  botPercentCurrent = currentState.players[bot].percent
  
  for i in opponents:
    opponentPercentLast[i] = lastState.players[opponents[i]].percent
    opponentPercentCurrent[i] = currentState.players[opponents[i]].percent
    
  for i in allies:
    allyPercentLast[i] = lastState.players[allies[i]].percent
    allyPercentCurrent[i] = currentState.players[allies[i]].percent
  
  #Dying
  botPrevDying = lastState.players[bot].action_state.value <= 0xA
  botNowDying = currentState.players[bot].action_state.value <= 0xA
  
  for i in opponents:
    opponentPrevDying[i] = lastState.players[opponents[i]].action_state.value <= 0xA
    opponentNowDying[i] = currentState.players[opponents[i]].action_state.value <= 0xA
    
  for i in allies:
    allyPrevDying[i] = lastState.players[allies[i]].action_state.value <= 0xA
    allyNowDying[i] = currentState.players[allies[i]].action_state.value <= 0xA
  
  #Determine Reward
  if (not opponentPrevDying[0] and opponentNowDying[0]) and (not botPrevDying and botNowDying):
    return 0
  elif (not opponentPrevDying[0] and opponentNowDying[0]):
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
  
