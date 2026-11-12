# import necessary dictionaries
#   moves might be redundant!!!!!!!!!!!!!!
from moveCube import cube, moves

# import necessary variables / definitions
#   might all be redundant!!!!!!!!!!!!!!!
from moveCube import whiteFace, yellowFace, blueFace, greenFace, redFace, orangeFace

# import necessary functions
#   some moveCube imports may be redundant!!!!!!!!!!!!!!!!
#   don't really use printCube anymore
#   don't use initFace, printFace, any xMoves, colorSquare
from moveCube import initCube, printCube, printFace, fMove, bMove, rMove, lMove, uMove, dMove, cubeMove, colorSquare, takeNextMove, printMoves
from cubeImager import createCubeImage

# init array to hold all moves
movesDone = []
# test print of cube
#printCube(cube)
createCubeImage(cube, "Python files/cubeImages/initialCube.png", movesDone)

# define string of test moves
testMoves = "R U F' U2 D R F"
testMoves2 = "B U' F D2 R2 L"
testMoves3 = "L' B2 U D' L2 R"

# test moves until 'testMoves' is empty
while testMoves:
    currentMove, testMoves = takeNextMove(testMoves)

    print("Executing move: " + currentMove)
    cubeMove(cube, currentMove)
    #printCube(cube)
    movesDone.append(currentMove)
    createCubeImage(cube, "Python files/cubeImages/cube" + str(len(movesDone)) + ".png", movesDone)
    printMoves(movesDone)

# clear movesDone and reset cube
movesDone = []
initCube(cube)
print("----------------------------------------------------------------------------------------------------\n"
      + "Resetting cube...\n"
      + "----------------------------------------------------------------------------------------------------")
#printCube(cube)

# #testMoves2
# while testMoves2:
#     currentMove, testMoves2 = takeNextMove(testMoves2)

#     print("Executing move: " + currentMove)
#     cubeMove(cube, currentMove)
#     printCube(cube)
#     movesDone.append(currentMove)
#     printMoves(movesDone)
    
# # clear movesDone and reset cube
# movesDone = []
# initCube(cube)
# print("----------------------------------------------------------------------------------------------------\n"
#       + "Resetting cube...\n"
#       + "----------------------------------------------------------------------------------------------------")
# printCube(cube)

# #testMoves3
# while testMoves3:
#     currentMove, testMoves3 = takeNextMove(testMoves3)

#     print("Executing move: " + currentMove)
#     cubeMove(cube, currentMove)
#     printCube(cube)
#     movesDone.append(currentMove)
#     printMoves(movesDone)