import pygame, sys
from spaceship import Spaceship

pygame.init()
WIDTH = 750
HEIGHT = 700

GREY = (29, 29, 27)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

spaceship = Spaceship(WIDTH, HEIGHT)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    spaceship_group.update()

    screen.fill(GREY)
    spaceship_group.draw(screen)

    pygame.display.update()
    clock.tick(60)