import pygame
import random

#créer une classe pr la comet
class Comet(pygame.sprite.Sprite):
    
    def __init__(self, comet_event):
        super().__init__() #charger le sprite
        #définir l'img
        self.image = pygame.image.load('D:/projet_3/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(2, 4)
        self.rect.x = random.randint(15, 1700)
        self.rect.y -= random.randint(0, 200)
        self.comet_event = comet_event
        
    def fall(self):
        self.rect.y += self.velocity
        
        #ne tombe pas sur le sol
        if self.rect.y >= 700:
            self.remove()
            
            #s'il n'y a plus de comete
            if len(self.comet_event.all_comets) == 0:
                #remettre la jauge au départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
            
        #vérifier si la comet touche le joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            # enlever la comete
            self.remove()
            #faire subir des dégâts (20)
            self.comet_event.game.player1.damage(20)
            
    def remove(self):
        self.comet_event.all_comets.remove(self)
        
        #vérifier si le nombre de comètes est de 0
        if len(self.comet_event.all_comets) == 0:
            #remettre la barre à 0
            self.comet_event.reset_percent()
            #apparaitre les 2 1er stremon
            self.comet_event.game.start()