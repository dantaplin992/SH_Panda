from panda3d.core import *
from src.Font import Font

class MenuTitle():
    def __init__(self, text):
        self.textObject = TextNode("text node")
        self.textObject.setFont(Font.lora_500())
        self.textObject.setText(text)
        self.textObject.setAlign(TextNode.ACenter)
        # self.textObject.setShadow(0.05, 0.05)
        # self.textObject.setShadowColor(0, 0, 0, 1)
        self.textNodePath = aspect2d.attachNewNode(self.textObject)
        self.textNodePath.setScale(0.2)
        self.textNodePath.setPos(0, 0, 0.65)

    def confirm(self):
        print("MenuTitle exists")

    def destroy(self):
        self.textNodePath.removeNode()
