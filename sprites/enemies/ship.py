from sprites.enemies.base_enemy import Enemy


class Ship(Enemy):
    def __init__(self, clsz, ground_element):
        super().__init__(clsz, ground_element, "./assets/enemies/ship.png", frames=1)
        self.set_sequence_time(0, 2, 75)
