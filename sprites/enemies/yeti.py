from sprites.enemies.base_enemy import Enemy


class Yeti(Enemy):
    def __init__(self, clsz, ground_element):
        super().__init__(clsz, ground_element, "./assets/enemies/yeti.png", frames=8)
        self.set_sequence_time(0, 7, 75)
