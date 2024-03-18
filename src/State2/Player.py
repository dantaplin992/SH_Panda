from panda3d.core import *
from direct.actor.Actor import Actor

class Player():
    def __init__(self, render):
        self.name = "Player"

        self.walkSpeed = 5

        # self.animeActor = Actor("assets/models/gits.bam")
        self.animeActor = Actor("assets/models/multiAnim.bam")
        self.animeActor.reparentTo(render)
        self.capCtrl = self.animeActor.getAnimControl("Cap")
        self.animeActor.setPos(0, 1, 0)
        # self.capCtrl.loop("Cap")

    def moveForward(self):
        dt = globalClock.getDt()
        self.animeActor.setY(self.animeActor, self.walkSpeed * dt)
    
    def moveBackward(self):
        dt = globalClock.getDt()
        self.animeActor.setY(self.animeActor, -self.walkSpeed * dt)
    
    def turn(self, angle):
        dt = globalClock.getDt()
        self.animeActor.setH(self.animeActor, angle * dt)
    
    def pause(self):
        self.animeActor.stop()
    
    def resume(self):
        self.animeActor.loop("Cap")

    def destroy(self):
        self.animeActor.cleanup()
        del self
