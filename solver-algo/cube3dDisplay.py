# import for this file
#------------------------------------------
import panda3d.core
from direct.showbase.ShowBase import ShowBase
#------------------------------------------

# import cubeTester.py things
#------------------------------------------
# import necessary dictionaries
from moveCube import cube

# import necessary variables / definitions

# import necessary functions
from moveCube import initCube, cubeMove, takeNextMove
from cubeImager import createCubeImage
#------------------------------------------

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # create cube with a model (already has uv data in the obj file)
        self.cube = self.loader.loadModel("../blenderFiles/test cube.obj")
        self.cube.reparentTo(self.render)
        self.cube.setScale(1, 1, 1)
        self.cube.setPos(0, 10, 0)
        
        # start texture update loop
        self.startUpdates()

    # non-task to begin the texture update loop
    def startUpdates(self):
        
        # register event handler
        self.accept("updateTexture", self.updateTexture)
        self.accept("makeMove", self.makeMove)
        
        # apply initial texture
        self.updateTexture()
            
    # non-task (requires event handler) to update cube texture
    def updateTexture(self):
        # make a panda3d image
        test_img = panda3d.core.PNMImage()
        test_img.read("cubeImages/currentCube.png")
        
        texture = panda3d.core.Texture("cubeTexture")
        # load texture
        texture.load(test_img)
        #texture.setCullMode(0)
        # apply texture to cube
        self.cube.set_texture(texture)
    
    # non-task (requires event handler) to initialize moves and start executing them
    def makeMove(self):
        # init array to hold all moves
        self.movesDone = []
        # init texture path
        self.texture_path = "cubeImages/currentCube.png"
        # make initial image
        createCubeImage(cube, self.texture_path, self.movesDone)
        # apply new texture
        app.messenger.send("updateTexture")

        # define string of test moves
        self.testMoves = "R U F' U2 D R F"
        
        # begin executing moves
        self.taskMgr.doMethodLater(1, self.executeMove, "executeMove")
    
    # task to perform moves from testMoves until it is empty with 1 second apart from each
    def executeMove(self, task):
        
        # perform move if textMoves is not empty
        if self.testMoves:
            # grab next move
            currentMove, self.testMoves = takeNextMove(self.testMoves)
            # perform next move
            print("Executing move: " + currentMove)
            cubeMove(cube, currentMove)
            # add move to memory
            self.movesDone.append(currentMove)
            # create new texture
            createCubeImage(cube, self.texture_path, self.movesDone)
            # apply new texture
            app.messenger.send("updateTexture")
            # execute next move after 1 second
            return task.again

        # wait another second
        self.taskMgr.doMethodLater(1, self.resetCube, "resetCube")
        
        return task.done

    # task to initialize cube
    def resetCube(self, task):
        # clear movesDone
        self.movesDone = []
        # reset cube
        print("----------------------------------------------------------------------------------------------------\n"
            + "Resetting cube...\n"
            + "----------------------------------------------------------------------------------------------------")
        initCube(cube)
        # create new texture
        createCubeImage(cube, self.texture_path, self.movesDone)
        # apply new texture
        app.messenger.send("updateTexture")
        
        return task.done

# create the app
app = App()
# start the makeMove function
app.messenger.send("makeMove")
# open the app
app.run()
