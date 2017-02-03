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
    last_frame = 0
    while(True):
      res = next(mw)
      if res is not None:
        stateManager.handle(*res)
      if st.frame > last_frame:
        last_frame = st.frame
        if st.menu == state.Menu.Game:
          pipeout.write(output_map[random.choice(list(outputs))])
          pipeout.flush()
      #time.sleep(0.02)

  pipeout.close()

if __name__=="__main__": main()
