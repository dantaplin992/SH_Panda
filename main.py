from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task

from src.node1 import Node1
from src.node2 import Node2

from panda3d.core import PandaSystem
print("Panda version:", PandaSystem.getVersionString())

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        # self.scene = self.loader.loadModel("models/environment")
        # self.scene.reparentTo(self.render)
        # self.scene.setScale(0.25, 0.25, 0.25)
        # self.scene.setPos(-8, 42, 0)

        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        self.child = Node1("NEW NODE", self.render)
        self.child.path.reparentTo(self.render)

        self.accept("space", self.printGraph)

        self.accept("stateChangeEvent", self.changeState)
        
    
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
    
    def printGraph(self):
        print(self.render.ls())
        print(" ")
    
    def changeState(self, newState):
        self.child.destroy()

        if newState == 1:
            self.child = Node1("NEW NODE", self.render)
        elif newState == 2:
            self.child = Node2("NODE 2", self.render)
        
        self.child.path.reparentTo(self.render)

def main():
    app = MyApp()
    app.run()

if __name__ == "__main__":
    main()
