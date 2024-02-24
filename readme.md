# Chess Answer
## Explaination of PlayGame
PlayGame is the most import class in programTests/Game.py which package the function to play game,the exact explaination of PlayGame is as followings
+ Initializes the game: The class initializes an 8x8 chessboard where each cell is initially empty ("0"). It also creates an empty dictionary database to store the positions and types of players, and an empty list points to store all the non-empty cells on the board.

+ Custom setup: The setup() method allows the user to input the initial positions of the knight, queen, and bishop. It creates new instances of these pieces, updates the chessboard, and records the players' positions.

+ Random setup: The randomSetup() method generates random positions for the knight, queen, and bishop, updates the chessboard, and records the players' positions.

+ Customized setup (player vs. player): The custmorized_setup() method allows the user to choose to play against a computer or another player, and input the types of the player pieces. It creates new instances of these pieces, updates the chessboard, and records the players' positions.

+ Customized gameplay (player vs. computer): The customrizedPlayWithComputer() method starts a game of player vs. computer. It takes turns prompting the player and the computer to make moves, updating the chessboard, and checking if the players are still alive.

+ Customized gameplay (player vs. player): The customrizedPlayWithPlayer() method starts a game of player vs. player. It takes turns prompting the two players to make moves, updating the chessboard, and checking if the players are still alive.

+ Automatic gameplay: The autoPlay() method allows the user to specify the number of rounds to play automatically. It randomly moves the knight, queen, and bishop, and checks if the players are still alive.

+ Sets up a player: The set_player() method creates a new player instance based on the input type ("k", "q", or "b").

+ Adds a new player: The newPlayer() method adds the player's position and type to the database dictionary.

+ Updates the chessboard: The newDots() method updates the chessboard to reflect the player's move.

+ Displays the chessboard: The showBoard() method prints the current state of the chessboard.

+ Displays the players on the chessboard: The showPointsinBoard() method prints all the non-empty cells on the chessboard and their corresponding player types.

+ Checks if a player is alive: The is_live() method checks if a given player is still alive. If the player's position no longer contains their type, the player is marked as dead and False is returned. Otherwise, True is returned.


## Test Function
two test function `autoPlay()` and `customrizedPlay()` are in programTests/answertest.py.`autoPlay()` can run the game with  computer to computer randomly ,while `customrizedPlay()` can run the game with  computer to user or user to user.

