'''
Find the total area covered by two rectilinear rectangles in a 2D plane.
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, point1, point2):
        self.left = min(point1.x, point2.x)
        self.top = max(point1.y, point2.y)
        self.right = max(point1.x, point2.x)
        self.bottom = min(point1.y, point2.y)

    def calculateArea(self):
        return (self.right - self.left) * (self.top - self.bottom)

    def intersection(self, other):
        if self.left > other.right or self.right < other.left or self.top < other.bottom or self.bottom > self.top:
            return 0

        l = max(self.left, other.left)
        t = min(self.top, other.top)
        r = min(self.right, other.right)
        b = max(self.bottom, other.bottom)

        si = (r - l) * (t - b)

        return si if si > 0 else 0


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        p1, p2, p3, p4 = Point(A, B), Point(C, D), Point(E, F), Point(G, H)
        rect1, rect2 = Rectangle(p1, p2), Rectangle(p3, p4)
        return rect1.calculateArea() + rect2.calculateArea() - rect1.intersection(rect2)


if __name__ == '__main__':
    assert 16 == Solution().computeArea(-2, -2, 2, 2, -2, -2, 2, 2)
