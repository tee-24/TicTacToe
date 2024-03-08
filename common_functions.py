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