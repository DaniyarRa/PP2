def Starting():
    SCREEN.blit(Snake_Back,(900,50))
    SCREEN.blit(Text_1, (500, 20))
    SCREEN.blit(Choose_Level,(100, 100))
    SCREEN.blit(Choose_Level_2,(400,80))
    SCREEN.blit(Text_2, (160,215))
    SCREEN.blit(Text_3_1,(510, 120))
    SCREEN.blit(Text_3_2,(480, 203))
    SCREEN.blit(Text_3_3,(510, 290))
    SCREEN.blit(Choose_Level,(100, 320))
    SCREEN.blit(Choose_Players,(15,430))
    SCREEN.blit(Text_4,(160,435))
    SCREEN.blit(Text_4_1,(60,523))
    SCREEN.blit(Text_4_2,(275,523))
    SCREEN.blit(Play, (500, 400))
def restart():
    the_mod_is_chosen = False
    the_level_is_chosen = False
    snake.elementy = [[1280, 200]]
    snake.dlina = 1
    snake.cord_po_x = 0
    snake.cord_po_y = 10
    snake.dovavit_chast = False
    snake.level = 1
    snake2.elementy = [[100, 200]]
    snake2.dlina = 1
    snake2.cord_po_x = 0
    snake2.cord_po_y = 10
    snake2.dovavit_chast = False
    snake2.level = 1
    
import pygame
import random
import sys
import json
#pylint:disable=no-member
pygame.init()
WIDTH = 1380
HEIGHT = 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zmeika")

is_running = True
start_the_game = False
the_mod_is_chosen = False
the_level_is_chosen = False

class Zmeika:
    def  __init__(self):
        
        self.elementy = [[1280, 200]]
        self.dlina = 1
        self.shag = 10
        #self.razmer = 5
        #self.uroven = 1
        self.cord_po_x = 0
        self.cord_po_y = 10
        self.dovavit_chast = False
        self.level = 1
        self.skin = Yellow_Snake_Texture
        
    def dvizhenie(self):
        if self.dovavit_chast == True:
            self.dlina += 1
            self.elementy.append([0,0])
            self.dovavit_chast = False
        
        
        for i in range(len(self.elementy) - 1, 0, -1):
            self.elementy[i][0] = self.elementy[i - 1][0]
            self.elementy[i][1] = self.elementy[i - 1][1]
        
        
        self.elementy[0][0] += self.cord_po_x
        self.elementy[0][1] += self.cord_po_y

        

        
        

    def narisovka(self):
        for element in self.elementy:
            SCREEN.blit(self.skin, element)
            #pygame.draw.circle(SCREEN,RED, element,self.razmer)
class Eda:
    def __init__(self):
        self.fruits = [Mango_Texture, Strawberry_Texture, Apple_Texture]
        self.show_rand_fruit = random.randint(0, len(self.fruits) - 1)
        self.dx = random.randint(20, 1360)
        self.dy = random.randint(20, 680)
        self.fruit_was_eaten = False
    def show_fruit(self):
        if self.fruit_was_eaten == True:
            self.dx = random.randint(20, 1360)
            self.dy = random.randint(20, 680)
            if snake.level >= 2:
                while (self.dx >= 684 and self.dx <= 696 and self.dy >= 100 and self.dy <= 600) or (self.dx >= 200 and self.dx <= 1180 and self.dy >= 344 and self.dy <= 356):
                    self.dx = random.randint(20, 1360)
                    self.dy = random.randint(20, 680)
                if snake.level == 3:
                    while (self.dx >= 342 and self.dx <= 1038 and self.dy >= 172 and self.dy <= 184) or (self.dx >= 342 and self.dx <= 1038 and self.dy >= 528 and self.dy <= 540) or (self.dx >= 342 and self.dx <= 354 and self.dy >= 258 and self.dy <= 450) or(self.dx >= 1026 and self.dx <= 1038 and self.dy >= 258 and self.dy <= 450):
                        self.dx = random.randint(20, 1360)
                        self.dy = random.randint(20, 680)
            
            self.show_rand_fruit = random.randint(0, len(food.fruits) - 1)
            #snake.dovavit_chast = True
            self.fruit_was_eaten = False
            

        SCREEN.blit(self.fruits[self.show_rand_fruit], (self.dx, self.dy))





 

