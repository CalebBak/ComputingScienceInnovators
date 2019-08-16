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
    def __init__(self, display, colour, block_width, offset_x, offset_y):
        """
        Creates a new snake.
        """
        self.head = [250+offset_x, 250+offset_y]
        self.position = [[250+offset_x, 250+offset_y], [250+offset_x, 260+offset_y], [250+offset_x, 270+offset_y]]
        self.score = 0

        self.display = display
        self.colour = colour
        self.BLOCK_WIDTH = block_width
        self.elongate = False
        self.dead = False

    def move(self, direction):
        """
        Moves the snake
        """
        if self.dead:
            return
        if direction == Directions.RIGHT:
            self.head[0] += self.BLOCK_WIDTH
        elif direction == Directions.LEFT:
            self.head[0] -= self.BLOCK_WIDTH
        elif direction == Directions.DOWN:
            self.head[1] += self.BLOCK_WIDTH
        elif direction == Directions.UP:
            self.head[1] -= self.BLOCK_WIDTH

        self.position.insert(0, list(self.head))
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

    def check_collision(self, win_size, others):
        """
        Checks if the snake has crashed with itself or the borders
        """
        head = self.position[0]
        if head[0] < 0 or head[0] >= win_size[0] or head[1] < self.BLOCK_WIDTH*2 or head[1] >= win_size[1]:
            # Collision with boundaries
            self.dead = True
            return True
        elif head in self.position[1:]:
            # Collision with self
            self.dead = True
            return True

        # Collision with another snake
        for other in others:
            if head in other.position:
                self.dead = True
                return True
        return False

    def add_segment(self):
        self.elongate = True

class Game:
    DEFAULT_DIMENSIONS = (500, 500)
    MAX_BLOCK_WIDTH = 10
    SCORE_BANNER_HEIGHT = MAX_BLOCK_WIDTH*2
    
    def __init__(self, bg_colour, difficulty):
        """
        Creates and configures the game window
        """
        self.bg_colour = bg_colour

        self.window = pygame.display.set_mode(self.DEFAULT_DIMENSIONS)
        self.window.fill(self.bg_colour)
        self.font = pygame.font.Font(None, self.SCORE_BANNER_HEIGHT-3)
        self.clock = pygame.time.Clock()
        self.clock_tick_speed = {"e": 15, "n": 20, "h": 30}[difficulty]

        pygame.display.set_caption("Snake Game")
        pygame.display.update()
        
    def play(self):
        snake1 = Snake(self.window, (255, 0, 0), self.MAX_BLOCK_WIDTH, 30, 0)
        snake2 = Snake(self.window, (0, 0, 255), self.MAX_BLOCK_WIDTH, -30, 0)
        foods = [Food(self.window, (self.window.get_width(), self.window.get_height()), self.MAX_BLOCK_WIDTH, [snake1, snake2], self.bg_colour)]
        bomb = None

        p_crashed = [False, False]
        crashed = False
        first_run = True
        dont_redraw = False

        dir1 = Directions.UP
        dir2 = Directions.UP

        while not crashed:
            # Take input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True

                if event.type == pygame.KEYDOWN:
                    if not p_crashed[0] and event.key == pygame.K_RIGHT:
                        dir1 = Directions.RIGHT
                    elif not p_crashed[0] and event.key == pygame.K_LEFT:
                        dir1 = Directions.LEFT
                    elif not p_crashed[0] and event.key == pygame.K_DOWN:
                        dir1 = Directions.DOWN
                    elif not p_crashed[0] and event.key == pygame.K_UP:
                        dir1 = Directions.UP
                    elif not p_crashed[1] and event.key == pygame.K_w:
                        dir2 = Directions.UP
                    elif not p_crashed[1] and event.key == pygame.K_a:
                        dir2 = Directions.LEFT
                    elif not p_crashed[1] and event.key == pygame.K_s:
                        dir2 = Directions.DOWN
                    elif not p_crashed[1] and event.key == pygame.K_d:
                        dir2 = Directions.RIGHT

            # Ensure player always travels in same direction on game start
            if first_run:
                dir1 = Directions.UP
                dir2 = Directions.UP
                first_run = False

            # check if snakes are both dead
            if snake1.dead and snake2.dead:
                return

            # move snake
            if not p_crashed[0]:
                snake1.move(dir1)
            if not p_crashed[1]:
                snake2.move(dir2)

            # Generate new food on chance
            if random.randint(1, 50) == 1:
                foods.append(Food(self.window, (self.window.get_width(), self.window.get_height()),  self.MAX_BLOCK_WIDTH, [snake1, snake2], self.bg_colour))

            # Generate a bomb on chance
            if bomb is None and random.randint(1, 150) == 1:
                bomb = Bomb(self.window, (self.window.get_width(), self.window.get_height()), self.MAX_BLOCK_WIDTH)

            # draw
            self.window.fill(self.bg_colour)
            snake1.draw()
            snake2.draw()
            for food in foods:
                food.draw()
                self.draw_score(snake1.score, snake2.score)
            if bomb is not None:
                if bomb.draw([snake1, snake2]):
                    bomb = None
            pygame.display.update()

            # check if food collected
            for food in foods:
                if food.collected(snake1):
                    snake1.add_segment()
                    snake1.score += food.value
                    foods.remove(food)
                    foods.append(Food(self.window, (self.window.get_width(), self.window.get_height()),  self.MAX_BLOCK_WIDTH, [snake1, snake2], self.bg_colour))
                elif food.collected(snake2):
                    snake2.add_segment()
                    snake2.score += food.value
                    foods.remove(food)
                    foods.append(Food(self.window, (self.window.get_width(), self.window.get_height()), self.MAX_BLOCK_WIDTH, [snake1, snake2], self.bg_colour))

            # Check if crashed
            p_crashed[0] = snake1.check_collision([self.window.get_width(), self.window.get_height()], [snake2])
            p_crashed[1] = snake2.check_collision([self.window.get_width(), self.window.get_height()], [snake1])

            crashed = p_crashed[0] and p_crashed[1]

            self.clock.tick(self.clock_tick_speed)

    def draw_score(self, score1, score2):
        # Draw score banner
        banner = pygame.Rect(0, 0, self.window.get_height(), self.SCORE_BANNER_HEIGHT)
        pygame.draw.rect(self.window, (0, 0, 0), banner)
        
        # Draw text
        score1_text = self.font.render("P1: %d" % score1, 1, (255, 255, 255))
        score2_text = self.font.render("P2: %d" % score2, 1, (255, 255, 255))
        
        score2_rect = score2_text.get_rect()
        score2_rect.right = banner.right
        
        self.window.blit(score1_text, (0, 1))
        self.window.blit(score2_text, score2_rect)

