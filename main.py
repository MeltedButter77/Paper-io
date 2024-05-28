import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
grid_size = 30

time_delay = 1000
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, time_delay)


class Snake():
    def __init__(self, location, controls):
        self.head = pygame.Rect(location, (grid_size, grid_size))
        self.body = []

        self.controls = controls

        self.direction = None

    def handle_event(self, event):
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
            if self.direction == 'left':
                self.head.x -= grid_size
            elif self.direction == 'right':
                self.head.x += grid_size
            elif self.direction == 'up':
                self.head.y -= grid_size
            elif self.direction == 'down':
                self.head.y += grid_size
            self.body.append(self.head.copy())

    def draw(self):
        pygame.draw.rect(screen, "green", self.head)
        for rect in self.body:
            pygame.draw.rect(screen, "green", rect)


snake1 = Snake((5 * grid_size, 5 * grid_size), (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN))
snake2 = Snake((15 * grid_size, 15 * grid_size), (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s))
snakes = [snake1, snake2]

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

    pygame.display.update()
