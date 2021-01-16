from controller import main_controller
from game_logic import main_logic
import pygame

def start(settings):
    settings = calibrate_settings(settings)
    main_controller.update_settings(settings)
    if main_logic.check_winning_method() is False or \
            main_logic.check_score_method() is False:
        print("wrong")
        return main_controller.call_main_menu()
    clock = pygame.time.Clock()
    # draw playgame
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONUP:
                controller = get_callable(pygame.mouse.get_pos())
                if controller is not None:
                    return controller


def calibrate_settings(settings):
    # adjust piece number to the board
    if settings["number_of_pieces"] > settings["board_width"]:
        settings["number_of_pieces"] = settings["board_width"]
        # remove blocks that are on initial pieces, pieces can be on

    return settings


def init_board(settings):
    pass
