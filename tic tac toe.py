import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        # Colors
        self.bg_color = "#3498db"  # Background color
        self.button_color = "#ecf0f1"  # Button color
        self.font_color = "#2c3e50"  # Font color

        # Board
        self.board = [""] * 9

        # Player and Computer symbols
        self.player_symbol = "X"
        self.computer_symbol = "O"

        # Player goes first
        self.current_turn = self.player_symbol

        # Buttons
        self.buttons = [tk.Button(root, text="", font=("Arial", 24), width=6, height=3,
                                  command=lambda i=i: self.make_move(i), bg=self.button_color,
                                  fg=self.font_color) for i in range(9)]

        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col, padx=5, pady=5)

        # Reset button
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game, bg=self.button_color, fg=self.font_color)
        self.reset_button.grid(row=3, columnspan=3, pady=10)

        # Background color
        self.root.config(bg=self.bg_color)

        # Initialize the game
        self.reset_game()

    def make_move(self, index):
        if self.board[index] == "" and self.current_turn == self.player_symbol:
            self.update_board(index, self.player_symbol)
            self.check_winner()
            if not self.check_tie():
                self.current_turn = self.computer_symbol
                self.computer_move()

    def update_board(self, index, symbol):
        self.board[index] = symbol
        self.buttons[index].config(text=symbol, state=tk.DISABLED)

    def computer_move(self):
        empty_cells = [i for i, cell in enumerate(self.board) if cell == ""]
        if empty_cells:
            computer_choice = random.choice(empty_cells)
            self.update_board(computer_choice, self.computer_symbol)
            self.check_winner()
            self.check_tie()
            self.current_turn = self.player_symbol

    def check_winner(self):
        for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                self.display_winner(self.current_turn)

    def check_tie(self):
        if "" not in self.board:
            self.display_tie()
            return True
        return False

    def display_winner(self, winner):
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.reset_game()

    def display_tie(self):
        messagebox.showinfo("Game Over", "It's a Tie!")
        self.reset_game()

    def reset_game(self):
        for i in range(9):
            self.buttons[i].config(text="", state=tk.NORMAL)
            self.board[i] = ""
        self.current_turn = self.player_symbol

if __name__ == "__main__":
    root = tk.Tk()
    tic_tac_toe = TicTacToe(root)
    root.mainloop()
