import os
import sys
import pygame
import random

from.config import *
from .platform import Platform
from .player import Player 

class Game:
    def __init__(self):
        pygame.init()

        self.surface = pygame.display.set_mode((WIDTH,HEIGHT ))
        pygame.display.set_caption(TITLE)
        
        self.running = True

    def start(self):
        self.new()

    def new(self):
        self.run()

    def generate_elements(self):
        self.platform = Platform()
        self.player = Player(100, self.platform.rect.top - 200, self.dir_images) 
        
    
        self.sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()


        self.sprites.add(self.platform)
        self.sprites.add(self.player)

        self.generate_walls() 

    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

    def draw(self):
        pass

    def update(self):
        pygame.display.flip()

    def stop(self):
        pass

    


                
 

                      