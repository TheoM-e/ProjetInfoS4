import tkinter as tk

from algo import generator, solver
from utils.board import SudokuBoard



class SudokuGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.board = SudokuBoard()
        # Créez la grille de Sudoku et les autres éléments de l'interface graphique.

    def run(self):
        self.window.mainloop()


board = SudokuBoard()
print(board)
generator.generate(board, 60, timeout=0.5)
print(board)
solver.print_resolved_board(board)