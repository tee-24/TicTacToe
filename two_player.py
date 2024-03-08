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

