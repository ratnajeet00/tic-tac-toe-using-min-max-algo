import tkinter as tk
from tkinter import messagebox

ai = 'O'
player = 'X'
ai_first = False
ai_delay = 1.0

def evaluate(b):
    for i in range(3):
        if b[i] == b[i + 3] == b[i + 6] != " ":
            return 10 if b[i] == ai else -10
        if b[i * 3] == b[i * 3 + 1] == b[i * 3 + 2] != " ":
            return 10 if b[i * 3] == ai else -10
    if b[0] == b[4] == b[8] != " ":
        return 10 if b[0] == ai else -10
    if b[2] == b[4] == b[6] != " ":
        return 10 if b[2] == ai else -10
    return 0

def minimax(b, depth, is_maximizing):
    score = evaluate(b)
    if score == 10 or score == -10:
        return score
    if all(cell != " " for cell in b):
        return 0

    if is_maximizing:
        best = -1000
        for i in range(9):
            if b[i] == " ":
                b[i] = ai
                best = max(best, minimax(b, depth + 1, not is_maximizing))
                b[i] = " "
        return best
    else:
        best = 1000
        for i in range(9):
            if b[i] == " ":
                b[i] = player
                best = min(best, minimax(b, depth + 1, not is_maximizing))
                b[i] = " "
        return best

def find_best_move(b):
    best_val = -1000
    best_move = -1
    for i in range(9):
        if b[i] == " ":
            b[i] = ai
            move_val = minimax(b, 0, False)
            b[i] = " "
            if move_val > best_val:
                best_val = move_val
                best_move = i
    return best_move

def is_game_over():
    return evaluate(board) != 0 or all(cell != " " for cell in board)

def make_move(index, player_symbol):
    global game_over
    if board[index] == " " and not game_over:
        board[index] = player_symbol
        buttons[index].config(text=player_symbol)
        if is_game_over():
            game_over = True
            winner = "AI" if player_symbol == ai else "Player"
            messagebox.showinfo("Game Over", f"{winner} wins!")
        elif all(cell != " " for cell in board):
            game_over = True
            messagebox.showinfo("Game Over", "It's a tie!")
        return True
    return False

def on_button_click(index):
    global ai_turn
    if make_move(index, player):
        ai_turn = True
        window.after(int(ai_delay * 1000), ai_move)

def ai_move():
    global ai_turn
    if ai_turn and not game_over:
        best_move = find_best_move(board)
        make_move(best_move, ai)
        ai_turn = False

def reset_game():
    global board, game_over, ai_turn
    board = [" " for _ in range(9)]
    game_over = False
    ai_turn = ai_first
    for button in buttons:
        button.config(text="")

window = tk.Tk()
window.title("Tic Tac Toe")

buttons = []
for i in range(9):
    button = tk.Button(window, text=" ", font=("Arial", 20), width=5, height=2,
                       command=lambda i=i: on_button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

reset_button = tk.Button(window, text="Reset", font=("Arial", 20), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

reset_game()
window.mainloop()

