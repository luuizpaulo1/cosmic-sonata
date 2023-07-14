from PPlay.sprite import Sprite


class Projectile(Sprite):
    def __init__(self, clsz):
        super().__init__("./assets/enemies/plant_shot.png", frames=1)
        self.game = clsz
        self.velocity = -500

    def action(self):
        print(f"{self.x=}")
        self.x += (self.velocity - self.game.astronaut.velocity.x) * self.game.window.delta_time()
