import pygame
import random
from pygame.locals import *
from src.bread import Bread
from src.obstacle import Obstacle
from src.movableobstacle import MovableObstacle
from src.maze import Maze
from src.volcano import Volcano

class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.clock = pygame.time.Clock()
        self.toast, self.game_over = False, False
        self.maze = Maze(30, 40)
        self.bread = Bread(0, 0, "assets/bread_image.png")
        self.volcano = Volcano(1150, 630, "assets/volcano_image.png")
        self.volcano_group = pygame.sprite.GroupSingle(self.volcano)
        self.font, self.small_font = pygame.font.Font(None, 36), pygame.font.Font(None, 24)
        self.timer = 90
        self.obstacles = pygame.sprite.Group()
        self.movable_obstacles = pygame.sprite.Group()
        self.place_obstacles()
        self.toasty_visible, self.toasty_timer, self.toasty_duration = False, 0, 30

    def place_obstacles(self):
        black_edges = {(col, row) for row in range(1, self.maze.rows - 1) for col in range(1, self.maze.cols - 1)
                        if self.maze.maze[row][col] == 1 and
                        (self.maze.maze[row - 1][col] == 0 or self.maze.maze[row + 1][col] == 0 or
                         self.maze.maze[row][col - 1] == 0 or self.maze.maze[row][col + 1] == 0)}

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
        if keys[K_a]: self.bread.move_left(3)
        if keys[K_d]: self.bread.move_right(3)
        if keys[K_w]: self.bread.jump()

    def update(self):
        def collision_check(object1, object2):
            return pygame.Rect.colliderect(object1.get_rect(), object2.rect)
        
        if not self.game_over:
            self.bread.update()
            self.maze.fall_collide(self.bread)
            self.maze.jump_collide(self.bread)
            self.maze.run_collide(self.bread)
            self.movable_obstacles.update()
            if pygame.sprite.spritecollideany(self.bread, self.obstacles, collision_check) or pygame.sprite.spritecollideany(self.bread, self.movable_obstacles, collision_check):
                self.game_over = True
                self.toast = False
            if not self.maze.fall_collide(self.bread): self.bread.update()
            self.movable_obstacles.update()
            if pygame.sprite.spritecollideany(self.bread, self.obstacles) or pygame.sprite.spritecollideany(self.bread, self.movable_obstacles):
                self.game_over, self.toast = True, False
            elif pygame.sprite.spritecollideany(self.bread, self.volcano_group):
                self.game_over, self.toast, self.toasty_visible, self.toasty_timer = True, True, True, self.toasty_duration * 2
            
            fps = self.clock.get_fps()
            if fps == 0:
                fps = 60
            self.timer -= 1 / fps
            if self.timer <= 0:
                self.game_over = True
                self.timer = 0
            if self.timer <= 0: self.game_over, self.timer = True, 0
            if self.toasty_visible:
                self.toasty_timer -= 1
                if self.toasty_timer <= 0: self.toasty_visible = False
                elif self.toasty_timer % 30 == 0: self.toasty_visible = not self.toasty_visible

    def draw(self):
        self.screen.fill('white')
        self.maze.draw(self.screen)
        self.screen.blit(self.small_font.render("Start", True, 'green'), (10, 10))
        end_text = self.small_font.render("End", True, 'green')
        self.screen.blit(end_text, (self.screen.get_width() - end_text.get_width() - 20, self.screen.get_height() - end_text.get_height() - 20))
        minutes, seconds = int(self.timer) // 60, int(self.timer) % 60
        self.screen.blit(self.font.render(f"Time: {minutes}:{seconds:02}", True, 'blue'), self.font.render(f"Time: {minutes}:{seconds:02}", True, 'blue').get_rect(topright=(self.screen.get_width() - 32, 20)))
        if self.game_over:
            font_color = 'white' if self.toast else 'red'
            self.screen.blit(self.font.render("Game Over!", True, font_color), (550, 350))
            if self.toast:
                toasty_text = self.font.render("Toasted!!!", True, 'brown')
                self.screen.fill('black')
                self.screen.blit(toasty_text, toasty_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() //2)))   
        else:
            self.screen.blit(self.bread.image, self.bread.rect)
            self.obstacles.draw(self.screen)
            self.movable_obstacles.draw(self.screen)
            self.screen.blit(self.volcano.image, self.volcano.rect)
        
        self.screen.blit(self.font.render("W: Jump   A: Left   D: Right", True, 'blue'), (20, 760))
        pygame.display.flip()

    def mainloop(self):
        while not self.game_over:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()
        while True:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    quit()

if __name__ == "__main__":
    controller = Controller()
    controller.mainloop()
