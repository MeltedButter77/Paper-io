import random
import pygame

# Pygame and window setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Segoe UI", 35)

# Game variables
grid_size = 80
move_interval = 200  # snake moves every speed milliseconds
pygame.time.set_timer(pygame.USEREVENT, move_interval)

# Cherry Info
cherry_location = random.randint(0, round(screen.get_width() / grid_size) - 1) * grid_size, random.randint(0, round(screen.get_height() / grid_size) - 1) * grid_size

# Snake information
snake = [(5 * grid_size, 5 * grid_size), (4 * grid_size, 5 * grid_size)]
snake_direction = 'right'

# Sets game variables
is_alive = True
running = True

# Create game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if is_alive:
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
                    snake.insert(0, snake[0])
            if event.type == pygame.USEREVENT:
                # Get current head
                x, y = snake[-1][0], snake[-1][1]
                # Add new block of body in appropriate direction
                if snake_direction == 'down':
                    snake.append((x, y + grid_size))
                if snake_direction == 'up':
                    snake.append((x, y - grid_size))
                if snake_direction == 'left':
                    snake.append((x - grid_size, y))
                if snake_direction == 'right':
                    snake.append((x + grid_size, y))
                snake.pop(0)
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    snake = [(5 * grid_size, 5 * grid_size), (4 * grid_size, 5 * grid_size)]
                    snake_direction = 'right'
                    is_alive = True

        # iterate through the snake excluding the head
        body = snake.copy()
        body.pop(-1)
        for body_piece in body:
            # Check for Collisions with the body
            if snake[-1] == body_piece and len(snake) > 3:
                is_alive = False
        # Check for Collisions with the cherry
        if snake[-1] == cherry_location:
            snake.insert(0, snake[0])
            cherry_location = random.randint(0, round(screen.get_width() / grid_size) - 1) * grid_size, random.randint(0, round(screen.get_height() / grid_size) - 1) * grid_size
            while cherry_location in snake:
                cherry_location = random.randint(0, round(screen.get_width() / grid_size) - 1) * grid_size, random.randint(0, round(screen.get_height() / grid_size) - 1) * grid_size

    # Draws the snake
    for body in snake:
        # multiplies the location tuple by grid_size
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(body, (grid_size, grid_size)))

    # Redraw the head in green
    head_rect = pygame.Rect(snake[-1], (grid_size, grid_size))
    pygame.draw.rect(screen, (0, 255, 0), head_rect)

    # Draw Cherry, multiplies the location tuple by grid_size
    cherry_rect = pygame.Rect(cherry_location, (grid_size, grid_size))
    pygame.draw.rect(screen, (255, 0, 0), cherry_rect)

    # Create a surface with text on it
    textsurface = font.render(str(len(snake)), False, "blue")
    # Draw the textSurface to the screen
    screen.blit(textsurface, (10, 10))

    # Update the drawings onto the screen
    pygame.display.update()
    # Clear the screen
    screen.fill((0, 0, 0))
    # Ratelimit program to run at 60 frames per second
    clock.tick(60)


pygame.quit()
sys.exit()
quit()