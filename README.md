# Dodgeball
This code is a dodgeball game implemented in Python. The game allows a human player to compete against the computer by selecting actions such as "throw," "dodge," or "pickup." The objective is to reach 5 points before the opponent.

The game starts with both players having zero points and no balls. The player and computer take turns choosing actions. The computer's action is determined based on the number of balls held by both players. The player's action is inputted through the command line.

During the game, the program keeps track of the number of points and the number of balls held by each player. If the player selects "pickup," they gain a ball, and if they select "throw," they lose a ball. The same applies to the computer.

The program determines the winner of each round based on the actions chosen by both players. If a point is gained, the program updates the respective player's points. At the end of each round, the program displays the current score, the number of balls held by each player, and any points gained.

The game continues until one of the players reaches 5 points. If both players reach 5 points simultaneously, it's considered a tie. The program then declares the winner or displays a message if both players win at the same time.
