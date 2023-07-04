from PPlay.gameimage import GameImage
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
from PPlay.window import Window
from sprites.astronaut import Astronaut
from sprites.ground import Ground


class CosmicSonata:
    def __init__(self, window: Window, mouse: Mouse, keyboard: Keyboard):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.background = GameImage("./assets/background.png")
        self.ground = Ground(self)
        self.astronaut = Astronaut(self)

        self.finish = False

    def loop(self):
        self.background.draw()
        self.astronaut.draw()
        self.ground.draw()

        self.astronaut.action()
        self.ground.action()

        self.astronaut.update()

        if self.keyboard.key_pressed("ESC"):
            self.finish = True