pygame.mixer.music.load('5e7dc8338369265.mp3')
sound1 = pygame.mixer.Sound('81cebf7e45fdef7 (1).mp3')
sound1.play(-1)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
    
#imported pictures
Yellow_Snake_Texture = pygame.image.load(r'C:\Users\danii\Documents\Work\Yellow_Snake_Texture (1) (1) (1).png')
Red_Snake_Texture = pygame.image.load(r'C:\Users\danii\Documents\Work\Red_Snake_Texture (1) (1).png')
Mango_Texture = pygame.image.load(r'C:\Users\danii\Documents\Work\1-2-mango-png_800x800 (2).png')
Strawberry_Texture = pygame.image.load(r'C:\Users\danii\Documents\Work\1-strawberry-png-images (1).png')
Apple_Texture = pygame.image.load(r'C:\Users\danii\Documents\Work\9-apple-png-image (1).png')
Snake_Back = pygame.image.load(r'C:\Users\danii\Documents\Work\PinClipart.com_viper-clipart_5532593 (2).png')
Choose_Level = pygame.image.load(r'C:\Users\danii\Documents\Work\—Pngtree—cartoon button button icon icon_3797082 (2).png')
Choose_Level_2 = pygame.image.load(r'C:\Users\danii\Documents\Work\Lovepik_com-401151017-cartoon-button-click-button (2).png')
Choose_Players = pygame.image.load(r'C:\Users\danii\Documents\Work\favpng_creative-cartoon-button-border (2).png')
Play = pygame.image.load(r'C:\Users\danii\Documents\Work\start-button-green-arrow-357247 (3).png')
#usable texts and etc
Font_1 = pygame.font.SysFont('cambria', 75)
Text_1 = Font_1.render('Snake',True, GREEN)
Font_2 = pygame.font.SysFont('cambria', 25)
Text_2 = Font_2.render('Choose a level:', True, WHITE)
Font_3 = pygame.font.SysFont('cambria', 35)
Text_3_1 = Font_3.render('EASY', True, WHITE)
Text_3_2 = Font_3.render('NORMAL', True, WHITE)
Text_3_3 = Font_3.render('HARD', True, WHITE)
Text_4 = Font_2.render('Select a Mode:', True, WHITE)
Text_4_1 = Font_3.render('1 Player', True, WHITE)
Text_4_2 = Font_3.render('2 Players', True, WHITE)

snake = Zmeika()
food = Eda()
    
snake2 = Zmeika()
snake2.elementy[0] = [100, 200]
snake2.cord_po_x = 0
snake2.cord_po_y = 10
snake2.skin = Red_Snake_Texture
food2 = Eda()
food2.dx = random.randint(20, 1360)
food2.dy = random.randint(20,680)
food2.show_rand_fruit = random.randint(0, len(food2.fruits) - 1)
clock = pygame.time.Clock()


