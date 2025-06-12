import pygame
class ResetButton:
    def __init__(self, width, height, x, y, scale):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.scale = scale
        self.sprite = pygame.transform.rotozoom(pygame.image.load("../img/resetbutton.png").convert_alpha(),0,scale)
        self.isDrawn = False

    def is_over(self, pos):

        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False

    def draw(self, win):

        # pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        win.blit(self.sprite, (self.x, self.y))