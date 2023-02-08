import pygame


# this is simply a square in the level to make up the stage
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, color="grey"):
        # tiles will default to being grey, other colours may be reserved for something like the win tile
        super().__init__()
        self.color = color
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)

    def get_color(self):
        return self.color

    def update(self, x_shift):
        # moves as the stage moves
        self.rect.x += x_shift
