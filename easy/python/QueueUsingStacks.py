'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
'''
class Queue(object):
    def __init__(self):
        self.sAdd = []
        self.sPop = []

    def push(self, x):
        self.sAdd.append(x)

    def pop(self):
        if not self.sPop:
            for _ in xrange(len(self.sAdd)):
                self.sPop.append(self.sAdd.pop())

        self.sPop.pop()

    def peek(self):
        if not self.sPop:
            for _ in xrange(len(self.sAdd)):
                self.sPop.append(self.sAdd.pop())
        return self.sPop[-1]

    def empty(self):
        return not self.sAdd and not self.sPop


if __name__=="__main__":
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    assert 1 == q.peek()
    q.pop()
    assert 2 == q.peek()
    q.push(5)
    q.pop()
    q.pop()
    q.pop()
    assert 5 == q.peek()