class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack:
            minimum = val
        else:
            minimum = min(val, self.minStack[-1])

        self.minStack.append(minimum)


    def pop(self) -> None:
        self.minStack.pop()
        return self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
