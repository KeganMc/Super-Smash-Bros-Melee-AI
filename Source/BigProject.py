import os, time

def main():
  i = 0
  while(True):
    pipeName = "../../../../.local/share/dolphin-emu/Pipes/pipe"
    pipeout = open(pipeName, "w")
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
