import pygame 
from support import import_folder

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,surface):
		super().__init__()
		self.import_character_assets()
		self.frame_index = 0
		self.animation_speed = 0.15
		self.image = self.animations['idle'][0]
		self.rect = self.image.get_rect(topleft = pos)

		# player movement
		self.direction = pygame.math.Vector2(0,0)
		self.speed = 1000
		self.gravity = 0.8
		self.jump_speed = -16

		# player status
		self.status = 'idle'
		self.facing_right = True
		self.on_ground = False
		self.on_ceiling = False
		self.on_left = False
		self.on_right = False

	def import_character_assets(self):
		character_path = '../graphics/character/'
		self.animations = {'idle':[]}

		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)

	def get_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
			self.facing_right = True
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
			self.facing_right = False
		else:
			self.direction.x = 0

		if keys[pygame.K_SPACE] and self.on_ground:
			self.jump()
			

	def get_status(self):
		if self.direction.y < 0:
			self.status = 'jump'
		elif self.direction.y > 1:
			self.status = 'fall'
		else:
			if self.direction.x != 0:
				self.status = 'run'
			else:
				self.status = 'idle'

	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y

	def jump(self):
		self.direction.y = self.jump_speed

	def update(self):
		self.get_input()
		self.get_status()
		