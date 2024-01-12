from panda3d.core import NodePath
from direct.showbase import *

class StateBase(DirectObject.DirectObject):
    def __init__(self, name):
        self.name = name
        self.path = NodePath(self.name)
        self.accept("a", self.confirm)
    
    def destroy(self):
        self.ignoreAll()
        self.path.removeNode()
        del self
    
    def sendChangeStateEvent(self, newState):
        messenger.send("stateChangeEvent", [newState])
    
    def confirm(self):
        print(f"{self.name} still exists")
