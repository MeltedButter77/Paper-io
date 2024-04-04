import random
import sys
import pygame
import copy
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont("Segoe UI", 35)

grid_size = 20
head = pygame.Rect(grid_size * 5, grid_size * 5, grid_size, grid_size)
body = [
    pygame.Rect(grid_size * 4, grid_size * 5, grid_size, grid_size)
]
direction = "up"

apple = pygame.Rect(grid_size * 3, grid_size * 3, grid_size, grid_size)

pygame.time.set_timer(pygame.USEREVENT, 250)
isAlive = True
while True:
    while not isAlive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Reset game
                    head = pygame.Rect(grid_size * 5, grid_size * 5, grid_size, grid_size)
                    body = [
                        pygame.Rect(grid_size * 4, grid_size * 5, grid_size, grid_size)
                    ]
                    direction = "up"
                    isAlive = True

        # Rendering every frame
        screen.fill((64, 64, 64))
        textsurface = font.render("GAME OVER", False, "red")  # "text", antialias, color
        screen.blit(textsurface, (200, 200))

        for square in body:
            pygame.draw.rect(screen, "blue", square)
        pygame.draw.rect(screen, "blue", head)
        pygame.draw.rect(screen, "red", apple)
        pygame.display.update()

    while isAlive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction = "right"
                if event.key == pygame.K_LEFT:
                    direction = "left"
                if event.key == pygame.K_UP:
                    direction = "up"
                if event.key == pygame.K_DOWN:
                    direction = "down"
                if event.key == pygame.K_SPACE:
                    body.insert(-1, pygame.Rect(body[-1].x, body[-1].y, grid_size, grid_size))
            if event.type == pygame.USEREVENT:
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
                if direction:
                    body.pop()

                if head.colliderect(apple):
                    apple.x = random.randint(0, (screen.get_width() - grid_size) // grid_size) * grid_size
                    apple.y = random.randint(0, (screen.get_height() - grid_size) // grid_size) * grid_size
                    body.insert(-1, pygame.Rect(body[-1].x, body[-1].y, grid_size, grid_size))

                for segment in body:
                    # Check for Collisions with the body
                    if segment.topleft == head.topleft:
                        isAlive = False

        # Rendering every frame
        screen.fill((64, 64, 64))
        textsurface = font.render(f"Length: {int(len(body) + 1)}", False, "white")  # "text", antialias, color
        screen.blit(textsurface, (2, 2))

        for square in body:
            pygame.draw.rect(screen, "blue", square)
        pygame.draw.rect(screen, "blue", head)
        pygame.draw.rect(screen, "red", apple)
        pygame.display.update()
