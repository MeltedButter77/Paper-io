import pygame
import game
import menu


class App:
    def __init__(self):
        self.window_size = (800, 800)
        self.active_game = None
        self.selected = menu.Menu(self, self.window_size, menu="main_menu").run()

    def run(self):
        while True:
            match self.selected:
                case "play":
                    self.active_game = game.Game(self.window_size)
                    self.selected = self.active_game.run()
                case "resume":
                    self.selected = self.active_game.run()
                case "quit":
                    pygame.quit()
                    quit()

                # if the button does not return an action case
                # send button's id to the menu selector
                case _:
                    self.selected = menu.Menu(self, self.window_size, menu=self.selected).run()

                    # Handle invalid menu case
                    if self.selected is None:
                        self.selected = menu.Menu(self, self.window_size, menu="main_menu").run()


App().run()
