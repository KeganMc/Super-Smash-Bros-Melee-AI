import os, time
import state
import state_manager
import memory_watcher
from controller_outputs import outputs
from controller_outputs import output_map
import random

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

def main():
  dolphinPath = find_directory()
  if dolphinPath is None:
    print("Could not find dolphin directory!")
    return

  pipe = find_make_pipe_dir(dolphinPath) + "/pipe"
  try:
    os.mkfifo(pipe)
  except OSError:
    pass

  pipeout = open(pipe, "w")
  while(True):
    pipeout.write(output_map[random.choice(list(outputs))])
    pipeout.flush()
    time.sleep(0.02)

  pipeout.close()
    
if __name__=="__main__": main()
