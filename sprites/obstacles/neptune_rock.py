from sprites.obstacles.base_obstacle import Obstacle


class NeptuneRock(Obstacle):
    def __init__(self, clsz, ground_element):
        super().__init__(clsz, ground_element, "./assets/obstacles/neptune_rock.png")
