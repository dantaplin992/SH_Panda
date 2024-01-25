from panda3d.core import *
from direct.actor.Actor import Actor

from src.stateBase import StateBase
from src.State2.Player import Player
from src.Font import Font

class GameplayState(StateBase):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.paused = False

        self.textObject = TextNode("text node")
        self.textObject.setFont(Font.lora_500())
        self.textObject.setText("State 2")
        self.textObject.setAlign(TextNode.ACenter)
        self.textObject.setShadow(0.05, 0.05)
        self.textObject.setShadowColor(0, 0, 0, 1)
        self.textNodePath = aspect2d.attachNewNode(self.textObject)
        self.textNodePath.setScale(0.07)

        self.player = Player(self.render)

        self.accept("0", self.sendChangeStateEvent, [0])
        self.accept("1", self.sendChangeStateEvent, [1])

        self.accept("p", self.togglePause)
    
    def togglePause(self):
        if self.paused:
            self.resume()
            self.paused = False
        else:
            self.pause()
            self.paused = True

    def pause(self):
        self.player.pause()
    
    def resume(self):
        self.player.resume()
    
    def destroy(self):
        self.textNodePath.removeNode()
        self.player.destroy()
        super(self.__class__, self).destroy()
