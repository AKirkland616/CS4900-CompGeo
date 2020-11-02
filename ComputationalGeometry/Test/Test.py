'''
Created on Sep 19, 2020

@author: anthonykirkland
'''

import unittest
from ComputationalGeometry.Point import Point
from ComputationalGeometry.LineSegment import Segment
from ComputationalGeometry.LineSegmentIntersection import LineSegmentIntersection
from ComputationalGeometry.ClosestPairOfPoints import ClosestPairOfPoints
from ComputationalGeometry.ConvexHull import ConvexHull
from ComputationalGeometry.LargestEmptyCircle import LargestEmptyCircle


class Test(unittest.TestCase):

    def test_Point(self):
        testPoint = Point(5, 9)
        self.assertEqual(str(Point(1, 1)), str(Point(1, 1)))
        self.assertEqual(5, testPoint.x)
        self.assertEqual(9, testPoint.y)

    def test_Segment(self):
        testPointA = Point(5, 9)
        testPointB = Point(7, 2)
        testSeg = Segment(testPointA, testPointB)
        self.assertEqual(5, testSeg.a.x)
        self.assertEqual(9, testSeg.a.y)
        self.assertEqual(7, testSeg.b.x)
        self.assertEqual(2, testSeg.b.y)

    def test_LineSegmentIntersection(self):
        testSeg1 = Segment(Point(-3, -4), Point(-3, 4))
        testSeg2 = Segment(Point(-4, -3), Point(-1, 3))
        testSeg3 = Segment(Point(-2, 2), Point(2, 2))
        testSeg4 = Segment(Point(-1, 1), Point(2, -3))

        test8 = LineSegmentIntersection(testSeg1, testSeg2).lineLineIntersection(testSeg1.a, testSeg1.b, testSeg2.a,
                                                                                 testSeg2.b)
        test9 = LineSegmentIntersection(testSeg1, testSeg1).lineLineIntersection(testSeg1.a, testSeg1.b, testSeg1.a,
                                                                                 testSeg1.b)

        self.assertEqual(-3, test8.x)
        self.assertEqual(-1, test8.y)

        self.assertEqual(False, test9)

        test10 = LineSegmentIntersection(testSeg1, testSeg2).on_segment(testSeg1.a, testSeg1.b, testSeg2.b)
        test11 = LineSegmentIntersection(testSeg1, testSeg1).on_segment(Point(0, 0), Point(0, 1), Point(0, 2))

        self.assertEqual(False, test10)

        self.assertEqual(True, test11)

        test12 = LineSegmentIntersection(testSeg1, testSeg2).orientation(testSeg1.a, testSeg1.b, testSeg2.b)
        test13 = LineSegmentIntersection(testSeg1, testSeg1).orientation(Point(0, 0), Point(0, 1), Point(0, 2))
        test14 = LineSegmentIntersection(testSeg1, testSeg2).orientation(testSeg1.a, testSeg2.b, testSeg1.b)

        self.assertEqual(1, test12)

        self.assertEqual(0, test13)

        self.assertEqual(2, test14)

        test1 = LineSegmentIntersection(testSeg1, testSeg2).intersect
        test2 = LineSegmentIntersection(testSeg1, testSeg3).intersect
        test3 = LineSegmentIntersection(testSeg1, testSeg4).intersect
        test4 = LineSegmentIntersection(testSeg2, testSeg3).intersect
        test5 = LineSegmentIntersection(testSeg2, testSeg4).intersect
        test6 = LineSegmentIntersection(testSeg3, testSeg4).intersect
        test7 = LineSegmentIntersection(testSeg4, testSeg4).intersect

        self.assertEqual(-3, test1.x)
        self.assertEqual(-1, test1.y)

        self.assertEqual(False, test2)

        self.assertEqual(False, test3)

        self.assertEqual(-1.5, test4.x)
        self.assertEqual(2, test4.y)

        self.assertEqual(False, test5)

        self.assertEqual(False, test6)

        self.assertEqual(False, test7)

    def test_ClosestPairOfPoints(self):
        test_data_1 = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
        expected_output_1 = [[[1, 1], [2, 2]], [[2, 2], [3, 3]], [[3, 3], [4, 2]], [[2, 4], [3, 3]], [[1, 1], [2, 0]]]
        self.assertEqual(sorted(expected_output_1), sorted(ClosestPairOfPoints(test_data_1).get_ClosestPairOfPoints()))

    def test_ConvexHull(self):
        test_data_1 = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
        expected_output_1 = [[1, 1], [2, 0], [4, 2], [3, 3], [2, 4]]
        self.assertEqual(sorted(expected_output_1), sorted(ConvexHull(test_data_1).get_ConvexHull()))

    def test_LargestEmptyCircle(self):
        test_data_1 = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
        expected_output_1 = "I have NO idea!"
        self.assertEqual(sorted(expected_output_1), sorted(LargestEmptyCircle(test_data_1).get_LargestEmptyCircle()))



if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
