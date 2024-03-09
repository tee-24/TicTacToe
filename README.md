
# Design
## Flowchart
![game.gif](docs/flowchart.png)

## Color Scheme
* Error messages are printed in red
* The introduction message is printed in cyan
* In the single player game, the message is printed in green if the user wins
* In the single player game, the message is printed in blue if the user loses
* In the two player game, the message is printed in green when Player 1 or Player 2 wins
* When there is a tie, the message is printed in yellow

## Future Implementations
 I would like to develop this game using Pygame to create a more interactive and user friendly game that is responsive and can be played on various devices.

# Technologies Used
* Python3 - Delivers the structure and content for the game
* Git - For version control
*  Gitpod - Used to develop the game
* Gitbash - Terminal used to push changes to the GitHub repository
* GitHub - Used to host the game
* Heroku - Used to deploy the game
* [Lucid](https://lucid.app/documents?referringApp=slack#/documents?folder_id=recent) - Used to create flowchart
* [ezgif.com](https://ezgif.com/) - Used to create Gif
* [Colorama](https://pypi.org/project/colorama/) - Used to add colour to the terminal
* [Emoji](https://pypi.org/project/emoji/) - Used to add emojis to the terminal
* [Black](https://pypi.org/project/black/) - Used to format code
* [PyPI](https://pypi.org/) - Used to import Colorama and Emoji packages
*  [CI Python Linter](https://pep8ci.herokuapp.com/) - Used to validate code


# Testing
Testing was ongoing throughout the entire build. As this game runs on a mock terminal, it will not work on mobile devices so no accessibility or responsitivity testing was required.

### Code Institute Python Linter
Validation was done using [CI Python Linter](https://pep8ci.herokuapp.com/) 

run.py
![run](docs/run.png)

common_functions.py
![common](docs/common.png)

one_player.py
![oneplayer](docs/oneplayer.png)

two_player.py
![twoplayer](docs/twoplayer.png)

### Manual Testing
To fully test my game, I performed the following tests:

| Test                                                                 | Action                                                                        | Expected Result                                                                                                                                                                                                                                            | Pass/Fail |
| -------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| get_num_of_players()                                                 | Enter h<br>Enter 6<br>Enter 1<br>Enter 2                                      | Error message, ask user to try again<br>Error message, ask user to try again<br>Ask for user's name<br>Ask player 1 to enter name                                                                                                                          | Pass      |
| get_user_name()                                                      | Enter 5<br>Enter am<br>Enter dan1<br>Enter mynameislong<br>Enter tee          | Error message, ask user to try again<br>Error message, ask user to try again<br>Error message, ask user to try again<br>Error message, ask user to try again<br>Ask user to select X or O                                                                  | Pass      |
| get_user_marker()                                                    | Enter 5<br>Enter a<br>Enter .<br>Enter x<br>Enter o                           | Error message, ask user to try again<br>Error message, ask user to try again<br>Error message, ask user to try again<br>Ask where user wants to play<br>Ask where user wants to play                                                                       | Pass      |
| player_choice()                                                      | Enter 0<br>Enter a<br>Enter .<br>Enter 1                                      | Error message, ask user to try again<br>Error message, ask user to try again<br>Error message, ask user to try again<br>Replace 1 with marker and print the board                                                                                          | Pass      |
| check_winner(player)                                                 | Win against computer<br>Lose against computer<br>Tie with computer            | Print that player has won<br>Print that computer has won<br>Print that there is a tie                                                                                                                                                                      | Pass      |
| play_again()                                                         | Enter 5<br>Enter ok<br>Enter .<br>Enter n<br>Enter no<br>Enter y<br>Enter yes | Error message, ask user to try again<br>Error message, ask user to try again<br>Error message, ask user to try again<br>Thank user for playing and exit game<br>Thank user for playing and exit game<br>Restart one player game<br>Restart one player game | Pass      |
| get_player1_name()                                                   | Enter 5<br>Enter am<br>Enter dan1<br>Enter mynameislong<br>Enter tee          | Error message, ask user to try again<br>Error message, ask user to try again<br>Error message, ask user to try again<br>Error message, ask user to try again<br>Ask player 2 to enter name                                                                 | Pass      |
| get_player2_name()                                                   | Enter 5<br>Enter am<br>Enter dan1<br>Enter mynameislong<br>Enter dee          | Error message, ask user to try again<br>Error message, ask user to try again<br>Error message, ask user to try again<br>Error message, ask user to try again<br>Ask player 1 to select X or O                                                              | Pass      |
| player1_choice(player1_marker, player1)                              | Enter 5<br>Enter a<br>Enter .<br>Enter x<br>Enter o                           | Error message, ask user to try again<br>Error message, ask user to try again<br>Error message, ask user to try again<br>Ask where player1 wants to play<br>Ask where player1 wants to play                                                                 | Pass      |
| place_marker(board, position, marker, player1, player2, player=None) | Enter 0<br>Enter a<br>Enter .<br>Enter 1                                      | Error message, ask user to try again<br>Error message, ask user to try again<br>Error message, ask user to try again<br>Replace 1 with marker and print the board                                                                                          | Pass      |
| player2_choice(player2_marker, player2)                              | Enter 0<br>Enter a<br>Enter .<br>Enter 1<br>Enter 3                           | Error message, ask user to try again<br>Error message, ask user to try again<br>Error message, ask user to try again<br>Error message, ask user to try again<br>Replace 3 with marker and print the board                                                  | Pass      |
| check_winner(player1, player2, player)                               | Player 1 beats Player 2<br>Player 2 beats Player 1<br>Tie                     | Print that Player 1 has won<br>Print that Player 2 has won<br>Print that there is a tie                                                                                                                                                                    | Pass      |
| play_again()                                                         | Enter 5<br>Enter ok<br>Enter .<br>Enter n<br>Enter no<br>Enter y<br>Enter yes | Error message, ask user to try again<br>Error message, ask user to try again<br>Error message, ask user to try again<br>Thank user for playing and exit game<br>Thank user for playing and exit game<br>Restart two player game<br>Restart two player game | Pass      |

# Bugs
### Known Bugs
1. In the 2 player game, the users are asked for their names again when they choose to play again.

# Credits
* Emojis were sourced from [PyPI](https://pypi.org/project/emoji/)
* Colorama was learned from [PyPI](https://pypi.org/project/colorama/)
*  Black was learned from [PyPI](https://pypi.org/project/black/)
* Images were compressed by [iLoveIMG](https://www.iloveimg.com/)
* https://ezgif.com/
* isalpha() method was learned from [W3 Schools](https://www.w3schools.com/python/ref_string_isalpha.asp#:~:text=The%20isalpha()%20method%20returns,!%23%25%26%3F%20etc.)

# Acknowledgements
This game was designed and developed in conjunction with the Full Stack Software Developer Diploma course (ecommerce) at the Code Institute. I would like to thank my mentor, Daisy, the Slack community, and Code Institute for all their support.