import pygame
from pygame.constants import QUIT
import random


pygame.init()

FPS=pygame.time.Clock()

screen=width, heith= 720, 1500
BLACK=0, 0, 0
WHITE=255, 255, 255
RED=255, 0, 0
BLUE=0,255,0


scores=0

font=pygame.font.SysFont('Verdana',20)



def push(but):
	mouse=pygame.mouse.get_pos()
	keys=pygame.mouse.get_pressed()
	if but.x<mouse[0]<but.x+but.w:
		if but.y<mouse[1]<but.y+but.h:
			if keys[0]==1:
				return True
		

#Кнопки
up=pygame.Rect((300, 1000), (100, 100))
down=pygame.Rect((300, 1210), (100, 100))
left=pygame.Rect((100, 1210), (100, 100))
right=pygame.Rect((500, 1210), (100, 100))



main_surface=pygame.display.set_mode(screen)

#Ігрок
#ball=pygame.Surface((30, 30))
#ball.fill(WHITE)
ball=pygame.transform.scale(pygame.image.load('player.png').convert_alpha(),(90,50))
bal_rect=ball.get_rect()
ball_sped=5


#Противник
def create_enemy():
	#enemy = pygame.Surface((30,30))
	#enemy.fill(RED)
	enemy=pygame.transform.scale(pygame.image.load('enemy.png').convert_alpha(),(110,40))
	enemy_rect=pygame.Rect(width, random.randint(0, 500), *enemy.get_size())
	enemy_sped=random.randint(2, 5)
	return [enemy, enemy_rect, enemy_sped]

#Бонуси
def create_bonus():
	#bonus = pygame.Surface((30,30))
	#bonus.fill(BLUE)
	bonus=pygame.transform.scale(pygame.image.load('bonus.png').convert_alpha(),(80,80))
	bonus_rect=pygame.Rect(random.randint(0, width), 0, *bonus.get_size())
	bonus_sped=random.randint(2, 5)
	return [bonus, bonus_rect, bonus_sped]
	

#Фон ігри	
bg=pygame.transform.scale(pygame.image.load('background.png').convert(),(720,1000))
#bgX=0
#bgX2=bg.get.width()
#bg_speed=3
	
CREATE_BONUS=pygame.USEREVENT+2
pygame.time.set_timer(CREATE_BONUS, 2500)

CREATE_ENEMY=pygame.USEREVENT+1
pygame.time.set_timer(CREATE_ENEMY, 1500)
	
	
enemies=[]
bonuses=[]

is_working=True

while is_working:
	
	FPS.tick(60)
	
	for event in pygame.event.get():
		if event.type==QUIT:
			is_working=False
		if event.type==CREATE_ENEMY:
			enemies.append(create_enemy())
		if event.type==CREATE_BONUS:
			bonuses.append(create_bonus())
	
		
	#main_surface.fill(BLACK)	
	main_surface.blit(bg,(0,0))
	
	#bgX -=bg_speed
	#bgX2 -=bg_speed
	
	#main_surface.blit(bg(bgX, 0))
	#main_surface.blit(bg(bgX2, 0))
		
	main_surface.blit(ball, bal_rect)
	
	main_surface.blit(font.render(str(scores),True,WHITE), (width-30 ,0))
	
	for enemy in enemies:
		enemy[1]=enemy[1].move(-enemy[2], 0)
		main_surface.blit(enemy[0], enemy[1])
		
		if enemy[1].left<0:
			enemies.pop(enemies.index(enemy))
			
		if bal_rect.colliderect(enemy[1]):
			is_working=False
	
	for bonus in bonuses:
		bonus[1]=bonus[1].move(0, bonus[2])
		main_surface.blit(bonus[0], bonus[1])
		
		if bonus[1].bottom>=1000:
			bonuses.pop(bonuses.index(bonus))
		
		if bal_rect.colliderect(bonus[1]):
			bonuses.pop(bonuses.index(bonus))	
			scores +=1
	
	
	main_surface.fill((RED), up)
	main_surface.fill((RED), down)
	main_surface.fill((RED), left)
	main_surface.fill((RED), right)	
	
	#Рух ігрока
	if push(up):
		bal_rect=bal_rect.move(0,-ball_sped)
	elif push(down):
		bal_rect=bal_rect.move(0,ball_sped)
	elif push(left):
		bal_rect=bal_rect.move(-ball_sped,0)
	elif push(right):
		bal_rect=bal_rect.move(ball_sped,0)
		
	
		
	
			
			
	#main_surface.fill((155, 155, 155))
	
	pygame.display.flip()
	
