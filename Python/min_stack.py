class MinStack:

    def __init__(self):
        self.lis = []

    def push(self, val: int) -> None:
        self.lis.append(val)

    def pop(self) -> None:
        self.lis.pop()

    def top(self) -> int:
        return self.lis[-1]

    def getMin(self) -> int:
        return min(self.lis)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()