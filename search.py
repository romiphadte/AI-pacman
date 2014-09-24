# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import sys
import copy
import pdb 

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.

    You are not required to implement this, but you may find it useful for Q5.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def iterativeDeepeningSearch(problem):
    """
    Perform DFS with increasingly larger depth.

    Begin with a depth of 1 and increment depth by 1 at every step.
    """
    "*** YOUR CODE HERE ***"
    for i in range(0, 500):
        actions = depthFirstSearchToDepth(problem, i)
        if actions:
            return actions

def depthFirstSearchToDepth(problem, depth):
    frontier = []
    paths = {}
    explored = []
    frontier.append(problem.getStartState())
    while (len(frontier) > 0):
        s = frontier.pop()
        if s is not problem.getStartState():
            if s in paths.keys():
                paths[s].append(s[1])
            else:
                paths[s] = [s[1]]
        if problem.isGoalState(s[0]):
            return paths[s]
        if (s in paths.keys() and len(paths[s]) == depth) or depth == 0:
            continue;
        if len(s) == 3:
            explored.append(s[0])
            successors = problem.getSuccessors(s[0])
        else:
            explored.append(s)
            successors = problem.getSuccessors(s)
        if depth > 0:
            for successor in successors:
                if successor[0] not in explored and not stackContainsNode(frontier, successor):
                    frontier.append(successor)
                    if s in paths.keys():
                        paths[successor] = list(paths[s])

def stackContainsNode(stack, node):
    for n in stack:
        if n[0] == node[0]:
            return True
    return False

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    frontier.push(problem.getStartState(), heuristic(problem.getStartState(), problem))
    explored = []
    paths = {}
    totalCost = {}
    paths[problem.getStartState()]=list()
    totalCost[problem.getStartState()]=0

    def isBestCostforState(cost,state):
        for n in frontier.heap:
            if n[2] == state:
                if (n[2] in totalCost.keys()) and (totalCost[n[2]]> cost):
                    frontier.heap.remove(n)
                    return True
                else:
                    return False
        return True

    while not frontier.isEmpty():
        s = frontier.pop()
        if problem.isGoalState(s):
            return paths[s]
        explored.append(s)
        successors = problem.getSuccessors(s)
        for successor in successors:
            successorState=successor[0]
            move=successor[1]
            cost=successor[2]
            if (successorState not in explored and isBestCostforState(totalCost[s]+cost,successorState)):
                paths[successorState] = list(paths[s]) + [move]
                totalCost[successorState] = totalCost[s] + cost 
                frontier.push(successorState, heuristic(successorState, problem) + totalCost[successorState])
    return []
    
# Abbreviations
bfs = breadthFirstSearch
astar = aStarSearch
ids = iterativeDeepeningSearch
