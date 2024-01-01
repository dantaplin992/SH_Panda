from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

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

        self.animeActor = Actor("assets/multiAnim.bam")
        # ctrl = self.animeActor.getAnimControl("Backwards")
        self.animeActor.setPos(0, 1, 0)
        self.animeActor.reparentTo(self.render)
        self.animeActor.loop("Cap")

        self.accept("a", self.printHello)
    
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
    
    def printHello(arg):
        print("Hello!")


app = MyApp()
app.run()
