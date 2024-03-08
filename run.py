import common_functions
import one_player

def run_game():
    # Intro
    print('\nHello! Welcome to Tic Tac Toe :grinning_face_with_big_eyes:')
    # Instructions
    print('Instructions:')
    print('First to get 3 in a row wins!')
    # Blank line
    print()
    # Get number of players
    player_number = common_functions.get_num_of_players()

    if player_number == 1:
        # Start one player game
        one_player.get_user_name()
        one_player.one_player_game()
    else:
        # Start two player game
        pass


run_game()