import pygame 

# this is simply a square in the level to make up the stage
class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,size):
		super().__init__()
		self.image = pygame.Surface((size,size))
		self.image.fill('grey')
		self.rect = self.image.get_rect(topleft = pos)

	def update(self,x_shift):
		# moves as the stage moves
		self.rect.x += x_shift