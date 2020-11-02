'''
Created on Sep 26, 2020

@author: anthonykirkland
'''


class Segment(object):

    def __init__(self, point1, point2):
        self.a = point1
        self.b = point2

    def __str__(self):
        return ("[("+str(self.a.x) + ", " + str(self.a.y) + ") -> ("+str(self.b.x) + ", " + str(self.b.y) + ")]")

    def __eq__(self, other):
        if (isinstance(other, Segment)):
            return ((self.a == other.a and self.b == other.b) or (self.a == other.b and self.b == other.a))
        return False