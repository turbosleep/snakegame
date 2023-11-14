import pygame
import time
import random
pygame.init()
width, height = 800, 600
fullscreen = False
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')
def toggle_fullscreen():
    global width, height, fullscreen
    fullscreen = not fullscreen
    if fullscreen:
        pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    else:
        width, height = 800, 600
        pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')

def game_loop():
    global width, height, fullscreen
    clock = pygame.time.Clock()
    
    while True:
        game_over = False
        game_close = False
        snake_list = []
        length_of_snake = 1
        x = width / 2
        y = height / 2
        x_change = 0
        y_change = 0
        apples = []
        
        for _ in range(apples_count):
            apple_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            apple_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            apples.append((apple_x, apple_y))
        
        while not game_over:
            while game_close:
                game_display.fill(black)
                our_snake(snake_block, snake_list)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            game_loop()
                        elif event.key == pygame.K_c:
                            pygame.quit()
                            quit()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        x_change = -snake_block
                        y_change = 0
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        x_change = snake_block
                        y_change = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        y_change = -snake_block
                        x_change = 0
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        y_change = snake_block
                        x_change = 0
                    elif event.key == pygame.K_f:
                        toggle_fullscreen()

            x += x_change
            y += y_change

            if x >= width or x < 0 or y >= height or y < 0:
                game_close = True

            for apple in apples:
                apple_x, apple_y = apple
                if x == apple_x and y == apple_y:
                    apples.remove(apple)
                    apples.append((round(random.randrange(0, width - snake_block) / 10.0) * 10.0,
                                   round(random.randrange(0, height - snake_block) / 10.0) * 10.0))
                    length_of_snake += 1

            game_display.fill(black)
            for apple in apples:
                draw_apple(apple[0], apple[1])
            snake_head = []
            snake_head.append(x)
            snake_head.append(y)
            snake_list.append(snake_head)

            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for segment in snake_list[:-1]:
                if segment == snake_head:
                    game_close = True

            our_snake(snake_block, snake_list)
            pygame.display.update()
            clock.tick(fps)

        pygame.quit()
        quit()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
snake_block = 10
initial_speed = 10
fps = 20
apples_count = 3
hard_mode = False
font = pygame.font.SysFont(None, 35)

def our_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        if i == 0:
            pygame.draw.rect(game_display, (0, 255, 0), [x[0], x[1], snake_block, snake_block])
        else:
            color = green if i % 2 == 0 else (0, 100, 0)
            pygame.draw.rect(game_display, color, [x[0], x[1], snake_block, snake_block])

def draw_apple(apple_x, apple_y):
    pygame.draw.rect(game_display, red, [apple_x, apple_y, snake_block, snake_block])

def hard_mode_update():
    global width, height, fps
    width -= 100
    height -= 100
    fps += 5

game_loop()
