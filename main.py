import pygame

pygame.init()

gameWindow = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

keys = []
key = None
length = 1
speed = 200  # snake moves every speed milliseconds
pygame.time.set_timer(pygame.USEREVENT, speed)
isAlive = True

snake = [(0,0)]

while True:
    while isAlive:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                keys.insert(0, event.key)
                if event.key == pygame.K_f:
                    length += 1
            if event.type == pygame.KEYUP:
                keys.remove(event.key)

            if event.type == pygame.USEREVENT:
                if key == pygame.K_w:
                    snake.append(snake[0][0] + 20, snake[0[1]])
                if key == pygame.K_s:
                    y += 10
                    print("down")
                if key == pygame.K_d:
                    x += 10
                    print("right")
                if key == pygame.K_a:
                    x -= 10
                    print("left")
                snake.insert(0, {'rect': pygame.Rect(x, y, 10, 10), 'color': (0, 0, 255)})
                if len(snake) > length:
                    snake.pop()
        # Store last wasd key as key
        if len(keys) > 0:
            if keys[0] == pygame.K_w or keys[0] == pygame.K_s or keys[0] == pygame.K_d or keys[0] == pygame.K_a:
                key = keys[0]

        for i in range(len(snake) - 1):
            if snake[0]['rect'].colliderect(snake[i + 1]['rect']):
                isAlive = False

        for square in snake:
            pygame.draw.rect(gameWindow, square['color'], square['rect'])
        pygame.display.update()
        gameWindow.fill((0, 0, 0))
        clock.tick(60)
