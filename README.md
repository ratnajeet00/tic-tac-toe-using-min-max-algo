Tic Tac Toe with AI
Description
This is a simple Tic Tac Toe game implemented in Python using the Tkinter library for the graphical user interface (GUI). The game allows a player to compete against an AI that uses the Minimax algorithm for decision-making. The AI can play optimally to provide a challenging game experience.

Features
Play against an AI opponent
AI uses the Minimax algorithm for optimal moves
User-friendly GUI created with Tkinter
Reset button to start a new game
Displays the winner or declares a tie when the game ends
Requirements
Python 3.x
Tkinter (usually included with Python installations)
Installation
Clone or download the repository.
Navigate to the project directory.
Run the following command to start the game:
```
python tic_tac_toe.py

```
Usage
Click on any of the 9 buttons to make a move as the player (X).
The AI will then take its turn (O).
The game will display a message box when a player wins or if the game ends in a tie.
Click the Reset button to start a new game.
Code Explanation
Main Logic: The game board is represented as a list of 9 elements, initialized with spaces (" "). The evaluate() function checks for a win or a tie, and the minimax() function implements the Minimax algorithm for the AI's decision-making process.
GUI: The game interface is created using the Tkinter library, with buttons representing the Tic Tac Toe grid. Each button triggers the player's move and updates the game state.
AI Moves: The AI's best move is calculated using the find_best_move() function, which evaluates all possible moves using the Minimax algorithm.
