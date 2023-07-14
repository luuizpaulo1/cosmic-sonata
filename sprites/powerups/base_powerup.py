from PPlay.sprite import Sprite


class BasePowerUp(Sprite):
    def __init__(self, clsz, ground_element, *args, **kwargs):
        self.game = clsz
        self.ground_element = ground_element
        super().__init__(*args, **kwargs)

    def action(self):
        self.x = self.ground_element.x + self.ground_element.sprite_offset
