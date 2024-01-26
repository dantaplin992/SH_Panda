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

        self.keyMap = {
            "up": False,
            "down": False,
            "left": False,
            "right": False
        }

        self.player = Player(self.render)

        self.accept("0", self.sendChangeStateEvent, [0])
        self.accept("1", self.sendChangeStateEvent, [1])

        self.addPlayerControls()

        self.accept("p", self.togglePause)

        self.taskMgr.add(self.update, "update")

        # EXAMPLE OF DOING A TASK AFTER A DELAY
        self.taskMgr.doMethodLater(3, self.delay, "delay")
    
    def delay(self, task):
        print("delay")
        return task.done

    def updateKeyMap(self, key, value):
        self.keyMap[key] = value
    
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
    
    def addPlayerControls(self):
        self.accept("w", self.updateKeyMap, ["up", True])
        self.accept("w-up", self.updateKeyMap, ["up", False])
        self.accept("s", self.updateKeyMap, ["down", True])
        self.accept("s-up", self.updateKeyMap, ["down", False])
        self.accept("a", self.updateKeyMap, ["left", True])
        self.accept("a-up", self.updateKeyMap, ["left", False])
        self.accept("d", self.updateKeyMap, ["right", True])
        self.accept("d-up", self.updateKeyMap, ["right", False])
    
    def update(self, task):
        dt = globalClock.getDt()
        if self.keyMap["up"]:
            self.player.moveForward()
        if self.keyMap["down"]:
            self.player.moveBackward()
        if self.keyMap["left"]:
            self.player.turn(100)
        if self.keyMap["right"]:
            self.player.turn(-100)

        return task.cont
    
    def destroy(self):
        self.textNodePath.removeNode()
        self.player.destroy()
        super(self.__class__, self).destroy()
