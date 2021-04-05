import time
import pygame
import math
# pylint: disable=no-member
width = 1200
height = 700

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

pygame.init()
pygame.display.set_caption("The Graph")
screen = pygame.display.set_mode((width, height))
screen.fill(WHITE)

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    freq = 3
    amp = 288
    d1 = dict()
    d2 = dict()
    pygame.draw.line(screen, BLACK, [264,0], [1200,0], 2)
    pygame.draw.line(screen, BLACK, [1200,0], [1200,648], 2)
    pygame.draw.line(screen, BLACK, [264,0], [264,648], 2)
    pygame.draw.line(screen, BLACK, [264,648], [1200,648], 2)
    
    
    pygame.draw.line(screen, BLACK, [300,0], [300,648], 2)
    pygame.draw.line(screen, BLACK, [264,36], [1200,36], 2)
    pygame.draw.line(screen, BLACK, [264,612], [1200,612], 2)
    pygame.draw.line(screen, BLACK, [1164,0], [1164,648], 2)

    
    x1 = 108
    while x1 <= 540:
        if x1 == 324:
            pygame.draw.line(screen, BLACK, [264,x1], [1200,x1], 3)
        else:
            pygame.draw.line(screen, BLACK, [264,x1], [1200,x1], 2)
        x1 += 72
    
    
    y1 = 444
    while y1 <= 1020:
        if y1 == 732:
            pygame.draw.line(screen, BLACK, [y1,0], [y1,648], 3)
        else:
            pygame.draw.line(screen, BLACK, [y1,0], [y1,648], 2)
        y1 += 144
    
    
    x2 = 36
    x_2 = 0
    while x2 <= 612:
        if x_2 % 2 == 0:
            pygame.draw.line(screen, BLACK, [264,x2], [284,x2], 2)
            pygame.draw.line(screen, BLACK, [1180,x2], [1200,x2], 2)
        else:
            pygame.draw.line(screen, BLACK, [264,x2], [272,x2], 2)
            pygame.draw.line(screen, BLACK, [1192,x2], [1200,x2], 2)
        x2 += 18
        x_2 += 1
    
    
    y2 = 300
    y_2 = 0
    while y2 <= 1164:
        if y_2 % 4 == 0:
            pygame.draw.line(screen, BLACK, [y2,0], [y2,28], 2)
            pygame.draw.line(screen, BLACK, [y2,648], [y2,620], 2)
        elif y_2 % 2 == 0:
            pygame.draw.line(screen, BLACK, [y2,0], [y2,20], 2)
            pygame.draw.line(screen, BLACK, [y2,648], [y2,628], 2)
        else:
            pygame.draw.line(screen, BLACK, [y2,648], [y2,640], 2)
            pygame.draw.line(screen, BLACK, [y2,0], [y2,8], 2)
        y2 += 18
        y_2 += 1
    
    
    for x in range(width - 336):
        y = int( 324 + amp * math.sin(freq * ((float(x)/864) * (2 * math.pi))))
        d1[x] = [x,y]
        if x != 0:
            pygame.draw.aaline(screen, RED,[d1[x-1][0] + 300, d1[x-1][1] ],[d1[x][0] + 300, d1[x][1] ])
    
    
    for x in range(width - 336):
        y = int( 324 + amp * math.cos(freq * ((float(x)/864) * (2 * math.pi))))
        d2[x] = [x,y]
        if x != 0 and x % 5 != 0:
            pygame.draw.aaline(screen, BLUE,[d2[x-1][0] + 300, d2[x-1][1] ],[d2[x][0] + 300, d2[x][1] ])
    
    
    List_of_numbers_on_left = ["1.00","0.75","0.50","0.25","0.00","-0.25","-0.50","-0.75","-1.00"]
    like_a_float_number = pygame.font.SysFont('ariel', 30, False, True)
    x = 28
    for num in List_of_numbers_on_left:
        screen.blit(like_a_float_number.render(num, True, BLACK),(205, x))
        x += 72

    
    List_of_numbers_on_bottom = ["-3pi","-5pi/2","-2pi","-3pi/2","-pi","-pi/2","0","pi/2","pi","3pi/2","2pi","5pi/2","3pi"]
    screen.blit(like_a_float_number.render(List_of_numbers_on_bottom[0],True,BLACK),(276,660))
    screen.blit(like_a_float_number.render(List_of_numbers_on_bottom[1],True,BLACK),(345,660))
    screen.blit(like_a_float_number.render(List_of_numbers_on_bottom[2],True,BLACK),(426,660))
    screen.blit(like_a_float_number.render(List_of_numbers_on_bottom[3],True,BLACK),(489,660))
    screen.blit(like_a_float_number.render(List_of_numbers_on_bottom[4],True,BLACK),(574,660))
    screen.blit(like_a_float_number.render(List_of_numbers_on_bottom[5],True,BLACK),(637,660))
    screen.blit(like_a_float_number.render(List_of_numbers_on_bottom[6],True,BLACK),(726,660))
    screen.blit(like_a_float_number.render(List_of_numbers_on_bottom[7],True,BLACK),(786,660))
    screen.blit(like_a_float_number.render(List_of_numbers_on_bottom[8],True,BLACK),(867,660))
    screen.blit(like_a_float_number.render(List_of_numbers_on_bottom[9],True,BLACK),(925,660))
    screen.blit(like_a_float_number.render(List_of_numbers_on_bottom[10],True,BLACK),(1002,660))
    screen.blit(like_a_float_number.render(List_of_numbers_on_bottom[11],True,BLACK),(1069,660))
    screen.blit(like_a_float_number.render(List_of_numbers_on_bottom[0],True,BLACK),(1142,660))
    
    
    pygame.display.flip()
pygame.quit()