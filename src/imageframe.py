import pygame
class ImageFrame:
    
    def __init__(self ,img, scale):
        self.img = pygame.transform.rotozoom(pygame.image.load(img).convert_alpha(),0,scale)
    def draw(self, win, x, y):
        win.blit(self.img, (x,y))
        
        
        
        