import common_functions

# Global variables
Board = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}

ef get_player1_name():
    """
    Get the name of Player 1
    """
    player1 = ''

    while len(player1) < 3 or not player1.isalpha() or len(player1) > 10:
        player1 = input('\nPlayer 1, enter your name: ').capitalize()

        if player1.isalpha() == False:
            print('Name can only contain letters, please try again')
        elif len(player1) < 3:
            print('Name must be a minimum of 3 letters, please try again')
        elif len(player1) > 10:
            print('Name can only be a maximum of 10 letters, please try again')

    print(f'{player1} is Player 1')

    return player1

def get_player2_name():
    """
    Get the name of Player 2
    """
    player2 = ''

    while len(player2) < 3 or not player2.isalpha() or len(player2) > 10:
        player2 = input('\nPlayer 2, enter your name: ').capitalize()

        if player2.isalpha() == False:
            print('Name can only contain letters, please try again')
        elif len(player2) < 3:
            print('Name must be a minimum of 3 letters, please try again')
        elif len(player2) > 10:
            print('Name can only be a maximum of 10 letters, please try again')
        
    print(f'{player2} is Player 2')

    return player2

def get_player1_marker(player1, player2):
    """
    Get the marker for Player 1
    """

    choice = ''

    while choice not in ['X','O']:
        choice = input(f'\n{player1}, would you like to be X or O? ').upper()

        if choice not in ['X','O']:
            print('Invalid choice, please choose X or O')

    if choice == 'X':
        print(f'{player1} is X')           
        print(f'{player2} is O')
    else:
        print(f'{player1} is O')
        print(f'{player2} is X')

    return choice

def player1_choice(player1_marker, player1):
    """
    Get Player 1 position 
    and place it on the board
    """
    position = ''

    while position not in Board or Board[position] in ['X', 'O']:
        try:
            position = int(input(f'Where would you like to play {player1}? '))
        except ValueError:
            print('Invalid choice, please choose a number from 1-9')
            continue

        if position not in Board:
            print('Invalid choice, please choose a number from 1-9')

        elif Board[position] in ['X', 'O']:
            print('That spot has been taken, please choose another number')
    # Place marker on the board
    place_marker(Board, position, player1_marker)

    return position 

def player2_choice(player2_marker, player2):

    position = ''

    while position not in Board or Board[position] in ['X', 'O']:
        try:
            position = int(input(f'Where would you like to play {player2}? '))
        except ValueError:
            print('Invalid choice, please choose a number from 1-9')
            continue

        if position not in Board:
            print('Invalid choice, please choose a number from 1-9')

        elif Board[position] in ['X', 'O']:
            print('That spot has been taken, please choose another number')

    # Place marker on the board
    place_marker(Board, position, player2_marker)

    return position 

def place_marker(Board, position, marker):
    """
    Place the marker on the board 
    and display the board
    """
    Board[position] = marker
    common_functions.display_board(Board)
    # Check for winner
