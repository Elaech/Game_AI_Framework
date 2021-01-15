import pygame
import json
import main_menu_graphics

window = None
color_scheme = None


def init_window(screen):
    global window
    window = screen


def init_colors():
    global color_scheme
    with open("../resources/color_settings.json") as settings_file:
        color_scheme = json.load(settings_file)


if __name__ == '__main__':
    print("Sunt un main!")
