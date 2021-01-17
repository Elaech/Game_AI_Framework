import copy
import math
from game_logic import game_logic
import random

settings = None
score_heuristic = None
win_heuristic = None


def init_ai_logic(options, score_method, winning_method):
    global settings
    global score_heuristic
    global win_heuristic
    settings = options
    score_heuristic = score_method
    win_heuristic = winning_method


def get_next_move():
    return AI_minmax(game_logic.board)


def AI_minmax(board):
    initial_line = 0
    initial_column = 0
    after_line = 0
    after_column = 0
    max_value = -math.inf

    shuffled_settings = copy.deepcopy(settings["simple_moves"])

    for i in range(0, settings["board_height"]):
        for j in range(0, settings["board_width"]):
            if board[i][j] == game_logic.PosTypes.AI:
                random.shuffle(shuffled_settings)
                for move in shuffled_settings:
                    if game_logic.legal_move(i, j, i - move[0], j - move[1], game_logic.PosTypes.AI):
                        gained_value = minmax(board, 2, True)
                        if gained_value >= max_value:
                            print(gained_value, " ", max_value)
                            max_value = gained_value
                            initial_line = i
                            initial_column = j
                            after_line = i - move[0]
                            after_column = j - move[1]

    return initial_line, initial_column, after_line, after_column


def minmax(board, depth, maximizing_player):
    if depth == 0:
        return score_heuristic(settings["board_height"], settings["board_width"], game_logic.board, game_logic.PosTypes)

    win_state = win_heuristic(settings["board_height"], settings["board_width"], game_logic.board, settings["number_of_pieces"],
                              game_logic.PosTypes)

    if win_state is True:
        return -math.inf
    elif win_state is False:
        return math.inf
    elif win_state is None:
        pass

    if maximizing_player:
        max_eval = -math.inf
        for i in range(0, settings["board_height"]):
            for j in range(0, settings["board_width"]):
                if board[i][j] == game_logic.PosTypes.AI:
                    for move in settings["simple_moves"]:
                        if game_logic.legal_move(i, j, i - move[0], j - move[1], game_logic.PosTypes.AI):
                            game_logic.make_move_AI(i, j, i - move[0], j - move[1])
                            eval = minmax(board, depth - 1, False)
                            game_logic.make_move_AI(i - move[0], j - move[1], i, j)
                            max_eval = max(max_eval, eval)

        return max_eval

    else:
        min_eval = math.inf
        for i in range(0, settings["board_height"]):
            for j in range(0, settings["board_width"]):
                if board[i][j] == game_logic.PosTypes.HUMAN:
                    for move in settings["simple_moves"]:
                        if game_logic.legal_move(i, j, i + move[0], j + move[1], game_logic.PosTypes.HUMAN):
                            game_logic.make_move_AI(i, j, i + move[0], j + move[1])
                            eval = minmax(board, depth - 1, True)
                            game_logic.make_move_AI(i + move[0], j + move[1], i, j)
                            min_eval = min(min_eval, eval)
        return min_eval
