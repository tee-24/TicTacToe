import common_functions

# Global variables
Board = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}

def get_player1_name():
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

def player1_choice(player1_marker):
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
    place_marker(Board, position, player1_marker, player=True)

    return position 

def player2_choice(player2_marker):

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
    place_marker(Board, position, player2_marker, player=False)

    return position 

def place_marker(Board, position, marker, player=None):
    """
    Place the marker on the board 
    and display the board
    """
    Board[position] = marker
    common_functions.display_board(Board)
    # Check for winner

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
            print(f'\nCongrats {player1}, you won!')
            
        else:
            print(f'\nCongrats {player2}, you won!')

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
            print(f'\nCongrats {player1}, you won! ')
            
        else:
            print(f'\nCongrats {player2}, you won!')

        # Replay
        play_again()
    # Diagonal wins
    elif (
        board[1] == board[5] == board[9]
        ) or (
            board[3] == board[5] == board[7]):
        # If Player 1 wins
        if player:
            print(f'\nCongrats {player1}, you won!')
            
        else:
            print(f'\nCongrats {player2}, you won! ')

       
        # Replay
        play_again()
    # Check for tie
    elif common_functions.check_tie(board):
        print("It's a tie!")
        # Replay
        play_again()
        
def play_again():
    """
    Starts game again if user chooses 'yes'
    and ends the game if user chooses 'no
    """

    answer = input('Do you want to play again? ').capitalize()
    while answer not in ['Y', 'N', 'Yes', 'No']:
        print("I'm sorry, I don't understand")
        answer = input('Please type Yes or No: ').capitalize()
    # If user chooses yes
    if answer in ['Y', 'Yes']:
        print("Great, let's play again!")
        two_player_game()
    # If user chooses no
    else:
        print('\nThanks for playing!\n')
        exit()

def two_player_game():

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
    # Blank line
    print()
    # Display board
    common_functions.display_board(board)
    # Start game
    while play_game == True:
        print()
        # Where Player 1 wants to play
        player1_choice(player1_marker, player1)
        # Where Player 2 wants to play
        player2_choice(player2_marker, player2)