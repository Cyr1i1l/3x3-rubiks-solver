import numpy as np

n=3

whiteFace = np.full((n, n), 'W',dtype='<U1') #down
redFace = np.full((n, n), 'R',dtype='<U1') #front
greenFace = np.full((n, n), 'G',dtype='<U1') #right
orangeFace = np.full((n, n), 'O',dtype='<U1') #back
blueFace = np.full((n, n), 'B',dtype='<U1') #left
yellowFace = np.full((n, n), 'Y',dtype='<U1') #up

# resets cube
def initCube(cube):
    n=3
    cube['U'] = np.full((n, n), 'Y',dtype='<U1') #up
    cube['D'] = np.full((n, n), 'W',dtype='<U1') #down
    cube['F'] = np.full((n, n), 'R',dtype='<U1') #front
    cube['B'] = np.full((n, n), 'O',dtype='<U1') #back
    cube['R'] = np.full((n, n), 'G',dtype='<U1') #right
    cube['L'] = np.full((n, n), 'B',dtype='<U1') #left

#create cube dictionary
cube = {
    'U': yellowFace,
    'D': whiteFace,
    'F': redFace,
    'B': orangeFace,
    'R': greenFace,
    'L': blueFace
}

# updated with colorSquare
def printFace(face):
    
    print("              |",colorSquare(face[0][0]),colorSquare(face[0][1]),colorSquare(face[0][2]),"|")
    print("              |",colorSquare(face[1][0]),colorSquare(face[1][1]),colorSquare(face[1][2]),"|")
    print("              |",colorSquare(face[2][0]),colorSquare(face[2][1]),colorSquare(face[2][2]),"|")

# updated with colorSquare
def printCube(cube):  
    print("              ---------------")
    printFace(cube['U'])
    print("---------------------------------------------------------")
    for i in range(n):
        print(
        "|", *[colorSquare(c) for c in cube['L'][i]],
        "|", *[colorSquare(c) for c in cube['F'][i]],
        "|", *[colorSquare(c) for c in cube['R'][i]],
        "|", *[colorSquare(c) for c in cube['B'][i]], "|"
    )
    print("---------------------------------------------------------")    
    printFace(cube['D'])
    print("              ---------------")
    

#cube move functions
def fMove(cube):
    cube['F'] = np.rot90(cube['F'], -1).copy()

    u = cube['U'][2,:].copy()
    r = cube['R'][:,0].copy()
    d = cube['D'][0,:].copy()
    l = cube['L'][:,2].copy()

    cube['U'][2,:] = l[::-1]
    cube['R'][:,0] = u
    cube['D'][0,:] = r[::-1]
    cube['L'][:,2] = d
    

def bMove(cube):
    cube['B'] = np.rot90(cube['B'], -1).copy()

    u = cube['U'][0,:].copy()
    r = cube['R'][:,2].copy()
    d = cube['D'][2,:].copy()
    l = cube['L'][:,0].copy()

    cube['U'][0,:] = r
    cube['R'][:,2] = d[::-1]
    cube['D'][2,:] = l
    cube['L'][:,0] = u[::-1]
    

def rMove(cube):
    cube['R'] = np.rot90(cube['R'], -1).copy()

    u = cube['U'][:,2].copy()
    b = cube['B'][:,0].copy()
    d = cube['D'][:,2].copy()
    f = cube['F'][:,2].copy()

    cube['U'][:,2] = f
    cube['B'][:,0] = u[::-1]  
    cube['D'][:,2] = b[::-1]
    cube['F'][:,2] = d 

def lMove(cube):
    cube['L'] = np.rot90(cube['L'], -1).copy()

    u = cube['U'][:,0].copy()
    b = cube['B'][:,2].copy()
    d = cube['D'][:,0].copy()
    f = cube['F'][:,0].copy()

    cube['U'][:,0] = b[::-1]
    cube['B'][:,2] = d[::-1]
    cube['D'][:,0] = f
    cube['F'][:,0] = u
    
def uMove(cube):
    cube['U'] = np.rot90(cube['U'], -1).copy()

    f = cube['F'][0,:].copy()
    l = cube['L'][0,:].copy()
    b = cube['B'][0,:].copy()
    r = cube['R'][0,:].copy()

    cube['F'][0,:] = r
    cube['L'][0,:] = f
    cube['B'][0,:] = l
    cube['R'][0,:] = b

