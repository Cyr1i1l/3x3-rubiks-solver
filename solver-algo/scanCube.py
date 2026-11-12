import cv2 as cv
import numpy as np
import cubeMove as cubeMove

rawImage = cv.imread('cube1.jpg')
image = cv.cvtColor(rawImage, cv.COLOR_BGR2HSV)


# THIS CODE WAS USED TO DETERMINE THE PIXEL LOCATIONS FOR THE EXAMPLE IMAGE
# THIS CODE WILL BE REUSED ONCE WE GET ACTUAL PI CAMERA IMAGES 
# def clickEvent(event, x, y, flags, params):
#     # Check if the left mouse button was clicked
#     if event == cv.EVENT_LBUTTONDOWN:
#         print(f"Clicked coordinate: ({x}, {y})")
#         # Draw a little circle where you clicked so you know it registered
#         cv.circle(image, (x, y), 5, (0, 255, 0), -1)
#         cv.imshow('Find Coordinates', image)

# cv.imshow('Find Coordinates', image)
# # Set the mouse callback function to capture clicks
# cv.setMouseCallback('Find Coordinates', clickEvent)

squareCorners = np.float32([
    [0, 0],         # top left
    [299, 0],       # top right
    [299, 299],     # bottom right
    [0,299]         # bottom left
])

orangeCorners = np.float32([
    [237, 138],
    [354, 202],
    [238, 286],
    [120, 203]
])

whiteCorners = np.float32([
    [120, 203],
    [236, 286],
    [238, 386],
    [143, 307]
])

blueCorners = np.float32([
    [239, 286],
    [352, 201],
    [331, 311],
    [239, 384]
])

def extractFace(cubeImage, faceCorners):
    transformation = cv.getPerspectiveTransform(faceCorners, squareCorners)
    transformedImg = cv.warpPerspective(cubeImage, transformation, (300, 300), flags=cv.INTER_NEAREST)

    return transformedImg

def detectColor(hsvPixel):
    h, s, v = hsvPixel
    if s < 65 and v > 70:   return 'W'
    if 5 <= h <= 22:        return 'O'
    if 100 <= h <= 135:     return 'B'
    if 25 <= h < 38:        return 'Y'
    if 38 <= h <= 75:       return 'G' 
    if h < 5 or h > 165:    return 'R'
    return '?'

def findFaceColors(faceImage, n=3, centerColor = None):
    height, width = faceImage.shape[:2]

    colorMatrix = np.full((n, n), '?',dtype='<U1')

    for i in range(n):
        for j in range(n):
            x = int((j + 0.5) * width/n)
            y = int((i + 0.5) * height/n)

            hsvPixel = faceImage[y, x]
            colorMatrix[i,j] = detectColor(hsvPixel)
            colorMatrix[1,1] = centerColor

            if colorMatrix[i, j] == '?':
                print(
                    f"Unknown at row {i + 1}, column {j + 1}: "
                    f"H={hsvPixel[0]}, S={hsvPixel[1]}, V={hsvPixel[2]}"
                    )
    return colorMatrix

#extract faces
orangeFace = extractFace(image, orangeCorners)
whiteFace = extractFace(image, whiteCorners)
blueFace = extractFace(image, blueCorners)

#display images in BGR
cv.imshow('Orange Face', cv.cvtColor(orangeFace, cv.COLOR_HSV2BGR))
cv.imshow('White Face', cv.cvtColor(whiteFace, cv.COLOR_HSV2BGR))
cv.imshow('Blue Face', cv.cvtColor(blueFace, cv.COLOR_HSV2BGR))

print("ORANGE FACE:")
orangeFaceMatrix = findFaceColors(orangeFace, centerColor='O')
print(orangeFaceMatrix)

print("WHITE FACE:")
whiteFaceMatrix = findFaceColors(whiteFace, centerColor='W')
print(whiteFaceMatrix)

print("BLUE FACE:")
blueFaceMatrix = findFaceColors(blueFace, centerColor='B')
print(blueFaceMatrix)

cv.imshow('Cube', rawImage)

cv.waitKey(0)
cv.destroyAllWindows()
