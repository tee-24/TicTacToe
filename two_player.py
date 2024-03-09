import common_functions
import emoji
from colorama import Fore, Back, Style

# Global variables
board = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
play_game = True
player1 = ''
player2 = ''

def get_player1_name():
    """
    Get the name of Player 1
    """
    player1 = ''

    while len(player1) < 3 or not player1.isalpha() or len(player1) > 10:
        player1 = input('Player 1, enter your name: ').capitalize()

        if player1.isalpha() == False:
            print(Fore.RED + 'Name can only contain letters, please try again')
            print(Style.RESET_ALL)
        elif len(player1) < 3:
            print(Fore.RED + 'Name must be a minimum of 3 letters, please try again')
            print(Style.RESET_ALL)
        elif len(player1) > 10:
            print(Fore.RED + 'Name can only be a maximum of 10 letters, please try again')
            print(Style.RESET_ALL)

    print(Fore.YELLOW + f'{player1} is Player 1')
    print(Style.RESET_ALL)

    return player1

def get_player2_name():
    """
    Get the name of Player 2
    """
    player2 = ''

    while len(player2) < 3 or not player2.isalpha() or len(player2) > 10:
        player2 = input('Player 2, enter your name: ').capitalize()

        if player2.isalpha() == False:
            print(Fore.RED + 'Name can only contain letters, please try again')
            print(Style.RESET_ALL)
        elif len(player2) < 3:
            print(Fore.RED + 'Name must be a minimum of 3 letters, please try again')
            print(Style.RESET_ALL)
        elif len(player2) > 10:
            print(Fore.RED + 'Name can only be a maximum of 10 letters, please try again')
            print(Style.RESET_ALL)
        
    print(Fore.YELLOW + f'{player2} is Player 2')
    print(Style.RESET_ALL)

    return player2

def get_player1_marker(player1, player2):
    """
    Get the marker for Player 1
    """

    choice = ''

    while choice not in ['X','O']:
        choice = input(f'\n{player1}, would you like to be X or O? ').upper()

        if choice not in ['X','O']:
            print(Fore.RED + 'Invalid choice, please choose X or O')
            print(Style.RESET_ALL)

    if choice == 'X':
        print(Fore.YELLOW + f'\n{player1} is X')           
        print(f'{player2} is O')
        print(Style.RESET_ALL)
    else:
        print(Fore.YELLOW + f'\n{player1} is O')
        print(f'{player2} is X')
        print(Style.RESET_ALL)

    return choice

def player1_choice(player1_marker, player1):
    """
    Get Player 1 position 
    and place it on the board
    """
    position = ''

    while position not in board or board[position] in ['X', 'O']:
        try:
            position = int(input(f'Where would you like to play {player1}? '))
        except ValueError:
            print(Fore.RED + 'Invalid choice, please choose a number from 1-9')
            print(Style.RESET_ALL)
            continue

        if position not in board:
            print(Fore.RED + 'Invalid choice, please choose a number from 1-9')
            print(Style.RESET_ALL)

        elif board[position] in ['X', 'O']:
            print(Fore.BLUE + 'That spot has been taken, please choose another number')
            print(Style.RESET_ALL)
    # Place marker on the board
    place_marker(board, position, player1_marker, player1, player2, player=True)

    return position 

def player2_choice(player2_marker, player2):

    position = ''

    while position not in board or board[position] in ['X', 'O']:
        try:
            position = int(input(f'Where would you like to play {player2}? '))
        except ValueError:
            print(Fore.RED + 'Invalid choice, please choose a number from 1-9')
            print(Style.RESET_ALL)
            continue

        if position not in board:
            print(Fore.RED + 'Invalid choice, please choose a number from 1-9')
            print(Style.RESET_ALL)

        elif board[position] in ['X', 'O']:
            print(Fore.BLUE + 'That spot has been taken, please choose another number')
            print(Style.RESET_ALL)

    # Place marker on the board
    place_marker(board, position, player2_marker, player1, player2, player=False)

    return position 

def place_marker(board, position, marker, player1, player2, player=None):
    """
    Place the marker on the board 
    and display the board
    """
    board[position] = marker
    common_functions.display_board(board)
    # Check for winner
    check_winner(player1, player2, player)

def check_winner(player1, player2, player):
    
    # Horizontal wins
    if (
        board[1] == board[2] == board[3]
        ) or (
            board[4] == board[5] == board[6]
            ) or (
                board[7] == board[8] == board[9]):
        # If Player 1 wins
        if player:
            print(Fore.GREEN + emoji.emojize(f'\nCongrats {player1}, you won! :party_popper:'))
            print(Style.RESET_ALL)
            
        else:
            print(Fore.GREEN + emoji.emojize(f'\nCongrats {player2}, you won! :party_popper:'))
            print(Style.RESET_ALL)

        # Replay
        play_again()
    # Vertical wins
    elif (
        board[1] == board[4] == board[7]
        ) or (
            board[2] == board[5] == board[8]
            ) or (
                board[3] == board[6] == board[9]):
        # If Player 1 wins
        if player:
            print(Fore.GREEN + emoji.emojize(f'\nCongrats {player1}, you won! :party_popper:'))
            print(Style.RESET_ALL)
            
        else:
            print(Fore.GREEN + emoji.emojize(f'\nCongrats {player2}, you won! :party_popper:'))
            print(Style.RESET_ALL)

        # Replay
        play_again()
    # Diagonal wins
    elif (
        board[1] == board[5] == board[9]
        ) or (
            board[3] == board[5] == board[7]):
        # If Player 1 wins
        if player:
            print(Fore.GREEN + emoji.emojize(f'\nCongrats {player1}, you won! :party_popper:'))
            print(Style.RESET_ALL)
            
        else:
            print(Fore.GREEN + emoji.emojize(f'\nCongrats {player2}, you won! :party_popper:'))
            print(Style.RESET_ALL)

       
        # Replay
        play_again()
    # Check for tie
    elif common_functions.check_tie(board):
        print(Fore.YELLOW + "It's a tie!")
        print(Style.RESET_ALL)
        # Replay
        play_again()
        
def play_again():
    """
    Starts game again if user chooses 'yes'
    and ends the game if user chooses 'no
    """

    answer = input('Do you want to play again? ').capitalize()
    while answer not in ['Y', 'N', 'Yes', 'No']:
        print(Fore.RED + "I'm sorry, I don't understand")
        print(Style.RESET_ALL)
        answer = input('Please type Yes or No: ').capitalize()
    # If user chooses yes
    if answer in ['Y', 'Yes']:
        print(emoji.emojize("\nGreat, let's play again! :grinning_face_with_big_eyes:\n"))
        two_player_game()
    # If user chooses no
    else:
        print(Fore.CYAN + emoji.emojize('\nThanks for playing! :waving_hand:\n'))
        exit()

def two_player_game():
    # Blank line
    print()
    # Get names of players
    player1 = get_player1_name()
    player2 = get_player2_name()
    # Get Player 1 marker
    player1_marker = get_player1_marker(player1, player2)
    # Determine Player 2 marker based on Player 1 marker
    if player1_marker == 'X':
        player2_marker = 'O'
    else:
        player2_marker = 'X'
    # Reset the board
    common_functions.reset_board(board)
    # Blank line
    print()
    # Display board
    common_functions.display_board(board)
    # Start game
    while play_game:
        # Blank line
        print()
        # Where Player 1 wants to play
        player1_choice(player1_marker, player1)
        # Blank line
        print()
        # Where Player 2 wants to play
        player2_choice(player2_marker, player2)