#Use Cases

##Use Case: 1 Running the Bot for the First Time

###CHARACTERISTIC INFORMATION

**Goal in Context:** A player wants to play Super Smash Bros. Melee, and needs a better opponent.

**Scope:** The Player's computer.

**Level:** Summary

**Preconditions:** The Player has Ubuntu 16.04, and a copy of Super Smash Bros Melee.

**Success End Condition:** The player has completed a match against the bot.

**Failed End Condition:** The player encountered an error, and was not able to complete a match against the bot.

**Primary Actor:** Player, the person playing the game.

**Trigger:** Player begins setup.

###MAIN SUCCESS SCENARIO

1. The Player installs Dolphin (use case 2).

2. Player configures the controller for the bot (use case 3).

3. Player runs Super Smash Bros Melee from Dolphin.

4. Player navigates to VS. Mode and hits start.

5. Player navigates to Melee and hits start.

6. Player runs the bot (use case 4).

7. Player selects their character, and the character of the AI.

8. Player sets the rules to 4 stocks with an 8 minute time limit by navigating to the
"2-minute KO fest!" banner at the top.

9. Player presses start and moves to the stage select screen.

10. Player selects the stage to begin the match.

11. Player plays the match against the bot.

12. The player returns to the select character screen and can continue from 3. or end the game.

###EXTENSIONS

* 10a. The bot does not move:

  + 10a1. Configure the controller for the bot (use case 3)

###SUB-VARIATIONS

* 8a. Player may use
time or stock rules.


###RELATED INFORMATION

**Priority:** maximum

**Performance Target:** 20 minutes to install and configure Dolphin, 8 minutes to play the match.

**Frequency:** Once per machine the Player wants to play on.

**Superordinate Use Case:** N/A

**Subordinate Use Cases:**

* Installing Dolphin (use case 2)

* Configuring the Controller (use case 3)

* Running the bot (use case 4)

**Channel to primary actor:** project files

###OPEN ISSUES

* What happens if the directory structure for the Player's Dolphin installation is not supported?

* Move running the bot to happen before opening Dolphin. This will avoid the Player switching between windows too much?

###SCHEDULE

**Due Date:** release 1.0
