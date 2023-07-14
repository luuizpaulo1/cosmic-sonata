from sprites.obstacles.base_obstacle import Obstacle


class MarsFire(Obstacle):
    def __init__(self, clsz, ground_element):
        super().__init__(clsz, ground_element, "./assets/obstacles/mars_fire.png", frames=7)
        self.set_sequence_time(0, 6, 75)
