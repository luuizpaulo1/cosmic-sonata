from PPlay.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, clsz, ground_element, *args, **kwargs):
        self.game = clsz
        self.ground_element = ground_element
        self.velocity = -100
        super().__init__(*args, **kwargs)

    def action(self):
        new_offset = self.ground_element.sprite_offset + self.velocity * self.game.window.delta_time()
        self.ground_element.sprite_offset = new_offset
        self.x = self.ground_element.x + new_offset
