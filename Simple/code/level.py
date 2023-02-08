import pygame, sys
from tiles import Tile 
from settings import tile_size, screen_width
from player import Player


class Level:
	#Set up the class
	def __init__(self,level_data,surface):
		self.max_speed = 8
		# level setup
		self.display_surface = surface
		self.setup_level(level_data) #takes the setting files to use to set up the tiles
		self.world_shift = 0  #Value for scrolling along the x
		self.current_x = 0	  #Current value of x of the player


	#Sets ground variable
	def get_player_on_ground(self):
		if self.player.sprite.on_ground:
			self.player_on_ground = True
		else:
			self.player_on_ground = False

	#Sets up the tiles on the level
	def setup_level(self,layout):
		self.tiles = pygame.sprite.Group() #Sets up the group of sprites of tiles and groups them
		self.player = pygame.sprite.GroupSingle() #Sets the player sprite

		#Adds all the tiles according to the setting file
		for row_index,row in enumerate(layout):
			for col_index,cell in enumerate(row):
				x = col_index * tile_size
				y = row_index * tile_size


				if cell == 'X': #Adds a tile
					tile = Tile((x,y),tile_size,"lime")
					self.tiles.add(tile)
				elif cell == 'P': #Adds the player
					player_sprite = Player((x,y), self.display_surface)
					self.player.add(player_sprite)
				elif cell == 'E': #Adds the win tile
					tile = Tile((x, y), tile_size, "blue")
					self.tiles.add(tile)

	#Makes it so the map scrolls along the x
	def scroll_x(self):
		#Gets the player info used
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
			player.speed = self.max_speed

	#Makes win condition
	def win(self):
		#Gets the info of the player
		player = self.player.sprite
		player.rect.x += player.direction.x * player.speed
		player.apply_gravity()

		for sprite in self.tiles.sprites(): #Checks if any of the tiles collide
			if sprite.rect.colliderect(player.rect):
				if sprite.get_colour() == "blue": #Checks if the tile is the win one - we are doing this via colour
					print("YOU WINNNNNNNN")
					pygame.quit()
					sys.exit()

	#Checks if player is colliding with tiles on the x
	def horizontal_movement_collision(self):
		#Gets the info about the player
		player = self.player.sprite
		player.rect.x += player.direction.x * player.speed

		#Checks if there is movement collision in horizontal direction
		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect): #If statement to check collision
				if player.direction.x < 0: 
					player.rect.left = sprite.rect.right
					player.on_left = True
					self.current_x = player.rect.left
				elif player.direction.x > 0:
					player.rect.right = sprite.rect.left
					player.on_right = True
					self.current_x = player.rect.right

		if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
			player.on_left = False
		if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
			player.on_right = False

	#Checks if player is colliding with tiles on the y - same as above but along y
	def vertical_movement_collision(self):
		player = self.player.sprite
		player.apply_gravity()

		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):

				if player.direction.y > 0: 
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
					player.on_ground = True
				elif player.direction.y < 0:
					player.rect.top = sprite.rect.bottom
					player.direction.y = 0
					player.on_ceiling = True

		if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
			player.on_ground = False
		if player.on_ceiling and player.direction.y > 0.1:
			player.on_ceiling = False

	#runs the level
	def run(self):


		# level tiles
		self.tiles.update(self.world_shift)
		self.tiles.draw(self.display_surface)
		self.scroll_x()
		#self.scroll_y()


		# player
		self.player.update()
		self.horizontal_movement_collision()
		self.get_player_on_ground()
		self.vertical_movement_collision()
		self.win()
		self.player.draw(self.display_surface)
