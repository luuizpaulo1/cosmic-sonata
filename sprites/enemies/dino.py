from sprites.enemies.base_enemy import Enemy


class Dinosaur(Enemy):
    def __init__(self, clsz, ground_element):
        super().__init__(clsz, ground_element, "./assets/enemies/dino.png", frames=4)
        self.set_sequence_time(0, 2, 75)
