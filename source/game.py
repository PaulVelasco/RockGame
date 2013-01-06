#!/usr/bin/env python

#!/usr/bin/env python

import os, pygame, sys
from pygame.locals import *

pygame.init()


player = pygame.image.load('../images/hero_placeholder.png')
HEIGHT = 500
WIDTH = 675
"Window 675 x 500"
windowSurface = pygame.display.set_mode((WIDTH,HEIGHT))
x = WIDTH / 2
y = HEIGHT / 2
# new_position = (x,y)

BLACK = pygame.Color(255,255,255) #Temp background
fpsClock = pygame.time.Clock()
windowSurface.blit(player, (x,y))

pygame.key.set_repeat(1, 10)
while True:
    windowSurface.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0) # Clicking the x now closes the game, not ESC
    
    keys = pygame.key.get_pressed()
    
    if keys[K_LEFT]:
        x -= 10
        if x <= 0:
            x = 0
    if keys[K_RIGHT]:
        x += 10
        if x >= 643:
            x = 643        
    if keys[K_DOWN]:
        y += 10
        if y >= 468:
            y = 468
    if keys[K_UP]:
        y -= 10
        if y <= 0:
            y = 0
        
    windowSurface.blit(player, (x,y))
    pygame.display.update()
    fpsClock.tick(30)

    
    
