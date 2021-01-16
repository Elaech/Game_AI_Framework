import numpy
import copy
from controller import main_controller
from game_graphics import settings_menu_graphics
import pygame
import tkinter
from game_logic import main_logic
from tkinter import Text
import tkinter.font as Font

"""
Global Variables
"""
root = None
text_entry = None
input_text = None


def clicked_on_back(mouse):
    return settings_menu_graphics.is_back_button_pressed(mouse)


def clicked_on_board_width(mouse):
    return settings_menu_graphics.is_board_width_button_pressed(mouse)


def clicked_on_board_height(mouse):
    return settings_menu_graphics.is_board_height_button_pressed(mouse)


def clicked_on_alfabeta(mouse):
    return settings_menu_graphics.is_alfa_beta_button_pressed(mouse)


def clicked_on_simple_moves(mouse):
    return settings_menu_graphics.is_define_moves_button_pressed(mouse)


def clicked_on_score_method(mouse):
    return settings_menu_graphics.is_define_score_button_pressed(mouse)


def clicked_on_define_board(mouse):
    return settings_menu_graphics.is_define_board_button_pressed(mouse)


def clicked_on_define_winning(mouse):
    return settings_menu_graphics.is_define_win_condition_button_pressed(mouse)


def clicked_on_moves_per_turn(mouse):
    return settings_menu_graphics.is_moves_per_turn_button_pressed(mouse)


def clicked_on_nr_of_pieces(mouse):
    return settings_menu_graphics.is_number_of_pieces_button_pressed(mouse)


def get_callable(mouse):
    if clicked_on_back(mouse):
        return -1
    elif clicked_on_define_winning(mouse):
        return modify_winning_condition
    elif clicked_on_define_board(mouse):
        return modify_board
    elif clicked_on_score_method(mouse):
        return modify_score_method
    elif clicked_on_simple_moves(mouse):
        return modify_simple_moves
    elif clicked_on_alfabeta(mouse):
        return modify_alfabeta
    elif clicked_on_board_height(mouse):
        return modify_board_height
    elif clicked_on_board_width(mouse):
        return modify_board_width
    elif clicked_on_moves_per_turn(mouse):
        return modify_moves_per_turn
    elif clicked_on_nr_of_pieces(mouse):
        return modify_nr_of_pieces
    return None


def modify_board(settings):
    clock = pygame.time.Clock()
    settings_menu_graphics.draw_move_board()
    board_blocks = settings["board_blocks"]
    board = numpy.full((settings["board_width"], settings["board_height"]), False, dtype=bool)
    for el in board_blocks:
        if el[0] < settings["board_width"] and el[1] < settings["board_height"]:
            settings_menu_graphics.color_select_space(el[0], el[1], True)
            board[el[0]][el[1]] = True
    local_quit = False
    while not local_quit:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                local_quit = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if settings_menu_graphics.is_back_button_pressed(pygame.mouse.get_pos()):
                    updated_blocked = []
                    for index_i in range(len(board)):
                        for index_j in range(len(board[0])):
                            if board[index_i][index_j]:
                                updated_blocked.append([index_i, index_j])
                    settings["board_blocks"] = updated_blocked
                    local_quit = True
                x, y = settings_menu_graphics.get_board_click(pygame.mouse.get_pos())
                if x != -1 and y != -1:
                    board[x][y] = (not board[x][y])
                    settings_menu_graphics.color_select_space(x, y, board[x][y])
    return settings


def normalize_possible_moves(center_point, move_spaces):
    normalized_moves = []
    for point in move_spaces:
        normalized_x = point[0] - center_point[0]
        normalized_y = point[1] - center_point[1]
        normalized_moves.append([normalized_x, normalized_y])
    return normalized_moves


