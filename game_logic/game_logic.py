from game_logic import main_logic
from enum import Enum
import copy


class PosTypes(Enum):
    EMPTY = 0,
    AI = 1,
    HUMAN = 2,
    BLOCKED = -1


settings = None
board = None


def update_settings(options):
    global settings
    settings = options


def init_game_logic(options):
    global settings
    settings = options
    init_board()
    pass


def init_board():
    global board
    board = []
    nr_pieces = settings["number_of_pieces"]
    board_width = settings["board_width"]
    start_pos = (board_width - nr_pieces) // 2
    empty_line = [PosTypes.EMPTY for index in range(board_width)]
    ai_line = copy.deepcopy(empty_line)
    for index in range(start_pos, start_pos + nr_pieces):
        ai_line[index] = PosTypes.AI
    human_line = copy.deepcopy(empty_line)
    for index in range(start_pos, start_pos + nr_pieces):
        human_line[index] = PosTypes.HUMAN
    board.append(ai_line)
    for index in range(board_width - 2):
        board.append(copy.deepcopy(empty_line))
    board.append(human_line)


def init_blocked_positions():
    global board
    positions = settings["board_blocks"]
    for pos in positions:
        board[pos[1]][pos[0]] = PosTypes.BLOCKED
    print_board_to_console()


def get_ai_pieces():
    ai_positions = []
    for index_i in range(len(board)):
        for index_j in range(len(board[0])):
            if board[index_i][index_j] == PosTypes.AI:
                ai_positions.append([index_j, index_i])
    return ai_positions


def get_human_pieces():
    human_positions = []
    for index_i in range(len(board)):
        for index_j in range(len(board[0])):
            if board[index_i][index_j] == PosTypes.HUMAN:
                human_positions.append([index_j, index_i])
    return human_positions


def print_board_to_console():
    for line in board:
        print(line)
