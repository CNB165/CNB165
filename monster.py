import pygame
import random

class Monster(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('D:/projet_3/ennemi.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1600 + random.randint(0, 300)
        self.rect.y = 725
        self.velocity = random.randint(1, 3)
        
        
    def damage(self, amount#montant de point de vie qu'on doit retirer
               ):
        #infliger les degats
        self.health -= amount
        
        #vérifier si le nb de PV est < à 0
        if self.health <= 0:
            #renouveler le stremon
            self.rect.x = 1600 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health
        
    
    def update_health_bar(self, surface):
        #appliquer la BdV
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 75, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 75, self.rect.y - 10, self.health, 5])
            
    
        
    def forward(self):
        #le déplacement se fait que s'il y a pas de collisions avc un grp de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si collision
        else:
            #infliger des dégâts CàC
            self.game.player1.damage(self.attack)