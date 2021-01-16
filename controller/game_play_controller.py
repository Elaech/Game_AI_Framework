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
        # if game_logic.somebody_won() is not None:
        #     if game_logic.somebody_won() is True:
        #         HUMAN_won("HUMAN acomplished the objective")
        #     else:
        #         AI_won("AI acomplished the objective")
        # if not game_logic.there_are_possible_moves(current_turn):
        #     if not game_logic.there_are_possible_moves(game_logic.get_other_turn()):
        #         if game_logic.is_AI_turn():
        #             HUMAN_won("AI player has no moves")
        #         else:
        #             AI_won("Human player has no moves")
        #         playing_game = False
        #         continue
        #     else:
        #         game_logic.change_turn()
        if game_logic.is_AI_turn():
            AI_turn()
        else:
            player_exits = HUMAN_turn(settings)
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


def draw_hover(line, column, changes):
    hovers = []
    for change in changes:
        if game_logic.is_pos_within_bounds(column + change[1], line + change[0]) and not game_logic.is_occupied(
                column + change[1], line + change[0]):
            play_game_graphics.color_hover_cell(line + change[0], column + change[1])
            hovers.append([line + change[0], column + change[1]])
        elif game_logic.is_pos_within_bounds(column + change[1], line + change[0]) and change[1] == 0 \
                and change[0] == 0:
            play_game_graphics.color_hover_cell(line, column)
            play_game_graphics.draw_player_piece(line, column, True)
            hovers.append([line, column])
    return hovers


def delete_hover(list_of_positions, selected_piece):
    for pos in list_of_positions:
        play_game_graphics.clear_cell(pos[0], pos[1])
        if pos[0] == selected_piece[0] and pos[1] == selected_piece[1]:
            play_game_graphics.draw_player_piece(pos[0], pos[1], True)


def HUMAN_turn(settings):
    clock = pygame.time.Clock()
    selected_piece = None
    last_hover = None
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.MOUSEBUTTONUP:
                if play_game_graphics.is_back_button_pressed(pygame.mouse.get_pos()):
                    return True
                line, column = play_game_graphics.get_board_click(pygame.mouse.get_pos())
                if line > -1 and column > -1:
                    if game_logic.is_my_piece(game_logic.PosTypes.HUMAN, column, line):
                        if selected_piece is None:
                            selected_piece = [line, column]
                            last_hover = draw_hover(line, column, settings["simple_moves"])
                        else:
                            delete_hover(last_hover, selected_piece)
                            selected_piece = [line, column]
                            last_hover = draw_hover(line, column, settings["simple_moves"])
                    elif game_logic.is_my_piece(game_logic.PosTypes.EMPTY, column, line) and selected_piece is not None:
                        if game_logic.legal_move(selected_piece[1], selected_piece[0], column, line):
                            game_logic.make_move(selected_piece[1], selected_piece[0], column, line)
                            play_game_graphics.clear_cell(selected_piece[0], selected_piece[1])
                            delete_hover(last_hover, selected_piece)
                            play_game_graphics.draw_player_piece(line, column, True)
                            return False


def AI_won(message):
    pass


def HUMAN_won(message):
    pass


def AI_turn():
    pass
