
d2 = dict()
def starting_page():
    SCREEN.blit(image, (205, -250))
    pygame.draw.line(SCREEN, BLACK, (400,200), (0, 600), 10)
    pygame.draw.line(SCREEN, BLACK, (980,150 ), (1380, 600), 10)
    pygame.draw.line(SCREEN, BLACK, (700,480 ), (700, 670), 30)
    Starting_Word = pygame.font.SysFont('ariel', 40,False, True)
    pygame.draw.rect(SCREEN, (150,150,255), (490, 540, 475, 50))
    text1 = Starting_Word.render('...To start the game, press {}Space{}'.format('"','"'), True,WHITE)
    SCREEN.blit(text1, (500, 550))

    
    
import pygame
import time
import random
import sys

#pylint:disable=no-member
pygame.init()

WIDTH = 1380
HEIGHT = 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch a coin, catch!")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)
##clock = pygame.time.Clock()
image = pygame.image.load(r'C:\Users\danii\Documents\Work\—Pngtree—vector car icon_3989896.png')
image_car = pygame.image.load(r'C:\Users\danii\Documents\Work\machine.png')
image_coin = pygame.image.load(r'C:\Users\danii\Documents\Work\coin_PNG36871 (1).png')

is_running = True
The_Space_was_touched = False   

velocity = 1

clock = pygame.time.Clock()    
x = -100
y = 60 
z = 220
i = 380
q = 540
n = -1000

l_velocity = [1, 1.2 , 1.4, 1.6, 1.8]

pi = 3.14
text2 = pygame.font.SysFont('corbel', 30)
text4 = pygame.font.Font(None, 200)
pygame.mixer.music.load('zvuk-monet-mario.wmDcd.mp3')
dx = 0
gt = float(0)
sum_of_coin = 0
cord_x = random.randint(175,925)
cord_y = -100
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                The_Space_was_touched = True
            elif event.key == pygame.K_ESCAPE:
                The_Space_was_touched = False
            elif event.key == pygame.K_UP:
                velocity += 1
                if velocity == 6:
                    velocity = 5
            elif event.key == pygame.K_DOWN:
                velocity -= 1
                if velocity == 0:
                    velocity = 1
            elif event.key == pygame.K_LEFT:
                dx -= 25
            elif event.key == pygame.K_RIGHT:
                dx += 25   

    text5 = text4.render('A', True,BLACK)  
    
    SCREEN.fill(WHITE)        
    if The_Space_was_touched == False:
        starting_page()
    else:
        pygame.draw.rect(SCREEN,BLACK, (550, x,10,100))
        pygame.draw.rect(SCREEN,BLACK, (550, y,10,100))
        pygame.draw.rect(SCREEN,BLACK, (550, z,10,100))
        pygame.draw.rect(SCREEN,BLACK, (550, i,10,100))
        pygame.draw.rect(SCREEN,BLACK, (550, q,10,100))
        
        
        pygame.draw.rect(SCREEN,BLACK, (750, x,10,100))
        pygame.draw.rect(SCREEN,BLACK, (750, y,10,100))
        pygame.draw.rect(SCREEN,BLACK, (750, z,10,100))
        pygame.draw.rect(SCREEN,BLACK, (750, i,10,100))
        pygame.draw.rect(SCREEN,BLACK, (750, q,10,100))


        pygame.draw.rect(SCREEN,BLACK, (350, x,10,100))
        pygame.draw.rect(SCREEN,BLACK, (350, y,10,100))
        pygame.draw.rect(SCREEN,BLACK, (350, z,10,100))
        pygame.draw.rect(SCREEN,BLACK, (350, i,10,100))
        pygame.draw.rect(SCREEN,BLACK, (350, q,10,100))

        pygame.draw.rect(SCREEN,BLACK, (150, 0,10,700))

        pygame.draw.rect(SCREEN,BLACK, (950, n,10,3000))
        pygame.draw.rect(SCREEN,BLACK, (950, 0,10,700))
        pygame.draw.rect(SCREEN,BLACK, (1200, n,10,3000))
        
        pygame.draw.rect(SCREEN,BLACK, (970, n + 2900,5,70))
        pygame.draw.rect(SCREEN,BLACK, (970, n + 2800,5,70))
        pygame.draw.rect(SCREEN,BLACK, (970, n + 2700,5,70))

        pygame.draw.rect(SCREEN,BLACK, (1200, n + 2990,200,10))
        pygame.draw.rect(SCREEN,BLACK, (1200, n ,200,10))
        

        
        


        pygame.draw.rect(SCREEN,BLACK, (930, n + 30,5,70))
        pygame.draw.rect(SCREEN,BLACK, (930, n + 130,5,70))
        pygame.draw.rect(SCREEN,BLACK, (930, n + 230,5,70))
        
        SCREEN.blit(text5, (1025, n + 2500))
        SCREEN.blit(text5, (1025, n + 1000))
        
        SCREEN.blit(image_coin,(cord_x, cord_y))
        if cord_x >= 560 + dx + 20 and cord_x <= 560 + dx + 125 and cord_y >= 500 and cord_y <= 650:
            pygame.mixer.music.play()
            cord_x = random.randint(175,925)
            cord_y = -100
            sum_of_coin += 50
        else:
            if cord_y >= 700:
                cord_x = random.randint(175,925)
                cord_y = -100
                sum_of_coin -= 20
            else:
                SCREEN.blit(image_coin,(cord_x, cord_y))
        cord_y += 5 * l_velocity[velocity - 1]
        
        

        x += 5 * l_velocity[velocity - 1]
        y += 5 * l_velocity[velocity - 1]
        z += 5 * l_velocity[velocity - 1]
        i += 5 * l_velocity[velocity - 1]
        q += 5 * l_velocity[velocity - 1]
        n += 5 * l_velocity[velocity - 1]
        
        
        
        if x >= 700:
            x = -100
        elif y >= 700:
            y = -100
        elif z >= 700:
            z = -100
        elif i >= 700:
            i = -100
        elif q >= 700:
            q = -100
        elif n >= 700:
            n = -3000
        
        gt += float(1) / float(60)    
        text3 = text2.render('Score: {}'.format(sum_of_coin), True,BLACK)
        SCREEN.blit(text3, (6, 30))
        text6 = text2.render('Game time: ', True,BLACK)
        text7 = text2.render('{:.2f}'.format(gt), True,BLACK)
        SCREEN.blit(text6, (6, 55))
        SCREEN.blit(text7,(10, 75))
        

            
        
        
            
        
        SCREEN.blit(image_car, (560 + dx,500))
        
        
    
    clock.tick(60)
    pygame.display.flip()

pygame.quit()