SCREEN.fill(WHITE)
while is_running:
    with open("Saving_Snake.json") as open_ach:
        ach = json.load(open_ach)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                achievment = {
                    "elementy": snake.elementy,
                    "elementy2": snake2.elementy,
                    "dlina" : snake.dlina,
                    "dlina2": snake2.dlina,
                    "cord_po_x" : snake.cord_po_x,
                    "cord_po_x2" : snake2.cord_po_x, 
                    "cord_po_y" : snake.cord_po_y,
                    "cord_po_y2" : snake2.cord_po_y,
                    "level" : snake.level,
                    "level2" : snake2.level,
                    "mode" : mode
                }
                rec = json.dumps(achievment,indent = 4)
                with open('Saving_Snake.json' , "w") as res:
                    res.write(rec)
                start_the_game = False
                restart()
            if event.key == pygame.K_SPACE and start_the_game == False:
                with open("Saving_Snake.json") as open_ach:
                    ach = json.load(open_ach)
                snake.elementy = list(ach["elementy"])
                snake2.elementy = list(ach["elementy2"])
                snake.dlina = int(ach["dlina"])
                snake2.dlina = int(ach["dlina2"])
                snake.cord_po_x = int(ach["cord_po_x"])
                snake2.cord_po_x = int(ach["cord_po_x2"])
                snake.cord_po_y = int(ach["cord_po_y"])
                snake2.cord_po_y = int(ach["cord_po_y2"])
                snake.level = int(ach["level"])
                snake2.level = int(ach["level2"])
                mode = int(ach["mode"])
                start_the_game = True
                the_level_is_chosen = True
                the_mod_is_chosen = True
                open_ach.close()
            if event.key == pygame.K_RIGHT and snake.cord_po_x >= 0: 
                snake.cord_po_x = snake.shag 
                snake.cord_po_y = 0
            if event.key == pygame.K_LEFT and snake.cord_po_x <= 0: 
                snake.cord_po_x = -snake.shag
                snake.cord_po_y = 0 
            if event.key == pygame.K_UP and snake.cord_po_y != snake.shag: 
                snake.cord_po_x = 0 
                snake.cord_po_y = -snake.shag
            if event.key == pygame.K_DOWN and snake.cord_po_y != -snake.shag: 
                snake.cord_po_x = 0 
                snake.cord_po_y = snake.shag
            if event.key == pygame.K_d and snake2.cord_po_x >= 0: 
                snake2.cord_po_x = snake2.shag 
                snake2.cord_po_y = 0
            if event.key == pygame.K_a and snake2.cord_po_x <= 0: 
                snake2.cord_po_x = -snake2.shag
                snake2.cord_po_y = 0 
            if event.key == pygame.K_w and snake2.cord_po_y != snake2.shag: 
                snake2.cord_po_x = 0 
                snake2.cord_po_y = -snake2.shag
            if event.key == pygame.K_s and snake2.cord_po_y != -snake2.shag: 
                snake2.cord_po_x = 0 
                snake2.cord_po_y = snake2.shag
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] >= 430 and event.pos[0] <= 670 and start_the_game == False:
                if event.pos[1] >= 117 and event.pos[1] <= 170:
                    snake.level = 1
                    the_level_is_chosen = True
                    pygame.mixer.music.play()
                elif event.pos[1] >= 200 and event.pos[1] < 253:
                    snake.level = 2
                    the_level_is_chosen = True
                    pygame.mixer.music.play()
                elif event.pos[1] >= 288 and event.pos[1] <= 342:
                    snake.level = 3 
                    the_level_is_chosen = True
                    pygame.mixer.music.play()
            if event.pos[1] >= 510 and event.pos[1] <= 580 and start_the_game == False:
                if event.pos[0] >= 30 and event.pos[0] <= 230:
                    mode = 1
                    the_mod_is_chosen = True
                    pygame.mixer.music.play()
                elif event.pos[0] >= 250 and event.pos[0] <= 450:
                    mode = 2
                    the_mod_is_chosen = True
                    pygame.mixer.music.play()
            if event.pos[0] >= 500 and event.pos[0] <= 600 and event.pos[1] >= 400 and event.pos[1] <= 500 and the_mod_is_chosen == True and the_level_is_chosen == True:
                start_the_game = True
            
    SCREEN.fill(WHITE)
    
    

    
    if start_the_game == False:
        Starting()
    else:
        snake.dvizhenie()
        snake.narisovka()
        if mode == 2:
            snake2.dvizhenie()
            snake2.narisovka()
        
        for i in range(1, len(snake.elementy)):
            if snake.elementy[0][0] == snake.elementy[i][0] and snake.elementy[0][1] == snake.elementy[i][1]:
                start_the_game = False
        if mode == 2:
            for i in range(1, len(snake2.elementy)):
                if snake2.elementy[0][0] == snake2.elementy[i][0] and snake2.elementy[0][1] == snake2.elementy[i][1]:
                    start_the_game = False
                    
        if snake.elementy[0][0] >= food.dx - 3 and snake.elementy[0][1] >= food.dy - 3 and snake.elementy[0][0] <= food.dx + 23 and snake.elementy[0][1] <= food.dy + 23:
            food.fruit_was_eaten = True
            snake.dovavit_chast = True
        if mode == 2:
            if snake.elementy[0][0] >= food2.dx - 3 and snake.elementy[0][1] >= food2.dy - 3 and snake.elementy[0][0] <= food2.dx + 23 and snake.elementy[0][1] <= food2.dy + 23:
                food2.fruit_was_eaten = True
                snake.dovavit_chast = True
            if snake2.elementy[0][0] >= food.dx - 3 and snake2.elementy[0][1] >= food.dy - 3 and snake2.elementy[0][0] <= food.dx + 23 and snake2.elementy[0][1] <= food.dy + 23:
                food.fruit_was_eaten = True
                snake2.dovavit_chast = True 
            if snake2.elementy[0][0] >= food2.dx - 3 and snake2.elementy[0][1] >= food2.dy - 3 and snake2.elementy[0][0] <= food2.dx + 23 and snake2.elementy[0][1] <= food2.dy + 23:
                food2.fruit_was_eaten = True
                snake2.dovavit_chast = True
        
        food.show_fruit()
        if mode == 2:
            food2.show_fruit()

        if snake.level >= 2:
            pygame.draw.rect(SCREEN,BLACK,(200, 344,980,12))
            pygame.draw.rect(SCREEN,BLACK,(684,100, 12,500))
            if (snake.elementy[0][0] >= 200 and snake.elementy[0][0] <= 1180 and snake.elementy[0][1] >= 344 and snake.elementy[0][1] <= 356) or (snake2.elementy[0][0] >= 200 and snake2.elementy[0][0] <= 1180 and snake2.elementy[0][1] >= 344 and snake2.elementy[0][1] <= 356) or (snake.elementy[0][0] >= 684 and snake.elementy[0][0] <= 696 and snake.elementy[0][1] >= 100 and snake.elementy[0][1] <= 600) or (snake2.elementy[0][0] >= 684 and snake2.elementy[0][0] <= 696 and snake2.elementy[0][1] >= 100 and snake2.elementy[0][1] <= 600):
                start_the_game = False
                
            if snake.level == 3:
                pygame.draw.rect(SCREEN,BLACK,(342,172,696,12))
                pygame.draw.rect(SCREEN, BLACK,(342,528,696,12))
                pygame.draw.rect(SCREEN,BLACK,(342,258,12,192))
                pygame.draw.rect(SCREEN,BLACK,(1026,258,12,192))
                if (snake.elementy[0][0] >= 342 and snake.elementy[0][0] <= 1038 and snake.elementy[0][1] >= 172 and snake.elementy[0][1] <= 184) or (snake.elementy[0][0] >= 342 and snake.elementy[0][0] <= 1038 and snake.elementy[0][1] >= 528 and snake.elementy[0][1] <= 540) or (snake.elementy[0][0] >= 342 and snake.elementy[0][0] <= 354 and snake.elementy[0][1] >= 258 and snake.elementy[0][1] <= 450) or (snake.elementy[0][0] >= 1026 and snake.elementy[0][0] <= 1038 and snake.elementy[0][1] >= 258 and snake.elementy[0][1] <= 450) or (snake2.elementy[0][0] >= 342 and snake2.elementy[0][0] <= 1038 and snake2.elementy[0][1] >= 172 and snake2.elementy[0][1] <= 184) or (snake2.elementy[0][0] >= 342 and snake2.elementy[0][0] <= 1038 and snake2.elementy[0][1] >= 528 and snake2.elementy[0][1] <= 540) or (snake2.elementy[0][0] >= 342 and snake2.elementy[0][0] <= 354 and snake2.elementy[0][1] >= 258 and snake2.elementy[0][1] <= 450) or (snake2.elementy[0][0] >= 1026 and snake2.elementy[0][0] <= 1038 and snake2.elementy[0][1] >= 258 and snake2.elementy[0][1] <= 450):
                    start_the_game = False
                    
        if snake.elementy[0][0] > 1380 or snake.elementy[0][0] < 0 or snake.elementy[0][1]> 700 or snake.elementy[0][1] < 0 or snake2.elementy[0][0] > 1380 or snake2.elementy[0][0] < 0 or snake2.elementy[0][1]> 700 or snake2.elementy[0][1] < 0:
            start_the_game = False
            
            
        if start_the_game == False:
            restart()
        
        Text5 = Font_2.render("Score of Yellow snake: {}".format(10*(snake.dlina - 1)), True, YELLOW)
        Text5_2 = Font_2.render("Score of Red snake: {}".format(10*(snake2.dlina - 1)), True, RED)
        
        SCREEN.blit(Text5, (20,20))
        if mode == 2:
            SCREEN.blit(Text5_2, (20,70))
    clock.tick(18 + 3*snake.level)
    pygame.display.flip()
    
    

pygame.quit()





            











        