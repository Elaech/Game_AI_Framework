def winning_method():
    # True - HUMAN wins
    # False - AI wins
    # None - Nobody won
    height = settings["board_height"]
    width = settings["board_width"]
    number_of_pieces = settings["number_of_pieces"]
    piece_count = 0
    for i in range(width):
        if board[0][i] == 2:
            piece_count += 1
    if number_of_pieces == piece_count:
        return True
    piece_count = 0
    for i in range(width):
        if board[height - 1][i] == 1:
            piece_count += 1
    if number_of_pieces == piece_count:
        return False
    return True

