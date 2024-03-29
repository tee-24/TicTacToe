import common_functions
import random
import emoji
from colorama import Fore, Back, Style

# Global variables
board = {
    1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"
}
play_game = True


def get_user_name():
    """
    Get the name of the player
    """
    player = ""

    while len(player) < 3 or not player.isalpha() or len(player) > 10:
        player = input("What is your name? ").capitalize()
        # If name contains anything but letters
        if player.isalpha() is False:
            print(Fore.RED + "Name can only contain letters, please try again")
            print(Style.RESET_ALL)
        # If name is less than 3 letters
        elif len(player) < 3:
            print(
                Fore.RED + "Name must be a min of 3 letters, please try again"
                )
            print(Style.RESET_ALL)
        # If name is longer than 10 letters
        elif len(player) > 10:
            print(
                Fore.RED + "Name must be a max of 10 letters, please try again"
            )
            print(Style.RESET_ALL)

    print(f"\nHi {player}!")
    return player


def get_user_marker():
    """
    Get user marker
    """
    choice = ""

    while choice not in ["X", "O"]:
        choice = input("Would you like to be X or O? ").upper()

        if choice not in ["X", "O"]:
            print(Fore.RED + "Invalid choice, please choose X or O")
            print(Style.RESET_ALL)

    return choice


def player_choice(user_marker):
    """
    Get player's position
    and place on the board
    """
    position = ""

    while position not in board or board[position] in ["X", "O"]:
        try:
            position = int(input("Where would you like to play? "))
        except ValueError:
            print(
                Fore.RED + "\nInvalid choice, please choose a number from 1-9"
                )
            print(Style.RESET_ALL)
            continue

        if position not in board:
            print(
                Fore.RED + "\nInvalid choice, please choose a number from 1-9"
                )
            print(Style.RESET_ALL)

        elif board[position] in ["X", "O"]:
            print(
                Fore.BLUE + "\nThat spot is taken, choose another number"
            )
            print(Style.RESET_ALL)
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

    while choice not in board or board[choice] in ["X", "O"]:
        choice = random.randint(1, 9)
    # Place marker on the board
    place_marker(board, choice, computer_marker, player=False)

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
        (board[1] == board[2] == board[3])
        or (board[4] == board[5] == board[6])
        or (board[7] == board[8] == board[9])
    ):
        # If user wins
        if player:
            print(
                Fore.GREEN + emoji.emojize(
                    "\nCongrats, you won! :party_popper:"
                    ))
            print(Style.RESET_ALL)
        else:
            print(
                Fore.BLUE + emoji.emojize(
                    "\nOh no! You lost :pensive_face:"
                    ))
            print("The computer wins")
            print(Style.RESET_ALL)
        # Replay
        play_again()
    # Vertical wins
    elif (
        (board[1] == board[4] == board[7])
        or (board[2] == board[5] == board[8])
        or (board[3] == board[6] == board[9])
    ):
        # If user wins
        if player:
            print(
                Fore.GREEN + emoji.emojize(
                    "\nCongrats, you won! :party_popper:"
                    ))
            print(Style.RESET_ALL)
        else:
            print(
                Fore.BLUE + emoji.emojize(
                    "\nOh no! You lost :pensive_face:"
                    ))
            print("The computer wins")
            print(Style.RESET_ALL)
        # Replay
        play_again()
    # Diagonal wins
    elif (
        board[1] == board[5] == board[9]
        ) or (
            board[3] == board[5] == board[7]):
        # If user wins
        if player:
            print(
                Fore.GREEN + emoji.emojize(
                    "\nCongrats, you won! :party_popper:"
                    ))
            print(Style.RESET_ALL)
        else:
            print(
                Fore.BLUE + emoji.emojize(
                    "\nOh no! You lost :pensive_face:"
                    ))
            print("The computer wins")
            print(Style.RESET_ALL)
        # Replay
        play_again()
    # Check for tie
    elif common_functions.check_tie(board):
        print(Fore.YELLOW + "\nIt's a tie!")
        print(Style.RESET_ALL)
        # Replay
        play_again()


def play_again():
    """
    Starts game again if user chooses 'yes'
    and ends the game if user chooses 'no
    """

    answer = input("Do you want to play again? ").capitalize()
    while answer not in ["Y", "N", "Yes", "No"]:
        print(Fore.RED + "I'm sorry, I don't understand")
        print(Style.RESET_ALL)
        answer = input("Please type Yes or No: ").capitalize()
    # If user chooses yes
    if answer in ["Y", "Yes"]:
        print(
            emoji.emojize(
                "\nGreat, let's play again :grinning_face_with_big_eyes:!\n"
                )
        )
        one_player_game()
    # If user chooses no
    else:
        print(
            Fore.CYAN + emoji.emojize(
                "\nThanks for playing! :waving_hand:\n"
            ))
        exit()


def one_player_game():
    """
    Play the game in single player mode,
    the computer will be the other player
    """

    # Get the user's marker
    user_marker = get_user_marker()
    # Determine computer marker based on user's marker
    if user_marker == "X":
        computer_marker = "O"
    else:
        computer_marker = "X"
    # Reset the board
    common_functions.reset_board(board)
    # Blank line
    print()
    # Display the board
    common_functions.display_board(board)
    # Start game
    while play_game is True:
        # Blank line
        print()
        # Where the user wants to play
        player_choice(user_marker)
        # Where the computer wants to play
        computer_choice(computer_marker)
