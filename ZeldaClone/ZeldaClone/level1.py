import pygame
from settings import *
from tile import tile
from player import player
from Debug import debug

class level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()


    def run(self):
        pass

    def create_map(self):
        for row_index,row in enumerate(world_map):
            for col_index,col in enumerate(row):
                x = col_index * tilesize
                y = row_index * tilesize
                if col == "x":
                    tile((x,y),[self.visible_sprites, self.obstacles_sprites])
                if col =="p":
                    self.player = player((x,y),[self.visible_sprites], self.obstacles_sprites)
                    


    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)



