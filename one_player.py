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