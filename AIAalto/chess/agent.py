from envs.game import State
from agent_interface import AgentInterface
import random
from game import Game
from random_agent import RandomAgent

class Agent(AgentInterface):
    """
    An agent who plays Chess

    Methods
    -------
    `info` returns the agent's information
    `decide` chooses an action from possible actions
    """

    def __init__(self, state = None, parent = None, parent_action=None):
        self.state = state
        self.parent = parent
        self.parent_action = parent_action
        self.children = []
        self._number_of_visits = 0
        self._results = {}
        self._results[1] = 0
        self._results[-1] = 0
        self._results[0] = 0
        self._untried_actions = None
        self._untried_actions = self.untried_actions()
        self.__simulator = Game([RandomAgent(), RandomAgent()])

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

        return {"agent name": "Mexichess",  # COMPLETE HERE
                "student name": ["Carlos Elias Rivera Mercado"],  # COMPLETE HERE
                "student number": ["102179473"]}  # COMPLETE HERE
    

    def untried_actions(self):
        if self.state is not None:
            self._untried_actions = self.state.applicable_moves()
            return self._untried_actions
        else: 
            return None
    def wins(self):
        return self._results[1]
    
    def num_visits(self):
        return self._number_of_visits
    def expansion(self):
        action = self._untried_actions.pop()
        newstate = self.state.clone()
        newstate.execute_move(action)
        child = Agent(newstate, parent=self, parent_action=action)
        self.children.append(child)
        #print(f'child: {child.state}')
        return child
    def is_final_node(self):
        #print(f'result of is_final_node: {self.state.is_winner() is not None}')
        return self.state.is_winner() is not None
    
    def rollout(self, current_state):
        #current_state = self.state
        #print(f'current_state: {current_state}')
        current_state = current_state.clone()
        #counter = 0
        while current_state.is_winner() is None:
            
            possible_moves = current_state.applicable_moves()
            action = self.rollout_decision(possible_moves)
            current_state.execute_move(action)
            self.__simulator.play(current_state)
            #print(f'current state result: {current_state.is_winner()}')
        self.reset_simulator()
        return current_state.is_winner()

    def reset_simulator(self):
        self.__simulator = Game([RandomAgent(), RandomAgent()])

    def get_legal_moves(self):
        return self.state.applicable_moves()

    
    def backpropagation(self, result):
        self._number_of_visits += 1
        self._results[result] += 1
        if self.parent:
            self.parent.backpropagation(result)

    

    def is_fully_expanded(self):
        return len(self._untried_actions) == 0
    
    def favoritechild(self):
        def handln(x):
            n = 1000000
            return n*((x**(1/n))-1)
        best_child = self.children[0]
        best_val = best_child.wins()/(best_child.num_visits() + 1e-16) + (2* handln(self.num_visits())/(best_child.num_visits() + 1e-16))**(0.5)
        for child in self.children:
            val = child.wins()/(child.num_visits() + 1e-16) + (2* handln(self.num_visits())/(child.num_visits() + 1e-16))**(0.5)
            if val > best_val:
                best_child = child
                best_val = val
        return best_child
    
    def rollout_decision(self, possible_moves):
        return random.choice(possible_moves)
    
    def _tree_policy(self):
        current_node = self
        while not current_node.is_final_node():
            if not current_node.is_fully_expanded():
                return current_node.expansion()
            else:
                print(f'I entered the else')
                current_node = current_node.favoritechild()
        return current_node

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
        #print(f'Al recibir el state: {state}')
        self.state = state
        self.untried_actions()
        #best_action, next_state = state.successors()[0]
        numsimulations = 50
        #while True:
        for _ in range(numsimulations):
            v = self._tree_policy()
            #print(f'result: {v.state}')
            reward = v.rollout(state)
            print(f'for current_state we have reward: {reward}')
            v.backpropagation(reward)

        yield self.favoritechild().parent_action
