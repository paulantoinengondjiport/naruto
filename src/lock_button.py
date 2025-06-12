import pygame

class LockButton:
    
    def __init__(self, width, height, x, y, pos, scale, text=''):
        self.text = text
        self.height = height
        self.width = width
        self.isPressed = False
        self.x = x
        self.y = y
        self.scale = scale

        self.pressed_button_sprite = pygame.transform.rotozoom(pygame.image.load("../img/pressedbutton.png").convert_alpha(),0,scale)
        self.unpressed_button_sprite = pygame.transform.rotozoom(
            pygame.image.load("../img/unpressedbutton.png").convert_alpha(), 0, scale)
        self.button_sprite = self.unpressed_button_sprite
        self.font = pygame.font.Font("../font/njnaruto.ttf", int(13 * scale))
        self.shinobi = None
        self.pos = pos
    
    def draw(self, win):

        # pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        win.blit(self.button_sprite, (self.x, self.y))
        if self.text != '' and not self.isPressed:
            text = self.font.render(self.text,1, (int(240*0.2),int(235*0.2),int(223*0.2)))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2) + 2 * self.scale, self.y + (self.height/2 - text.get_height()/2) + 2 * self.scale))
            text = self.font.render(self.text,1, (240,235,223))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        elif self.text != '' and self.isPressed:
            text = self.font.render(self.text, 1, (int(240 * 0.2) , int(235 * 0.2), int(223 * 0.2) ))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2) + 2 * self.scale, self.y + (self.height/2 - text.get_height()/2) + int(5 * self.scale)+ 2 * self.scale))
            text = self.font.render(self.text,1, (240,235,223))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2) + int(5 * self.scale)))
            
    def is_over(self, pos):
        
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
    
        return False
    
    def press(self):
        if not self.isPressed:
            self.isPressed = True
            self.button_sprite = self.pressed_button_sprite
            return self.pos
        return None

    def unpress(self):
        self.isPressed = False
        self.button_sprite = self.unpressed_button_sprite
        self.shinobi = None