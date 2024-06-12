import pygame
import snake


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.font = font = pygame.font.SysFont('Comic Sans MS', 10)

        self.screen = pygame.display.set_mode((800, 800))
        self.grid_size = 20

        # Create a "timer_event" which will be triggered evey "time_delay" milliseconds. This will act as an event which will be processed in the event loop.
        time_delay = 200
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, time_delay)

        self.area = {}

        # We have created the class, now we need to create objects. This creates instances (in this case 2) of the Snake class allowing us to make as many as we want without having to repeat the snake's logic.
        self.snakes = pygame.sprite.Group()

        snake.Snake(self, (15 * self.grid_size, 15 * self.grid_size), pygame.color.Color(200, 0, 0), (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN), self.snakes)
        snake.Snake(self, (6 * self.grid_size, 6 * self.grid_size), pygame.color.Color(0, 200, 0), (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s), self.snakes)
        snake.Snake(self, (25 * self.grid_size, 6 * self.grid_size), pygame.color.Color(0, 0, 200), (pygame.K_j, pygame.K_l, pygame.K_i, pygame.K_k), self.snakes)

    def run(self):
        # This is the entire game loop. Look how much smaller and easier it is to read now that we are using objects!
        while True:
            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                for snake in self.snakes:
                    snake.handle_event(event, self.snakes)

            # Rendering
            for loc, colour in self.area.items():
                pygame.draw.rect(self.screen, colour, pygame.Rect(loc, (self.grid_size, self.grid_size)))
            for snake in self.snakes:
                snake.draw()

            # Don't forget to update the screen after rendering
            pygame.display.update()
            self.screen.fill("gray")


Game().run()
