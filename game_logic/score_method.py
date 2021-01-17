def score_method(height, width, board, enum):
    # Returns an int or float
    # Represents the value of a state for the AI
    human_score = 0
    AI_score = 0
    for i in range(height):
        for j in range(width):
            if board[i][j] == enum.HUMAN:
                human_score += (height - i)
            elif board[i][j] == enum.AI:
                AI_score += (i + 1)

    #print(AI_score ," ", human_score)


    return AI_score - human_score
