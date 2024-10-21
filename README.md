# Tic Tac Toe with AI

## Overview
This project is a simple Tic Tac Toe game built with Python using the Tkinter library for the graphical user interface (GUI). The game allows a player to compete against an AI that employs the Minimax algorithm for optimal decision-making.

## Features
- Play against an AI opponent that plays optimally.
- User-friendly GUI created with Tkinter.
- Reset button to start a new game.
- Displays the winner or announces a tie when the game concludes.

## Requirements
- Python 3.x
- Tkinter (usually included with Python installations)

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/tic-tac-toe-ai.git
   ```
Navigate to the project directory:
```
cd tic-tac-toe-ai
```
Run the game:
```
python tic_tac_toe.py
```
Usage
Click on any of the 9 buttons to make a move as the player (X).
The AI will take its turn as O.
A message box will display the result when the game ends, indicating the winner or a tie.
Click the Reset button to start a new game.
Code Explanation
Game Logic: The board is represented as a list of 9 elements initialized with spaces (" "). The evaluate() function checks for wins or ties, while the minimax() function implements the Minimax algorithm for AI moves.
Graphical Interface: The interface is created using Tkinter, with buttons for the Tic Tac Toe grid. Each button click triggers the player's move and updates the game state.
AI Decision Making: The AI's optimal move is calculated using the find_best_move() function, evaluating all possible moves with the Minimax algorithm.
Author
