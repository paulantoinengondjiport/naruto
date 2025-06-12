import csv
import pygame
from character import Character
from lock_button import LockButton
import random

random.seed()
pygame.init()
scale_factor = 1.3
characters = []
background_colour = (240,235,223)
width = int(900 * scale_factor)
height = int(700 * scale_factor)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Create your Shinobi")
frame = pygame.transform.rotozoom(pygame.image.load("../img/frame.png"),0,scale_factor)
pygame.display.flip()
clock = pygame.time.Clock()
background = pygame.transform.rotozoom(pygame.image.load("../img/background.png").convert_alpha(), 0, scale_factor)
fontrank = pygame.font.Font("../font/njnaruto.ttf", int(70 * scale_factor))
font = pygame.font.Font("../font/njnaruto.ttf", int(50 * scale_factor))
main_text_font = pygame.font.Font("../font/njnaruto.ttf",int(150 * scale_factor))
main_text = main_text_font.render("Choose !",1,(240,235,224))
main_text_shadow = main_text_font.render("Choose !",1,(int(240 * 0.2),int(235 * 0.2),int(224 * 0.2)))
shading_surf = pygame.Surface((width,height))
shading_surf.set_alpha(128)
shading_surf.fill((54,54,65))
# End screen
shading_surf_end = pygame.Surface((width,height))
shading_surf_end.set_alpha(128)
shading_surf_end.fill((54,54,65))
closed_scroll = pygame.transform.rotozoom(pygame.image.load("../img/closed_scroll.png"),0,scale_factor)
open_scroll = pygame.transform.rotozoom(pygame.image.load("../img/open_scroll.png"),0,scale_factor)
scroll_offset = -open_scroll.get_width()
# Create and store the characters/shinobi objects
with open("characters.csv",mode="r") as file:
    csv_reader = csv.DictReader(file)
    data_list = []
    for row in csv_reader:
        data_list.append(row)
for shinobi in data_list:
    characters.append(Character(shinobi,scale_factor))

# Create lock buttons
button_colour = (70,145,204)
button_width = int(100 * scale_factor)
button_height = int(40 * scale_factor)
ninjutsu_button = LockButton(button_width, button_height,int(200 * scale_factor),int(175 * scale_factor),button_colour, 0, scale_factor, "Ninjutsu")
genjutsu_button = LockButton(button_width, button_height,int(400 * scale_factor),int(175 * scale_factor),button_colour, 1, scale_factor, "Genjutsu")
taijutsu_button = LockButton(button_width, button_height,int(600 * scale_factor),int(175 * scale_factor),button_colour, 2, scale_factor,"Taijutsu")
battleiq_button = LockButton(button_width, button_height,int(200 * scale_factor),int(475 * scale_factor),button_colour, 3, scale_factor,"Battle IQ")
kekkeigenkai_button = LockButton(button_width, button_height,int(400 * scale_factor),int(475 * scale_factor),button_colour, 4, scale_factor,"Kekkei Genkai")
chakratype_button = LockButton(button_width, button_height,int(600 * scale_factor),int(475 * scale_factor),button_colour, 5, scale_factor,"Chakra  Type")

button_list = [ninjutsu_button, battleiq_button,
               genjutsu_button, kekkeigenkai_button,
               taijutsu_button, chakratype_button]

# Selected shinobis
selected_list = []
selected_list_pos = [(int(200 * scale_factor),int(70 * scale_factor)),(int(400 * scale_factor),int(70 * scale_factor)),(int(600 * scale_factor),int(70 * scale_factor)),
                     (int(200 * scale_factor),int(530 * scale_factor)),(int(400 * scale_factor),int(530 * scale_factor)),(int(600 * scale_factor),int(530 * scale_factor))]
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
    screen.blit(background, (0,0))
    screen.blit(shading_surf,(0,0))
    screen.blit(main_text_shadow, ((width / 2 - main_text.get_width() / 2) + int(5 * scale_factor),
                                   (height / 2 - main_text.get_height() / 2) + int(5 * scale_factor)))
    screen.blit(main_text,((width/2 - main_text.get_width()/2),(height/2 - main_text.get_height()/2)))
    screen.blit(closed_scroll, (int(-3*scale_factor), int(229 * scale_factor)))
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
                    if b.is_over(pos) and howManyFrames >= 20:
                        pressedButtonPos = b.press()
                        howManyFrames = 0
                        b.shinobi = selected_list[b.pos]
                        for k in range(len(toCheck)):
                            if b.pos == toCheck[k]:
                                toPop = k
                        toCheck.pop(toPop)




    if len(toCheck) > 0:
        for i in toCheck:
            if howManyFrames < 20:
                selected_list[i] = characters[random.randint(0,len(characters) - 1)]
            selected_list[i].img.draw(screen,
                                      selected_list_pos[i][0],
                                      selected_list_pos[i][1])
            screen.blit(frame,(selected_list_pos[i][0],selected_list_pos[i][1]))
            
    for fixedCharacterButton in button_list:
        if fixedCharacterButton.shinobi is not None:
            fixedCharacterButton.shinobi.img.draw(screen,
                                                      selected_list_pos[fixedCharacterButton.pos][0],
                                                      selected_list_pos[fixedCharacterButton.pos][1])
            screen.blit(frame,(selected_list_pos[fixedCharacterButton.pos][0],selected_list_pos[fixedCharacterButton.pos][1]))
                
    
    
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
        if scroll_offset < 0:
            scroll_offset += int(6 * scale_factor)
        screen.blit(shading_surf_end, (0,0))
        screen.blit(open_scroll, (int(-3 * scale_factor) + scroll_offset, int(229 * scale_factor)))


        rank_text = fontrank.render(rank ,1,(246, 108, 45))
        text = font.render("Top " + str(61 - total_score) + " Shinobi",1,(54, 54, 65))
        screen.blit(rank_text, ((width/2 - rank_text.get_width()/2) + scroll_offset ,int(270 * scale_factor)))
        screen.blit(text, ((width/2 - text.get_width()/2) + scroll_offset,int(370 * scale_factor)))
        screen.blit(closed_scroll,(int(-3*scale_factor),int(229 * scale_factor)))
    pygame.display.update()
    howManyFrames += 1
    clock.tick(60)