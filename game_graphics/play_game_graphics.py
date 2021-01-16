import pygame
import pygame.freetype
from game_graphics import main_graphics as mg

cell_dim = None
board_width = None
board_height = None
board_pixel_width = None
board_pixel_height = None


def init_game_graphics():
    global board_height
    global board_width
    global board_pixel_height
    global board_pixel_width
    global cell_dim
    board_width = mg.settings["board_width"]
    board_height = mg.settings["board_height"]
    board_pixel_width = mg.settings["screen_width"] * 17 / 20
    board_pixel_height = mg.settings["screen_height"]
    cell_dim = min(board_pixel_height / board_height, board_pixel_width / board_width)


def is_back_button_pressed(mouse):
    x = mouse[0]
    y = mouse[1]
    width_proportion = mg.width / 20
    height_proportion = mg.height / 20
    if width_proportion * 17 < x < width_proportion * 19 and height_proportion * 17 < y < height_proportion * 19:
        return True
    else:
        return False


def game_finish_prompt(human_won, text):
    winner = ""
    if human_won:
        winner = "Human"
    else:
        winner = "AI"
    font = pygame.freetype.SysFont("Arial", 14)
    mg.draw_button(board_pixel_width * 4 / 10, board_pixel_height * 3 / 10,
                   board_pixel_width * 2 / 10, board_pixel_height / 10, winner + " Won!")
    mg.draw_custom_font_button(board_pixel_width * 1 / 10, board_pixel_height * 4 / 10,
                   board_pixel_width * 8 / 10, board_pixel_height / 10, text, font, 14)
    pygame.display.update()


def get_board_click(mouse):
    x = mouse[0]
    y = mouse[1]
    found_x = -1
    found_y = -1
    for i in range(0, board_width):
        if i * cell_dim <= x < (i + 1) * cell_dim:
            found_x = i
            break
    for i in range(0, board_height):
        if i * cell_dim <= y < (i + 1) * cell_dim:
            found_y = i
            break
    return found_x, found_y


def draw_player_piece(x, y, piece_type):
    if piece_type:
        pygame.draw.circle(mg.window, mg.color_scheme["human_player_piece_color"],
                           ((x + 0.5) * cell_dim, (y + 0.5) * cell_dim), cell_dim / 3)
    else:
        pygame.draw.circle(mg.window, mg.color_scheme["AI_piece_color"],
                           ((x + 0.5) * cell_dim, (y + 0.5) * cell_dim), cell_dim / 3)
    pygame.display.update()


def clear_cell(x, y):
    mg.window.fill(mg.color_scheme["background_color"],
                   (x * cell_dim + 5, y * cell_dim + 5, cell_dim - 10, cell_dim - 10))
    pygame.display.update()


def draw_selected_piece(x, y):
    pygame.draw.circle(mg.window, mg.color_scheme["human_player_piece_color"],
                       ((x + 0.5) * cell_dim, (y + 0.5) * cell_dim), cell_dim / 3)
    pygame.draw.circle(mg.window, mg.color_scheme["AI_piece_color"],
                       ((x + 0.5) * cell_dim, (y + 0.5) * cell_dim), cell_dim / 5)
    pygame.display.update()


def color_blocked_cell(x, y):
    mg.window.fill(mg.color_scheme["board_cell_selection_color"],
                   (x * cell_dim + 5, y * cell_dim + 5, cell_dim - 10, cell_dim - 10))
    pygame.display.update()


def color_hover_cell(x, y):
    mg.window.fill(mg.color_scheme["board_hover_color"],
                   (x * cell_dim + 5, y * cell_dim + 5, cell_dim - 10, cell_dim - 10))
    pygame.display.update()


def draw_play_board():
    mg.window.fill(mg.color_scheme["background_color"])
    board_columns = board_width
    board_rows = board_height
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

