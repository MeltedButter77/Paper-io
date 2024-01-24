import pygame

pygame.init()

gameWindow = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

grid_size = 20
move_interval = 200  # snake moves every speed milliseconds
snake = [(0, 0)]
pygame.time.set_timer(pygame.USEREVENT, move_interval)
snake_direction = 'right'
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                snake_direction = 'down'
            if event.key == pygame.K_w:
                snake_direction = 'up'
            if event.key == pygame.K_a:
                snake_direction = 'left'
            if event.key == pygame.K_d:
                snake_direction = 'right'

            if event.key == pygame.K_f:
                snake.insert(0, snake[-1])

        if event.type == pygame.USEREVENT:
            # Get current head
            x, y = snake[-1][0], snake[-1][1]
            if snake_direction == 'down':
                snake.append((x, y + grid_size))
            if snake_direction == 'up':
                snake.append((x, y - grid_size))
            if snake_direction == 'left':
                snake.append((x - grid_size, y))
            if snake_direction == 'right':
                snake.append((x + grid_size, y))
            snake.pop(0)

    for loc in snake:
        pygame.draw.rect(gameWindow, (0, 0, 255), pygame.Rect(loc, (grid_size, grid_size)))
    head_rect = pygame.Rect(snake[-1], (grid_size, grid_size))
    pygame.draw.rect(gameWindow, (0, 255, 0), head_rect)

    pygame.display.update()
    gameWindow.fill((0, 0, 0))
    clock.tick(60)
