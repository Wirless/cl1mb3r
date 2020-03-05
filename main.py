#  climber
# eksdee
# ^
# ^
# ^

from random import randint
import pygame
from climber import Climber


def main():
    pygame.init()
    score = 0
    size = (700, 700)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Climber 1.0")
    climberactor = Climber((255, 255, 255), (0, 0), (350, 350))
    carry = True
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(climberactor)
    clock = pygame.time.Clock()
    x = 50
    y = 50
    width = 40
    height = 60
    vel = 5
    
    while carry:
        screen.fill((0, 0, 0))
        all_sprites_list.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carry = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    carry = False
                if event.key == pygame.K_RIGHT:
                    climberactor.moveRight()
                if event.key == pygame.K_LEFT:
                    climberactor.moveLeft()
                if event.key == pygame.K_SPACE:
                    climberactor.jump()

            
            
        climberactor.update()    
        font = pygame.font.Font(None, 50)
        text = font.render(str(climberactor.rect.y), 255, (255, 255, 0))
        screen.blit(text, (355, 10))
        pygame.display.flip()
        clock.tick(60)

    while not carry:
        pygame.quit()


if __name__ == "__main__":
    main()
