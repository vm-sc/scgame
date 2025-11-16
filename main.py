import sys
import pygame

from Player import Player

DISPLAY_SIZE = WIDTH, HEIGHT = (800,800)
FPS = 60

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

keys = set()
 
player = Player(WIDTH/2 - 50, HEIGHT/2 - 50)

while True:
    display.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keys.add(event.key)
        if event.type == pygame.KEYUP:
            keys.remove(event.key)

    player.update(keys)
    player.render(display)
    
    pygame.display.flip()
    clock.tick(FPS)
