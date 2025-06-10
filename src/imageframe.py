import pygame

class ImageFrame:
    
    def __init__(self ,img):
        self.img = pygame.image.load(img).convert_alpha()
        
    def draw(self, win, x, y):
        win.blit(self.img, (x,y))
        
        
        
        