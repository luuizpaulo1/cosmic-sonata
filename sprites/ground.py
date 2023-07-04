from typing import Optional

from PPlay.sprite import Sprite
from sprites.rock import Rock


class GroundElement(Sprite):
    def __init__(self, sprite=None):
        super().__init__("./assets/ground.png")
        self.sprite: Optional[Sprite] = sprite


class Ground:
    def __init__(self, game):
        self.game = game
        self.elements: list[GroundElement] = [GroundElement() for _ in range(3)]  # elements of the ground

        for index, element in enumerate(self.elements):
            element.set_position(index * element.width, self.game.window.height - element.height)

        self.height = self.elements[0].height
        self.width = self.game.window.width

    def move_elements(self):
        for element in self.elements:
            element.x -= self.game.astronaut.velocity.x * self.game.window.delta_time()

    def expire_elements(self):
        left_element = self.elements[0]
        if left_element.x <= -left_element.width:
            self.elements.remove(left_element)

    def create_new_elements(self):
        right_element = self.elements[-1]
        if right_element.x + right_element.width <= self.game.window.width + 15:
            sprite = Rock(self.game)
            new_element = GroundElement(sprite)
            new_element.set_position(
                right_element.x + right_element.width,
                self.game.window.height - new_element.height
            )
            self.elements.append(new_element)

    def action(self):
        self.move_elements()
        self.expire_elements()
        self.create_new_elements()
        for element in self.elements:
            if element.sprite:
                element.sprite.set_position(element.x + element.width / 2, element.y - element.sprite.height)
                element.sprite.draw()

    def draw(self):
        for element in self.elements:
            element.draw()


