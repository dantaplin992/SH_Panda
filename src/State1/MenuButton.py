from panda3d.core import *
from src.Font import Font

class MenuButton():
    def __init__(self, text, scale, pos):
        self.textObject = TextNode("button text")
        self.textObject.setFont(Font.lora_500())
        self.textObject.setText(text)
        self.textObject.setAlign(TextNode.ACenter)
        # self.textObject.setShadow(0.05, 0.05)
        # self.textObject.setShadowColor(0, 0, 0, 1)
        self.textNodePath = aspect2d.attachNewNode(self.textObject)
        self.textNodePath.setScale(scale)
        self.textNodePath.setPos(pos)

        self.textObject.setCardAsMargin(0.25, 0.25, 0.15, 0)
        self.textObject.setCardColor(0, 0, 0, 0)
    
    def select(self):
        self.textObject.setCardColor(0, 0, 1, 0.65)
        self.textObject.setCardDecal(True)
    
    def deselect(self):
        self.textObject.setCardColor(0, 0, 0, 0)
        self.textObject.setCardDecal(False)
        
    def destroy(self):
        self.textNodePath.removeNode()