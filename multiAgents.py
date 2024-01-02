"""
Introduction to Artificial Intelligence, 89570, Bar Ilan University, ISRAEL

Student name: Shachar Oron
Student ID: 322807231

"""

# multiAgents.py
# --------------
# Attribution Information: part of the code were created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# http://ai.berkeley.edu.
# We thank them for that! :)


import random, util, math
import gameUtil as u

from connect4 import Agent


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    """
    score = currentGameState.getScore()
    return score

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxAgent, AlphaBetaAgent & ExpectimaxAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        print("eval")
        self.index = 1 # agent is always index 1
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class BestRandom(MultiAgentSearchAgent):

    def getAction(self, gameState):

        return gameState.pick_best_move()

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 1)
    minimax function return a value and an action
    """
    def minimax(self, gameState, agent, depth):
        if gameState.is_terminal() or depth == 0:
            eva = self.evaluationFunction(gameState)
            return eva, None
        legal_actions = gameState.getLegalActions()
        if gameState.turn == agent: # maximizing the agent
            temp_max = -math.inf
            for action in legal_actions:
                new_gameState = gameState.generateSuccessor(u.AI, action)
                new_gameState.switch_turn(new_gameState.turn)
                eva = self.minimax(new_gameState, agent, depth - 1)[0]
                if eva > temp_max:
                    temp_max = eva
                    select_action = action
            return temp_max, select_action
        else: # this is the player turn, minimize
            temp_min = math.inf
            for action in legal_actions:
                new_gameState = gameState.generateSuccessor(u.AI, action)
                new_gameState.switch_turn(new_gameState.turn)
                eva = self.minimax(new_gameState, agent, depth - 1)[0]
                if eva < temp_min:
                    temp_min = eva
                    select_action = action
            return temp_min, select_action


    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.isWin():
        Returns whether or not the game state is a winning state for the current turn player

        gameState.isLose():
        Returns whether or not the game state is a losing state for the current turn player

        gameState.is_terminal()
        Return whether or not that state is terminal
        """

        "*** YOUR CODE HERE ***"
        select_action = self.minimax(gameState, u.AI, self.depth)[1]
        return select_action
       # util.raiseNotDefined()


class AlphaBetaAgent(MultiAgentSearchAgent):

    def alphaBeta(self, gameState, agent, depth, alpha, beta):
        if gameState.is_terminal() or depth == 0:
            eva = self.evaluationFunction(gameState)
            return eva, None
        legal_actions = gameState.getLegalActions()
        if gameState.turn == agent:  # maximizing the agent
            temp_max = -math.inf
            for action in legal_actions:
                new_gameState = gameState.generateSuccessor(u.AI, action)
                new_gameState.switch_turn(new_gameState.turn)
                eva = self.alphaBeta(new_gameState, agent, depth - 1, alpha, beta)[0]
                if eva > temp_max:
                    temp_max = eva
                    select_action = action
                if temp_max > beta:
                    return temp_max, select_action
                alpha = max(alpha, temp_max)
            return temp_max, select_action
        else: # this is the player turn, minimize
            temp_min = math.inf
            for action in legal_actions:
                new_gameState = gameState.generateSuccessor(u.AI, action)
                new_gameState.switch_turn(new_gameState.turn)
                eva = self.alphaBeta(new_gameState, agent, depth - 1, alpha, beta)[0]
                if eva < temp_min:
                    temp_min = eva
                    select_action = action
                if temp_min < alpha:
                    return temp_min, select_action
                beta = min(beta, temp_min)
            return temp_min, select_action

    def getAction(self, gameState):

        """
            Your minimax agent with alpha-beta pruning (question 2)
        """
        "*** YOUR CODE HERE ***"
        select_action = self.alphaBeta(gameState, u.AI, self.depth, -math.inf, math.inf)[1]
        return select_action
        # util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 3)
    """
    def expectimax(self, gameState, agent, depth):
        if gameState.is_terminal() or depth == 0:
            eva = self.evaluationFunction(gameState)
            return eva, None
        legal_actions = gameState.getLegalActions()
        if gameState.turn == agent:  # maximizing the agent
            temp_value = -math.inf
            for action in legal_actions:
                new_gameState = gameState.generateSuccessor(u.AI, action)
                new_gameState.switch_turn(new_gameState.turn)
                eva = self.expectimax(new_gameState, agent, depth - 1)[0]
                if eva > temp_value:
                    temp_value = eva
                    select_action = action
            return temp_value, select_action
        else:  # this is the player turn, exp
            temp_value = 0
            for action in legal_actions:
                new_gameState = gameState.generateSuccessor(u.AI, action)
                new_gameState.switch_turn(new_gameState.turn)
                probability = 1 / len(legal_actions)
                eva = self.expectimax(new_gameState, agent, depth - 1)[0]
                temp_value += probability * eva
            return temp_value, None


    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        select_action = self.expectimax(gameState, u.AI, self.depth)[1]
        return select_action
        # util.raiseNotDefined()
