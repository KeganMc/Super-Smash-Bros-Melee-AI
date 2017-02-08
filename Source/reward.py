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
  botDying = 0
  if(not(botPrevDying) and botNowDying):
    botDying = 1
    
  opponentsDying = 0
  for i in opponents:
    if(not(opponentPrevDying[i]) and opponentNowDying[i]):
      opponentsDying+=1
      
  alliesDying = 0
  for i in allies:
    if(not(allyPrevDying[i]) and allyNowDying[i]):
      alliesDying+=1

  #Don't give negative reward for the opponent respawning.
  botPercentPenalty = 0
  if not (botPercentCurrent == 0 and botPercentLast > 0):
      botPercentPenalty += botPercentCurrent - botPercentLast
  
  opponentPercentReward = 0
  for i in opponents:
    if not (opponentPercentCurrent[i] == 0 and opponentPercentLast[i] > 0):
      opponentPercentReward += opponentPercentCurrent[i] - opponentPercentLast[i]

  allyPercentPenalty = 0
  for i in allies:
    if not (allyPercentCurrent[i] == 0 and allyPercentLast[i] > 0):
      allyPercentPenalty += allyPercentCurrent[i] - allyPercentLast[i]

  botReward = opponentPercentReward - botPercentPenalty - (allyPercentPenalty*0.2)
  return opponentsDying - botDying - alliesDying*0.2 + (botReward * 0.01)
  
