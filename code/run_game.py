from generate_board import *
from players.random_bot import *

board = generate_board_size(10,10)
game_over = False
turn = 0

while not game_over:
    # Bot 1 move
    if turn == 0:
        bot_move(board, 1)
        if winning_move(board, 1):
            print("Bot 1 wins!")
            game_over = True

    # Bot 2 move
    else:
        bot_move(board, 2)
        if winning_move(board, 2):
            print("Bot 2 wins!")
            game_over = True

    print_board(board)
    turn += 1
    turn = turn % 2