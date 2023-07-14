from sprites.obstacles.base_obstacle import Obstacle


class EarthRock(Obstacle):
    def __init__(self, clsz, ground_element):
        super().__init__(clsz, ground_element, "./assets/obstacles/earth_rock.png")
