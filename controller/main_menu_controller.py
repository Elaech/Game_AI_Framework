from controller import main_controller
import pygame
from game_graphics import main_menu_graphics

"""
Main Menu controller that controls the interaction between the user and the application's main menu

Made by Minut Mihai Dimitrie
"""


def get_callable(mouse):
    if clicked_on_play(mouse):
        return main_controller.call_play()
    elif clicked_on_settings(mouse):
        return main_controller.call_game_settings()
    elif clicked_on_exit(mouse):
        return main_controller.call_quit()
    return None


def clicked_on_play(mouse):
    return main_menu_graphics.is_play_button_pressed(mouse)


def clicked_on_exit(mouse):
    return main_menu_graphics.is_exit_button_pressed(mouse)


def clicked_on_settings(mouse):
    return main_menu_graphics.is_settings_button_pressed(mouse)


def start(settings):
    clock = pygame.time.Clock()
    main_menu_graphics.draw_main_menu()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONUP:
                controller = get_callable(pygame.mouse.get_pos())
                if controller is not None:
                    return controller
