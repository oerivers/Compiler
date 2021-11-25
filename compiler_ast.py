import operator
from types import LambdaType

class InstructionList:
    def __init__(self, children=None):
        if children is None:
            children = []
        self.children = children
