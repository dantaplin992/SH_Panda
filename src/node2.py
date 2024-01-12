from panda3d.core import NodePath
from src.stateBase import StateBase

class Node2(StateBase):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        child1 = NodePath('node_2_child_1')
        child1.reparentTo(self.path)
        child2 = NodePath('node_2_child_2')
        child2.reparentTo(self.path)

        self.accept("p", self.sendChangeStateEvent, [1])

        print("Node 2 created")
