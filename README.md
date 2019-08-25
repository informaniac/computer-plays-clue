# computer-plays-clue
Simple implementation of CLUE Board Game Mechanics to test automatic game playing strategies for it. Want to propose own strategies? Fork this repository!

This implementation is only available in the purpose of creating bots to play the game. All rights of the original game are held by Parker Brothers.

## Rules

The framework tries to simulate the basic rules of the classic CLUE game with some simplifications. Mainly, the board itself is not simulated but it is supposed that in every round at least one room can be reached from the current player position. Hence only distances between the rooms are stored. Additionally, each player is placed inside a random room at game initialisation phase.
