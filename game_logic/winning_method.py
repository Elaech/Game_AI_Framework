def winning_method(height, width, board, number_of_pieces, enum):
    # True - HUMAN wins
    # False - AI wins
    # None - Nobody won
    piece_count = 0
    for i in range(width):
        if board[0][i] == enum.HUMAN:
            piece_count += 1
    if number_of_pieces == piece_count:
        return True
    piece_count = 0
    for i in range(width):
        if board[height - 1][i] == enum.AI:
            piece_count += 1
    if number_of_pieces == piece_count:
        return False
    return None
