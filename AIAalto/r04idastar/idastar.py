
import random
from math import inf
from action import Action

### Iterative Deepening A* -- IDA*

totalcalls = 0
        
def IDAstar(s0,goaltest,h):
    global totalcalls
    bound = h(s0)
    totalcalls = 0
    while True:
        print("Calling doDFS with bound " + str(bound))
        t = doDFS(s0,0,bound,goaltest,h,[s0])
        if t==None:
            print("TIMEOUT")
            return None
        if isinstance(t,list):
            print("SOLVED (" + str(totalcalls) + " recursive calls)")
            return t
        if t == float('inf'):
            print("NOT SOLVABLE")
            return None
        bound = t

# The main subprocedure of IDA*, performing DFS up to a given
# bound.
# doDFS returns
#   None                if spent too much time
#   a list of actions   if a shortest path to goal states was found
#   a number            for the next bound otherwise
#
# The arguments are
#    s        The state to search
#    g        The g-value of 's'
#    bound    The threshold to cut off the DFS search
#    goaltest Function to test if 's' is a goal state
#    h        The function for computing the h-value of 's'
#    path     List of all states encountered in the current
#             branch. Test successors s2 of s with "s2 in path"
#             to see if the path would have a cycle (and then
#             ignore that kind of s2.)



def doDFS(s,g,bound,goaltest,h,path):
    global totalcalls
    
    totalcalls = totalcalls + 1
    if totalcalls > 10000000:
        return None
    fvalue = g + h(s)
    if fvalue > bound:
        return fvalue
    # esta resuelto
    if goaltest(s):
        return []
    
    min = inf
    for action,state in s.successors():
        # esto es como si tomara esa accion
        if not state in path:
            path.append(state)
            fprime = doDFS(state, g + action.cost, bound, goaltest, h, path)
            # esto significa que lo resolvió
            if isinstance(fprime, list):
                fprime.insert(0,action)
                return fprime
            if fprime is None:
                return None
            if fprime < min:
                min = fprime
            

            path.remove(state)

    return min

