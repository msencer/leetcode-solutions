from collections import deque


class Stack(object):
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

        self.current = False

    def _current(self):
        return self.q1 if self.current else self.q2

    def _other(self):
        return self.q2 if self.current else self.q1

    def push(self, x):
        c, o = self._current(), self._other()
        while c:
            o.appendleft(c.pop())
        c.appendleft(x)

    def pop(self):
        c, o = self._current(), self._other()
        if not c:
            while len(o) > 1:
                c.appendleft(o.pop())
            self.current = not self.current

        self._current().pop()

    def top(self):
        c, o = self._current(), self._other()
        if not c:
            while len(o) > 1:
                c.appendleft(o.pop())
            self.current = not self.current
        v1 = self._current().pop()
        self._current().appendleft(v1)
        return v1

    def empty(self):
        return not self.q1 and not self.q2


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    assert 2 == s.top()
    s.pop()
    assert 1 == s.top()
    s.pop()
    s.push(3)
    assert 3 == s.top()