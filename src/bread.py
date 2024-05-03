import pygame

class Bread(pygame.sprite.Sprite):
    def __init__(self, x, y, image_file):
        super().__init__()
        self.image = pygame.image.load(image_file).convert_alpha()
        crop = pygame.Surface((16,16))
        crop.blit(self.image, (0, 0), (8, 8, 16, 16))
        self.image = crop
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_y = 0
        self.gravity = 1
        self.jump_strength = -8
        self.ground_level = 703
        self.is_jumping = False 
        
    
    def get_rect(self):
        new_rect = self.rect.copy()
        new_rect.inflate_ip(-40, -40)
        return new_rect
        

    def jump(self):
        self.velocity_y = self.jump_strength
        self.is_jumping = True

    def move_left(self, step):
        self.rect.x -= step

    def move_right(self, step):
        self.rect.x += step

    def update(self):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y
        if self.is_jumping and (self.velocity_y == 0):
            self.is_jumping = False
        elif self.is_jumping == False:
            self.velocity_y = 0
