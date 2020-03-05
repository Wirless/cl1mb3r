# Climber 1.0
# codename ^
#          |
#          |
#          |
#          |
import pygame


class Climber(pygame.sprite.Sprite):
    def __init__(self, color, size, pos):
        """
        initialize Climber object as an actor that will interact with the scene.
        prop -> map
        :type pos: object *xy
        """
        super().__init__()
        self.image = pygame.Surface(size)
        self.image = pygame.image.load("standby.png")
        self.collision = [False]
        pygame.draw.rect(self.image, color, [0, 0, size[0], size[1]])
        self.rect = self.image.get_rect()
        self.reach = 0
        self.rect.y = 0
        self.rect.x = 0
        self.rotation = 0
        self.bounce = 0
        self.velocity = 5
    
    def update(self):
        self.rect.y += self.velocity
        if self.rect.y > 615:
            self.rect.y = 615
            
    def jump(self):
        if self.rect.y == 615:
            self.rect.y -= self.velocity
            
    def moveRight(self):
        self.rect.x += self.velocity
        if self.rect.x > 615:
            self.rect.x = 615        
    def moveLeft(self):
        self.rect.x -= self.velocity
        if self.rect.x < 0:
            self.rect.x = 0