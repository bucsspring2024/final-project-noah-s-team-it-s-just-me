import pygame
class Obstacle (pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        super().__init__()
        self.image = pygame.image.load(img_file)
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.rect.inflate_ip(-23, -23)