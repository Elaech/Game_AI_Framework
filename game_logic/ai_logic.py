
import math
from game_logic import game_logic

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
                if board[i][j] == game_logic.PosTypes.AI:
                    for move in settings["simple_moves"]:
                        if game_logic.legal_move(i, j, i - move[0], j - move[1]):
                            game_logic.make_move(i, j, i - move[0], j - move[1])
                            eval = minmax(board, depth - 1, False, score_heuristic, win_heuristic)
                            game_logic.make_move(i - move[0], j - move[1], i, j)
                            max_eval = max(max_eval, eval)

        return max_eval

    else:
        min_eval = math.inf
        for i in range(0, settings["board_height"]):
            for j in range(0, settings["board_width"]):
                if board[i][j] == game_logic.PosTypes.HUMAN:
                    for move in settings["simple_moves"]:
                        if game_logic.legal_move(i, j, i + move[0], j + move[1]):
                            game_logic.make_move(i, j, i + move[0], j + move[1])
                            eval = minmax(board, depth - 1, True, score_heuristic, win_heuristic)
                            game_logic.make_move(i + move[0], j + move[1], i, j)
                            min_eval = min(min_eval, eval)
        return min_eval
