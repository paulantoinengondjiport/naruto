import glob
import csv
import pygame
from character import Character
from lock_button import LockButton
from PIL import Image
from PIL.ExifTags import TAGS
import random

random.seed()
pygame.init()
characters = []
background_colour = (240,235,223)
screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Create your Shinobi")
screen.fill(background_colour)
pygame.display.flip()
clock = pygame.time.Clock()
konoha_logo = pygame.image.load("../img/konoha_logo.png").convert_alpha()
fontrank = pygame.font.Font("../font/njnaruto.ttf", 70)
font = pygame.font.Font("../font/njnaruto.ttf", 50)
# Create and store the characters/shinobi objects
with open("characters.csv",mode="r") as file:
    csv_reader = csv.DictReader(file)
    data_list = []
    for row in csv_reader:
        data_list.append(row)
for shinobi in data_list:
    characters.append(Character(shinobi))

# Create lock buttons
button_colour = (70,145,204)
button_width = 100
button_height = 40
ninjutsu_button = LockButton(button_width, button_height,250,175,button_colour, 0, "Lock Ninjutsu", "Ninjutsu")
genjutsu_button = LockButton(button_width, button_height,250,375,button_colour, 1, "Lock Genjutsu", "Genjutsu")
taijutsu_button = LockButton(button_width, button_height,250,575,button_colour, 2, "Lock Taijutsu", "Taijutsu")
battleiq_button = LockButton(button_width, button_height,550,175,button_colour, 3, "Lock Battle IQ", "Battle IQ")
kekkeigenkai_button = LockButton(button_width, button_height,550,375,button_colour, 4, "Lock Kekkei Genkai", "Kekkei Genkai")
chakratype_button = LockButton(button_width, button_height,550,575,button_colour, 5, "Lock Chakra  Type", "Chakra  Type")

button_list = [ninjutsu_button, battleiq_button,
               genjutsu_button, kekkeigenkai_button,
               taijutsu_button, chakratype_button]

# Selected shinobis
selected_list = []
selected_list_pos = [(250,50),(250,250),(250,450),
                     (550,50),(550,250),(550,450)]
for i in range(6):
    selected_list.append(characters[0])

# game loop
running = True
howManyFrames = 0
toCheck = [0,1,2,3,4,5]
toPop = 0
scored = False
total_score = 0
rank = ""
while running:
    
    
# for loop through the event queue  
    for event in pygame.event.get():
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                for b in button_list:
                    if b.isOver(pos) and howManyFrames >= 20:
                        pressedButtonPos = b.press()
                        howManyFrames = 0
                        b.shinobi = selected_list[b.pos]
                        for k in range(len(toCheck)):
                            if b.pos == toCheck[k]:
                                toPop = k
                        toCheck.pop(toPop)
                        
                                
                        
    screen.blit(konoha_logo, (100,100))
    if len(toCheck) > 0:
        for i in toCheck:
            if howManyFrames < 20:
                selected_list[i] = characters[random.randint(0,len(characters) - 1)]
            selected_list[i].img.draw(screen,
                                      selected_list_pos[i][0],
                                      selected_list_pos[i][1])
            
    for fixedCharacterButton in button_list:
        if fixedCharacterButton.shinobi != None:
            fixedCharacterButton.shinobi.img.draw(screen,
                                                      selected_list_pos[fixedCharacterButton.pos][0],
                                                      selected_list_pos[fixedCharacterButton.pos][1])
                
    
    
    for b in button_list:
        b.draw(screen)
    if scored == False and len(toCheck) < 1:
        for b in button_list:
            total_score += int(b.shinobi.attributes[b.pos])
        scored = True
        if total_score < 15:
            rank = "Chunin"
        elif total_score < 25:
            rank = "Jounin"
        elif total_score < 41:
            rank = "Elite Juunin"
        elif total_score < 51:
            rank = "Legendary Shinobi"
        elif total_score < 56:
            rank = "Kage"
        else:
            rank = "Shinobi God"
    if scored:
        rank_text = fontrank.render(rank ,1,(246, 108, 45))
        text = font.render("Top " + str(61 - total_score) + " Shinobi",1,(54, 54, 65))
        screen.blit(rank_text, (300,200))
        screen.blit(text, (300,300))
    pygame.display.update()
    print(total_score)
    howManyFrames += 1
    clock.tick(60)