def modify_simple_moves(settings):
    clock = pygame.time.Clock()
    saved_width = copy.copy(settings["board_width"])
    saved_height = copy.copy(settings["board_height"])
    local_width = int(settings["board_width"] * 2.0) - 1
    local_height = int(settings["board_height"] * 2.0) - 1
    settings["board_width"] = local_width
    settings["board_height"] = local_height
    main_controller.update_settings(settings)
    settings_menu_graphics.draw_move_board()
    board = numpy.full((local_width, local_height), False, dtype=bool)

    for el in settings["simple_moves"]:
        if 0 <= el[1] + (local_width // 2) < local_width \
                and 0 <= el[0] + (local_height // 2) < local_height:
            settings_menu_graphics.color_select_space(el[1] + local_width // 2, el[0] + local_height // 2, True)
            board[el[1] + local_width // 2][el[0] + local_height // 2] = True
    settings_menu_graphics.draw_player_piece(local_width // 2, local_height // 2, True)
    local_quit = False
    while not local_quit:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                local_quit = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if settings_menu_graphics.is_back_button_pressed(pygame.mouse.get_pos()):
                    updated_simple_moves = []
                    for index_i in range(len(board)):
                        for index_j in range(len(board[0])):
                            if board[index_i][index_j]:
                                updated_simple_moves.append([index_j, index_i])
                    settings["simple_moves"] = normalize_possible_moves([local_width // 2, local_height // 2],
                                                                        updated_simple_moves)
                    local_quit = True
                x, y = settings_menu_graphics.get_board_click(pygame.mouse.get_pos())
                if x != -1 and y != -1:
                    board[x][y] = (not board[x][y])
                    settings_menu_graphics.color_select_space(x, y, board[x][y])
                    if x == local_width // 2 and y == local_height // 2:
                        settings_menu_graphics.draw_player_piece(local_width // 2, local_height // 2, True)
    pygame.quit()
    settings["board_width"] = saved_width
    settings["board_height"] = saved_height
    main_controller.update_settings(settings)
    return settings


def modify_winning_condition(settings):
    pygame.quit()
    with open("../game_logic/winning_method.py", "r") as win_method_file:
        method = win_method_file.read()
    code_text_interface("Change Winning Method", method)
    if main_logic.check_winning_method(input_text):
        with open("../game_logic/winning_method.py", "w") as win_method_file:
            win_method_file.write(input_text)
    return settings


def modify_score_method(settings):
    pygame.quit()
    with open("../game_logic/score_method.py", "r") as score_method_file:
        method = score_method_file.read()
    code_text_interface("Change Score Method", method)
    if main_logic.check_score_method(input_text):
        with open("../game_logic/score_method.py", "w") as score_method_file:
            score_method_file.write(input_text)
    return settings


def modify_nr_of_pieces(settings):
    pygame.quit()
    number_text_interface("Change Number of Pieces")
    try:
        number = int(input_text)
        if settings["board_width"] < number or number < 1:
            return settings
        settings["number_of_pieces"] = number
    except Exception:
        pass
    return settings


def modify_moves_per_turn(settings):
    pygame.quit()
    number_text_interface("Change Moves per Turn")
    try:
        number = int(input_text)
        if number < 1:
            return settings
        settings["moves_per_turn"] = number
    except Exception:
        pass
    return settings


def modify_board_width(settings):
    pygame.quit()
    number_text_interface("Change Board Width")
    try:
        number = int(input_text)
        if number < 4:
            return settings
        settings["board_width"] = number
    except Exception:
        pass
    return settings


def modify_board_height(settings):
    pygame.quit()
    number_text_interface("Change Board Height")
    try:
        number = int(input_text)
        if number < 4:
            return settings
        settings["board_height"] = number
    except Exception:
        pass
    return settings


def modify_alfabeta(settings):
    if settings["alfa-beta"] == True:
        settings["alfa-beta"] = False
    else:
        settings["alfa-beta"] = True
    pygame.quit()
    return settings


def local_controller_manager(settings):
    local_controller = settings_loop(settings)
    while local_controller != -1:
        settings = local_controller(settings)
        main_controller.update_settings(settings)
        main_controller.init_application_window()
        local_controller = settings_loop(settings)
    return main_controller.call_main_menu()


def settings_loop(settings):
    global input_text
    clock = pygame.time.Clock()
    settings_menu_graphics.draw_settings_menu()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONUP:
                controller = get_callable(pygame.mouse.get_pos())
                if controller is not None:
                    return controller


def start(settings):
    return local_controller_manager(settings)


def code_text_interface(title, method_code):
    global root
    global text_entry

    def _callback():
        global input_text
        input_text = text_entry.get("1.0", tkinter.END)
        root.destroy()

    global root
    global text_entry
    root = tkinter.Tk()
    root.title(title)

    button_font = Font.Font(size=16)
    text_font = Font.Font(size=10)
    canvas = tkinter.Canvas(root)
    canvas.pack()

    text_entry = tkinter.Text(canvas, height=30, width=100)
    text_entry["font"] = text_font
    text_entry.insert(tkinter.INSERT, chars=method_code)
    text_entry.pack()
    submit_button = tkinter.Button(canvas, text="Submit", command=_callback)
    submit_button["font"] = button_font
    submit_button.pack()
    canvas.pack()
    root.mainloop()


def number_text_interface(title):
    global root
    global text_entry

    def _callback():
        global input_text
        input_text = text_entry.get("1.0", tkinter.END)
        root.destroy()

    root = tkinter.Tk()
    root.title(title)

    button_font = Font.Font(size=12)
    text_font = Font.Font(size=20)

    canvas = tkinter.Canvas(root)
    canvas.pack()

    text_entry = tkinter.Text(canvas, height=1, width=2)
    text_entry["font"] = text_font
    text_entry.pack()
    submit_button = tkinter.Button(canvas, text="Submit", command=_callback, width=40)
    submit_button["font"] = button_font
    submit_button.pack()
    canvas.pack()
    root.mainloop()
