import pygame.freetype
import pygame
from game_graphics import main_graphics as mg


def is_play_button_pressed(mouse):
    x = mouse[0]
    y = mouse[1]
    if mg.width * 2 / 5 < x < mg.width * 3 / 5 and mg.height * 2 / 16 < y < mg.height * 4 / 16:
        return True
    else:
        return False


def is_settings_button_pressed(mouse):
    x = mouse[0]
    y = mouse[1]
    if mg.width * 2 / 5 < x < mg.width * 3 / 5 and mg.height * 6 / 16 < y < mg.height * 8 / 16:
        return True
    else:
        return False


def is_exit_button_pressed(mouse):
    x = mouse[0]
    y = mouse[1]
    if mg.width * 2 / 5 < x < mg.width * 3 / 5 and mg.height * 10 / 16 < y < mg.height * 12 / 16:
        return True
    else:
        return False


def draw_main_menu():
    mg.window.fill(mg.color_scheme["background_color"])
    mg.draw_button(mg.width * 2 / 5, mg.height * 2 / 16, mg.width / 5, mg.height * 2 / 16, "Play")
    mg.draw_button(mg.width * 2 / 5, mg.height * 6 / 16, mg.width / 5, mg.height * 2 / 16, "Settings")
    mg.draw_button(mg.width * 2 / 5, mg.height * 10 / 16, mg.width / 5, mg.height * 2 / 16, "Exit")
    pygame.display.update()
