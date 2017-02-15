import os, time
from reward import reward
from workerThread import workerThread
import state
import state_manager
import memory_watcher
from controller_outputs import outputs
from controller_outputs import output_map
import random
import tensorflow as tf
import numpy as np
import random
from actor_critic import ActorCriticNetwork

def find_directory():
  possible = ["~/.dolphin-emu", "~/.local/share/.dolphin-emu", "~/Library/Application/ Support/Dolphin", "~/.local/share/dolphin-emu"]
  for path in possible:
    fullPath = os.path.expanduser(path)
    if os.path.isdir(fullPath):
      return fullPath
  return None

def find_make_pipe_dir(dolphinPath):
  pipesPath = dolphinPath + "/Pipes"
  if os.path.isdir(pipesPath):
    return pipesPath
  os.mkdir(pipesPath)
  return pipesPath


def write_locations(dolphin_dir, locations):
  path = dolphin_dir + '/MemoryWatcher/Locations.txt'
  with open(path, 'w') as f:
    f.write('\n'.join(locations))
  return

def find_socket(dolphinPath):
  socketDir = dolphinPath + "/MemoryWatcher"
  if not os.path.isdir(socketDir):
    os.mkdir(socketDir)
  socketPath = socketDir + "/MemoryWatcher"
  return socketPath

def appendPlayerInfoToStateList(stList, players):
  for playerID in players:
    player = st.players[playerID]
    stList.append(player.stocks)
    stList.append(player.cursor_x)
    stList.append(player.cursor_y)
    stList.append(player.type.value)
    stList.append(player.character.value)
    stList.append(player.action_state.value)
    stList.append(player.facing)
    stList.append(player.self_air_vel_x)
    stList.append(player.self_air_vel_y)
    stList.append(player.attack_vel_x)
    stList.append(player.attack_vel_y)
    stList.append(player.pos_x)
    stList.append(player.pos_y)
    stList.append(player.on_ground)
    stList.append(player.action_frame)
    stList.append(player.percent)
    stList.append(player.hitlag)
    stList.append(player.jumps_used)
    stList.append(player.body_state.value)

#TODO: Preprocess for certain player numbers (ie player 3 vs player 4)
"""
Input: The current states our bot is in
    players = A list containing character information. The index of each element in the
    list reflects the id number for each character and the value reflects the character allegiance.
        0 = Does not exist in game
        1 = Our Bot
        2 = Opponent
        3 = Ally
Process: Past and current state variables such as player stocks and percentages are
    examined and a reward is assigned to our bot based off the differences in those variables
Output: Reward to be given to our bot
"""
def preprocess(st, players):
  # Find bot, then ally, then enemy
  botID = None
  allies = []
  enemies = []
  for playerID, relation in enumerate(players):
    if relation == 1:
      botID = playerID
    elif relation == 3:
      allies.append(playerID)
    else:
      enemies.append(playerID)
  stList = []
  stList.append(st.frame)
  stList.append(st.stage.value)
  appendPlayerInfoToStateList(stList, [botID])
  appendPlayerInfoToStateList(stList, allies)
  appendPlayerInfoToStateList(stList, enemies)
  return np.reshape(np.array(stList), [1,78])

def updateNetwork(sess, network, actionList, stateList, valList, rewardList, gamma):
  R = valList[0]
  actionList.reverse()
  stateList.reverse()
  valList.reverse()
  rewardList.reverse()
  batch_a = []
  batch_s = []
  batch_r = []
  batch_td = []
  for(ai, ri, si, vi) in zip(actionList, rewardList, stateList, valList):
    R = ri + gamma * R
    td = R - vi
    a = np.zeros([40])
    a[ai.value] = 1
    batch_a.append(a)
    batch_s.append(si)
    batch_td.append(td)
    batch_r.append(R)
    network.apply_grads(sess, batch_a, batch_r, batch_s, batch_td, 0.01)

def getLatestState(mw, sm):
  res = next(mw)
  while res is not None:
    sm.handle(*res)
    res = next(mw)

def main():
  dolphinPath = find_directory()
  if dolphinPath is None:
    print("Could not find dolphin directory!")
    return

  pipe = find_make_pipe_dir(dolphinPath) + "/pipe"
  mwLocation = find_socket(dolphinPath)
  st = state.State()
  stateManager = state_manager.StateManager(st)
  write_locations(dolphinPath, stateManager.locations())
  try:
    os.mkfifo(pipe)
  except OSError:
    pass

  pipeout = open(pipe, "w")
  with memory_watcher.MemoryWatcher(mwLocation) as mw:
    with tf.Session() as sess:
      learning_rate_tensor = tf.placeholder(tf.float32)
      network = ActorCriticNetwork(40,
                    tf.train.RMSPropOptimizer(learning_rate=learning_rate_tensor, decay=0.9))
      network.set_up_loss(0.01)
      network.set_up_apply_grads(learning_rate_tensor)
      last_frame = 0
      actionList = []
      stateList = []
      valList = []
      rewardList = []
      lastState = None
      sess.run(tf.global_variables_initializer())
      pipeout.write(output_map[outputs.RESET])
      pipeout.flush()
      while(True):
        getLatestState(mw,stateManager)
        if st.frame > last_frame+3:
          last_frame = st.frame
          if st.menu == state.Menu.Game:
            currentState = preprocess(st)
            if lastState is not None:
              rewardList.append(reward(lastState, st, [2,1,0,0]))
            if len(valList) >= 64:
              updateNetwork(sess, network, actionList, stateList, valList, rewardList, 0.99)
              actionList = []
              stateList = []
              valList = []
              rewardList = []
            action, val =  network.run_policy_and_value(sess, currentState)
            chosenAction = np.random.choice(list(outputs), p=action)
            print(chosenAction)
            actionList.append(chosenAction)
            valList.append(val)
            stateList.append(currentState)
            lastState = st
            pipeout.write(output_map[chosenAction])
            pipeout.flush()

  pipeout.close()

if __name__=="__main__": main()
