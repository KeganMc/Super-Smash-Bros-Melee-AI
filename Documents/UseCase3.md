#Use Cases

##Use Case: 3 Configuring Controller

###CHARACTERISTIC INFORMATION

**Goal in Context:** User configures controller to which the bot will use.

**Scope:** Dolphin Emulator (GameCube)

**Level:** Subfunction

**Preconditions:** User has Dolphin downloaded, and deepbot.ini downloaded.

**Success End Condition:** Bot controller configuration is set up.

**Failed End Condition:** Bot controller configuration is not set up.

**Primary Actor:** User, the person configuring the controller.

**Trigger:** User downloads the bot and emulator for the first time.

###MAIN SUCCESS SCENARIO

1. User locates the gcpad folder in dolphin.emu

2. User Places the deepbot.ini file into the gcpad folder

3. User launches the Dolphin Emulator

4. User navigates to the controller menu in the emulator (drop down box in the upper-right)

5. User selects standard controller for controller port 2 under "Gamecube Controllers" and clicks on the configure button to its right

6. User selects the deepbot.ini file under the profile drop-down menu and then clicks the load button to the right

###EXTENSIONS

* 1a. User is having difficulties locating the gcpad folder:

  + 1a1. Open up the terminal (linux)

  + 1a2. Move to the root directory
  
  + 1a3. Type in "locate gcpad"
  
  + 1a4. Change directories to the path given from the command
  
* 2b. User still cannot locate the gcpad folder:
  
  + 1b1. Installing Dolphin Emulator (Use Case 2)

###SUB-VARIATIONS

###RELATED INFORMATION (optional)

**Priority:** High

**Performance Target:** 5 minutes

**Frequency:** 1 time for each user

**Superordinate Use Case:** Running the bot for the first time (use case 1)

**Subordinate Use Cases:** Installing Dolphin Emulator (use case 2)

**Channel to primary actor:** Interactive

**Secondary Actors:** Dolphin Emulator

**Channel to Secondary Actors:** File

###SCHEDULE

Due Date: release 1.0
