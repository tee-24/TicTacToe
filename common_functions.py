# Global variables
Board = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}


def get_num_of_players():
    """
    Get the number of players from user
    """

    answer = 0

    while answer not in [1, 2]:
        try:
            answer = int(input('1 or 2 players? '))
        except ValueError:
            print('\nInvalid choice, please choose 1 or 2')
            
            continue

        if answer not in [1, 2]:
            print('\nInvalid choice, please choose 1 or 2')
    
    return answer

def display_board(Board):
    """
    Print out the game board
    """
    print(f' {Board[1]} | {Board[2]} | {Board[3]}')
    print(f' {Board[4]} | {Board[5]} | {Board[6]}')
    print(f' {Board[7]} | {Board[8]} | {Board[9]}')