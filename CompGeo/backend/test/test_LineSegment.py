import unittest
from CompGeo.backend.ds.point import Point
from CompGeo.backend.ds.LineSegment import LineSegment


class Tests(unittest.TestCase):

    def test_LineSegment(self):

        # test values
        zero = 0
        positive = 1
        negative = -1
        non_num = 'a'

        # Test cases
        test1 = LineSegment(Point(zero, zero), Point(zero, zero))
        test2 = LineSegment(Point(negative, zero), Point(positive, non_num))
        test3 = LineSegment(Point(negative, zero), Point(positive, positive))
        test4 = LineSegment(positive, negative)
        test5 = LineSegment(zero, non_num)

        # tests
        self.assertEqual(-1, test1)
        self.assertEqual(-1, test2)
        self.assertNotEqual("[(-1, 0) -> (1,1)]", test3)
        self.assertEqual(-1, test4)
        self.assertEqual(-1, test5)


if __name__ == '__main__':
    unittest.main()
