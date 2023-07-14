from PPlay.gameimage import GameImage
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
from PPlay.sprite import Sprite
from PPlay.window import Window
from db import DB
from loops.cosmic_sonata import CosmicSonata
from loops.difficulty_menu import DifficultyMenu
from loops.ranking_menu import RankingMenu


class MainMenu:
    def __init__(self, window: Window, mouse: Mouse, keyboard: Keyboard, database: DB):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.database = database
        self.background = GameImage("./assets/backgrounds/earth_background.png")
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
        self.ranking_menu = RankingMenu(self.window, self.mouse, self.keyboard, self.database)
        self.cosmic_sonata = CosmicSonata(self.window, self.mouse, self.keyboard, self.database)

    def loop(self):
        if self.mouse.is_over_object(self.start) and self.mouse.is_button_pressed(1):
            self.cosmic_sonata = CosmicSonata(self.window, self.mouse, self.keyboard, self.database)
            self.cosmic_sonata.loop()

        if self.mouse.is_over_object(self.difficulty_button) and self.mouse.is_button_pressed(1):
            self.diff_menu.finish = False
            self.diff_menu.loop()

        if self.mouse.is_over_object(self.ranking_button) and self.mouse.is_button_pressed(1):
            self.ranking_menu.finish = False
            self.ranking_menu.loop()

        if self.mouse.is_over_object(self.exit_button) and self.mouse.is_button_pressed(1):
            self.finish = True

        self.background.draw()
        self.start.draw()
        self.difficulty_button.draw()
        self.ranking_button.draw()
        self.exit_button.draw()
        self.window.update()
