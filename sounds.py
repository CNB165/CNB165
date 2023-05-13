import pygame

class SoundManager:
    
    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound("D:/projet_3/sounds/click.ogg"),
            'game_over': pygame.mixer.Sound("D:/projet_3/sounds/game_over.ogg"),
            'meteorite': pygame.mixer.Sound("D:/projet_3/sounds/meteorite.ogg"),
            'tir': pygame.mixer.Sound("D:/projet_3/sounds/tir.ogg"),
        }
        
    def play(self, name):
        self.sounds[name].play()