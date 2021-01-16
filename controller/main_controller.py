import pygame
import json
import game_logic
from game_graphics import main_graphics
import main_menu_controller
import game_settings_controller
import game_play_controller

"""
Main Controller of the application
Contains methods of initialisation and calls to other controllers

Made by Minut Mihai Dimitrie
"""

"""
Global Variables
"""
settings = None
application_screen = None
"""
Controller Methods
"""


def call_main_menu():
    return main_menu_controller.start


def call_game_settings():
    return game_settings_controller.start


def call_play():
    return game_play_controller.start


def call_quit():
    return quit


def quit(settings):
    return None


def init_settings():
    global settings
    with open("../resources/settings.json", "r") as settings_file:
        settings = json.load(settings_file)
    with open("../game_logic/default_score_method.py", "r") as def_score_file:
        with open("../game_logic/score_method.py", "w") as score_file:
            score_file.write(def_score_file.read())
    with open("../game_logic/default_winning_method.py", "r") as def_score_file:
        with open("../game_logic/winning_method.py", "w") as score_file:
            score_file.write(def_score_file.read())


def init_application_window():
    global application_screen
    pygame.init()
    application_screen = pygame.display.set_mode((settings["screen_width"], settings["screen_height"]))
    pygame.display.set_caption(settings["application_name"])
    main_graphics.init_graphics(application_screen, settings)


def start_application():
    controller_call = call_main_menu()
    while controller_call is not None:
        controller_call = controller_call(settings)


def end_application():
    pygame.quit()


def update_settings(options):
    global settings
    settings = options


if __name__ == '__main__':
    init_settings()
    init_application_window()
    start_application()
    end_application()
