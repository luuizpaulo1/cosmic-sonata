from PPlay.sprite import Sprite


class Rock(Sprite):
    def __init__(self, clsz):
        super().__init__("./assets/obstacles/rock.png")
        self.game = clsz
