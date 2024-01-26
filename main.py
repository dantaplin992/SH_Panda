from math import pi, sin, cos
import sys

from direct.showbase.ShowBase import ShowBase
from direct.task import Task

from src.State0.MovieState import MovieState
from src.State1.MenuState import MenuState
from src.State2.GameplayState import GameplayState

from panda3d.core import *
print("Panda version:", PandaSystem.getVersionString())

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # example of a task
        # self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        self.child = MenuState("State 0", self.render, self.taskMgr)
        self.child.path.reparentTo(self.render)

        base.disableMouse()
        base.camera.setPos(3, -20, 2)
        base.camera.lookAt(0, 0, 0)

        self.accept("space", self.printGraph)

        self.accept("stateChangeEvent", self.changeState)
        self.accept("quitEvent", self.quit)
        
    # KEEPING THIS AS AN EXAMPLE OF ROTATING THE CAMERA
    #
    # def spinCameraTask(self, task):
    #     angleDegrees = task.time * 6.0
    #     angleRadians = angleDegrees * (pi / 180.0)
    #     self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
    #     self.camera.setHpr(angleDegrees, 0, 0)
    #     return Task.cont
    
    def printGraph(self):
        print(self.render.ls())
        print(" ")
    
    def changeState(self, newState):
        self.child.destroy()

        stateOptions = {
            0: MovieState,
            1: MenuState,
            2: GameplayState
        }
        self.child = stateOptions[newState](f"State {newState}", self.render, self.taskMgr)
        self.child.path.reparentTo(self.render)
    
    def quit(self):
        self.child.destroy()
        self.ignoreAll()
        sys.exit()

def main():
    # TODO: figure out how to load from config.prc file
    configVars="""
    win-size 800 600
    # undecorated 1
    """
    loadPrcFileData("", configVars)

    app = MyApp()
    app.run()

if __name__ == "__main__":
    main()
