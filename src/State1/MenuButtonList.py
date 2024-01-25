from direct.showbase import *
from src.State1.MenuButton import MenuButton

class MenuButtonList(DirectObject.DirectObject):
    def __init__(self):
        self.buttonList = []
        self.buttonList.append(MenuButton("Start", 0.1, (0, 0, 0.1)))
        self.buttonList.append(MenuButton("Quit", 0.1, (0, 0, -0.1)))

        self.selectedButton = 0
        self.accept("arrow_down", self.selectNext)
        self.accept("arrow_up", self.selectPrevious)

        self.accept("enter", self.buttonAction)

        self.buttonList[self.selectedButton].select()
    
    def selectNext(self):
        self.buttonList[self.selectedButton].deselect()
        self.selectedButton += 1
        if self.selectedButton >= len(self.buttonList):
            self.selectedButton = 0
        self.buttonList[self.selectedButton].select()
    
    def selectPrevious(self):
        self.buttonList[self.selectedButton].deselect()
        self.selectedButton -= 1
        if self.selectedButton < 0:
            self.selectedButton = len(self.buttonList) - 1
        self.buttonList[self.selectedButton].select()

    def sendStartEvent(self):
        messenger.send("stateChangeEvent", [2])

    def sendQuitEvent(self):
        messenger.send("quitEvent")
    
    def buttonAction(self):
        options = {
            0: self.sendStartEvent,
            1: self.sendQuitEvent
        }
        options[self.selectedButton]()
        
        self.destroy()
    
    def destroy(self):
        self.ignoreAll()
        for button in self.buttonList:
            button.destroy()
        self.buttonList = []

        