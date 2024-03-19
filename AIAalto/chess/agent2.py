import random
from agent_interface import AgentInterface
from envs.game import State

import chess


class Agent(AgentInterface):
    """
    An agent who plays Chess

    Methods
    -------
    `info` returns the agent's information
    `decide` chooses an action from possible actions
    """

    def __init__(self, depth: int = 5):
        self.depth = depth
        self.__player = None

    @staticmethod
    def info():
        """
        Return the agent's information

        Returns
        -------
        Dict[str, str]
            `agent name` is the agent's name
            `student name` is the list team members' names
            `student number` is the list of student numbers of the team members
        """
        # -------- Task 1 -------------------------
        # Please complete the following information
        # NOTE: Please try to pick a unique name for you agent. If there are
        #       some duplicate names, we have to change them.

        return {"agent name": "Peso plumaa",  # COMPLETE HERE
                "student name": ["Peso Plumaaaa"],  # COMPLETE HERE
                "student number": ["?"]}  # COMPLETE HERE

    


    def heuristic(self, state: State, deciding_agent: int):
        if deciding_agent == 0:
            COLOR = chess.WHITE
            otherCOLOR = chess.BLACK
        else: 
            COLOR = chess.BLACK
            otherCOLOR = chess.WHITE

        piece_values = {
            chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
            chess.KING: 100
        }

        material_score = 0

        for piece_type in piece_values:
            material_score += ( 
                len(state.board.pieces(piece_type, COLOR)) * piece_values[piece_type] - 
                len(state.board.pieces(piece_type, otherCOLOR)) * piece_values[piece_type]
                
            )
        CENTER_SQUARES = [chess.E4, chess.E5, chess.D4, chess.D5, chess.C4, chess.C5, chess.F4, chess.F5]

        pawns_controlled = 0#len(state.board.pawns(COLOR)) - len(state.board.pawns(otherCOLOR))
        center_squares_controlled = sum(1 for sq in chess.SQUARES if sq in CENTER_SQUARES and state.board.piece_at(sq) is not None)

        num_pinned_pieces = 0#len(self.get_pinned_pieces(state, COLOR))
        num_attacked_squares = len(state.board.attacks(COLOR)) - len(state.board.attacks(otherCOLOR))

        heuristic = material_score*.7 + .1*(pawns_controlled - pawns_controlled//2) + .1*center_squares_controlled - num_pinned_pieces*(.2) + .1*num_attacked_squares

        return heuristic


    def decide(self, state: State):
        """
        Generate a sequence of increasingly preferable actions

        Given the current `state`, this function should choose the action that
        leads to the agent's victory.
        However, since there is a time limit for the execution of this function,
        it is possible to choose a sequence of increasing preferable actions.
        Therefore, this function is designed as a generator; it means it should
        have no return statement, but it should `yield` a sequence of increasing
        good actions.

        IMPORTANT: If no action is yielded within the time limit, the game will
        choose a random action for the player.

        NOTE: You can find the possible actions and next states by using
              the `successors()` method of the `state`. In other words,
              `state.successors()` return a list of pairs of `action` and its
              corresponding next state.

        Parameters
        ----------
        state: State
            Current state of the game

        Yields
        ------
        action
            the chosen `action`
        """

        # -------- TASK 2 ------------------------------------------------------
        # Your task is to implement an algorithm to choose an action form the
        # possible `actions` in the `state.successors()`. You can implement any
        # algorithm you want.
        # However, you should keep in mind that the execution time of this
        # function is limited. So, instead of choosing just one action, you can
        # generate a sequence of increasingly good action.
        # This function is a generator. So, you should use `yield` statement
        # rather than `return` statement. To find more information about
        # generator functions, you can take a look at:
        # https://www.geeksforgeeks.org/generators-in-python/
        #
        # If you generate multiple actions, the last action will be used in the
        # game.
        #
        #
        # Tips
        # ====
        # 0. You can improve the `MinimaxAgent` to implement the Alpha-beta
        #    pruning approach.
        #    Also, By using `IterativeDeepening` class you can simply add
        #    the iterative deepening feature to your Alpha-beta agent.
        #    You can find an example of this in `id_minimax_agent.py` file.
        # 
        # 1. You can improve the heuristic function of `MinimaxAgent`.
        #
        # 2. If you need to simulate a game from a specific state to find the
        #    the winner, you can use the following pattern:
        #    ```
        #    simulator = Game(FirstAgent(), SecondAgent())
        #    winner = simulator.play(starting_state=specified_state)
        #    ```
        #    The `MCSAgent` has illustrated a concrete example of this
        #    pattern.
        #
        #
        #
        # GL HF :)
        # ----------------------------------------------------------------------

        # Replace the following lines with your algorithm
        """
        Get the value of each action by passing its successor to min_value
        function.
        """
        state = state.clone() # Must clone if used inside Iterative Deepening
        deciding = state.current_player() # Which agent's decision this is?
        ## lets order the moves, to make a more informed decision
        moves = state.applicable_moves()
        mapping_moves = [move for move in moves]
        resultingstates = [state.clone().execute_move(move) for move in moves]
        print(resultingstates)
        #states_values = [self.heuristic(state, deciding) for state in resultingstates]
        #moves = sorted(moves, key=lambda move: self.heuristic(mapping_moves[move],deciding))
        #random.shuffle(moves)
        alpha = float('-inf')
        beta = float('inf')
        best_action = moves[0]
        max_value = float('-inf')
        for action in moves:
            state.execute_move(action)
            action_value = self.min_value(state, self.depth - 1,deciding, alpha, beta)
            state.undo_last_move()
            if action_value > max_value:
                max_value = action_value
                best_action = action

            if alpha >= beta:
                #print('i did alpha beta pruning')
                break
        print("Best action is " + str(best_action) + "  value " + str(max_value))

        yield best_action

    def max_value(self, state: State, depth: int, deciding : int, alpha, beta):
        """
        Get the value of each action by passing its successor to min_value
        function. Return the maximum value of successors.
        
        The value is from the perspective of the player who is trying to
        decide which move to make, as in function 'define' above.
        The parameter 'deciding' indicates which agent's perspective it is.
        
        NOTE: when passing the successor to min_value, `depth` must be
        reduced by 1, as we go down the Minimax tree.
        
        NOTE: the player must check if it is the winner (or loser)
        of the game, in which case, a large value (or a negative value) must
        be assigned to the state. Additionally, if the game is not over yet,
        but we have `depth == 0`, then we should return the heuristic value
        of the current state.
        """

        # Termination conditions
        winner = state.is_winner()
        if winner is not None:
            if winner == 1: return 1000+(depth-self.depth) # Maximizing player wins
            if winner == -1: return -1000-(depth-self.depth) # Minimizing palyer wins
            return 0 # Stalemate
        if depth == 0:
            return self.heuristic(state,deciding)

        # If it is not terminated
        moves = state.applicable_moves()
        value = float('-inf')
        for action in moves:
            state.execute_move(action)
            value = max(value, self.min_value(state, depth - 1,deciding, alpha, beta))
            state.undo_last_move()
            if value >= beta:
                #print('i did alpha beta pruning')
                break

            alpha = max(alpha, value)
        return value


    def min_value(self, state: State, depth: int, deciding : int, alpha, beta):
        """
        Get the value of each action by passing its successor to max_value
        function. Return the maximum value of successors.
        
        The value is from the perspective of the player who is trying to
        decide which move to make, as in function 'define' above.
        The parameter 'deciding' indicates which agent's perspective it is.
        
        NOTE: when passing the successor to max_value, `depth` must be
        reduced by 1, as we go down the Minimax tree.
        
        NOTE: the player must check if it is the winner (or loser)
        of the game, in which case, a large value (or a negative value) must
        be assigned to the state. Additionally, if the game is not over yet,
        but we have `depth == 0`, then we should return the heuristic value
        of the current state.
        """

        # Termination conditions
        winner = state.is_winner()
        if winner is not None:
            if winner == 1: return -1000-(depth-self.depth) # Minimizing player wins
            if winner == -1: return 1000+(depth-self.depth) # Maximizing player wins
            return 0 # Stalemate
        if depth == 0:
            return self.heuristic(state,deciding)

        # If it is not terminated
        moves = state.applicable_moves()
        value = float('inf')
        for action in moves:
            state.execute_move(action)
            value = min(value, self.max_value(state, depth - 1,deciding, alpha, beta))
            state.undo_last_move()
            if value <= alpha:
                #print('i did alpha beta pruning')
                break
            beta = min(beta, value)
        return value

