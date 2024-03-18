import time
from typing import List, Optional
from copy import deepcopy
from random import choice

from agent_interface import AgentInterface
from envs.environment import AbstractState
from time_limit import time_limit

import chess

# Run a game: alternate between players, asking for a sequence of
# increasingly good next moves from each player, until the per-player
# time limit is reached.


class Game:
    def __init__(self, players: List[AgentInterface]):
        self.__players = players

    def play(self,
             starting_state: AbstractState,
             output=False,
             timeout_per_turn=[None, None]):
        winners = self.__play(starting_state,
                              output,
                              timeout_per_turn)
        if output:
            print("Game is over!")
            if len(winners) != 1:
                print("The game ended in a draw!")
            else:
                if winners[0] == 0:
                    s = "White"
                else:
                    s = "Black"
                print(f"Player {s}, {self.__players[winners[0]]} WON!")
        return winners

    def __play(self, state: AbstractState, output, timeout_per_turn):
        duration = None
        if(output): print("Starting game!\n")
        MOVES = 0
        while True:
            is_winner = state.is_winner()
            if is_winner is not None:
                if(output): print("Game ends after " + str(MOVES) + " moves\n")
                if state.stalemate():
                    if(output): print("Stalemate!")
                    return []
                if state.checkmate():
                    if(output): print("Player " + str(state.current_player()) + " lost: checkmate!")
                    return [1 - state.current_player()]
            if MOVES > 100:
                if(output): print("Played 100 moves without a winner. Terminate.\n")
                return []
            moves = state.applicable_moves()
            if output:
                if state.current_player() == 0:
                    print("Player: WHITE")
                else:
                    print("Player: BLACK")
            if output: print("Possible moves:", len(moves))
            start_time = time.time()
            action = self.__get_action(self.__players[state.current_player()],
                                       state,
                                       timeout_per_turn[state.current_player()])
            duration = time.time() - start_time
            if action is None or action not in moves:
                if action is None:
                    if(output): print ("Time out!")
                else:
                    if(output): print("Illegal move!")
                if(output): print("Choosing a random action!")
                if len(moves) > 0:
                    action = choice(moves)
                else:
                    if(output): print("No actions to choose from!\n")
                    return [1 - state.current_player()]
            state.execute_move(action)
            if output:
                print(f"Decision time: {duration:0.3f}")
                print("Move:", action)
                print("===================================================")
                print(state)
            MOVES += 1

    def __get_action(self, player: AgentInterface, state, timeout):
        action = None
        try:
            with time_limit(timeout):
                for decision in player.decide(state.clone()):
                    action = decision
        except TimeoutError:
            pass
        # NOTE: The following lines will be uncommented during tournament
        except Exception as e:
            print("Got an EXCEPTION:", e)
            print()
            import traceback
            traceback.print_exc()
        return action
