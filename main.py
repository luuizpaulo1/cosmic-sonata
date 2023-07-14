from pygame import mixer

from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
from PPlay.window import Window
from db import DB
from loops.main_menu import MainMenu

window = Window(1000, 500)
keyboard = Keyboard()
mouse = Mouse()

database = DB()
database.create_user_score_table()

main_menu = MainMenu(window, mouse, keyboard, database)

mixer.init()
mixer.music.load("./assets/song.mp3")
mixer.music.play()

while True:
    main_menu.loop()
    if main_menu.finish:
        break
    window.update()
