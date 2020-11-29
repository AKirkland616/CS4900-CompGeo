class LineSegment(object):
    # create line segment from 2 points possibly throw error if input is incorrect
    def __init__(self, point1, point2):
        if (isinstance(point1, Point) and isinstance(point2, Point)):
            self.a = point1
            self.b = point2
        else:
            # throw error? or will wrong input be caught as read of inputed

    # prints line segment in an understandable way. can be rewritten easily
    def __str__(self):
        return ("[("+str(self.a.x) + ", " + str(self.a.y) + ") -> ("+str(self.b.x) + ", " + str(self.b.y) + ")]")

    # compares line segments. Returns true if equal, or false if not.
    def __eq__(self, other):
        if (isinstance(other, LineSegment)):
            return ((self.a == other.a and self.b == other.b) or (self.a == other.b and self.b == other.a))
        return False