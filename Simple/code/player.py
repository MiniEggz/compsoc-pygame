import pygame 


class Player(pygame.sprite.Sprite):

	#Setup the player
	def __init__(self,pos,surface):
		super().__init__()
		self.frame_index = 0
		self.animation_speed = 0.15
		self.image = pygame.image.load("../graphics/1.png")
		self.rect = self.image.get_rect(topleft = pos)

		# player movement
		self.direction = pygame.math.Vector2(0,0)
		self.speed = 8
		self.gravity = 0.8
		self.jump_speed = -16

		# player status
		self.status = 'idle'
		self.facing_right = True
		self.on_ground = False
		self.on_ceiling = False
		self.on_left = False
		self.on_right = False

	#Gets the user
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

	#Gets the player status
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

	#Is used to make the player be able to fall
	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y

	#Is used to make the player be able to jumper
	def jump(self):
		self.direction.y = self.jump_speed

	#Updates player
	def update(self):
		self.get_input()
		self.get_status()
		