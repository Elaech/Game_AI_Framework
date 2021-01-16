import main_logic
import game_logic
import math
from game_logic.game_logic import PosTypes, legal_move, make_move, there_are_possible_moves

settings = None


def init_ai_logic(options):
    global settings
    settings = options


def get_next_move():
    pass


def minmax(board, depth, maximizing_player, score_heuristic, win_heuristic):
    if depth == 0:
        return score_heuristic()

    win_state = win_heuristic()

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
                if board[i][j] == PosTypes.AI:
                    for move in settings["simple_moves"]:
                        if legal_move(i, j, i - move[0], j - move[1]):
                            make_move(i, j, i - move[0], j - move[1])
                            eval = minmax(board, depth - 1, False, score_heuristic, win_heuristic)
                            make_move(i - move[0], j - move[1], i, j)
                            max_eval = max(max_eval, eval)

        return max_eval

    else:
        min_eval = math.inf
        for i in range(0, settings["board_height"]):
            for j in range(0, settings["board_width"]):
                if board[i][j] == PosTypes.HUMAN:
                    for move in settings["simple_moves"]:
                        if legal_move(i, j, i + move[0], j + move[1]):
                            make_move(i, j, i + move[0], j + move[1])
                            eval = minmax(board, depth - 1, True, score_heuristic, win_heuristic)
                            make_move(i + move[0], j + move[1], i, j)
                            min_eval = min(min_eval, eval)
        return min_eval
