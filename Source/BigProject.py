import os, time
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

#TODO: Preprocess for certain player numbers (ie player 3 vs player 4)
def preprocess(st):
  stList = []
  stList.append(st.frame)
  stList.append(st.stage.value)
  for playerID in range(4):
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
  return np.reshape(np.array(stList), [1,78])

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
      sess.run(tf.global_variables_initializer())
      while(True):
        res = next(mw)
        if res is not None:
          stateManager.handle(*res)
        if st.frame > last_frame+3:
          last_frame = st.frame
          if st.menu == state.Menu.Game:
            action, val =  network.run_policy_and_value(sess, preprocess(st))
            print(action)
            pipeout.write(output_map[np.random.choice(list(outputs), p=action)])
            pipeout.flush()
      #time.sleep(0.02)

  pipeout.close()

if __name__=="__main__": main()
