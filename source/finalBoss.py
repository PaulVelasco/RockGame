import os, pygame, sys, helpers, math
from pygame.locals import *
from attack import *
from rocks import Rock
class FinalBoss(pygame.sprite.Sprite):


 def __init__(self, screen):
       pygame.sprite.Sprite.__init__(self)
       self.faceSmile = pygame.image.load('../images/final_boss_head_smile.png')
       self.faceGrowl = pygame.image.load('../images/final_boss_head.png')
       self.leftFist = pygame.image.load('../images/final_boss_left_fist.png')
       self.leftHand = pygame.image.load('../images/final_boss_left_hand.png')
       self.rightFist = pygame.image.load('../images/final_boss_right_fist.png')
       self.rightHand = pygame.image.load('../images/final_boss_right_hand.png')
       self.image = self.faceGrowl
       self.rect = self.image.get_rect()
       self.rect.topleft = (290, 40)
       self.health = 5
       self.bob_timer = 1
       self.attack_timer = 0
       self.attack_group = pygame.sprite.RenderPlain(Leftie(self.leftFist, self.leftHand), PamalaHanderson(self.rightFist, self.rightHand))
       self.screen = screen
       
       
       
 def update(self, player, rocks):
	if self.attack_timer == 0:
		self.__loadShot(player)
		self.attack_timer = 130
	elif self.attack_timer <10:
		self.image = self.faceGrowl
		self.attack_timer -=1
	else:
		self.__bob()
		self.attack_timer -=1
		self.image = self.faceSmile
	
	self.attack_group.update(player, rocks)
	self.attack_group.draw(self.screen)

 def __bob(self):
 	if self.bob_timer > 0:
 		self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1]+1)
 		self.bob_timer +=1
 	else:
 		self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1]-1)
 		self.bob_timer +=1
 	if self.bob_timer > 30:
 		self.bob_timer = -30
 		
 def __loadShot(self, player):
 	target = player
 	if player.hasFriend:
		freind = player.passComp()
		if helpers.distance(player.rect.topleft, self.rect.topleft) > helpers.distance(freind.rect.topleft, self.rect.topleft):
			target = freind    
	attack = Fire_Attack(self.rect.center, target.rect.center, helpers.checkOrient(target, self))
	self.attack_group.add(attack)






class Leftie(pygame.sprite.Sprite):
 def __init__(self, fist, hand):
       pygame.sprite.Sprite.__init__(self)
       self.fist = fist
       self.hand = hand
       self.image = hand
       self.rect = self.image.get_rect()
       self.bob_timer = 0
       self.rect.topleft = (100,80)
       self.cool_down = 0
       self.slam_complete = True
       self.reset_complete = True
       self.placedRock = False
       
   
 def update(self, player, rocks):
 	if helpers.distance(player.rect.topleft, self.rect.topleft) < 15 and self.reset_complete:
			self.image = self.fist
			self.__slam(player, rocks)
			self.cool_down = 60
 	else:
 		self.image = self.hand
 		self.__bob()
 		if self.cool_down > 0:
 			self.cool_down -=1
 		
 def __bob(self):
	if self.reset_complete and self.slam_complete:
		self.image = self.hand
		if self.bob_timer > 0:
			self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1]+1)
			self.bob_timer +=1
		else:
			self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1]-1)
			self.bob_timer +=1
		if self.bob_timer > 20:
			self.bob_timer = -20
	elif self.slam_complete:
		if self.rect.topleft[1] >= 70:
			self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1]-2)
		else:
			self.reset_complete = True
			self.placedRock = False
 		
 def __slam(self, player, rocks):
 	if self.rect.topleft[1] < 200 and self.reset_complete:
 		self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1] +4)
 		self.slam_complete = False
 	else:
 		if not self.placedRock:
 			hit_rock = pygame.sprite.spritecollide(self, rocks, False)
 			for i in range(len(hit_rock)):
 				if hit_rock[i].ID == 1:
 					hit_rock[i].getHit()
 			rocks.add(Rock((self.rect.topleft[0]+50, self.rect.topleft[1]+80)))
 			self.placedRock = True    
 		self.slam_complete = True
 		self.reset_complete = False
 		
 		
class PamalaHanderson(pygame.sprite.Sprite):
 def __init__(self, fist, hand):
       pygame.sprite.Sprite.__init__(self)
       self.fist = fist
       self.hand = hand
       self.image = hand
       self.rect = self.image.get_rect()
       self.bob_timer = 0
       self.rect.topleft = (480,80)
       self.cool_down = 0
       self.slam_complete = True
       self.reset_complete = True
       self.placedRock = False
       
   
 def update(self, player, rocks):
 	if helpers.distance(player.rect.topleft, self.rect.topleft) < 15 and self.reset_complete:
			self.image = self.fist
			self.__slam(player, rocks)
			self.cool_down = 60
 	else:
 		self.image = self.hand
 		self.__bob()
 		if self.cool_down > 0:
 			self.cool_down -=1
 		
 def __bob(self):
	if self.reset_complete and self.slam_complete:
		self.image = self.hand
		if self.bob_timer > 0:
			self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1]+1)
			self.bob_timer +=1
		else:
			self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1]-1)
			self.bob_timer +=1
		if self.bob_timer > 20:
			self.bob_timer = -20
	elif self.slam_complete:
		if self.rect.topleft[1] >= 70:
			self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1]-2)
		else:
			self.reset_complete = True
			self.placedRock = False
 		
 def __slam(self, player, rocks):
 	if self.rect.topleft[1] < 200 and self.reset_complete:
 		self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1] +4)
 		self.slam_complete = False
 	else:
 		if not self.placedRock:
 			hit_rock = pygame.sprite.spritecollide(self, rocks, False)
 			for i in range(len(hit_rock)):
 				if hit_rock[i].ID == 1:
 					hit_rock[i].getHit()
 			rocks.add(Rock((self.rect.topleft[0]+50, self.rect.topleft[1]+80)))
 			self.placedRock = True    
 		self.slam_complete = True
 		self.reset_complete = False