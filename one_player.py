import common_functions
import random

# Global variables
board = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}

def get_user_name():
    """
    Get the name of the player
    """
    player = ''

    while len(player) < 3 or not player.isalpha() or len(player) > 10:
        player = input('\nWhat is your name? ').capitalize()

        if player.isalpha() == False:
            print('Name can only contain letters, please try again')
            
        elif len(player) < 3:
            print('Name must be a minimum of 3 letters, please try again')
            
        elif len(player) > 10:
            print('Name can only be a maximum of 10 letters, please try again')
            

    print(f'\nHi {player}!')
    return player

def get_user_marker():
    """
    Get user marker
    """
    choice = ''

    while choice not in ['X','O']:
        choice = input('Would you like to be X or O? ').upper()

        if choice not in ['X','O']:
            print('Invalid choice, please choose X or O')

    return choice

def player_choice(user_marker):
    """
    Get player's position
    and place on the board
    """
    position = ''

    while position not in board or board[position] in ['X', 'O']:
        try:
            position = int(input('Where would you like to play? '))
        except ValueError:
            print('\nInvalid choice, please choose a number from 1-9')
            continue

        if position not in board:
            print('\nInvalid choice, please choose a number from 1-9')

        elif board[position] in ['X', 'O']:
            print('\nThat spot has been taken, please choose another number')
    # Place marker on the board
    place_marker(board, position, user_marker, player=True)

    return position


def computer_choice(computer_marker):
    """
    Get computer's position
    and place on the oard
    """

    print("\nComputer's turn...\n")

    choice = 0

    while choice not in board or board[choice] in ['X', 'O']:
        choice = random.randint(1,9)
    # Place marker on the board
    place_marker(board, position, user_marker, player=False)

    return choice 


def place_marker(board, position, marker, player=None):
    """
    Place the marker on the board 
    and display the board
    """
    board[position] = marker
    common_functions.display_board(board)
    # Check for winner
    check_winner(player)

def check_winner(player):
    # Horizontal wins
    if (
        board[1] == board[2] == board[3]
        ) or (
            board[4] == board[5] == board[6]
            ) or (
                board[7] == board[8] == board[9]):
        # If user wins
        if player:
            print('\nCongrats, you won! :party_popper:')
        else:
            print('\nOh no! You lost :pensive_face:')
            print('The computer wins')
        # Replay
    # Vertical wins
    elif (
        board[1] == board[4] == board[7]
        ) or (
            board[2] == board[5] == board[8]
            ) or (
                board[3] == board[6] == board[9]):
        # If user wins
        if player:
            print(Fore.GREEN + emoji.emojize('\nCongrats, you won! :party_popper:'))
            print(Style.RESET_ALL)
        else:
            print(Fore.BLUE + emoji.emojize('\nOh no! You lost :pensive_face:'))
            print('The computer wins')
            print(Style.RESET_ALL)
        # Replay
    # Diagonal wins
    elif (
        board[1] == board[5] == board[9]
        ) or (
            board[3] == board[5] == board[7]):
        # If user wins
        if player:
            print(Fore.GREEN + emoji.emojize('\nCongrats, you won! :party_popper:'))
            print(Style.RESET_ALL)
        else:
            print(Fore.BLUE + emoji.emojize('\nOh no! You lost :pensive_face:'))
            print('The computer wins')
            print(Style.RESET_ALL)
        # Replay