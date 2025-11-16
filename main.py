import sys
import pygame

DISPLAY_SIZE = WIDTH, HEIGHT = (800,800)
FPS = 60

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.image = pygame.Surface((75,75)) 
        self.image.fill((255,0,0))
        self.x, self.y = 50, 50

        self.moving_right, self.moving_up, self.moving_left, self.moving_down = False, False, False, False
        
    def update(self):
        if self.moving_right: self.x += 5
        if self.moving_left: self.x -= 5
        if self.moving_up: self.y -= 5
        if self.moving_down: self.y += 5

    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))

player = Player()
 
while True:
    display.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.moving_up = True
            if event.key == pygame.K_s:
                player.moving_down = True
            if event.key == pygame.K_a:
                player.moving_left = True
            if event.key == pygame.K_d:
                player.moving_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.moving_up = False
            if event.key == pygame.K_s:
                player.moving_down = False
            if event.key == pygame.K_a:
                player.moving_left = False
            if event.key == pygame.K_d:
                player.moving_right = False

    player.update()
    player.render(display)
    
    pygame.display.flip()
    clock.tick(FPS)
