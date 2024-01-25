from panda3d.core import *
from src.stateBase import StateBase
from src.Font import Font

class MovieState(StateBase):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.textObject = TextNode("text node")
        self.textObject.setFont(Font.lora_500())
        self.textObject.setText("State 0")
        self.textObject.setAlign(TextNode.ACenter)
        self.textObject.setShadow(0.05, 0.05)
        self.textObject.setShadowColor(0, 0, 0, 1)
        self.textNodePath = aspect2d.attachNewNode(self.textObject)
        self.textNodePath.setScale(0.07)

        self.accept("1", self.sendChangeStateEvent, [1])
        self.accept("2", self.sendChangeStateEvent, [2])
    
    def destroy(self):
        self.textNodePath.removeNode()
        super(self.__class__, self).destroy()
