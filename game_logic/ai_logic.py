import math
from game_logic import game_logic


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
    print(AI_minmax(game_logic.board))
    initial_line, initial_column, after_line, after_column = AI_minmax(game_logic.board)
    game_logic.make_move(initial_column, initial_line, after_column, after_line)



def AI_minmax(board):
    initial_line = 0
    initial_column = 0
    after_line = 0
    after_column = 0

    for i in range(0, settings["board_height"]):
        for j in range(0, settings["board_width"]):
            if board[i][j] == game_logic.PosTypes.AI:
                for move in settings["simple_moves"]:
                    max_value = 0
                    if game_logic.legal_move(i, j, i - move[0], j - move[1]):
                        gained_value = minmax(board, 2, True, score_heuristic, win_heuristic)
                        if gained_value > max_value:
                            max_value = gained_value
                            initial_line = i
                            initial_column = j
                            after_line = i - move[0]
                            after_column = j - move[1]

    return initial_line, initial_column, after_line, after_column


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
