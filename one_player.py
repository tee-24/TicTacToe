import commons
import random

# Global variables
Board = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}

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

    while position not in Board or Board[position] in ['X', 'O']:
        try:
            position = int(input('Where would you like to play? '))
        except ValueError:
            print('\nInvalid choice, please choose a number from 1-9')
            continue

        if position not in Board:
            print('\nInvalid choice, please choose a number from 1-9')

        elif Board[position] in ['X', 'O']:
            print('\nThat spot has been taken, please choose another number')
    # Place marker on the board
    place_marker(Board, position, user_marker, player=True)

    return position


def computer_choice(computer_marker):
    """
    Get computer's position
    and place on the oard
    """

    print("\nComputer's turn...\n")

    choice = 0

    while choice not in Board or Board[choice] in ['X', 'O']:
        choice = random.randint(1,9)
    # Place marker on the board
    place_marker(Board, position, user_marker, player=False)

    return choice 


def place_marker(Board, position, marker, player=None):
    """
    Place the marker on the board 
    and display the board
    """
    Board[position] = marker
    commons.display_board(Board)
    # Check for winner

def check_winner(player):
    # Horizontal wins
    if (
        Board[1] == Board[2] == Board[3]
        ) or (
            Board[4] == Board[5] == Board[6]
            ) or (
                Board[7] == Board[8] == Board[9]):
        # If user wins
        if player:
            print('\nCongrats, you won! :party_popper:')
        else:
            print('\nOh no! You lost :pensive_face:')
            print('The computer wins')
        # Replay
    # Vertical wins
    elif (
        Board[1] == Board[4] == Board[7]
        ) or (
            Board[2] == Board[5] == Board[8]
            ) or (
                Board[3] == Board[6] == Board[9]):
        # If user wins
        if player:
            print(Fore.GREEN + emoji.emojize('\nCongrats, you won! :party_popper:'))
            print(Style.RESET_ALL)
        else:
            print(Fore.BLUE + emoji.emojize('\nOh no! You lost :pensive_face:'))
            print('The computer wins')
            print(Style.RESET_ALL)
        # Replay