#!/usr/bin/python3
## instructions:

# This exercise is about transition system models that are central in many parts of AI and also common in other areas of computer science, including computer-aided verification and validation.

# A basic transition system model consists of

# a set of states, and

# a transition relation that associates with each state zero or more successor states.

# This type of model could be viewed as a directed graph, with the states coinciding with the nodes of the graph, and the elements of the transition relation corresponding to the (directed) arcs of the graph.

# More advanced transition system models could associate probabilities between the difference successor state of a state, or have multiple transition relations, each corresponding to a different action possible for the decision-maker, with each action associating alternative successor states for each state.

# In this exercise, we formalize the movements of the Pac-Man character from the 1980 video game. The states of the transition system represent the different locations in the maze Pac-Man moves in as well as the direction it is currently moving. The following rules govern Pac-Man’s movement.

# If there is an empty grid cell in the direction of movement, then Pac-Man can move to that cell.

# If there is an empty grid cell to the left of the current location (considering the current direction of movement), then Pac-Man can move to that cell and change the direction of movement 90 degrees to the left.

# Turning right is similarly possible.

# If no movement forward, left or right is possible, then Pac-Man moves one step backward and turns 180 degrees to the direction it came from.

# Your task is to implement this Pac-Man behavior in the code template, and to test that it works with the given code. The code allows you to find all states that are reachable from a given initial state, as well as to find shortest paths between given two states. This path would tell you how to reach a given goal from a given starting state, representing a simple form of sequential decision-making, where a sequence of decision about the next actions has to be taken to satisfy a given objective.

# NOTE: It is recommended to only add the missing code
# in places marked with comments ###
#
# NOTE 2: Do not change the name of the class or the methods, as
# the automated grader relies on the names.

import time
import queue

# Creating a grid for the Pac-Man to wander around.
# The grid is given as a list of string, e.g.
# [".......",
#  ".XXX.X.",
#  ".XXX...",
#  ".XXX.X.",
#  ".....X.",
#  ".XXXXX.",
#  "......."]
# Here the important information is the size of the grid,
# in Y direction the number of string, and in the X direction
# the length of the strings, and whether there is X in
# a grid cell. Pac-Man can enter any cell that is not a wall
# cell marked with X.
# The bottom left cell is (0,0). Cells outside the explicitly
# stated grid are all wall cells.

class PacManGrid:
    def __init__(self,grid):
        self.grid = grid
        self.xmax = len(grid[0]) - 1
        self.ymax = len(grid) - 1

    # Test whether the cell (x,y) is wall.

    def occupied(self,x,y):
        if x < 0 or y < 0 or x > self.xmax or y > self.ymax:
            return True
        s = self.grid[self.ymax-y]
        return (s[x] == 'X')

# State space search problems are represented in terms of states.
# For each state there are a number of actions that are applicable in
# that state. Any of the applicable actions will produce a successor
# state for the state. To use a state space in search algorithms, we
# also need functions for producing a hash value for a state
# (the function hash) and for testing equality of two states.
#
# In this exercise we represent states as Python classes with the
# following components.
#
#   __init__    To create a state (a starting state for search)
#   __repr__    To construct a string that represents the state
#   __hash__    Hash function for states
#   __eq__      Equality for states
#   successors  Returns a list [(a1,s1),...,(aN,sN)] where each si
#               is the successor state when action ai is taken.
#               Here the name ai of an action is a string.

# The state of the Pac-Man (given a grid) consists of
# three components:
# x: the X coordinate 0..self.grid.xmax
# y: the Y coordinate 0..self.grid.ymax
# d: the direction "N", "S", "E", "W" Pac-Man is going
# Based on this information, the possible successor states
# of (x,y,d) are computed by 'successors'.

class PacManState:

    # Creating a state:
    
    def __init__(self,x,y,direction,grid):
        self.x = x
        self.y = y
        self.d = direction
        self.grid = grid

    # Construct a string representing a state.

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + self.d + ")"

    # The hash function for states, mapping each state to an integer

    def __hash__(self):
        return self.x+(self.grid.xmax+1)*self.y

    # Equality for states

    def __eq__(self,other):
        return (self.x == other.x) and  (self.y == other.y) and  (self.d == other.d)

    



    # All successor states of a state

    def successors(self):
### Implement this function (mine is 67 lines, w/ 4 aux functions)
### You can come up with your own names for the different moves
# l, r, f, b
        # a lo más resp tiene 3
        # caso extremo solo tiene 1 que es ir en la dirección contraria
        resp = []
        map = {"N": "W",
               "W": "S", 
               "S": "E", 
               "E": "N"}
        # las acciones en todos los casos son f, l, r
        # b

        def goNorth():
            resp.append(("f", PacManState(self.x, self.y + 1, "N", self.grid)))
        
        def goSouth():
            resp.append(("b", PacManState(self.x, self.y - 1, "S", self.grid)))

        def goEast():
            resp.append(("r", PacManState(self.x + 1, self.y, "E", self.grid)))
        
        def goWest():
            resp.append(("l", PacManState(self.x - 1, self.y, "W", self.grid)))



        # caso para N
        # si estoy yendo N entonces debería intentar N, W, E
        # si ninguno de esos se puede entonces voy S
        if self.d == "N": 
            # intentar N
            if not self.grid.occupied(self.x, self.y + 1): 
                goNorth() 
            # intentar W
            if not self.grid.occupied(self.x - 1, self.y):
                goWest()
            # intentar E
            if not self.grid.occupied(self.x + 1, self.y):
                goEast()
            # este es el caso extremo
            #if len(resp) < 1: 
            if not self.grid.occupied(self.x, self.y - 1):
                goSouth()

            return resp
        
        # caso para S
        # si estoy yendo S entonces debería intentar S, E, W
        # si ninguno de esos se puede entonces voy N
        if self.d == "S": 
            # intentar S
            if not self.grid.occupied(self.x, self.y - 1):
                goSouth()
            # intentar E
            if not self.grid.occupied(self.x + 1, self.y):
                goEast()
            # intentar W
            if not self.grid.occupied(self.x - 1, self.y):
                goWest()
            # este es el caso extremo
            #if len(resp) < 1: 
            if not self.grid.occupied(self.x, self.y + 1):
                goNorth()

            return resp

        # caso para E
        # si estoy yendo S entonces debería intentar E, N, S
        # si ninguno de esos se puede entonces voy W

        if self.d == "E": 
            # intentar E
            if not self.grid.occupied(self.x + 1, self.y):
                goEast()
            # intentar N
            if not self.grid.occupied(self.x, self.y + 1): 
                goNorth()
            # intentar S
            if not self.grid.occupied(self.x, self.y - 1):
                goSouth()
            # este es el caso extremo
            #if len(resp) < 1: 
            if not self.grid.occupied(self.x - 1, self.y): 
                goWest()

            return resp
        
        # caso para W
        # si estoy yendo S entonces debería intentar W, S, N
        # si ninguno de esos se puede entonces voy E

        if self.d == "W": 
            # intentar W
            if not self.grid.occupied(self.x - 1, self.y):
                goWest()
            # intentar S
            if not self.grid.occupied(self.x, self.y - 1):
                goSouth()
            # intentar N
            if not self.grid.occupied(self.x, self.y + 1): 
                goNorth()
            # este es el caso extremo
            #if len(resp) < 1: 
            if not self.grid.occupied(self.x + 1, self.y):
                goEast()

            return resp
    
    