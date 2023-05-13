import pygame

class AnimateSprite(pygame.sprite.Sprite):
    
    #définir les choses à faire à la création de l'entité
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'D:/projet_3/{sprite_name}.png')
        self.current_image = 0 #= commencer l'animation à l'image 0
        self.images = animations.get(sprite_name)
        
    #définir une methode pr animer le sprite
    def animate(self):
        #passer à l'image suivante
        self.current_image += 1
        
        #vérifier si l'on a attient la fin de l'aniamtion
        if self.current_image >= len(self.images):
            #remettre l'animation au départ
            self.current_image = 0
            
        #modifier l'image précédente par la suivante
        self.image = self.images[self.current_image] 
        
        

#définir une def pr charger les img d'un sprite. Ici pcq sinon ça lag
def load_animation_images(sprite_name):
    #charger les 24 img du sprite
    images = []
    #récupérer le chemin du dossier pr ce sprite
    path = f"D:/projet_3/{sprite_name}/{sprite_name}"
    
    #boucler sur chaque img dans ce dossier
    for num in range(1,24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
        
    #renvoyer le contenu de la liste 'images'
    return images


#définir un dico qui va contenir les img chargées de chaque sprite
animations = {
    'ennemi': load_animation_images('ennemi')
}