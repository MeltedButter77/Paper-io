import pygame
import game
import menu

window_size = (800, 800)
selected = menu.Menu(window_size, menu="main_menu").run()
active_game = None

while True:
    match selected:
        case "play":
            active_game = game.Game(window_size)
            selected = active_game.run()
        case "resume":
            selected = active_game.run()
        case "quit":
            pygame.quit()
            quit()

        # if the button does not return an action case
        # send button's id to the menu selector
        case _:
            selected = menu.Menu(window_size, menu=selected).run()

            # Handle invalid menu case
            if selected is None:
                selected = menu.Menu(window_size, menu="main_menu").run()
