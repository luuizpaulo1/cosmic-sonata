from PPlay.gameimage import GameImage
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
from PPlay.window import Window
from db import DB


class RankingMenu:
    def __init__(self, window: Window, mouse: Mouse, keyboard: Keyboard, database: DB):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.database = database

        self.background = GameImage("./assets/backgrounds/earth_background.png")

        self.finish = False

    def show_scores(self):
        user_scores = self.database.get_top_5()
        self.window.draw_text("Name", size=30, color="red", x=200, y=100)
        self.window.draw_text("Score", size=30, color="red", x=400, y=100)
        self.window.draw_text("Date", size=30, color="red", x=600, y=100)
        for index, user_score in enumerate(user_scores):
            self.window.draw_text(
                user_score.name, size=30, color="red", x=200, y=100 + (index + 1) * 70
            )
            self.window.draw_text(
                str(user_score.score),
                size=30,
                color="red",
                x=400,
                y=100 + (index + 1) * 70,
            )
            self.window.draw_text(
                str(user_score.created_at[:19]),
                size=30,
                color="red",
                x=600,
                y=100 + (index + 1) * 70,
            )

    def loop(self):
        while not self.finish:
            self.background.draw()
            self.show_scores()
            self.window.update()
            if self.keyboard.key_pressed("ESC"):
                self.finish = True
