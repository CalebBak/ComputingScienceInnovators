import enum
import math
import random

import pygame

class Directions(enum.Enum):
    """
    Gives names to the valid directions
    """
    RIGHT = 0
    LEFT = 1
    DOWN = 2
    UP = 3

class Snake:
    def __init__(self, display, colour, block_width):
        """
        Creates a new snake.
        """
        self.position = [[250, 250], [240, 250], [230, 250]]
        self.score = 0
        
        self.display = display
        self.colour = colour
        self.BLOCK_WIDTH = block_width

    def move(self, direction):
        """
        Moves the snake
        """
        head = self.position[0]
        if direction == Directions.RIGHT:
            head[0] += self.BLOCK_WIDTH
        elif direction == Directions.LEFT:
            head[0] -= self.BLOCK_WIDTH
        elif direction == Directions.DOWN:
            head[1] += self.BLOCK_WIDTH
        elif direction == Directions.UP:
            head[1] -= self.BLOCK_WIDTH

        position.insert(0, list(head))
        position.pop()

    def draw(self):
        """
        Draws the snake
        """
        for pos in self.position:
            pygame.draw.rect(self.display, self.colour,
                             pygame.Rect(position[0], position[1],
                                         self.BLOCK_WIDTH, self.BLOCK_WIDTH))
            
    def check_collision(self, win_size):
        """
        Checks if the snake has crashed with itself or the borders
        """
        head = self.position[0]
        if head[0] < 0 or head[0] >= win_size[0] or head[1] < 0\
           or head[0] >= win_size[1]:
            return True
        return False

class Game:
    DEFAULT_DIMENSIONS = (500, 500)
    MAX_BLOCK_WIDTH = 10
    
    def __init__(self, bg_colour):
        """
        Creates and configures the game window
        """
        self.window = pygame.display.set_mode(self.DEFAULT_DIMENSIONS)
        self.window.fill(bg_colour)
        pygame.display.set_caption("Snake Game")
        pygame.display.update()
        
    def play():
        pass

class Food:
    FOOD_COLOUR = (0, 212, 0)
    
    def __init__(self, display, block_width):
        """
        Generates a random food
        """

        self.BLOCK_WIDTH = block_width
        
        self.value = random.randint(1, self.BLOCK_WIDTH)
        self.display = display
        self.x = math.ceil(
            random.randint(0, self.display.get_width()-self.BLOCK_WIDTH) / self.BLOCK_WIDTH) * self.BLOCK_WIDTH
        self.y = 0
        
    def draw(self):
        """
        Draws the food
        """
        pygame.draw.rect(self.display, self.FOOD_COLOUR,
                         pygame.Rect(self.x, self.y, self.BLOCK_WIDTH,
                                     self.BLOCK_WIDTH))


if __name__ == "__main__":
    pygame.init()

    game = Game((200,200,200))

    pygame.quit()