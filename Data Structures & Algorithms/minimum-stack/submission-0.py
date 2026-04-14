class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # push element in that stack -> save min
        self.stack.append(val)

    def pop(self) -> None:
        # pop that out -> if not min --> hold min --> else --> min = next
        if not self.stack:
            return
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min_val = float('inf')
        back_up = []
        while self.stack:
            temp = self.stack.pop()
            back_up.append(temp)
            min_val = min(temp, min_val)

        while back_up:
            self.stack.append(back_up.pop())
        return min_val

