import pygame
class MovableObstacle (pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        super().__init__()
        self.image = pygame.image.load(img_file)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
