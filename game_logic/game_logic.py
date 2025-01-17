from game_logic import main_logic
from enum import Enum
import copy
from game_logic import ai_logic


class PosTypes(Enum):
    EMPTY = 0,
    AI = 1,
    HUMAN = 2,
    BLOCKED = -1


settings = None
board = None
current_turn = None
turn_charge = None
max_turn_charge = None
winning_function = None
score_function = None


def update_settings(options):
    global settings
    settings = options


def init_game_logic(options):
    global turn_charge
    global max_turn_charge
    global settings
    global current_turn
    settings = options
    max_turn_charge = settings["moves_per_turn"]
    turn_charge = 0
    current_turn = PosTypes.HUMAN
    init_board()
    pass


def init_functions():
    global score_function
    global winning_function
    score_function = main_logic.score_function
    winning_function = main_logic.winning_function


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
    for index in range(settings["board_height"] - 2):
        board.append(copy.deepcopy(empty_line))
    board.append(human_line)


def init_blocked_positions():
    global board
    positions = settings["board_blocks"]
    for pos in positions:
        board[pos[1]][pos[0]] = PosTypes.BLOCKED


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


def get_board():
    return board


def print_board_to_console():
    for line in board:
        print(line)


def is_AI_turn():
    return current_turn == PosTypes.AI


def is_HUMAN_turn():
    return current_turn == PosTypes.HUMAN


def change_turn():
    global current_turn
    global turn_charge
    turn_charge = 0
    if is_AI_turn():
        current_turn = PosTypes.HUMAN
    else:
        current_turn = PosTypes.AI


def get_current_turn():
    return current_turn


def get_other_turn():
    if is_AI_turn():
        return PosTypes.HUMAN
    return PosTypes.AI


def charge_up_turn():
    global turn_charge
    turn_charge += 1
    if turn_charge == max_turn_charge:
        turn_charge = 0
        change_turn()


def somebody_won():
    return winning_function(settings["board_height"], settings["board_width"], board, settings["number_of_pieces"],
                            PosTypes)


def is_pos_within_bounds(line, column):
    if column >= settings["board_width"] or column < 0:
        return False
    if line >= settings["board_height"] or line < 0:
        return False
    return True


def legal_move(initial_line, initial_column, after_line, after_column, player_type):
    if player_type == PosTypes.HUMAN:
        if board[initial_line][initial_column] == PosTypes.HUMAN:
            if is_pos_within_bounds(after_line, after_column):
                if initial_line == after_line and initial_column == after_column:
                    for move in settings["simple_moves"]:
                        if move[0] == 0 and move[1] == 0:
                            return True

                if board[after_line][after_column] == PosTypes.EMPTY:
                    for move in settings["simple_moves"]:
                        if initial_line + move[0] == after_line:
                            if initial_column + move[1] == after_column:
                                return True

    if player_type == PosTypes.AI:
        if board[initial_line][initial_column] == PosTypes.AI:
            if is_pos_within_bounds(after_line, after_column):
                if initial_line == after_line and initial_column == after_column:
                    for move in settings["simple_moves"]:
                        if move[0] == 0 and move[1] == 0:
                            return True

                if board[after_line][after_column] == PosTypes.EMPTY:
                    for move in settings["simple_moves"]:
                        if initial_line - move[0] == after_line:
                            if initial_column - move[1] == after_column:
                                return True

    return False


def there_are_possible_moves(player_type):
    for i in range(0, settings["board_height"]):
        for j in range(0, settings["board_width"]):
            if board[i][j] == player_type:
                for move in settings["simple_moves"]:
                    t = 1
                    if player_type == PosTypes.AI:
                        t = -1
                    if legal_move(i, j, i + move[0] * t, j + move[1] * t, player_type):
                        return True
    print(player_type)
    return False


def make_move(initial_line, initial_column, after_line, after_column):
    if initial_line == after_line and initial_column == after_column:
        charge_up_turn()
    else:
        board[after_line][after_column] = board[initial_line][initial_column]
        board[initial_line][initial_column] = PosTypes.EMPTY
        charge_up_turn()


def make_move_AI(initial_line, initial_column, after_line, after_column):
    if initial_line == after_line and initial_column == after_column:
        pass
    else:
        board[after_line][after_column] = board[initial_line][initial_column]
        board[initial_line][initial_column] = PosTypes.EMPTY


def is_my_piece(player_type, line, column):
    if player_type == board[line][column]:
        return True

    return False


def is_occupied(line, column):
    if board[line][column] == PosTypes.EMPTY:
        return False
    return True
