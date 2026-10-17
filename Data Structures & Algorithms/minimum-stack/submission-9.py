class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        # two stacks
        self.stack.append(val)

        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        # just pop the top
        popped = self.stack.pop()
        
        self.minStack.pop()

    def top(self) -> int:
        # just peek the top stack[0]
        return self.stack[-1]

    def getMin(self) -> int:
        
        return self.minStack[-1]
