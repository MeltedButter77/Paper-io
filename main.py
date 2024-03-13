import random
import pygame
import sys

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
    # Loop through every event inputted to pygame from the user (this may be multiple per frame)
    for event in pygame.event.get():
        # if the event type is clicking the quit button
        if event.type == pygame.QUIT:
            running = False
        # if the snake is alive
        if is_alive:
            # if the event type is pressing a key down
            if event.type == pygame.KEYDOWN:
                # if the key being pressed is x, change snake_direction to relevant direction
                if event.key == pygame.K_s:
                    snake_direction = 'down'
                if event.key == pygame.K_w:
                    snake_direction = 'up'
                if event.key == pygame.K_a:
                    snake_direction = 'left'
                if event.key == pygame.K_d:
                    snake_direction = 'right'
            # if the event type is the userevent (triggered every 200 milliseconds)
            if event.type == pygame.USEREVENT:
                # Get current head
                x, y = snake[-1][0], snake[-1][1]
                # Add new block of body in appropriate direction
                if snake_direction == 'down':
                    x, y = x, y + grid_size
                if snake_direction == 'up':
                    x, y = x, y - grid_size
                if snake_direction == 'left':
                    x, y = x - grid_size, y
                if snake_direction == 'right':
                    x, y = x + grid_size, y
                
                # If the new location goes off-screen, loop it around
                if x > screen.get_width() - grid_size:
                    x = 0
                if x < 0:
                    x = screen.get_width() - grid_size
                if y > screen.get_height() - grid_size:
                    y = 0
                if y < 0:
                    y = screen.get_height() - grid_size
                
                # Add piece to the snake
                snake.append((x, y))
                # Remove last piece of snake
                snake.pop(0)
        # else if snake is dead
        else:
            # if event type is a key being pressed down
            if event.type == pygame.KEYDOWN:
                # if the event key is the space bar
                if event.key == pygame.K_SPACE:
                    # Reset snake information
                    snake = [(5 * grid_size, 5 * grid_size), (4 * grid_size, 5 * grid_size)]
                    snake_direction = 'right'
                    is_alive = True

    # iterate through the snake excluding the head
    for body_piece in snake:
        if snake.index(body_piece) == len(snake) - 1:
            continue
        # Check for Collisions with the body
        if snake[-1] == body_piece and len(snake) > 3:
            is_alive = False

    # Check for Collisions between the cherry and the head
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
    textsurface = font.render("Length: " + str(len(snake)), False, "white")
    # Draw the textSurface to the screen
    screen.blit(textsurface, (10, 10))

    # Update the drawings onto the screen
    pygame.display.update()
    # Clear the screen
    screen.fill((0, 0, 0))
    # Ratelimit program to run at 60 frames per second
    clock.tick(60)

# Quits the pygame window, then the application
pygame.quit()
sys.exit()
