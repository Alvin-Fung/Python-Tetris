import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20 
        self.num_cols = 10
        self.cell_size = 30
        # Array to represent the grid itself
        self.grid = [[0 for i in range(self.num_cols)] for j in range (self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                  # Rect method to be drawn on the screen - Margins are added to acquire the 29 pixels
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size +1, 
                                        self.cell_size -1, self.cell_size-1) 
                # Draw method (acquires color tuple for that specific cell)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect) 
