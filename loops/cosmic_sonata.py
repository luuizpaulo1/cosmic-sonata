from datetime import datetime
from random import randint, choice

from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
from PPlay.window import Window
from db import UserScore, DB
from enums import Scenario
from mappings import background_by_scenario
from sprites.astronaut import Astronaut, Velocity
from sprites.ground import Ground


class CosmicSonata:
    def __init__(self, window: Window, mouse: Mouse, keyboard: Keyboard, database: DB):
        now = datetime.now()
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.database = database

        self.scenario = Scenario.EARTH
        self.scenario_last_updated_at = now
        self.scenario_screen_time = randint(10, 20)
        self.projectiles = []

        self.started_at = now
        self.difficulty_multiplier = 1.0
        self.score = 0
        self.score_last_updated_at = now

        self.background = background_by_scenario[self.scenario]
        self.ground = Ground(self)
        self.astronaut = Astronaut(self)

        self.finish = False
        self.game_over = False

    def show_score(self):
        self.window.draw_text(
            f"SCORE: {str(int(self.score))}",
            color="red",
            size=20,
            x=self.window.width - 130,
            y=0,
        )

    def show_scenario_countdown(self):
        self.window.draw_text(
            f"{str(self.scenario_screen_time - (datetime.now() - self.scenario_last_updated_at).seconds)}",
            color="red",
            size=60,
            x=self.window.width / 2,
            y=self.window.height / 3,
        )

    def scenario_transition(self):
        now = datetime.now()
        self.projectiles = []
        self.scenario = choice([i for i in list(Scenario) if i != self.scenario])
        self.scenario_last_updated_at = now
        self.difficulty_multiplier += 0.15
        self.astronaut.velocity = Velocity(
            self.astronaut.velocity.x * self.difficulty_multiplier,
            self.astronaut.velocity.y,
        )
        self.background = background_by_scenario[self.scenario]
        self.ground.update()

    def draw_game_over(self):
        font_size_header = 50
        font_size_body = 30
        self.window.draw_text(
            "GAME OVER!",
            size=font_size_header,
            color="red",
            x=(self.window.width / 2) - 150,
            y=self.window.height / 2 - font_size_header / 2,
        )
        self.window.draw_text(
            "type your name in the terminal",
            size=font_size_body,
            color="red",
            x=300,
            y=self.window.height / 2 - font_size_body / 2 + font_size_body * 2,
        )

    def move_projectiles(self):
        for projectile in self.projectiles:
            projectile.action()

    def expire_projectiles(self):
        for index_projectile in range(len(self.projectiles) - 1, -1, -1):
            projectile = self.projectiles[index_projectile]
            if not self.astronaut.is_invincible:
                if projectile.collided(self.astronaut):
                    self.game_over = True
                    break

            if self.projectiles[index_projectile].x < 0:
                self.projectiles.pop(index_projectile)

    def draw_projectiles(self):
        for projectile in self.projectiles:
            projectile.draw()

    def loop(self):
        while not self.finish:
            now = datetime.now()

            if (now - self.scenario_last_updated_at).seconds < 1:
                self.astronaut.is_walking = False
            else:
                self.astronaut.is_walking = True

            self.background.draw()
            self.ground.draw()

            self.astronaut.action()
            self.ground.action()

            self.move_projectiles()
            self.expire_projectiles()
            self.draw_projectiles()

            self.astronaut.update()
            self.astronaut.draw()

            if (now - self.score_last_updated_at).seconds >= 1:
                self.score_last_updated_at = now
                self.score += 50 * self.difficulty_multiplier

            if (
                now - self.scenario_last_updated_at
            ).seconds >= self.scenario_screen_time - 5:
                self.show_scenario_countdown()

            if (
                now - self.scenario_last_updated_at
            ).seconds >= self.scenario_screen_time:
                self.scenario_transition()

            self.show_score()
            self.window.update()

            if self.game_over:
                self.draw_game_over()
                self.window.update()
                score = UserScore(
                    input("name: "), score=self.score, created_at=datetime.now()
                )
                self.database.save_user_score(score)
                self.finish = True

            if self.keyboard.key_pressed("ESC"):
                self.finish = True
