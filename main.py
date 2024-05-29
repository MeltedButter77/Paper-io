import pygame
import random
pygame.init()

screen = pygame.display.set_mode((600, 600))
grid_size = 30

time_delay = 200
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, time_delay)


class Snake():
    def __init__(self, location, controls):
        self.head = pygame.Rect(location, (grid_size, grid_size))
        self.body = [pygame.Rect((location[0] + grid_size, location[1]), (grid_size, grid_size))]

        self.controls = controls
        self.isAlive = True

        self.direction = None

    def handle_event(self, event):
        if not self.isAlive:
            return
        if event.type == pygame.KEYDOWN:
            if event.key == self.controls[0]:
                self.direction = 'left'
            elif event.key == self.controls[1]:
                self.direction = 'right'
            elif event.key == self.controls[2]:
                self.direction = 'up'
            elif event.key == self.controls[3]:
                self.direction = 'down'
        elif event.type == timer_event:
            if self.direction:
                self.body.insert(0, self.head.copy())
                self.body.pop()

            if self.direction == 'left':
                self.head.x -= grid_size
            elif self.direction == 'right':
                self.head.x += grid_size
            elif self.direction == 'up':
                self.head.y -= grid_size
            elif self.direction == 'down':
                self.head.y += grid_size

            for apple in apples:
                if self.head.colliderect(apple):
                    apple.x = random.randint(0, (screen.get_width() - grid_size) // grid_size) * grid_size
                    apple.y = random.randint(0, (screen.get_height() - grid_size) // grid_size) * grid_size
                    self.body.insert(-1, pygame.Rect(self.body[-1].x, self.body[-1].y, grid_size, grid_size))

            if self.head.right > (screen.get_width() - grid_size) or self.head.left < 0 or self.head.top < 0 or self.head.bottom > (screen.get_height() - grid_size):
                self.isAlive = False

            for segment in self.body:
                # Check for Collisions with the body
                if self.head.colliderect(segment):
                    self.isAlive = False

    def draw(self):
        if self.isAlive:
            colour = "green"
        else:
            colour = "red"

        pygame.draw.rect(screen, colour, self.head)
        for rect in self.body:
            pygame.draw.rect(screen, colour, rect)

# Setup, the game can be changed my modifying this without having to change the logic above!
snake1 = Snake((5 * grid_size, 5 * grid_size), (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN))
snake2 = Snake((15 * grid_size, 15 * grid_size), (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s))
snakes = [snake1, snake2]
apple1 = pygame.Rect(grid_size * 3, grid_size * 3, grid_size, grid_size)
apple2 = pygame.Rect(grid_size * 3, grid_size * 3, grid_size, grid_size)
apples = [apple1, apple2]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        for snake in snakes:
            snake.handle_event(event)

    screen.fill("gray")
    for snake in snakes:
        snake.draw()
    for apple in apples:
        pygame.draw.rect(screen, "red", apple)

    pygame.display.update()
