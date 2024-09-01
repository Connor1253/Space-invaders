import pygame, sys

pygame.init()
WIDTH = 750
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)