import pygame
from game_graphics import main_graphics as mg

"""
Made by Pristavu Dumitru-Dragos
"""


def is_back_button_pressed(mouse):
    x = mouse[0]
    y = mouse[1]
    width_proportion = mg.width / 20
    height_proportion = mg.height / 20
    if width_proportion * 17 < x < width_proportion * 19 and height_proportion * 17 < y < height_proportion * 19:
        return True
    else:
        return False


def is_board_width_button_pressed(mouse):
    x = mouse[0]
    y = mouse[1]
    width_proportion = mg.width / 20
    height_proportion = mg.height / 20
    if width_proportion * 2 < x < width_proportion * 6 and height_proportion * 3 < y < height_proportion * 5:
        return True
    else:
        return False


def is_board_height_button_pressed(mouse):
    x = mouse[0]
    y = mouse[1]
    width_proportion = mg.width / 20
    height_proportion = mg.height / 20
    if width_proportion * 2 < x < width_proportion * 6 and height_proportion * 6 < y < height_proportion * 8:
        return True
    else:
        return False


def is_alfa_beta_button_pressed(mouse):
    x = mouse[0]
    y = mouse[1]
    width_proportion = mg.width / 20
    height_proportion = mg.height / 20
    if width_proportion * 2 < x < width_proportion * 6 and height_proportion * 9 < y < height_proportion * 11:
        return True
    else:
        return False


def is_moves_per_turn_button_pressed(mouse):
    x = mouse[0]
    y = mouse[1]
    width_proportion = mg.width / 20
    height_proportion = mg.height / 20
    if width_proportion * 2 < x < width_proportion * 6 and height_proportion * 12 < y < height_proportion * 14:
        return True
    else:
        return False


def is_number_of_pieces_button_pressed(mouse):
    x = mouse[0]
    y = mouse[1]
    width_proportion = mg.width / 20
    height_proportion = mg.height / 20
    if width_proportion * 2 < x < width_proportion * 6 and height_proportion * 15 < y < height_proportion * 17:
        return True
    else:
        return False


def is_define_moves_button_pressed(mouse):
    x = mouse[0]
    y = mouse[1]
    width_proportion = mg.width / 20
    height_proportion = mg.height / 20
    if width_proportion * 12 < x < width_proportion * 18 and height_proportion * 3 < y < height_proportion * 5:
        return True
    else:
        return False


def is_define_score_button_pressed(mouse):
    x = mouse[0]
    y = mouse[1]
    width_proportion = mg.width / 20
    height_proportion = mg.height / 20
    if width_proportion * 12 < x < width_proportion * 18 and height_proportion * 6 < y < height_proportion * 8:
        return True
    else:
        return False


def is_define_board_button_pressed(mouse):
    x = mouse[0]
    y = mouse[1]
    width_proportion = mg.width / 20
    height_proportion = mg.height / 20
    if width_proportion * 12 < x < width_proportion * 18 and height_proportion * 9 < y < height_proportion * 11:
        return True
    else:
        return False


def is_define_win_condition_button_pressed(mouse):
    x = mouse[0]
    y = mouse[1]
    width_proportion = mg.width / 20
    height_proportion = mg.height / 20
    if width_proportion * 12 < x < width_proportion * 18 and height_proportion * 12 < y < height_proportion * 14:
        return True
    else:
        return False


def get_board_click(mouse):
    x = mouse[0]
    y = mouse[1]
    found_x = -1
    found_y = -1
    cell_dim = min(mg.height / mg.settings["board_height"], (mg.width * 17 / 20) / mg.settings["board_width"])
    for i in range(0, mg.settings["board_width"]):
        if i * cell_dim <= x < (i + 1) * cell_dim:
            found_x = i
            break
    for i in range(0, mg.settings["board_height"]):
        if i * cell_dim <= y < (i + 1) * cell_dim:
            found_y = i
            break
    return found_x, found_y


def color_select_space(x, y, color_type):
    cell_dim = min(mg.height / mg.settings["board_height"], (mg.width * 17 / 20) / mg.settings["board_width"])
    if color_type:
        mg.window.fill(mg.color_scheme["board_cell_selection_color"],
                       (x * cell_dim + 5, y * cell_dim + 5, cell_dim - 10, cell_dim - 10))
    else:
        mg.window.fill(mg.color_scheme["background_color"],
                       (x * cell_dim + 5, y * cell_dim + 5, cell_dim - 10, cell_dim - 10))
    pygame.display.update()


