from generate_board import *

def bot_move(board, piece):
    valid_locations = [col for col in range(COLUMN_COUNT) if is_valid_location(board, col)]
    col = random.choice(valid_locations)
    row = get_next_open_row(board, col)
    drop_piece(board, row, col, piece)