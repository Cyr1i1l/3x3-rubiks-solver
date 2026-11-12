import numpy as np
#from moveCube import movesDone

solveHistory = []

def printSolveCount():
    print("Amount of solves performed: " + len(solveHistory))

def printSolve(solveIndex):
    print("Solve #" + solveIndex + ": " + solveHistory[solveIndex+1])


# print(solveHistory)

# testMoves = ["R", "D", "F", "U2", "F'"]
# solveHistory.append(testMoves)
# print(solveHistory)

# testMoves = ["R'", "D2", "F'", "U", "F2"]
# solveHistory.append(testMoves)
# print(solveHistory)


