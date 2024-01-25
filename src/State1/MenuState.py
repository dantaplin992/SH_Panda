from panda3d.core import *
from src.stateBase import StateBase
from src.State1.MenuTitle import MenuTitle
from src.State1.MenuButtonList import MenuButtonList

class MenuState(StateBase):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.title = MenuTitle("Main Menu")
        self.buttonList = MenuButtonList()
    
    def destroy(self):
        self.title.destroy()
        super(self.__class__, self).destroy()
