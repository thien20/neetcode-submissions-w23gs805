class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val: int) -> None:
        # push element in that stack -> save min
        self.stack.append(val)
        min_val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(min_val)


    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

