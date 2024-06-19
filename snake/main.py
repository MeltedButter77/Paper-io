import random
import sys
import pygame
import copy

# Boiler plate code for pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont("Segoe UI", 35)

grid_size = 40
# Creates head variable as a Rect object which we will move around the screen.
head = pygame.Rect(grid_size * 5, grid_size * 5, grid_size, grid_size)

# Creates a body list which has Rect objects within it. 
# This allows us to easily add more bodies to the list to extend the snake. **This is an important idea**
body = [
    pygame.Rect(grid_size * 4, grid_size * 5, grid_size, grid_size),
]
# Direction variable allows the snake to travel in a direction different to the user input
direction = None

# Creates a Rect object to represent the apple
apple = pygame.Rect(grid_size * 3, grid_size * 3, grid_size, grid_size)

# Create a custom event which is added to the event loop every 0.25 seconds
move_event = pygame.USEREVENT + 1
pygame.time.set_timer(move_event, 250)

# Create a variable to keep track of whether the snake is alive or dead
isAlive = True

# Create the main game loop
while True:
    # Run the event code for every event in the pygame.event.get() list
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and isAlive:
            if event.key == pygame.K_RIGHT:
                if not direction == 'left':
                    direction = "right"
            if event.key == pygame.K_LEFT:
                if not direction == 'right':
                    direction = "left"
            if event.key == pygame.K_UP:
                if not direction == 'down':
                    direction = "up"
            if event.key == pygame.K_DOWN:
                if not direction == 'up':
                    direction = "down"
            if event.key == pygame.K_SPACE:
                body.insert(-1, pygame.Rect(body[-1].x, body[-1].y, grid_size, grid_size))

        elif event.type == pygame.KEYDOWN and not isAlive:
            if event.key == pygame.K_SPACE:
                # Reset game
                head = pygame.Rect(grid_size * 5, grid_size * 5, grid_size, grid_size)
                body = [
                    pygame.Rect(grid_size * 4, grid_size * 5, grid_size, grid_size)
                ]
                direction = None
                isAlive = True

        if event.type == move_event and isAlive:
            if direction == "right":
                body.insert(0, copy.copy(head))
                head.x = head.x + grid_size
            if direction == "left":
                body.insert(0, copy.copy(head))
                head.x = head.x - grid_size
            if direction == "up":
                body.insert(0, copy.copy(head))
                head.y = head.y - grid_size
            if direction == "down":
                body.insert(0, copy.copy(head))
                head.y = head.y + grid_size

            if head.colliderect(apple):
                apple.x = random.randint(0, (screen.get_width() - grid_size) // grid_size) * grid_size
                apple.y = random.randint(0, (screen.get_height() - grid_size) // grid_size) * grid_size
                body.insert(-1, pygame.Rect(body[-1].x, body[-1].y, grid_size, grid_size))

            if head.right > (screen.get_width()) or head.left < 0:
                isAlive = False
            if head.top < 0 or head.bottom > (screen.get_height()):
                isAlive = False

            for segment in body:
                # Check for Collisions with the body
                if head.colliderect(segment):
                    isAlive = False

            # If moving, remove the last segment
            if direction:
                body.pop()

    # Rendering every frame
    screen.fill((64, 64, 64))
    textsurface = font.render(f"Length: {int(len(body) + 1)}", False, "white")  # "text", antialias, color
    screen.blit(textsurface, (2, 2))
    if not isAlive:
        textsurface = font.render("GAME OVER", False, "red")  # "text", antialias, color
        screen.blit(textsurface, (200, 200))

    for square in body:
        pygame.draw.rect(screen, "blue", square)
    pygame.draw.rect(screen, "blue", head)
    pygame.draw.rect(screen, "red", apple)
    pygame.display.update()
