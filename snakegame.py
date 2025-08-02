import pygame
import time
import random

pygame.init()
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

width, height = 600, 400
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

def gameLoop():
    x = width // 2
    y = height // 2
    dx, dy = 0, 0
    snake = []
    length = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = snake_block, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -snake_block
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, snake_block

        x += dx
        y += dy
        win.fill(white)

        pygame.draw.rect(win, green, [foodx, foody, snake_block, snake_block])
        head = [x, y]
        snake.append(head)
        if len(snake) > length:
            del snake[0]
        for segment in snake[:-1]:
            if segment == head:
                run = False
        for segment in snake:
            pygame.draw.rect(win, black, [segment[0], segment[1], snake_block, snake_block])
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length += 1
        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()

gameLoop()