class Food:
    FOOD_COLOUR = (0, 212, 0)
    
    def __init__(self, display, dimens, block_width, snakes, bg_colour):
        """
        Generates a random food
        """

        self.BLOCK_WIDTH = block_width
        self.BG_COLOUR = bg_colour

        self.value = random.randint(3, self.BLOCK_WIDTH)
        self.display = display
        while True:
            try:
                self.x = math.ceil(random.randint(0, dimens[0]-self.BLOCK_WIDTH) / self.BLOCK_WIDTH) * self.BLOCK_WIDTH
                self.y = math.ceil(random.randint(self.BLOCK_WIDTH, dimens[1]-self.BLOCK_WIDTH) / self.BLOCK_WIDTH) * self.BLOCK_WIDTH
                for snake in snakes:
                    if [self.x, self.y] in snake.position:
                        raise Exception()
            except Exception:
                continue
            else:
                break

    def draw(self):
        """
        Draws the food
        """
        container = pygame.Rect(self.x, self.y, self.BLOCK_WIDTH, self.BLOCK_WIDTH)
        food = pygame.Rect(self.x, self.y, self.value, self.value)
        
        # Center food in a cell
        food.center = container.center
        
        pygame.draw.rect(self.display, self.BG_COLOUR, container)        
        pygame.draw.rect(self.display, self.FOOD_COLOUR, food)

    def collected(self, snake):
        snake_head = snake.position[0]

        if snake_head[0] == self.x and snake_head[1] == self.y:
            return True
        return False

class Bomb:
    BOMB_COLOUR = (227, 61, 0)
    BOMB_COLOUR_PRIMED = (255, 86, 23)
    EXPLOSION_COLOUR = (204, 55, 0)
    fuse = 50
    
    def __init__(self, display, dimens, block_width):
        """
        Generates a bomb
        """
        self.BLOCK_WIDTH = block_width
        self.display = display
        self.x = math.ceil(random.randint(0, dimens[0]-self.BLOCK_WIDTH) / self.BLOCK_WIDTH) * self.BLOCK_WIDTH
        self.y = math.ceil(random.randint(self.BLOCK_WIDTH, dimens[1]-self.BLOCK_WIDTH) / self.BLOCK_WIDTH) * self.BLOCK_WIDTH
        
    def draw(self, snakes):
        """
        Draws the food
        """
        colour = self.BOMB_COLOUR
        if self.fuse == 0:
            self._explode(snakes)
            return True
        elif self.fuse % 2 == 0:
            colour = self.BOMB_COLOUR_PRIMED
        
        pygame.draw.rect(self.display, colour, pygame.Rect(self.x, self.y, self.BLOCK_WIDTH, self.BLOCK_WIDTH))
        self.fuse -= 1
        return False

    def _explode(self, snakes):
        """
        Explode the bomb
        """
        explosion_x = self.x - self.BLOCK_WIDTH
        explosion_y = self.y - self.BLOCK_WIDTH
        
        # Explosion
        area = pygame.draw.rect(self.display, self.EXPLOSION_COLOUR, pygame.Rect(explosion_x, explosion_y, self.BLOCK_WIDTH*3, self.BLOCK_WIDTH*3))
        center = pygame.draw.rect(self.display, self.BOMB_COLOUR_PRIMED, pygame.Rect(self.x, self.y, self.BLOCK_WIDTH, self.BLOCK_WIDTH))
        
        pygame.display.update(area)
        pygame.display.update(center)
        #pygame.time.delay(100)
        
        
        # Check if snake got caught in the explosion
        explode_area = list()
        for i in range(1, 4):
            for j in range(1, 4):
                explode_area.append([self.x + (self.BLOCK_WIDTH*i), self.y + (self.BLOCK_WIDTH*j)])
        for snake in snakes:
            for position in snake.position:
                if position in explode_area:
                    if position in snake.position:
                        snake.dead = True

if __name__ == "__main__":
    # Ask difficulty
    diff = input("Select your difficulty ([e]asy, [N]ormal, [h]ard): ").lower()
    if diff not in ["e", "n", "h"]:
        diff = "n"
    
    pygame.init()    
    
    game = Game((200,200,200), diff)
    game.play()

    pygame.quit()