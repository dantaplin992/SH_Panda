from panda3d.core import *
from src.stateBase import StateBase

from src.Font import Font

class Node2(StateBase):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        child1 = NodePath('node_2_child_1')
        child1.reparentTo(self.path)
        child2 = NodePath('node_2_child_2')
        child2.reparentTo(self.path)

        self.textObject = TextNode("text node 1")
        self.textObject.setFont(Font.lora_500())
        self.textObject.setText("Node 2")
        self.textObject.setAlign(TextNode.ACenter)
        self.textObject.setShadow(0.05, 0.05)
        self.textObject.setShadowColor(0, 0, 0, 1)
        self.textNodePath = aspect2d.attachNewNode(self.textObject)
        self.textNodePath.setScale(0.07)

        self.accept("p", self.sendChangeStateEvent, [1])

        print("Node 2 created")
    
    def destroy(self):
        self.textNodePath.removeNode()
        super(self.__class__, self).destroy()
