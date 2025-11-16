import pygame
from math import sqrt

class Player:
    def __init__(self, x=0, y=0, width=75, height=75):
        self.image = pygame.Surface((width, height)) 
        self.image.fill((255,0,0))

        self.x, self.y = x, y
        self.speed = 7

    def update(self, keys):
        self.move(keys)

    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def move(self, keys):
        dx = 0
        dy = 0

        if pygame.K_w in keys: dy -= 1
        if pygame.K_s in keys: dy += 1
        if pygame.K_a in keys: dx -= 1
        if pygame.K_d in keys: dx += 1

        if dx != 0 and dy != 0:
            dx *= self.speed / sqrt(2)
            dy *= self.speed / sqrt(2)
        else:
            dx *= self.speed
            dy *= self.speed

        self.x += dx
        self.y += dy
