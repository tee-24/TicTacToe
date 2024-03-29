import common_functions
import one_player
import two_player
import emoji
from colorama import Fore, Back, Style


def run_game():
    # Intro
    print(
        Fore.CYAN
        + emoji.emojize(
            "\nHello! Welcome to Tic Tac Toe :grinning_face_with_big_eyes:"
            )
    )
    print(Style.RESET_ALL)
    # Instructions
    print(Fore.YELLOW + "Instructions:")
    print("First to get 3 in a row wins!")
    print(Style.RESET_ALL)
    # Get number of players
    player_number = common_functions.get_num_of_players()

    if player_number == 1:
        # Blank line
        print()
        # Start one player game
        one_player.get_user_name()
        one_player.one_player_game()
    else:
        # Start two player game
        two_player.two_player_game()


run_game()
