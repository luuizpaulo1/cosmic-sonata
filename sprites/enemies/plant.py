from dataclasses import dataclass
from datetime import datetime

from sprites.enemies.base_enemy import Enemy
from sprites.enemies.projectile import Projectile


@dataclass
class Velocity:
    x: int
    y: int


class Plant(Enemy):
    def __init__(self, clsz, ground_element):
        super().__init__(clsz, ground_element, "./assets/enemies/plant.png", frames=1)
        self.shoot_reload_time = 10
        self.last_shoot = None

    def shoot(self):
        new_projectile = Projectile(self.game)
        new_projectile.set_position(self.x, self.y + self.height / 3)
        self.game.projectiles.append(new_projectile)

    def action(self):
        self.x = self.ground_element.x + self.ground_element.sprite_offset
        now = datetime.now()
        if self.last_shoot is None or (now - self.last_shoot).seconds >= self.shoot_reload_time:
            self.shoot()
            self.last_shoot = now
