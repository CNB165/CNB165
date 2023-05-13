import pygame
from game import Game

pygame.init()

#définir une clock
clock = pygame.time.Clock()
FPS = 60


#générer la fenêtre
pygame.display.set_caption("Street Fighter")
screen = pygame.display.set_mode((1850, 900))

#importer le bg
background = pygame.image.load('D:/projet_3/fond.png')

#importer le bouton jouer
banner = pygame.image.load('D:/projet_3/logo.png')
banner = pygame.transform.scale(banner, (866, 318))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() / 3.4
banner_rect.y = screen.get_height() / 3


#charger le jeu
game = Game()

running = True

#boucle fenêtre
while running:
    #appliquer le bg
    screen.blit(background, (0,0))
    
    #vérifier si le jeu a commencé (ou non)
    if game.is_playing:
        #déclencher les instructions de la partie (update)
        game.update(screen)
    #vérifier si le jeu n'a pas commencé
    else:
        #ajouter l'écran 1
        screen.blit(banner, banner_rect)
    
    #le mettre à jour
    pygame.display.flip()
    
    
    #si on ferme
    for event in pygame.event.get():
        #fermeture ?
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture")
        
        # détecter les touches du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
            #détecter touche espace pr le projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player1.launch_gravier()
                else:
                    game.start()
            
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #vérif si la souris est sur le bouton
            if banner_rect.collidepoint(event.pos):
                #lancer le jeu
                game.start()
                
    #fixer le nb de fps sur la clock
    clock.tick(FPS)