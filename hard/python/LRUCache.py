import sys
sys.path.append("../../datastuctures")
from linkedlist.doublelinkedlist import DoubleListNode,DoubleLinkedList


class LRUCache(object):
    def __init__(self, capacity):
        self.maxcap = capacity
        self.values = {}
        self.nodes = {}
        self.list = DoubleLinkedList()
        self.currentSize = 0

    def get(self, key):
        if key not in self.values:
            return None
        n = self.nodes[key]
        self.list.remove(n)
        self.list.appendleft(n)
        return self.values[key]

    def set(self, key, value):
        if self.get(key):
            self.values[key] = value
            return

        newNode = DoubleListNode(key)
        self.list.appendleft(newNode)
        self.currentSize += 1
        self.values[key] = value
        self.nodes[key] = newNode

        if self.currentSize > self.maxcap:
            toRemove = self.list.tail
            self.values.pop(toRemove.val)
            self.nodes.pop(toRemove.val)
            self.list.remove(toRemove)
            self.currentSize -= 1

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.set(1, "selam")
    cache.set(2, "naber")
    cache.set(3, "heyhey")
    assert None == cache.get(1)