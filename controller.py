import pygame
from bread import Bread
from obstacle import Obstacle
from movableobstacle import Movableobstacle

class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600)) 
    
    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.flip()

if __name__ == "__main__":
    controller = Controller()
    controller.mainloop()
