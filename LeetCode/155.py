class StackNode:
    def __init__(self, val, minVal):
        self.val = val
        self.minVal = minVal

class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        self.minVal = min(val, self.minVal)
        newNode = StackNode(val, self.minVal)
        self.stack.append(newNode)

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.minVal = self.stack[-1].minVal
        else:
            self.minVal = float('inf')

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].minVal