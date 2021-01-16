import pygame
from game_graphics import main_graphics as mg

pad = None
cell_dim = None
height_offset = None
width_offset = None
board_width = None
board_height = None
board_pixel_width = None
board_pixel_height = None


def init_game_graphics():
    global pad
    global cell_dim
    global height_offset
    global width_offset
    global board_height
    global board_width
    global board_pixel_height
    global board_pixel_width
    board_width = mg.settings["board_width"]
    board_height = mg.settings["board_height"]
    board_pixel_width = mg.settings["screen_width"] * 17 / 20
    board_pixel_height = mg.settings["screen_height"]


def is_back_button_pressed(mouse):
    x = mouse[0]
    y = mouse[1]
    width_proportion = mg.width / 20
    height_proportion = mg.height / 20
    if width_proportion * 17 < x < width_proportion * 19 and height_proportion * 17 < y < height_proportion * 19:
        return True
    else:
        return False


def draw_play_board():
    global board_pixel_height
    global board_pixel_width
    global cell_dim
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