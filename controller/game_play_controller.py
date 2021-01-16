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
    play_game_graphics.init_game_graphics()
    play_game_graphics.draw_play_board()
    for piece in ai_pieces:
        play_game_graphics.draw_player_piece(piece[0], piece[1], False)
    for piece in human_pieces:
        play_game_graphics.draw_player_piece(piece[0], piece[1], True)
    for position in settings["board_blocks"]:
        play_game_graphics.color_blocked_cell(position[0], position[1])
    current_turn = game_logic.get_current_turn()
    playing_game = True
    while playing_game:
        if game_logic.somebody_won() is not None:
            if game_logic.somebody_won() is True:
                HUMAN_won("HUMAN acomplished the objective")
            else:
                AI_won("AI acomplished the objective")
        if not game_logic.there_are_possible_moves(current_turn):
            if not game_logic.there_are_possible_moves(game_logic.get_other_turn()):
                if game_logic.is_AI_turn():
                    HUMAN_won("AI player has no moves")
                else:
                    AI_won("Human player has no moves")
                playing_game = False
                continue
            else:
                game_logic.change_turn()
        if game_logic.is_AI_turn():
            AI_turn()
        else:
            player_exits = HUMAN_turn()
            if player_exits:
                break
        current_turn = game_logic.get_current_turn()
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


def AI_turn():
    pass


def HUMAN_turn():
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONUP:
                return False


def AI_won(message):
    pass


def HUMAN_won(message):
    pass
