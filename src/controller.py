import pygame
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
        self.obstacle = Obstacle(200, 400, "assets/obstacle_image.png")
        self.movable_obstacle = MovableObstacle(600, 200, "assets/movable_obstacle_image.png")
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.timer = 90

    def handle_events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        if keys[K_a]:
            self.bread.move_left(2)
        if keys[K_d]:
            self.bread.move_right(2)
        if keys[K_w]:
            self.bread.jump()

    def update(self):
        if not self.game_over:
            self.bread.update()
            self.movable_obstacle.update()
            if pygame.sprite.collide_rect(self.bread, self.obstacle) or pygame.sprite.collide_rect(self.bread, self.movable_obstacle):
                self.game_over = True
                self.toast = False
            for row in range(self.maze.rows):
                for col in range(self.maze.cols):
                    if self.maze.maze[row][col] == 0:
                        cell_rect = pygame.Rect(col * 30, row * 25, 30, 30)
                        if cell_rect.colliderect(self.bread.rect):
                            self.toast = False
                            return
                    
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
            self.screen.blit(self.obstacle.image, self.obstacle.rect)
            self.screen.blit(self.movable_obstacle.image, self.movable_obstacle.rect)
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
