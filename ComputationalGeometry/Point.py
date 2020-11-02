'''
Created on Sep 20, 2020

@author: anthonykirkland
'''


class Point(object):
    '''
    classdocs
    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return ("(" + str(self.x) + ", " + str(self.y) + ")")

    def __eq__(self, other):
        if (isinstance(other, Point)):
            return (self.x == other.x and self.y == other.y)
        return False