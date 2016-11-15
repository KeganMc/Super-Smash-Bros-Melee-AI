#Use Cases

##Use Case: 2 Installing Dolphin Emulator

###CHARACTERISTIC INFORMATION

**Goal in Context:** Download and install the Dolphin Emulator in order to run the
Super Smash Brothers Melee rom file, and play against the bot or watch the bot.

**Scope** Ubuntu OS

**Level** Instructions

**Preconditions:** We know that we need the Dolphin Emulator in order to run the game.

**Success End Condition:** The user has successfully dowlnoaded and installed the Dolphin
Emulator and is now able to run the game, and can then run the bot.

**Failed End Condition:** The user will neither be able to run the game, Super Smash Bros
Melee from their pc, and thus won't be able to play against or watch the bot play.

**Primary Actor:** The user/player who needs to install Dolphin.

**Trigger:** Open the Ubuntu Terminal

###MAIN SUCCESS SCENARIO

1. Open the Terminal

3. Add the PPA repository that contains the stable and latest development version
   of this software package.

4. Install the Dolphin emulator

5. Dolphin has now been installed. Update the database

6. Locate where dolphin was saved to.

###EXTENSIONS

* 1a. Click the "Search your computer" button in the upper left corner of the desktop.

* 1b. Type in "Terminal" and click the Terminal icon.

* 3a. Type: sudo add-apt-repository ppa:dolphin-emu/ppa, press Enter. Then type in your login password
   and press Enter.

* 4a. Type: sudo apt-get update, and press Enter.

* 4b. Type: sudo apt-get install dolphin-emu, and press enter.

* 5a. Type: sudo updatedb, and press enter.

* 6a. Type: locate dolphin-emu, and press enter.

###SUB-VARIATIONS

* 1a. Press Ctrl+Alt+T shortcut keys

###RELATED INFORMATION

**Priority** Maximum

**Frequency** Every time the game is to be loaded.

**SuperOrdinate Use Case:** Running the bot for the first time (Use Case 1)

###SCHEDULE

Due Date: Realease 1.0









