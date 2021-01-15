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


def quit():
    return None


def init_settings():
    global settings
    with open("../resources/settings.json") as settings_file:
        settings = json.load(settings_file)


def init_application_window():
    global application_screen
    pygame.init()
    pygame.display.set_caption(settings["application_name"])
    application_screen = pygame.display.set_mode((settings["screen_width"], settings["screen_height"]))
    main_graphics.init_graphics(application_screen, settings)


def start_application():
    controller_call = call_main_menu()
    while controller_call is not None:
        controller_call = controller_call()


def end_application():
    pygame.quit()


if __name__ == '__main__':
    init_settings()
    init_application_window()
    start_application()
    end_application()
