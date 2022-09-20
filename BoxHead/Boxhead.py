import pygame
from pygame.locals import *
import random

vec = pygame.math.Vector2 #2 for two dimensional
FPS = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y):
		# nos permite invocar métodos o atributos de Sprite
		super(Player, self).__init__()
		self.surf = pygame.Surface((40, 80))
		self.surf.fill((0, 0, 0))
		self.image = ""
		self.rect = self.surf.get_rect()
		self.pos = vec((x, y))
	
	def update(self):
		self.rect.midbottom = self.pos


pygame.init()

# definir el tamaño de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# crear el objeto pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#pygame.mixer.init()

pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()
pygame.mixer.init()

def play_music(cancion):
    x = pygame.mixer.Sound(cancion)
    x.play()


# instanciamos al jugador
player = Player(50, 50)

f = '8-BIT WONDER.TTF'

def draw_text(text, size, x, y ):
        font = pygame.font.Font(f,size)
        text_surface = font.render(text, True, (0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        screen.blit(text_surface,text_rect)


running = True
speed = 2

while running:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
		elif event.type == QUIT:
			running = False

	pressed_keys = pygame.key.get_pressed()
	if pressed_keys[K_a] and player.pos.x > 0:
		player.pos.x -= speed
	if pressed_keys[K_d] and player.pos.x < SCREEN_WIDTH-40:
		player.pos.x += speed
	if pressed_keys[K_w] and player.pos.y > 0:
		player.pos.y -= speed
	if pressed_keys[K_s] and player.pos.y < SCREEN_HEIGHT-80:
		player.pos.y += speed
		
	# rellena la screen con un color, en este caso blanco
	screen.fill((255, 255, 255))



	# dibujamos al jugador en screen
	player.update()


	screen.blit(player.surf, (player.pos.x, player.pos.y))


	pygame.display.flip()
	FPS.tick(60)