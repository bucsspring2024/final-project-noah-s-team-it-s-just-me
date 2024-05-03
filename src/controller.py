import pygame
import random
from pygame.locals import *
from src.bread import Bread
from src.obstacle import Obstacle
from src.movableobstacle import MovableObstacle
from src.maze import Maze

class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.clock = pygame.time.Clock()
        self.toast = False
        self.game_over = False
        self.maze = Maze(30, 40)
        self.bread = Bread(0, 0, "assets/bread_image.png")
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.timer = 90
        self.obstacles = pygame.sprite.Group()
        self.movable_obstacles = pygame.sprite.Group()
        self.place_obstacles()

    def place_obstacles(self):
        black_edges = set()
        for row in range(1, self.maze.rows - 1):
            for col in range(1, self.maze.cols - 1):
                if self.maze.maze[row][col] == 1:
                    if (self.maze.maze[row - 1][col] == 0 or self.maze.maze[row + 1][col] == 0 or
                        self.maze.maze[row][col - 1] == 0 or self.maze.maze[row][col + 1] == 0):
                        black_edges.add((col, row))
        
        black_edges = list(black_edges)
        random.shuffle(black_edges)
        
        for i in range(25):
            x, y = black_edges[i]
            self.obstacles.add(Obstacle(x * 30, y * 25, "assets/obstacle_image.png"))
        for i in range(25):
            x, y = black_edges[i + 25]
            self.movable_obstacles.add(MovableObstacle(x * 30, y * 25, "assets/movable_obstacle_image.png"))


    def handle_events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        if keys[K_a]:
            self.bread.move_left(3)
        if keys[K_d]:
            self.bread.move_right(3)
        if keys[K_w]:
            self.bread.jump()

    def update(self):
        if not self.game_over:
            if not self.maze.fall_collide(self.bread):
                self.bread.update()
            self.movable_obstacles.update()
            if pygame.sprite.spritecollideany(self.bread, self.obstacles) or pygame.sprite.spritecollideany(self.bread, self.movable_obstacles):
                self.game_over = True
                self.toast = False

            fps = self.clock.get_fps()
            if fps == 0:
                fps = 60
            self.timer -= 1 / fps
            if self.timer <= 0:
                self.game_over = True
                self.timer = 0

    def draw(self):
        self.screen.fill('white')
        self.maze.draw(self.screen)
        start_text = self.small_font.render("Start", True, 'green')
        self.screen.blit(start_text, (10, 10))
        end_text = self.small_font.render("End", True, 'green')
        self.screen.blit(end_text, (self.screen.get_width() - end_text.get_width() - 20, self.screen.get_height() - end_text.get_height() - 20))
        minutes = int(self.timer) // 60
        seconds = int(self.timer) % 60
        timer_text = self.font.render(f"Time: {minutes}:{seconds:02}", True, 'blue')
        timer_text_rect = timer_text.get_rect(topright=(self.screen.get_width() - 32, 20))
        self.screen.blit(timer_text, timer_text_rect)
        if self.game_over:
            font_color = 'white' if self.toast else 'red'
            text = self.font.render("Game Over!", True, font_color)
            self.screen.blit(text, (300, 100))
        else:
            self.screen.blit(self.bread.image, self.bread.rect)
            self.obstacles.draw(self.screen)
            self.movable_obstacles.draw(self.screen)
        control_text = self.font.render("W: Jump   A: Left   D: Right", True, 'blue')
        self.screen.blit(control_text, (20, 760))
        pygame.display.flip()

    def mainloop(self):
        while not self.game_over:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    controller = Controller()
    controller.mainloop()
