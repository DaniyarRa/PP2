import pygame
import sys
import math
#pylint:disable=no-member
pygame.init()
WIDTH = 1380
HEIGHT = 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

Color_Option = WHITE
#Figure_of_Drawing = Circle
Depth_of_Drawing = 5
Drawing_Process = False
is_running = True
Increase_Depth = False
Decrease_Depth = False
Rect_mode = False
Circle_mode = False
SCREEN.fill(WHITE)
saved_picture = pygame.image.load(r'C:\Users\danii\Documents\Work\Result.png')
SCREEN.blit(saved_picture, (0,0))
Font = pygame.font.SysFont(None, 20, False, False)
Text0 = Font.render('Press F5 to open new page', True, BLACK)
Text1 = Font.render('Press Backspace to choose eraser', True, BLACK)
Text2 = Font.render('Press 1:', True, YELLOW)
Text3 = Font.render('Press 2:', True, RED)
Text4 = Font.render('Press 3:', True, GREEN)
Text5 = Font.render('Press 4:', True, BLUE)
Text6 = Font.render('Press 5:', True, BLACK)
Text7 = Font.render('Press R to draw Rectangle', True, BLACK)
Text8 = Font.render('Press C to draw Circle', True, BLACK)

clock = pygame.time.Clock()

Left_Top_Cord = (0,0)
Right_Bottom_Cord = (0,0)
center_x = 0
center_y = 0

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                Color_Option = WHITE
            if event.key == pygame.K_1:
                Color_Option = YELLOW
            if event.key == pygame.K_2:
                Color_Option = RED
            if event.key == pygame.K_3:
                Color_Option = GREEN
            if event.key == pygame.K_4:
                Color_Option = BLUE
            if event.key == pygame.K_5:
                Color_Option = BLACK
            if event.key == pygame.K_UP:
                Depth_of_Drawing += 5
            if event.key == pygame.K_DOWN:
                Depth_of_Drawing -= 5
                if Depth_of_Drawing == 0:
                    Depth_of_Drawing = 5
            if event.key == pygame.K_F5:
                SCREEN.fill(WHITE)
            if event.key == pygame.K_r:
                Rect_mode = True
            if event.key == pygame.K_c:
                Circle_mode = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if Rect_mode == True:
                Left_Top_Cord = event.pos
            elif Circle_mode == True:
                Left_Top_Cord = event.pos
            else:
                Drawing_Process = True
                if Color_Option != None:
                    if event.pos[0] <= 1130 or event.pos[1] >= 220:
                        pygame.draw.circle(SCREEN,Color_Option, event.pos, Depth_of_Drawing)
        if event.type == pygame.MOUSEMOTION:
            if Drawing_Process == True:
                if event.pos[0] <= 1130 or event.pos[1] >= 220:
                    pygame.draw.circle(SCREEN,Color_Option, event.pos, Depth_of_Drawing)
        if event.type == pygame.MOUSEBUTTONUP:
            Right_Bottom_Cord = event.pos
            center_x = (Left_Top_Cord[0] + Right_Bottom_Cord[0]) // 2
            center_y = (Left_Top_Cord[1] + Right_Bottom_Cord[1]) // 2
            if Rect_mode == True:
                pygame.draw.rect(SCREEN, Color_Option, (Left_Top_Cord[0], Left_Top_Cord[1], abs(Left_Top_Cord[0] - Right_Bottom_Cord[0]), abs(Left_Top_Cord[1] - Right_Bottom_Cord[1])))
                Rect_mode = False
            if Circle_mode == True:
                pygame.draw.circle(SCREEN, Color_Option, (center_x, center_y), ((Left_Top_Cord[0] - center_x)**2 + (Left_Top_Cord[1] - center_y) **2 ) ** 0.5)
                Circle_mode = False
            else:
                Drawing_Process = False
    
    
    SCREEN.blit(Text0, (1150, 20))
    SCREEN.blit(Text1, (1150, 40))
    SCREEN.blit(Text2, (1150, 60))
    SCREEN.blit(Text3, (1150, 80))
    SCREEN.blit(Text4, (1150, 100))
    SCREEN.blit(Text5, (1150, 120))
    SCREEN.blit(Text6, (1150, 140))
    SCREEN.blit(Text7, (1150, 160))
    SCREEN.blit(Text8, (1150, 180))
    pygame.draw.rect(SCREEN,YELLOW,(1230,60, 50,20))
    pygame.draw.rect(SCREEN,RED,(1230,80, 50,20))
    pygame.draw.rect(SCREEN,GREEN,(1230,100, 50,20))
    pygame.draw.rect(SCREEN,BLUE,(1230,120, 50,20))
    pygame.draw.rect(SCREEN,BLACK,(1230,140, 50,20))


            
        
    pygame.image.save(SCREEN,'Result.png')
    clock.tick(60)    
    pygame.display.flip()
pygame.quit()    
                  
            


