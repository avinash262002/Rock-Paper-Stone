Key Concepts
Game Rules:

Rock beats Scissors.
Scissors beat Paper.
Paper beats Rock.
Inputs:

User selects between Rock, Paper, or Scissors.
Computer randomly selects one of the three options.
Logic:

Compare user and computer choices to determine the winner:
Same choice → Draw.
Rock beats Scissors, Paper beats Rock, Scissors beat Paper.
Features:

Validate user input.
Keep score for multiple rounds.
Add an option to exit the game.
Steps to Implement
Display Instructions:

Provide clear rules and choices to the player.
User Input:

Take user input (Rock, Paper, or Scissors).
Allow inputs like numbers (1, 2, 3) or text.
Validate input for correctness.
Computer Choice:

Use random.choice() to select Rock, Paper, or Scissors.
Determine Winner:

Compare user and computer choices using conditional statements.
Output Results:

Announce the choices and the round’s outcome.
Update and display the score.
Repeat or Exit:

Repeat the game until the user chooses to exit.
