import pygame
import random

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.maze = [[0 for _ in range(cols)] for _ in range(rows)]
        self.generate_recursive_backtracking(0, 0)

    def generate_recursive_backtracking(self, row, col):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)
        for dr, dc in directions:
            new_row, new_col = row + 2 * dr, col + 2 * dc
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.maze[new_row][new_col] == 0:
                self.maze[row + dr][col + dc] = 1
                self.maze[new_row][new_col] = 1
                self.generate_recursive_backtracking(new_row, new_col)
                

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.maze[row][col] == 0:
                    pygame.draw.rect(screen, 'black', (col * 30, row * 25, 30, 30))
