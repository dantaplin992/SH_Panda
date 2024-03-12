from panda3d.core import NodePath
from direct.showbase import *

class StateBase(DirectObject.DirectObject):
    def __init__(self, name, render, taskMgr):
        self.name = name
        self.path = NodePath(self.name)
        self.render = render
        self.taskMgr = taskMgr

        # WARN: need to remove this - for debugging only
        self.accept("a", self.confirm)
    
    def destroy(self):
        self.ignoreAll()
        self.path.removeNode()
        del self
    
    def sendChangeStateEvent(self, newState):
        messenger.send("stateChangeEvent", [newState])
    
    # WARN: need to remove this - for debugging only
    def confirm(self):
        print(f"{self.name} still exists")

