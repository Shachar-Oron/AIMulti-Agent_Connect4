# 4 Connect Agent-Multi
Welcome to 4 Connect Agent-Multi! This Python implementation of the classic Connect 4 game comes with an added twist – the ability to play against intelligent agents. In the py4.connect file, you'll find four parameters that define the game settings. Let's delve into each parameter:

1. **graphicMode:**
  A boolean variable that allows you to choose between playing the game with beautiful graphics (True) or through the command line (False).
2. **gameMode:**
  This variable determines the game mode and can take one of two values:
  * 2 for a game of two players.
  * 1 for a game of Player versus Agent.
3. **depth:**
  The depth variable contains the maximum depth for exploring the game tree. Adjusting this value can impact the agent's decision-making process.
4. **type:**
  The type variable contains the name of the agent you want to play against if gameMode is set to 1 (Player versus Agent). Different agent types are available, including:
  * "BestRandom"
  * "MinimaxAgent"
  * "AlphaBetaAgent"
  * "ExpectimaxAgent"
  Default values are already defined in the py4.connect file, providing a starting point for experimentation.

## Playing Against Agents
When *'gameMode'* is set to *'1'*, you can play against intelligent agents.
Here are a few examples:

* **MinimaxAgent:**

  To play against the Minimax agent, set the code as follows:
  '''shel
  gameMode = 1
  type = "MinimaxAgent"
  '''
* **Alpha-Beta Pruning:**
  
  To play against the Alpha-Beta Pruning agent, set the code as follows:
  '''shel
  gameMode = 1
  type = "AlphaBetaAgent"
  '''
* **ExpectimaxAgent:**
  
  '''shel
  Copy code
  gameMode = 1
  type = "ExpectimaxAgent"
  '''
## Running the Game
To run the game, execute the connect4.py script. Experiment with different parameter values to explore various game scenarios and challenge yourself against intelligent agents!
'''shell
python connect4.py
'''
## requirements
also, to run, u need to implement:
''' shel
pip install pygame
'''
