import os
import pygame
from .config import *

class Player(pygame.sprite.Sprite):

    def __init__(self, left, bottom, dir_images):
        pygame.sprite.Sprite.__init__(self)


        self.images = (
            pygame.image.load(os.path.join(dir_images, "player\corriendo.png") ),
            pygame.image.load(os.path.join(dir_images, "player\saltando.png") )
        )

        self.image = self.images [0]

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        self.pos_y = self.rect.bottom
        self.vel_y = 0

        self.can_jump = False
        self.playing = True

    def collide_with(self, sprites):
        objects =  pygame.sprite.spritecollide(self, sprites, False)
        if objects:
            return objects[0]

    def collide_bottom(self, zombie):
        return self.rect.colliderect(zombie.rect_top)

    def skid(self, zombie):
        self.pos_y = zombie.rect.top 
        self.vel_y = 0
        self.can_jump = True
        self.image = self.images[0]


    def validate_platform(self, platform):
        result = pygame.sprite.collide_rect(self, platform)
        if result:
            self.vel_y = 0
            self.pos_y = platform.rect.top
            self.can_jump = True

            self.image = self.images[0]

    def jump(self):
        if self.can_jump:
            self.vel_y = -23
            self.can_jump = False

            self.image = self.images[1]


    def update_pos(self):
        self.vel_y += PLAYER_GRAV
        self.pos_y += self.vel_y + 0.5 * PLAYER_GRAV

    def update(self):
        if self.playing:
            self.update_pos()

           
    

            self.rect.bottom = self.pos_y

    def stop(self):
        self.playing = False
