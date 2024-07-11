import pygame
import random

# Initialize Pygame
pygame.init()

# Screen Dimensions
WIDTH, HEIGHT = 800, 600
SNAKE_SIZE = 20
SNAKE_SPEED = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
YELLOW = (255, 255, 102)
GRAY = (192, 192, 192)
DARK_GREEN = (0, 100, 0)
BROWN = (139, 69, 19)
LIGHT_GREEN = (144, 238, 144)  # Light green color

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rajdeep\'s Snake Xenia')

# Font and Clock
font_style = pygame.font.SysFont(None, 50)
small_font = pygame.font.SysFont(None, 35)
clock = pygame.time.Clock()

def display_message(msg, color, font, y_displacement=0):
    message = font.render(msg, True, color)
    rect = message.get_rect(center=(WIDTH / 2, HEIGHT / 2 + y_displacement))
    screen.blit(message, rect)

def welcome_screen():
    welcome = True
    while welcome:
        screen.fill(WHITE)
        
        display_message("Welcome to", BLUE, font_style, -50)
        display_message("Rajdeep's Snake Xenia", GREEN, font_style, 0)
        display_message("Press Enter to Start the Game", BLACK, small_font, 50)
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    welcome = False

    game_loop()

def game_loop():
    game_over = False
    game_close = False

    x1, y1 = WIDTH / 2, HEIGHT / 2
    x1_change, y1_change = 0, 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 20.0) * 20.0
    foody = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 20.0) * 20.0

    while not game_over:
        while game_close:
            screen.fill(WHITE)
            display_message("You Lost! Press Q-Quit or C-Play Again", RED, font_style)
            display_message("Score: " + str(length_of_snake - 1), BLACK, small_font, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -SNAKE_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = SNAKE_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -SNAKE_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = SNAKE_SIZE
                    x1_change = 0
                elif event.key == pygame.K_RETURN:
                    game_close = False

        # Handle the snake crossing the screen boundaries
        if x1 >= WIDTH:
            x1 = 0
        elif x1 < 0:
            x1 = WIDTH - SNAKE_SIZE
        if y1 >= HEIGHT:
            y1 = 0
        elif y1 < 0:
            y1 = HEIGHT - SNAKE_SIZE

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLUE)
        
        # Draw grass and soil
        pygame.draw.rect(screen, DARK_GREEN, [0, HEIGHT - 100, WIDTH, 50])
        pygame.draw.rect(screen, BROWN, [0, HEIGHT - 50, WIDTH, 50])
        
        # Draw the food as a circle
        pygame.draw.circle(screen, RED, (foodx + SNAKE_SIZE // 2, foody + SNAKE_SIZE // 2), SNAKE_SIZE // 2)
        
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(SNAKE_SIZE, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

def display_score(score):
    value = small_font.render("Score: " + str(score), True, BLACK)
    screen.blit(value, [0, 0])

def our_snake(snake_size, snake_list):
    for i, (x, y) in enumerate(snake_list):
        pygame.draw.circle(screen, LIGHT_GREEN, (x + snake_size // 2, y + snake_size // 2), snake_size // 2)
        if i == 0:
            pygame.draw.circle(screen, DARK_GREEN, (x + snake_size // 2, y + snake_size // 2), snake_size // 2)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Start the game with the welcome screen
welcome_screen()
