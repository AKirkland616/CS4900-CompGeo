
from ComputationalGeometry.Point import Point
from ComputationalGeometry.LineSegment import Segment
from itertools import combinations
import sys


class LineSegmentIntersection(object):

    def __init__(self, seg1, seg2):
        self.seg1 = seg1
        self.seg2 = seg2
        self.intersect = self.do_intersect(seg1.a ,seg1.b ,seg2.a ,seg2.b)

    def lineLineIntersection(self, A,  B,  C,  D):

        # Line AB represented as a1x + b1y = c1
        a1 = B.y - A.y
        b1 = A.x - B.x
        c1 = a1 *(A.x) + b1 *(A.y)

        # Line CD represented as a2x + b2y = c2
        a2 = D.y - C.y
        b2 = C.x - D.x
        c2 = a2 *(C.x )+ b2 *(C.y)

        determinant = a1 *b2 - a2 *b1
        if (determinant == 0):
            # The lines are parallel. This is simplified
            return False

        x = (b2 *c1 - b1 *c2 ) /determinant
        y = (a1 *c2 - a2 *c1 ) /determinant
        return Point(x, y)

    def on_segment(self ,p, q, r):
        # Given three colinear points p, q, r, the function checks if
        # point q lies on line segment "pr"

        if (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and
                q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y)):
            return True
        return False

    def orientation(self ,p, q, r):
        # Find orientation of ordered triplet (p, q, r).
        # The function returns following values
        # 0 --> p, q and r are colinear
        # 1 --> Clockwise
        # 2 --> Counterclockwise

        val = ((q.y - p.y) * (r.x - q.x) -
               (q.x - p.x) * (r.y - q.y))
        if val == 0:
            return 0  # colinear
        elif val > 0:
            return 1   # clockwise
        else:
            return 2  # counter-clockwise

    def do_intersect(self, p1, q1, p2, q2):

        # Main function to check whether the closed line segments p1 - q1 and p2
        # - q2 intersect
        o1 = self.orientation(p1, q1, p2)
        o2 = self.orientation(p1, q1, q2)
        o3 = self.orientation(p2, q2, p1)
        o4 = self.orientation(p2, q2, q1)

        # General case
        if (o1 != o2 and o3 != o4):
            return self.lineLineIntersection(p1 ,q1 ,p2 ,q2)

        # Special Cases
        # p1, q1 and p2 are colinear and p2 lies on segment p1q1
        if (o1 == 0 and self.on_segment(p1, p2, q1)):
            return self.lineLineIntersection(p1 ,q1 ,p2 ,q2)

        # p1, q1 and p2 are colinear and q2 lies on segment p1q1
        if (o2 == 0 and self.on_segment(p1, q2, q1)):
            return self.lineLineIntersection(p1 ,q1 ,p2 ,q2)

        # p2, q2 and p1 are colinear and p1 lies on segment p2q2
        if (o3 == 0 and self.on_segment(p2, p1, q2)):
            return self.lineLineIntersection(p1 ,q1 ,p2 ,q2)

        # p2, q2 and q1 are colinear and q1 lies on segment p2q2
        if (o4 == 0 and self.on_segment(p2, q1, q2)):
            return self.lineLineIntersection(p1 ,q1 ,p2 ,q2)

        return False # Doesn't fall in any of the above cases


if __name__ == '__main__':
    print('hello')
    if sys.stdin.isatty():
        # print "Input a integer N, then follows 2N point sets"
        print("Please pass in a file with an inputed integer N followed by 2N point sets")
        sys.exit()
    N = int(sys.stdin.readline())
    points_str_list = sys.stdin.readlines()
    if(len(points_str_list) == (2*N)):
        index = 0
        segArray = []
        while(index != 2*N):
            a, b = [int(i) for i in points_str_list[index].split()]
            c, d = [int(i) for i in points_str_list[(index + 1)].split()]
            segArray.append(Segment(Point(a,b),Point(c,d)))
            index = index + 2

    else:
        print("Error! Invalid number of points/ Line segments!"
              "Please pass in a file with an inputed integer N followed by 2N point sets")
        sys.exit()

    for seg1, seg2 in combinations(segArray, 2):
        a = LineSegmentIntersection(seg1, seg2).intersect
        if (a):
            print(seg1, "and", seg2, "intersect at", a )





