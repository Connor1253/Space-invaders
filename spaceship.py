import pygame


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.image.load("/Users/connor/Desktop/Graphics/spaceship.png")
        self.rect = self.image.get_rect(midbottom=(self.width/2,self.height))
        self.speed = 6

    def get_user_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if keys[pygame.K_LEFT]:
            self.rect. x -= self.speed

    def update(self):
        self.get_user_input()
        self.constrain_movement()

    def constrain_movement(self):
        if self.rect.right > self.width:
            self.rect.right = self.width
        if self.rect.left < 0:
            self.rect.left = 0
