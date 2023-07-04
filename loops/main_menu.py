from PPlay.gameimage import GameImage
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
from PPlay.sprite import Sprite
from PPlay.window import Window
from loops.difficulty_menu import DifficultyMenu
from loops.cosmic_sonata import CosmicSonata


class MainMenu:
    def __init__(self, window: Window, mouse: Mouse, keyboard: Keyboard):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.background = GameImage("./assets/background.png")
        self.start = Sprite("./assets/buttons/start.png")
        self.difficulty_button = Sprite("./assets/buttons/difficulty.png")
        self.ranking_button = Sprite("./assets/buttons/ranking.png")
        self.exit_button = Sprite("./assets/buttons/exit.png")
        self.finish = False

        self.start.set_position((self.background.width / 2) - (self.start.width / 2), 50)
        self.difficulty_button.set_position((self.background.width / 2) - (self.difficulty_button.width / 2), 150)
        self.ranking_button.set_position((self.background.width / 2) - (self.ranking_button.width / 2), 250)
        self.exit_button.set_position((self.background.width / 2) - (self.exit_button.width / 2), 350)

        self.diff_menu = DifficultyMenu(self.window, self.mouse, self.keyboard)
        self.cosmic_sonata = CosmicSonata(self.window, self.mouse, self.keyboard)

    def loop(self):
        if self.mouse.is_over_object(self.start) and self.mouse.is_button_pressed(1):
            while True:
                self.cosmic_sonata.finish = False
                self.cosmic_sonata.loop()
                if self.cosmic_sonata.finish:
                    break
                self.window.update()

        if self.mouse.is_over_object(self.difficulty_button) and self.mouse.is_button_pressed(1):
            while True:
                self.diff_menu.finish = False
                self.diff_menu.loop()
                if self.diff_menu.finish:
                    break
                self.window.update()

        if self.mouse.is_over_object(self.ranking_button) and self.mouse.is_button_pressed(1):
            # see ranking menu
            ...

        if self.mouse.is_over_object(self.exit_button) and self.mouse.is_button_pressed(1):
            self.finish = True

        self.background.draw()
        self.start.draw()
        self.difficulty_button.draw()
        self.ranking_button.draw()
        self.exit_button.draw()
