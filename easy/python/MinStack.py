"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""


class MinStack(object):
    def __init__(self):
        self.min = 0xFFFFFFFF
        self.s = []

    def push(self, x):
        self.s.append((x, self.min))
        self.min = min(self.min, x)

    def pop(self):
        if not self.s:
            raise ValueError
        item, prevMin = self.s[-1]
        if self.min == item:
            self.min = prevMin
        return self.s.pop()[0]

    def top(self):
        return self.s[-1][0]

    def getMin(self):
        return self.min


if __name__ == "__main__":
     obj = MinStack()
     obj.push(5)
     obj.push(3)
     obj.push(6)

     assert 3 == obj.getMin()
     assert 6 == obj.pop()
     assert 3 == obj.getMin()
     assert 3 == obj.pop()
     assert 5 == obj.getMin()