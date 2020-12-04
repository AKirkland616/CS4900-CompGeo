import unittest
from CompGeo.backend.ds.point import Point

class TestPoint(unittest.TestCase):

    def test_point_constructor_x(self):
        # Tests non-number string values. This should raise an exception.
        self.assertEqual(Point("a", 0), -1)

        # Tests non-number boolean values. This should raise an exception.
        self.assertEqual(Point(True, 0), -1)

        # (zero, zero)
        point1 = Point(0, 0)
        self.assertEqual(point1.get_x(), 0)

        # (positive, zero)
        point1 = Point(1, 0)
        self.assertEqual(point1.get_x(), 1)

        # (negative, zero)
        point1 = Point(-1, 0)
        self.assertEqual(point1.get_x(), -1)

    def test_point_constructor_y(self):
        # Tests non-number values. This should raise an exception.
        self.assertEqual(Point(0, "a"), -1)

        # (zero,0)
        point1 = Point(0, 0)
        self.assertEqual(point1.get_y(), 0)

        # (zero, positive)
        point1 = Point(0, 1)
        self.assertEqual(point1.get_y(), 1)

        # (zero, negative)
        point1 = Point(-1, 0)
        self.assertEqual(point1.get_x(), -1)

if __name__ == '__main__':
    unittest.main()
