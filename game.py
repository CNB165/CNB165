import pygame
from player1 import Player1
from monster import Monster
from comet_event import CometFallEvent
from sounds import SoundManager

#créer class représente jeu
class Game:
    
    def __init__(self):
        #définir si le jeu a commencé
        self.is_playing = False
        #générer le joueur
        self.all_players = pygame.sprite.Group()
        self.player1 = Player1(self)
        self.all_players.add(self.player1)
        #générer l'event
        self.comet_event = CometFallEvent(self)
        #grp de monstre
        self.all_monsters = pygame.sprite.Group()
        #mettre le score à 0
        self.score = 0
        self.pressed = {}
        
        
    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        
        
    def game_over(self):
        #remettre le jeu à neuf
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player1.health = self.player1.max_health
        self.comet_event.reset_percent()
        self.is_playing = False 
        self.score = 0

    
        
    def update(self, screen):
        
        #afficher le score sur l'écran
        font = pygame.font.SysFont("rubik", 22)
        score_text = font.render(f"Score : {self.score}", 1, (255, 255, 255))
        screen.blit(score_text, (20, 20))
        
        
        #appliquer les joueurs
        screen.blit(self.player1.image, self.player1.rect)
        #actualiser les BdV
        self.player1.update_health_bar(screen)
        
        #actualiser la barre d'event du jeu
        self.comet_event.update_bar(screen)
        
        
        #récupérer les comets
        for comet in self.comet_event.all_comets:
            comet.fall()
                
        
        # récupérer le gravier du joueur
        for gravier in self.player1.all_gravier:
            gravier.move()
        #appliquer le gravier sur le screen
        self.player1.all_gravier.draw(screen)
        
        
        #appliquer les monsters sur l'écran
        self.all_monsters.draw(screen)
        
        #appliquer les img du grp de comets
        self.comet_event.all_comets.draw(screen)
        
        #récup les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()
        
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