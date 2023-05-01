import pygame
from game import Game
pygame.init()


#générer la fenêtre
pygame.display.set_caption("Street Fighter")
screen = pygame.display.set_mode((1850, 900))

#importer le bg
background = pygame.image.load("D:/projet_3/fond.png")

#importer le bouton jouer
banner = pygame.image.load('D:/projet_3/bouton_jouer.png')
banner = pygame.transform.scale(banner, (363, 188))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() / 2.5
banner_rect.y = screen.get_height() / 2.5


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
                game.player1.launch_gravier()
            
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #vérif si la souris est sur le bouton
            if banner_rect.collidepoint(event.pos):
                #lancer le jeu
                game.start()