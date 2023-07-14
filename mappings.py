from PPlay.gameimage import GameImage
from enums import Scenario
from sprites.enemies.alien import Alien
from sprites.enemies.dino import Dinosaur
from sprites.enemies.plant import Plant
from sprites.enemies.ship import Ship
from sprites.enemies.yeti import Yeti
from sprites.obstacles.earth_rock import EarthRock
from sprites.obstacles.jupiter_rock import JupiterRock
from sprites.obstacles.mars_fire import MarsFire
from sprites.obstacles.mars_rock import MarsRock
from sprites.obstacles.moon_rock import MoonRock
from sprites.obstacles.neptune_rock import NeptuneRock

background_by_scenario = {
    Scenario.EARTH: GameImage("./assets/backgrounds/earth_background.png"),
    Scenario.JUPITER: GameImage("./assets/backgrounds/jupiter_background.png"),
    Scenario.MOON: GameImage("./assets/backgrounds/moon_background.png"),
    Scenario.MARS: GameImage("./assets/backgrounds/mars_background.png"),
    Scenario.NEPTUNE: GameImage("./assets/backgrounds/neptune_background.png"),
}

ground_by_scenario = {
    Scenario.EARTH: "earth_ground.png",
    Scenario.JUPITER: "jupiter_ground.png",
    Scenario.MOON: "moon_ground.png",
    Scenario.MARS: "mars_ground.png",
    Scenario.NEPTUNE: "neptune_ground.png",
}

obstacles_by_scenario = {
    Scenario.EARTH: [EarthRock],
    Scenario.JUPITER: [JupiterRock],
    Scenario.MOON: [MoonRock],
    Scenario.MARS: [MarsRock, MarsFire],
    Scenario.NEPTUNE: [NeptuneRock],
}

enemies_by_scenario = {
    Scenario.EARTH: [Plant, Dinosaur],
    Scenario.JUPITER: [Alien],
    Scenario.MOON: [Ship],
    Scenario.MARS: [Alien],
    Scenario.NEPTUNE: [Yeti],
}

gravity_by_scenario = {
    Scenario.EARTH: 2500,
    Scenario.JUPITER: 2500,
    Scenario.MOON: 1750,
    Scenario.MARS: 2500,
    Scenario.NEPTUNE: 2500,
}