def draw_player_piece(x, y, piece_type):
    cell_dim = min(mg.height / mg.settings["board_height"], (mg.width * 17 / 20) / mg.settings["board_width"])
    if piece_type:
        pygame.draw.circle(mg.window, mg.color_scheme["human_player_piece_color"],
                           ((x+0.5)*cell_dim, (y+0.5)*cell_dim), cell_dim / 3)
    else:
        pygame.draw.circle(mg.window, mg.color_scheme["human_player_piece_color"],
                           ((x + 0.5) * cell_dim, (y + 0.5) * cell_dim), cell_dim / 3)
    pygame.display.update()


def delete_piece(x, y):
    cell_dim = min(mg.height / mg.settings["board_height"], (mg.width * 17 / 20) / mg.settings["board_width"])
    pygame.draw.circle(mg.window, mg.color_scheme["background_color"],
                       ((x + 0.5) * cell_dim, (y + 0.5) * cell_dim), cell_dim / 3)


def draw_move_board():
    mg.window.fill(mg.color_scheme["background_color"])
    board_pixel_width = mg.width * 17 / 20
    board_pixel_height = mg.height
    board_columns = mg.settings["board_width"]
    board_rows = mg.settings["board_height"]
    cell_dim = min(board_pixel_height/board_rows, board_pixel_width/board_columns)
    for i in range(1, board_columns):
        pygame.draw.line(mg.window, mg.color_scheme["text_color"],
                         (cell_dim * i, 1),
                         (cell_dim * i, cell_dim * board_rows), 3)
    for i in range(1, board_rows):
        pygame.draw.line(mg.window, mg.color_scheme["text_color"],
                         (1, cell_dim * i),
                         (cell_dim * board_columns, cell_dim * i), 3)
    pygame.draw.line(mg.window, mg.color_scheme["text_color"],
                     (1, 1), (1, cell_dim * board_rows), 3)
    pygame.draw.line(mg.window, mg.color_scheme["text_color"],
                     (1, 1), (cell_dim * board_columns, 1), 3)
    pygame.draw.line(mg.window, mg.color_scheme["text_color"],
                     (1, cell_dim * board_rows), (cell_dim * board_columns, cell_dim * board_rows), 3)
    pygame.draw.line(mg.window, mg.color_scheme["text_color"],
                     (cell_dim * board_columns, 1), (cell_dim * board_columns, cell_dim * board_rows), 3)
    mg.draw_button(mg.width * 17 / 20, mg.height * 17 / 20,
                   mg.width * 2 / 20, mg.height * 2 / 20, "Back")
    pygame.display.update()


def draw_settings_menu():
    mg.window.fill(mg.color_scheme["background_color"])
    width_proportion = mg.width / 20
    height_proportion = mg.height / 20
    mg.draw_button(width_proportion * 17, height_proportion * 17,
                   width_proportion * 2, height_proportion * 2, "Back")
    mg.draw_button(width_proportion * 2, height_proportion * 3,
                   width_proportion * 4, height_proportion * 2, "Board width: " + str(mg.settings["board_width"]))
    mg.draw_button(width_proportion * 2, height_proportion * 6,
                   width_proportion * 4, height_proportion * 2, "Board height: " + str(mg.settings["board_height"]))
    mg.draw_button(width_proportion * 2, height_proportion * 9,
                   width_proportion * 4, height_proportion * 2, "Alfa-beta: " + str(mg.settings["alfa-beta"]))
    mg.draw_button(width_proportion * 2, height_proportion * 12,
                   width_proportion * 4, height_proportion * 2,
                   "Moves per turn : " + str(mg.settings["moves_per_turn"]))
    mg.draw_button(width_proportion * 2, height_proportion * 15,
                   width_proportion * 4, height_proportion * 2, "No. of pieces: " + str(mg.settings["number_of_pieces"]))
    mg.draw_button(width_proportion * 12, height_proportion * 3,
                   width_proportion * 6, height_proportion * 2, "Define Moves")
    mg.draw_button(width_proportion * 12, height_proportion * 6,
                   width_proportion * 6, height_proportion * 2, "Define Score Function")
    mg.draw_button(width_proportion * 12, height_proportion * 9,
                   width_proportion * 6, height_proportion * 2, "Define Board")
    mg.draw_button(width_proportion * 12, height_proportion * 12,
                   width_proportion * 6, height_proportion * 2, "Define Win Condition")
    pygame.display.update()
