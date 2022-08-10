from IPython.display import clear_output
import random

def display_board(board): # prints out IU of game by receiving a list and using the index to display game
    clear_output()
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

def player_input(): # asks player 1 if they want to be x or o, then stores in tuple to use later on
    player1 = ''
    while player1 != 'X' and player1 != 'O':
        player1 = input('Player 1, choose X or O: ').upper()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)

def place_marker(board, marker, position): # example: place_marker(mainBoard, player1, 9); tells the game where and what marker to place
    board[position] = marker

def win_check(board, mark): # checks all conditions for a win
    return (board[7] == mark and board[8] == mark and board[9] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[1] == mark and board[2] == mark and board[3] == mark) or (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8] == mark) or (board[3] == mark and board[6] == mark and board[9] == mark) or (board[1] == mark and board[5] == mark and board[9] == mark) or (board[3] == mark and board[5] == mark and board[7] == mark)

def choose_first(): # using the random module, determine who goes first
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position): # determines if space on board is occupied, will return True if it is empty
    return board[position] == ' '

def full_board_check(board): # determines if all spaces on board are occupied (and no win condition), will return True if board is full
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board): # have the player choose a position to place their marker
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position, 1-9: '))
    return position

def replay(): # asks to play again
    return input('Do you want to play again, yes or no? ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    mainBoard = [' '] * 10
    player1, player2 = player_input()
    turn = choose_first()
    print(f'{turn} will go first')
    #pass
    play = input('Are you ready to play the game, yes or no? ').lower()
    if play[0] == 'y':
        game = True
    else:
        game = False

    while game:
        if turn == 'Player 1':
        #Player 1 Turn
            display_board(mainBoard)
            position = player_choice(mainBoard)
            place_marker(mainBoard, player1, position)

            if win_check(mainBoard, player1):
                display_board(mainBoard)
                print(f'Congratulations! {turn} have won Tic Tac Toe c:')
                game = False
            else:
                if full_board_check(mainBoard):
                    display_board(mainBoard)
                    print('The game is a draw :c')
                    break
                else:
                    turn = 'Player 2'
        
        else:
        # Player2's turn.
            display_board(mainBoard)
            position = player_choice(mainBoard)
            place_marker(mainBoard, player2, position)

            if win_check(mainBoard, player2):
                display_board(mainBoard)
                print(f'Congratulations! {turn} have won Tic Tac Toe c:')
                game = False
            else:
                if full_board_check(mainBoard):
                    display_board(mainBoard)
                    print('The game is a draw :c')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break