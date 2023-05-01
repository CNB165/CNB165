import pygame
from player1 import Player1
from monster import Monster

#créer class représente jeu
class Game:
    
    def __init__(self):
        #définir si le jeu a commencé
        self.is_playing = False
        #générer le joueur
        self.all_players = pygame.sprite.Group()
        self.player1 = Player1(self)
        self.all_players.add(self.player1)
        #grp de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        
        
    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        
        
    def game_over(self):
        #remettre le jeu à neuf
        self.all_monsters = pygame.sprite.Group()
        self.player1.health = self.player1.max_health
        self.is_playing = False    
    
        
    def update(self, screen):
        #appliquer les joueurs
        screen.blit(self.player1.image, self.player1.rect)
        #actualiser les BdV
        self.player1.update_health_bar(screen)
        
        
        # récupérer le gravier du joueur
        for gravier in self.player1.all_gravier:
            gravier.move()
        #appliquer le gravier sur le screen
        self.player1.all_gravier.draw(screen)
        
        
        #appliquer les monsters sur l'écran
        self.all_monsters.draw(screen)
        
        #récup les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
        
        
        #joueur gauche ou droite ?
        if self.pressed.get(pygame.K_d) and self.player1.rect.x < 1725:
            self.player1.move_right()
        elif self.pressed.get(pygame.K_q) and self.player1.rect.x > 0:
            self.player1.move_left()
        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)