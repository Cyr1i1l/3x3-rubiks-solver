import numpy as np
import matplotlib.pyplot as plt
    
# dictionary for colors to turn letters into
colorMap = {
    'R': [255, 0, 0],
    'G': [0, 255, 0],
    'B': [0, 0, 255],
    'Y': [255, 255, 0],
    'O': [255, 128, 0],
    'W': [255, 255, 255]
}

def createCubeImage(cube, filename, movesDone, show=True):

    # create a blank 9x12 array to hold the cube values
    image = np.full((9, 12), ' ', dtype='<U1')

    # arrange the six faces in the same layout as printCube()
    image[0:3, 3:6] = cube['U']

    image[3:6, 0:3] = cube['L']
    image[3:6, 3:6] = cube['F']
    image[3:6, 6:9] = cube['R']
    image[3:6, 9:12] = cube['B']

    image[6:9, 3:6] = cube['D']

    # convert letter array into RGB color array
    rgbImage = np.zeros((9, 12, 3))

    for row in range(9):
        for col in range(12):

            if image[row, col] == ' ':
                rgbImage[row, col] = [0.75, 0.75, 0.75]

            else:
                rgbImage[row, col] = np.array(colorMap[image[row, col]]) / 255
    

    plt.imshow(rgbImage) # displays RGB array as image
    plt.axis('off') # removes axis numbers
    
    # shows moves
    plt.text(0, 9, "Moves: " + " ".join(movesDone), fontsize=12)

    plt.savefig(filename) # saves image to filename

    if show:
        plt.show()  # shows image if it is open

    plt.close() # stops showing if image is closed