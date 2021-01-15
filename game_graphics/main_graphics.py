import pygame
import json
import main_menu_graphics

window = None
color_scheme = None
settings = None


def init_graphics(screen, options):
    global window
    global settings
    window = screen
    settings = options


def init_colors():
    global color_scheme
    with open("../resources/color_settings.json") as settings_file:
        color_scheme = json.load(settings_file)


if __name__ == '__main__':
    print("Sunt un main!")