def dMove(cube):
    cube['D'] = np.rot90(cube['D'], -1).copy()

    f = cube['F'][2,:].copy()
    l = cube['L'][2,:].copy()
    b = cube['B'][2,:].copy()
    r = cube['R'][2,:].copy()

    cube['F'][2,:] = l
    cube['L'][2,:] = b
    cube['B'][2,:] = r
    cube['R'][2,:] = f


#end cube move functions

#create dictionary for moves in the correct notation

moves = {
    "F":  (fMove, 1),
    "F'": (fMove, 3),
    "F2": (fMove, 2),

    "B":  (bMove, 1),
    "B'": (bMove, 3),
    "B2": (bMove, 2),

    "R":  (rMove, 1),
    "R'": (rMove, 3),
    "R2": (rMove, 2),

    "L":  (lMove, 1),
    "L'": (lMove, 3),
    "L2": (lMove, 2),

    "U":  (uMove, 1),
    "U'": (uMove, 3),
    "U2": (uMove, 2),

    "D":  (dMove, 1),
    "D'": (dMove, 3),
    "D2": (dMove, 2)
}

def cubeMove(cube, move):
    if move not in moves:
        raise ValueError(f"Unknown move: {move}")

    moveFunction, turns = moves[move]

    for i in range(turns):
        moveFunction(cube)

# function to translate letters in face to colors

def colorSquare(color):
    colors = {
        'Y': '\033[43m   \033[0m',  # Yellow
        'G': '\033[42m   \033[0m',  # Green
        'B': '\033[44m   \033[0m',  # Blue
        'R': '\033[41m   \033[0m',  # Red
        'O': '\033[48;5;208m   \033[0m',  # Orange
        'W': '\033[47m   \033[0m'   # White
    }

    return colors[color]

# extract next move from a string of moves separated by spaces
def takeNextMove(moveString):
    moveString = moveString.strip() # split moveString by spaces

    if ' ' in moveString:   # if still more than 1 move
        result = moveString[:moveString.find(' ')]  # extract move
        moveString = moveString[moveString.find(' ') + 1:]  # remove extracted move from moveString
    else:                   # if only 1 move left
        result = moveString # moveString is last move only
        moveString = "" # empty moveString

    return result, moveString

# function to print all variables of the array of moves done by the solver
def printMoves(moveArray):
    print("Moves executed: ")
    for i in moveArray:
        print(i + " ", end="")
    print("")   # print newline
    
# -------------------------------------------------------------------------------------------------------------
# test print of cube
printCube(cube)

# define string of test moves
testMoves = "R U F' U2 D R F"
testMoves2 = "B U' F D2 R2 L"
testMoves3 = "L' B2 U D' L2 R"

# init array to hold all moves
movesDone = []

# test moves until 'testMoves' is empty
while testMoves:
    currentMove, testMoves = takeNextMove(testMoves)

    print("Executing move: " + currentMove)
    cubeMove(cube, currentMove)
    printCube(cube)
    movesDone.append(currentMove)
    printMoves(movesDone)

# clear movesDone and reset cube
movesDone = []
initCube(cube)
print("----------------------------------------------------------------------------------------------------\n"
      + "Resetting cube...\n"
      + "----------------------------------------------------------------------------------------------------")
printCube(cube)

#testMoves2
while testMoves2:
    currentMove, testMoves2 = takeNextMove(testMoves2)

    print("Executing move: " + currentMove)
    cubeMove(cube, currentMove)
    printCube(cube)
    movesDone.append(currentMove)
    printMoves(movesDone)
    
# clear movesDone and reset cube
movesDone = []
initCube(cube)
print("----------------------------------------------------------------------------------------------------\n"
      + "Resetting cube...\n"
      + "----------------------------------------------------------------------------------------------------")
printCube(cube)

#testMoves3
while testMoves3:
    currentMove, testMoves3 = takeNextMove(testMoves3)

    print("Executing move: " + currentMove)
    cubeMove(cube, currentMove)
    printCube(cube)
    movesDone.append(currentMove)
    printMoves(movesDone)
