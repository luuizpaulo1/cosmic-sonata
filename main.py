from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
from PPlay.window import Window
from loops.main_menu import MainMenu

window = Window(1000, 500)
keyboard = Keyboard()
mouse = Mouse()

main_menu = MainMenu(window, mouse, keyboard)

while True:
    main_menu.loop()
    if main_menu.finish:
        break
    window.update()
