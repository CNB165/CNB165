import pygame

#définir la classe du gravier
class Gravier(pygame.sprite.Sprite):
    def __init__(self, player1):
        super().__init__()
        self.velocity = 10
        self.player1 = player1
        self.image = pygame.image.load('C:/Users/User/Documents/projet_3/gravier.png')
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = player1.rect.x
        self.rect.y = player1.rect.y
        self.origin_image = self.image
        self.angle = 0
        
    def rotate(self):
        #faire tourner le gravier
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)    
    
    
        
    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        #vérifier si le gravier se supprime
        if self.rect.x > 1850:
            #suppr
            self.remove()
            
            
            
    def remove(self):
         self.player1.all_gravier.remove(self)