import state
import state_manager
import enum

@enum.unique
class Player(enum.Enum):
    Unselected = 0
    Bot        = 1
    Opponent   = 2
    Ally       = 3

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
  bot = -1
  allies = []
  opponents = []
  
  opponentPercentLast = []
  opponentPercentCurrent = []
  
  allyPercentLast = []
  allyPercentCurrent = []
  
  opponentPrevDying = []
  opponentNowDying = []

  allyPrevDying = []
  allyNowDying = []
  
  #Bot Player Number
  for (playerID, relation) in enumerate(characters):
    if relation == Player.Bot:
      bot = playerID
    elif relation == Player.Ally:
      allies.append(playerID)
    elif relation == Player.Opponent:
      opponents.append(playerID)
  
  """variables pertinent to creating a reward from each state"""
  
  #Percentages
  botPercentLast = lastState.players[bot].percent
  botPercentCurrent = currentState.players[bot].percent
  
  for i in opponents:
    opponentPercentLast.append(lastState.players[opponents[i]].percent)
    opponentPercentCurrent.append(currentState.players[opponents[i]].percent)
    
  for i in allies:
    allyPercentLast.append(lastState.players[allies[i]].percent)
    allyPercentCurrent.append(currentState.players[allies[i]].percent)
  
  #Dying
  botPrevDying = lastState.players[bot].action_state.value <= 0xA
  botNowDying = currentState.players[bot].action_state.value <= 0xA
  
  for i in opponents:
    opponentPrevDying.append(lastState.players[opponents[i]].action_state.value <= 0xA)
    opponentNowDying.append(currentState.players[opponents[i]].action_state.value <= 0xA)
    
  for i in allies:
    allyPrevDying.append(lastState.players[allies[i]].action_state.value <= 0xA)
    allyNowDying.append(currentState.players[allies[i]].action_state.value <= 0xA)
  
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
  
