from sprites.enemies.base_enemy import Enemy


class Alien(Enemy):
    def __init__(self, clsz, ground_element):
        super().__init__(clsz, ground_element, "./assets/enemies/alien.png", frames=3)
        self.set_sequence_time(0, 2, 300)
