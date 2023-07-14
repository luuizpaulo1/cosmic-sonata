from sprites.obstacles.base_obstacle import Obstacle


class MoonRock(Obstacle):
    def __init__(self, clsz, ground_element):
        super().__init__(clsz, ground_element, "./assets/obstacles/moon_rock.png")
