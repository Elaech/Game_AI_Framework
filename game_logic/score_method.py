def score_method():
    height = settings["board_height"]
    width = settings["board_width"]
    human_score = 0
    AI_score = 0
    for i in range(height):
        for j in range(width):
            if board[i][j] == 2:
                human_score += (height - i)
            elif board[i][j] == 1:
                AI_score += (i + 1)
    return AI_score - human_score
