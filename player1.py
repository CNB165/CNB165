import pygame
from gravier import Gravier


#créer une classe pr le joueur
class Player1(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 10
        self.all_gravier = pygame.sprite.Group()
        self.image = pygame.image.load('D:/projet_3/1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 700
        
    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            #si le joueur a 0 PV
            self.game.game_over()


    def update_health_bar(self, surface):
        #appliquer la BdV
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 10, self.health, 5])    
        
    
    def launch_gravier(self):
        self.all_gravier.add(Gravier(self))
    
    def move_right(self):
        #que si le player ne le touche pas
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
        
    def move_left(self):
        self.rect.x -= self.velocity