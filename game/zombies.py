import os 
import pygame
from .config import *


class Zombies (pygame.sprite.Sprite):

    def __init__(self, left, bottom, dir_images):
        pygame.sprite.Sprite.__init__(self)

        self.images = (
            pygame.image.load(os.path.join(dir_images, "zom1.png") ),
            pygame.image.load(os.path.join(dir_images, "zom2.png") ),
            pygame.image.load(os.path.join(dir_images, "zom3.png") ),
            pygame.image.load(os.path.join(dir_images, "zom4.png") ),
            pygame.image.load(os.path.join(dir_images, "zom5.png") ),
            pygame.image.load(os.path.join(dir_images, "zom6.png") ),
            pygame.image.load(os.path.join(dir_images, "zom7.png") ),
            pygame.image.load(os.path.join(dir_images, "zom8.png") ),
            pygame.image.load(os.path.join(dir_images, "zom9.png") ),
            pygame.image.load(os.path.join(dir_images, "zom10.png") ),
            pygame.image.load(os.path.join(dir_images, "zom11.png") ),
            pygame.image.load(os.path.join(dir_images, "zom12.png") ),
            pygame.image.load(os.path.join(dir_images, "zom13.png") ),
            pygame.image.load(os.path.join(dir_images, "zom14.png") ),

        )

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        self.vel_x = SPEED
        self.rect_top = pygame.Rect(self.rect.x, self.rect.y,self.rect.width, 1 )

    def update(self):
        self.rect.left -= self.vel_x
        self.rect_top.x =self.rect.x

    def stop(self):
        self.vel_x = 0
