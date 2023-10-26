import pygame

pygame.init()

gameWindow = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

keys = []
key = None
grid_size = 20
keys_to_remove = []
speed = 200  # snake moves every speed milliseconds
snake = [(0, 0)]
pygame.time.set_timer(pygame.USEREVENT, speed)
isAlive = True
while True:
    while isAlive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                keys.insert(0, event.key)
                if event.key == pygame.K_f:
                    snake.insert(0, snake[-1])
            if event.type == pygame.KEYUP:
                keys_to_remove.append(event.key)

            if event.type == pygame.USEREVENT:
                # Store last wasd key as key
                if len(keys) > 0:
                    opposite_keys = {pygame.K_w: pygame.K_s, pygame.K_s: pygame.K_w,
                                     pygame.K_a: pygame.K_d, pygame.K_d: pygame.K_a}
                    # If the key is one of the specified ones and is not the opposite of the old key
                    if keys[0] in opposite_keys and keys[0] != opposite_keys.get(key, None):
                        key = keys[0]
                    for thing in keys_to_remove:
                        print(keys, keys_to_remove)
                        keys.remove(thing)
                    keys_to_remove = []

                x, y = snake[-1][0], snake[-1][1]
                if key == pygame.K_w:
                    y -= grid_size
                    print("up")
                if key == pygame.K_s:
                    y += grid_size
                    print("down")
                if key == pygame.K_d:
                    x += grid_size
                    print("right")
                if key == pygame.K_a:
                    x -= grid_size
                    print("left")
                # Adds new snake to the end of the list, head in -1 index
                snake.append((x, y))
                snake.pop(0)

        head_rect = pygame.Rect(snake[-1], (grid_size, grid_size))

        for loc in snake:
            rect = pygame.Rect(loc, (grid_size, grid_size))
            pygame.draw.rect(gameWindow, (0, 0, 255), rect)
        pygame.draw.rect(gameWindow, (0, 255, 0), head_rect)
        pygame.display.update()
        gameWindow.fill((0, 0, 0))
        clock.tick(60)
