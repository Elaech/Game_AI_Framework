from controller import main_controller
from game_logic import main_logic
from game_logic import game_logic
import pygame
from game_graphics import play_game_graphics


def start(settings):
    settings = calibrate_piece_settings(settings)
    game_logic.init_game_logic(settings)
    ai_pieces = game_logic.get_ai_pieces()
    human_pieces = game_logic.get_human_pieces()
    settings = calibrate_block_settings(settings, human_pieces, ai_pieces)
    game_logic.update_settings(settings)
    game_logic.init_blocked_positions()
    main_controller.update_settings(settings)
    if main_logic.check_winning_method() is False or \
            main_logic.check_score_method() is False:
        return main_controller.call_main_menu()
    clock = pygame.time.Clock()
    play_game_graphics.init_game_graphics()
    play_game_graphics.draw_play_board()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return main_controller.call_main_menu()
            elif event.type == pygame.MOUSEBUTTONUP:
                return main_controller.call_main_menu()


def calibrate_block_settings(settings, human_piece_position, ai_piece_position):
    updated_blocks = []
    for el in settings["board_blocks"]:
        if el not in human_piece_position and el not in ai_piece_position:
            updated_blocks.append(el)
    settings["board_blocks"] = updated_blocks
    return settings


def calibrate_piece_settings(settings):
    if settings["number_of_pieces"] > settings["board_width"]:
        settings["number_of_pieces"] = settings["board_width"]
    return settings
