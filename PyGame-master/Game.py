#import modules

import pygame

import math
import random
import time



def collision(snake_head, snake_position):
    # if snake is outside of boundaries return 1
    if snake_head[0] < 0 or snake_head[0] >= display.get_width()\
       or snake_head[1] < 0 or snake_head[1] >= display.get_height()\
       or snake_head in snake_position[1:]:
        return True
    return False
    
def generate_snake(snake_head, snake_position, button_direction):

    #uses button_direction to decide where snake head will go
    if button_direction == 0:
        snake_head[0] += 10
    elif button_direction == 1:
        snake_head[0] -= 10
    elif button_direction == 2:
        snake_head[1] += 10
    elif button_direction == 3:
        snake_head[1] -= 10
     
    snake_position.insert(0, list(snake_head))
    snake_position.pop()

    return snake_position
    

def display_snake(snake_position):
    #uses list of snake's positions to display snake
    for position in snake_position:
        pygame.draw.rect(display, player_color,
                         pygame.Rect(position[0], position[1], 10, 10))

def display_food(food_position):
    pygame.draw.rect(display, (0, 212, 0), pygame.Rect(food_position[0],
                                                       food_position[1], 10,
                                                       10))

def play_game(snake_head, snake_position, button_direction):

    crashed = False
    first_run = True
    
    food_position = generate_food()
    
    while not crashed:

        for event in pygame.event.get():

            #ends game if you click on X
            if event.type == pygame.QUIT:
                crashed = True

            #sets variable used to move snake using arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    button_direction = 0
                elif event.key == pygame.K_LEFT:
                    button_direction = 1
                elif event.key == pygame.K_DOWN:
                    button_direction = 2
                elif event.key == pygame.K_UP:
                    button_direction = 3

        if first_run:
            button_direction = 3
            first_run = False
        #moves snake position
        snake_position = generate_snake(snake_head, snake_position,
                                        button_direction)
        
        
        #display background, snake, and food
        display.fill(window_color)
        display_snake(snake_position)
        display_food(food_position)
        pygame.display.update()
        
        # Check if food collected
        if snake_head == food_position:
            snake_position = add_segment(snake_position, button_direction)
            food_position = generate_food()

        #ends game loop if snake leaves the boundary
        crashed = collision(snake_head, snake_position)

        clock.tick(20)

def add_segment(snake_position, direction):
    x_mod = 0
    y_mod = 0
    if direction == 0:
        x_mod = -10
    elif direction == 1:
        x_mod = 10
    elif direction == 2:
        y_mod = -10
    elif direction == 3:
        y_mod = 10
    snake_position.append([snake_position[-1][0] + x_mod,
                           snake_position[-1][0] + y_mod])
    return snake_position

def generate_food():
    return [math.ceil(random.randint(0, display.get_width()-10) / 10) * 10,
            math.ceil(random.randint(0, display.get_height()-10) / 10) * 10]

if __name__ == "__main__":

    # set variables

    display_width = 500

    display_height = 500

    player_color = (255,0,0)

    window_color = (200,200,200)

    clock=pygame.time.Clock()

    

    #create the snake

    snake_head = [250,250]

    snake_position = [[250,250],[240,250],[230,250]]



    #initialize pygame modules    

    pygame.init()

    

    #display game window

    display = pygame.display.set_mode((display_width,display_height))

    display.fill(window_color)

    pygame.display.set_caption("Snake Game")

    pygame.display.update()

    

    #start the game loop

    play_game(snake_head, snake_position, 1)
    
    

    pygame.quit()
