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
        self.image.fill((255, 9, 255))
        self.image.set_colorkey((255, 9, 255))
        self.collision = [False]
        pygame.draw.rect(self.image, color, [0, 0, size[0], size[1]])
        self.rect = self.image.get_rect()
        self.reach = 0
        self.rect.y = 0
        self.rect.x = 0
        self.rotation = 0
        self.bounce = 0

