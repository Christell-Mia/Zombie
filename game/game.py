import os
import sys
import pygame
import random

from.config import *
from .platform import Platform
from .player import Player 
from .zombies import Zombies
from .heart import Heart


class Game:
    def __init__(self):
        pygame.init()

        self.surface = pygame.display.set_mode((WIDTH,HEIGHT ))
        pygame.display.set_caption(TITLE)
        
        self.running = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.match_font(FONT)
        self.dir = os.path.dirname(__file__)
        self.dir_sounds = os.path.join(self.dir, "sounds")
        self.dir_images = os.path.join(self.dir, "Images")

        sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, "music.mp3"))
        sound.play()

    def start(self):
        self.menu
        self.new()

    def new(self):
        self.score = 0
        self.level = 0
        self.playing = True
        self.background = pygame.image.load(os.path.join(self.dir_images, "fondo.png"))
        self.generate_elements()
        self.run()
        self.run()

    def generate_elements(self):
        self.platform = Platform()
        self.player = Player(100, self.platform.rect.top - 200, self.dir_images) 
        
    
        self.sprites = pygame.sprite.Group()
        self.zombies = pygame.sprite.Group()
        self.heart = pygame.sprite.Group()


        self.sprites.add(self.platform)
        self.sprites.add(self.player)

        self.generate_zombies() 

    def score_format(self):
        return "Score : {}".format(self.score)

    def level_format(self):
        return "Level : {}".format(self.level)

    def generate_zombies(self):
        last_position = WIDTH + 100

        if not len(self.zombies) > 0:
            for w in range(0,MAX_ZOMBIES):
                left = random.randrange(last_position + 200, last_position + 400 )
                zombies = Zombies(left, self.platform.rect.top, self.dir_images)

                last_position  = zombies.rect.right

                self.sprites.add(zombies)
                self.zombies.add(zombies)
            
            self.level += 1
            self.generate_heart()

    def generate_heart(self):
        last_position = WIDTH + 100
        
        for c in range(0,MAX_HEARD):

            pos_x = random.randrange(last_position + 180, last_position + 300)
            heart = Heart(pos_x, 150, self.dir_images)
            last_position = heart.rect.right
            self.sprites.add(heart)
            self.heart.add(heart)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
        
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            self.player.jump()


        if key[pygame.K_r] and not self.playing:
            self.new()

    def draw(self):
        self.surface.blit(self.background, (0,0))
        self.draw_text()
        self.sprites.draw(self.surface)

        pygame.display.flip()

    def update(self):
        if not self.playing:
            return
        
        zombie = self.player.collide_with(self.zombies)
        if zombie:
                if self.player.collide_bottom(zombie):
                    self.player.skid(zombie)
                else:
                    self.stop()

        
        heart = self.player.collide_with(self.heart)
        if heart:
                self.score += 1
                heart.kill()
            
                

                sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, "heart.mp3"))
                sound.play()


        self.sprites.update()
        self.player.validate_platform(self.platform)
        self.update_elements(self.zombies)
        self.update_elements(self.heart)
        self.generate_zombies()        
    
    def update_elements(self, elements):
        for element in elements:
            if not element.rect.right > 0:
                element.kill()  

    def stop(self):
        self.player.stop()
        self.stop_element(self.zombies)
        self.playing = False 

    def stop_element(self, elements):
        for element in elements:
            element.stop()

    def draw_text(self):
       self.display_text( str(self.score_format()), 36, BROWN, WIDTH // 2, 30) 
       self.display_text( str(self.level_format()), 36, BROWN, WIDTH // 13, TEXT_POSY)
       
       if not self.playing:
           self.display_text( "Perdiste", 60, BLACK, WIDTH // 2, HEIGHT // 2 )
           self.display_text( "Presiona r para comenzar de nuevo", 30, BLACK, WIDTH // 2, 100 )
           
    def display_text(self, text, size, color, pos_x, pos_y):
        font = pygame.font.Font(self.font, size)

        text = font.render(text, True, color)
        rect = text.get_rect()
        rect.midtop = (pos_x, pos_y)

        self.surface.blit(text, rect) 
 
    def menu(self):
         self.surface.fill(GREEN_LIGHT)
         self.display_text("Presiona una tecla para comenzar", 36, BLACK, WIDTH // 2, 10 )
          
         pygame.display.flip()

         self.wait()
    
    def wait(self):
        wait = True

        while wait:
            self.clock.tick(FPS)

            for event in  pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.running = False
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYUP:
                wait = False  
    


                
 

                      