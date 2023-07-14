from dataclasses import dataclass
from datetime import datetime

import pygame

from PPlay.sprite import Sprite
from mappings import gravity_by_scenario
from sprites.powerups.base_powerup import BasePowerUp


@dataclass
class Velocity:
    x: int
    y: int


class Astronaut(Sprite):
    def __init__(self, clsz):
        super().__init__("./assets/astronaut.png", frames=8)
        self.game = clsz
        self.set_sequence_time(0, 7, 75)
        self.velocity = Velocity(x=350 * self.game.difficulty_multiplier, y=0)
        self.is_jumping = False
        self.is_walking = True
        self.is_invincible = False
        self.last_invincible_time = None
        self.invincible_time = 5

        self.set_position(20, self.game.window.height - self.game.ground.height - self.height)

    @property
    def is_touching_ground(self):
        return any([self.collided(ground) for ground in self.game.ground.elements])

    @property
    def is_colliding_with_obstacle(self):
        if self.is_invincible:
            return False
        obstacles = [element.sprite for element in self.game.ground.elements if element.sprite is not None and not isinstance(element.sprite, BasePowerUp)]
        return any(self.collided(obstacle) for obstacle in obstacles)

    @property
    def is_colliding_with_power_up(self):
        for element in self.game.ground.elements:
            if isinstance(element.sprite, BasePowerUp) and self.collided(element.sprite):
                element.sprite = None
                return True

    def jump(self):
        self.velocity.y = -1000
        self.is_jumping = True

    def update_jump(self):
        self.velocity.y += gravity_by_scenario[self.game.scenario] * self.game.window.delta_time()
        self.y += self.velocity.y * self.game.window.delta_time()

        if self.is_touching_ground:
            self.is_jumping = False
            self.velocity.y = 0

    def action(self):
        now = datetime.now()
        self.play()

        if not self.is_walking:
            self.set_curr_frame(0)
            self.pause()

        if self.is_jumping:
            self.update_jump()
            self.set_curr_frame(2)
            self.pause()

        elif self.game.keyboard.key_pressed("SPACE"):
            self.jump()

        if self.is_colliding_with_obstacle:
            self.game.game_over = True

        if self.is_colliding_with_power_up:
            self.is_invincible = True
            self.image = pygame.image.load("./assets/powerup_astronaut.png")
            self.last_invincible_time = now

        if self.is_invincible:
            if (now - self.last_invincible_time).seconds >= self.invincible_time:
                self.image = pygame.image.load("./assets/astronaut.png")
                self.is_invincible = False
