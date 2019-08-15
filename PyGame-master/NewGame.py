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

import time
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
        self.elongate = False

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

        self.position[0] = head

        self.position.insert(0, list(head))
        if not self.elongate:
            self.position.pop()
        else:
            self.elongate = False

    def draw(self):
        """
        Draws the snake
        """
        for pos in self.position:
            pygame.draw.rect(self.display, self.colour, pygame.Rect(pos[0], pos[1], self.BLOCK_WIDTH, self.BLOCK_WIDTH))

    def check_collision(self, win_size):
        """
        Checks if the snake has crashed with itself or the borders
        """
        head = self.position[0]
        if head[0] < 0 or head[0] >= win_size[0] or head[1] < 0 or head[1] >= win_size[1]:
            return True
        return False

    def add_segment(self):
        self.elongate = True

class Game:
    DEFAULT_DIMENSIONS = (500, 500)
    MAX_BLOCK_WIDTH = 10
    
    def __init__(self, bg_colour):
        """
        Creates and configures the game window
        """
        self.bg_colour = bg_colour

        self.window = pygame.display.set_mode(self.DEFAULT_DIMENSIONS)
        self.window.fill(self.bg_colour)
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Snake Game")
        pygame.display.update()
        
    def play(self):
        snake = Snake(self.window, (255, 0, 0), self.MAX_BLOCK_WIDTH)
        food = Food(self.window, self.MAX_BLOCK_WIDTH)

        crashed = False
        first_run = True

        direction = Directions.UP

        while not crashed:
            # Take input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        direction = Directions.RIGHT
                    elif event.key == pygame.K_LEFT:
                        direction = Directions.LEFT
                    elif event.key == pygame.K_DOWN:
                        direction = Directions.DOWN
                    elif event.key == pygame.K_UP:
                        direction = Directions.UP

            # Ensure player always travels in same direction on game start
            if first_run:
                direction = Directions.UP
                first_run = False

            # move snake
            snake.move(direction)

            # draw
            self.window.fill(self.bg_colour)
            snake.draw()
            food.draw()
            pygame.display.update()

            # check if food collected
            if food.collected(snake):
                snake.add_segment()
                food = Food(self.window, self.MAX_BLOCK_WIDTH)

            # Check if crashed
            crashed = snake.check_collision([self.window.get_width(), self.window.get_height()])

            self.clock.tick(20)

class Food:
    FOOD_COLOUR = (0, 212, 0)
    
    def __init__(self, display, block_width):
        """
        Generates a random food
        """

        self.BLOCK_WIDTH = block_width

        self.value = random.randint(1, self.BLOCK_WIDTH)
        self.display = display
        self.x = math.ceil(random.randint(0, self.display.get_width()-self.BLOCK_WIDTH) / self.BLOCK_WIDTH) * self.BLOCK_WIDTH
        self.y = 0

    def draw(self):
        """
        Draws the food
        """
        pygame.draw.rect(self.display, self.FOOD_COLOUR,
                         pygame.Rect(self.x, self.y, self.BLOCK_WIDTH,
                                     self.BLOCK_WIDTH))

    def collected(self, snake):
        snake_head = snake.position[0]

        if snake_head[0] == self.x and snake_head[1] == self.y:
            return True
        return False


if __name__ == "__main__":
    pygame.init()

    game = Game((200,200,200))
    game.play()

    pygame.quit()