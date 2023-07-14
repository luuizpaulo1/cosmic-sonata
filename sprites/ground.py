from random import random, choice, randint
from typing import Optional, Union

from PPlay.sprite import Sprite
from loops.cosmic_sonata import Scenario
from mappings import ground_by_scenario, enemies_by_scenario, obstacles_by_scenario
from sprites.enemies.base_enemy import Enemy
from sprites.obstacles.base_obstacle import Obstacle


class GroundElement(Sprite):
    def __init__(self, scenario: Scenario):
        super().__init__(f"./assets/grounds/{ground_by_scenario[scenario]}")
        self.sprite: Optional[Union[Obstacle, Enemy]] = None
        self.sprite_offset: int = randint(0, int(self.width / 2)) if not isinstance(self.sprite, Enemy) else self.width

    def add_sprite(self, sprite: Sprite):
        self.sprite = sprite
        if sprite:
            self.sprite.set_position(
                (self.x + self.sprite_offset) if isinstance(self.sprite, Obstacle) else self.x + self.width,
                self.y - sprite.height
            )


class Ground:
    def __init__(self, game):
        self.game = game
        self.elements: list[GroundElement] = [
            GroundElement(self.game.scenario) for _ in range(3)]  # elements of the ground

        for index, element in enumerate(self.elements):
            element.set_position(index * element.width, self.game.window.height - element.height)

        self.height = self.elements[0].height
        self.width = self.game.window.width

    def move_elements(self):
        for element in self.elements:
            element.x -= (
                             self.game.astronaut.velocity.x if self.game.astronaut.is_walking else 0
                         ) * self.game.window.delta_time()

    def expire_elements(self):
        left_element = self.elements[0]
        if left_element.x <= -left_element.width:
            self.elements.remove(left_element)

    def create_new_elements(self):
        right_element = self.elements[-1]
        random_value = random()
        if right_element.x + right_element.width <= self.game.window.width + 15:
            new_element = GroundElement(scenario=self.game.scenario)
            new_element.set_position(
                right_element.x + right_element.width,
                self.game.window.height - new_element.height
            )
            self.elements.append(new_element)

            if 0.0 <= random_value <= 0.0:  # 40% chance it will spawn some obstacle
                sprite_class = choice(obstacles_by_scenario[self.game.scenario])
                sprite = sprite_class(self.game, new_element)
            elif random_value > 0.5:  # 20% chance it will spawn some enemy
                sprite_class = choice(enemies_by_scenario[self.game.scenario])
                sprite = sprite_class(self.game, new_element)
            else:
                sprite = None
            new_element.add_sprite(sprite)

    def action(self):
        self.move_elements()
        self.expire_elements()
        self.create_new_elements()
        for element in self.elements:
            if element.sprite:
                element.sprite.draw()
                element.sprite.action()
                if element.sprite.number_of_frames > 1:
                    element.sprite.update()

    def draw(self):
        for element in self.elements:
            element.draw()

    def update(self):
        for index in range(len(self.elements)):
            self.elements[index] = GroundElement(self.game.scenario)
            element = self.elements[index]
            element.set_position(element.x, self.game.window.height - element.height)
