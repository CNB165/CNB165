import pygame
from comet import Comet

#créer une class pr gérer l'event
class CometFallEvent:
    #créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.fall_mode = False
        
        #définir un grp de sprite pr stocker les comets
        self.all_comets = pygame.sprite.Group()
    
        
    def add_percent(self):
        self.percent += self.percent_speed / 100
    
    def update_bar(self, surface):
        #ajouter du % à la barre
        self.add_percent()
        
        #barre bg
        pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])
        #barre fg
        pygame.draw.rect(surface, (187, 11, 11), [0, surface.get_height() - 20, (surface.get_width()/100) * self.percent, 10])
        
    
    
    
    def is_full_loaded(self):
        return self.percent >=100
    
    def reset_percent(self):
        self.percent = 0
    
    def meteor_fall(self):
        #boucle pr les valeurs entre 1 et 10
        for i in range(1, 20):
            #apparaitre 1 comete
            self.all_comets.add(Comet(self))
   
    def attempt_fall(self):
        #la jauge d'event est chargée
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True #activer l'event