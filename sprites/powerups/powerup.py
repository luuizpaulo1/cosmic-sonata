from sprites.powerups.base_powerup import BasePowerUp


class PowerUp(BasePowerUp):
    def __init__(self, clsz, ground_element):
        super().__init__(clsz, ground_element, "./assets/powerup.png")
