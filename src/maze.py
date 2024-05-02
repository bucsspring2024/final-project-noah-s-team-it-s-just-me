import pygame
import random

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.maze = [[0 for _ in range(cols)] for _ in range(rows)]
        self.generate_recursive_backtracking(0, 0)
        
    def make(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.maze[row][col] == 0:
                    self.walls.append(pygame.Rect((col * 30, row * 25, 30, 30)))

    def draw(self, screen):
        for wall in self.walls:
            pygame.draw.rect(screen, 'black',wall) 
            
    def run_collide(self,object):
            for wall in self.walls:
                if (wall.top <= object.rect.top <= wall.bottom) or (wall.top <= object.rect.bottom <= wall.bottom):
                    if (wall.left <= object.rect.left <= wall.right):
                        object.rect.left = wall.right
                        return True
                    if (wall.left <= object.rect.right <= wall.right):
                        object.rect.right = wall.left
                        return True
            return False
    def fall_collide(self,object):
            for wall in self.walls:
                if (object.rect.bottom >= wall.top) and ((wall.left <= object.rect.left <= wall.right) or (wall.left <= object.rect.right <= wall.right)):
                    object.rect.bottom = wall.top
                    return True
            return False


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
