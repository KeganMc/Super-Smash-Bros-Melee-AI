import os, time
import state
import state_manager
import memory_watcher

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
  i = 0
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
    pipeout.write("SET MAIN 0.5 0.3\n")
    pipeout.write("PRESS B\n")
    pipeout.flush()
    time.sleep(0.02)
    pipeout.write("RELEASE B\n")
    pipeout.write("SET MAIN 0.5 0.5\n")
    pipeout.flush()
    time.sleep(0.03)
    # double laser
    pipeout.write("PRESS X\n")
    pipeout.flush()
    time.sleep(.018)
    pipeout.write("RELEASE X\n")
    pipeout.flush()
    time.sleep(.05)
    pipeout.write("PRESS B\n")
    pipeout.flush()
    time.sleep(.02)
    pipeout.write("RELEASE B\n")
    pipeout.flush()
    time.sleep(.04)
    pipeout.write("PRESS B\n")
    pipeout.flush()
    time.sleep(.05)
    pipeout.write("RELEASE B\n")
    pipeout.flush()
    time.sleep(.05)
    time.sleep(.3)
    i = i + 1
  pipeout.close()
    
if __name__=="__main__": main()
