class LineSegment(object):

    # create line segment from two different points or return -1
    def __new__(cls, point1, point2):
        if ((isinstance(point1, Point) and isinstance(point2, Point)) and (point1 != point2)):
            return super(LineSegment, cls).__new__(cls, point1, point2)
        else:
            return -1

    # inits line segment from 2 points
    def __init__(self, point1, point2):
            self.a = point1
            self.b = point2

    # prints line segment in an understandable way. can be rewritten easily
    def __str__(self):
        return ("[("+str(self.a.x) + ", " + str(self.a.y) + ") -> ("+str(self.b.x) + ", " + str(self.b.y) + ")]")

    # compares line segments. Returns true if equal, or false if not.
    def __eq__(self, other):
        if (isinstance(other, LineSegment)):
            return ((self.a == other.a and self.b == other.b) or (self.a == other.b and self.b == other.a))
        return False