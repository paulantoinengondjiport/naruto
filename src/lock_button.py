import pygame

class LockButton:
    
    def __init__(self, width, height, x, y, color, pos, text='', pressedText=''):
        self.text = text
        self.pressedText = pressedText
        self.height = height
        self.width = width
        self.isPressed = False
        self.x = x
        self.y = y
        self.color = color
        self.font = pygame.font.Font("../font/njnaruto.ttf", 10)
        self.shinobi = None
        self.pos = pos
    
    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width + 4, self.height+4),0)
        
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            text = self.font.render(self.text,1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
            
    def isOver(self, pos):
        
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
    
        return False
    
    def press(self):
        if not self.isPressed:
            self.isPressed = True
            red = self.color[0] * 0.7
            green = self.color[1] * 0.7
            blue = self.color[2] * 0.7
            self.color = (red,green,blue)
            self.text = self.pressedText
            return self.pos
    