import random
import sys
import pygame
import copy
pygame.init()
screen = pygame.display.set_mode((800, 600))

grid_size = 100
head = pygame.Rect(grid_size * 5, grid_size * 5, grid_size, grid_size)
body = [
    pygame.Rect(grid_size * 4, grid_size * 5, grid_size, grid_size)
]
direction = "up"

apple = pygame.Rect(grid_size * 3, grid_size * 3, grid_size, grid_size)

pygame.time.set_timer(pygame.USEREVENT, 400)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
                    print("ded")

    screen.fill((255, 255, 255))
    for square in body:
        pygame.draw.rect(screen, "blue", square)
    pygame.draw.rect(screen, "blue", head)
    pygame.draw.rect(screen, "red", apple)
    pygame.display.update()

pygame.quit()
sys.exit()
