import pygame
import sys
from tiles import Tile 
from settings import tile_size, screen_width
from player import Player

class Level:
	def __init__(self,level_data,surface):
		
		# level setup
		self.display_surface = surface 
		self.setup_level(level_data)
		self.world_shift = 0
		self.current_x = 0

		# set player to not be on ground
		self.player_on_ground = False

	def get_player_on_ground(self):
		if self.player.sprite.on_ground:
			self.player_on_ground = True
		else:
			self.player_on_ground = False

	def setup_level(self,layout):
		# groups all tiles together
		self.tiles = pygame.sprite.Group()
		# player is separate entity
		self.player = pygame.sprite.GroupSingle()

		# sets up the level as outlined in the settings file
		for row_index,row in enumerate(layout):
			for col_index,cell in enumerate(row):
				x = col_index * tile_size
				y = row_index * tile_size
				
				if cell == 'X':
					tile = Tile((x,y),tile_size)
					self.tiles.add(tile)
				if cell == 'P':
					player_sprite = Player((x,y))
					self.player.add(player_sprite)
				if cell == 'W':
					tile = Tile((x, y), tile_size, 'blue')
					self.tiles.add(tile)

	def scroll_x(self):
		"""Scrolls in x direction when player moves off the screen."""
		# get all information needed to scroll
		player = self.player.sprite
		player_x = player.rect.centerx
		direction_x = player.direction.x

		# scroll left or right
		# if scrolling, player does not actually move, the world moves around them
		if player_x < screen_width / 4 and direction_x < 0:
			self.world_shift = 8
			player.speed = 0
		elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
			self.world_shift = -8
			player.speed = 0
		else:
			self.world_shift = 0
			player.speed = 8

	def horizontal_movement_collision(self):
		# get information about player
		player = self.player.sprite
		player.rect.x += player.direction.x * player.speed
		# player.direction.x => 0 if still, -1 if left, 1 if right

		# detect movement collision in horizontal direction
		for sprite in self.tiles.sprites():
			# if the sprite is colliding with the player rectangle
			if sprite.rect.colliderect(player.rect):
				self.check_win(sprite)
				if player.direction.x < 0: 
					# is not moving horizontally
					player.rect.left = sprite.rect.right
					# on left of tile
					player.on_left = True
					self.current_x = player.rect.left
				elif player.direction.x > 0:
					# moving right
					player.rect.right = sprite.rect.left
					# on right of tile
					player.on_right = True
					self.current_x = player.rect.right

		if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
			player.on_left = False
		if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
			player.on_right = False

	def vertical_movement_collision(self):
		player = self.player.sprite
		# unsurprisingly, just forces the player downwards to the floor
		player.apply_gravity()


		for sprite in self.tiles.sprites():
			# checks whether there is a collision
			if sprite.rect.colliderect(player.rect):
				self.check_win(sprite)
				if player.direction.y > 0: 
					# player is going downwards
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
					player.on_ground = True
				elif player.direction.y < 0:
					# player going upwards
					player.rect.top = sprite.rect.bottom
					player.direction.y = 0
					player.on_ceiling = True

		if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
			# on ground and going up or down
			player.on_ground = False
		if player.on_ceiling and player.direction.y > 0.1:
			# on ceiling and going down significantly
			player.on_ceiling = False

	def check_win(self, sprite):
		if sprite.get_color() == 'blue':
			print('You Win!')
			pygame.quit()
			sys.exit()

	def run(self):

		# level tiles
		# updates and changes everything
		self.tiles.update(self.world_shift)
		self.tiles.draw(self.display_surface)
		self.scroll_x()

		# player
		# update player data and handle collisions
		self.player.update()
		self.horizontal_movement_collision()
		self.get_player_on_ground()
		self.vertical_movement_collision()
		self.player.draw(self.display_surface)
