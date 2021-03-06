import os, pygame, sys, math, random
from pygame.locals import *
from enemy import M_Enemy
from dimmer import Dimmer
from levels import Levels
from HUB import Menu

dimmer = Dimmer()
set_enemy = pygame.sprite.RenderPlain()
set_rock = pygame.sprite.RenderPlain()
set_position = (0,0)
enemy_sprites = M_Enemy((500, 50), 1)

"""
I LOVE THIS THEROM TOO MUCH TO NOT MAKE IT A METHOD
""" 

def distance(player, enemy):
    distance = math.sqrt( (abs(player[0] - enemy[0])) + (abs(player[1] - enemy[1])) )
    return distance


"""
Used for enemies to face the player
"""    
   
def checkOrient(player, enemy):
	pX = player.rect.topleft[0]
	pY = player.rect.topleft[1]
	eX = enemy.rect.topleft[0]
	eY = enemy.rect.topleft[1]
	if pX < eX:
		
		if -100 < (pX - eX) <100:
			if pY < eY:
				return "up"
			if pY > eY:
				return "down"
		return "left"
	if pX > eX:
		
		if -100 < (pX - eX) <100:
			if pY < eY:
				return "up"
			if pY > eY:
				return "down"
		return "right"
"""
Shakes for damage or if a boss is big and stompy
""" 		
		
def shake(screen, amplitude):
    amplitude = min(amplitude -1, 100)
    nx = random.randint(-10,10)
    ny = random.randint(-10,10)
    nx *= amplitude/20.0
    ny *= amplitude/20.0
    screen.blit(screen, (nx,ny))
    return amplitude
    
    
def fadeOut(screen, amplitude):
    amplitude = min(amplitude-1, 100)
    surf = pygame.Surface(screen.get_size())
    surf.set_alpha(amplitude*10)
    screen.blit(surf, (0, 0))
    return amplitude
    
"""
Makes sure no ones going through any walls
"""     
    
def checkBoundry(position):
	new_x = position[0]
	new_y = position[1]
	if position[0] <= 15:
		new_x = 15
	if position [0] >= 600:
		new_x = 600
	if position [1] <= 15:
		new_y = 15
	if position[1] >= 430:
		new_y = 430
	return (new_x, new_y)


def set(level, position):
	global set_enemy
	print level
	set_enemy = Levels().getSingleEnemy(level)
	global set_rock 
	set_rock = Levels().getSingleRocks(level)
	global set_position 
	set_position= position #referring to player position
def reset(level, windowSurface):
	set_rocks = Levels().createLevels_Rock()
	level_rocks = set_rocks[level]
	set_enemy = Levels().createLevels_enemies(windowSurface)
	level_enemy = set_enemy[level]
	return [set_enemy, set_rocks]

"""
Pause screen loop is here
"""	

def pauseBalls(windowSurface): #by going up stairs, pauseballs, by going down stairs
    my_font = pygame.font.SysFont('Verdana', 15, True)
    option = 0
    reset = 0
    paused = True
    dimmer.dim()
    menu = Menu((480, 51), (255, 255, 204), 
       (102, 0, 0), my_font, ["Resume", "Restart", "Exit"])
    while (paused == True):
       menu.update_box()
       pygame.display.update()
       for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0) # Clicking the x now closes the game, not ESC
        if event.type ==KEYUP:
        	if event.key == K_ESCAPE:
        	   paused = False
        	if event.key == K_DOWN:
        	   menu.next_down()
        	if event.key == K_UP:
        	   menu.next_up()
        	if event.key == K_RETURN:
        	   option = menu.get_position()
        	   if option == 0:
        	      paused = False
        	   if option == 1:
        	      reset = 1
        	      paused = False
        	   if option == 2:
        	      sys.exit(0)
    dimmer.undim()
    return reset
    
def dead(windowSurface):
    option = 0
    reset = 0
    paused = True
    dimmer.dim()
    menu = Menu((480, 51), (255, 255, 204), 
       (102, 0, 0), pygame.font.SysFont('Verdana', 15), ["Load Checkpoint", "Restart", "Exit"])
    while (paused == True):
       menu.update_box()
       pygame.display.update()
       for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0) # Clicking the x now closes the game, not ESC
        if event.type ==KEYUP:
        	if event.key == K_ESCAPE:
        	   paused = False
        	if event.key == K_DOWN:
        	   menu.next_down()
        	if event.key == K_UP:
        	   menu.next_up()
        	if event.key == K_RETURN:
        	   option = menu.get_position()
        	   if option == 0:
        	      paused = False
        	      return reset
        	   if option == 1:
        	      reset = 5
        	      paused = False
        	      return reset
        	   if option == 2:
        	      sys.exit(0)
    dimmer.undim()
    
