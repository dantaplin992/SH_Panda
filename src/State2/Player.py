from panda3d.core import *
from direct.actor.Actor import Actor

class Player():
    def __init__(self, render):
        self.name = "Player"

        self.animeActor = Actor("assets/models/multiAnim.bam")
        self.animeActor.reparentTo(render)
        self.capCtrl = self.animeActor.getAnimControl("Cap")
        self.animeActor.setPos(0, 1, 0)
        self.capCtrl.loop("Cap")

    def move(self):
        print("moving")
    
    def pause(self):
        self.animeActor.stop()
    
    def resume(self):
        self.animeActor.loop("Cap")

    def destroy(self):
        self.animeActor.cleanup()
        del self
