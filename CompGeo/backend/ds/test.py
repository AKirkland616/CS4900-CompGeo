import unittest
import cg
from cg import Point
from cg import LineSeg

class TestPoint(unittest.TestCase):

	def test_point_constructor_x(self):
	
		# Tests non-number string values. This should raise an exception.
		with self.assertRaises(Exception):
    			point1 = Point("a",0)

		# Tests non-number boolean values. This should raise an exception.
		with self.assertRaises(Exception):
    			point1 = Point(true,0)

		# (zero, zero)
		point1 = Point(0,0) 
		self.assertEqual(point1.getX(), 0)
		
		# (positive, zero)
		point1 = Point(1,0)
		self.assertEqual(point1.getX(), 1)

		# (negative, zero)
		point1 = Point(-1,0)
		self.assertEqual(point1.getX(), -1)
		
	def test_point_constructor_y(self):

		# Tests non-number values. This should raise an exception.
		with self.assertRaises(Exception):
    			point1 = Point(0, a)

		# (zero,0)
		point1 = Point(0,0) 
		self.assertEqual(point1.getY(), 0)
		
		# (zero, positive)
		point1 = Point(0,1)
		self.assertEqual(point1.getY(), 1)

		# (zero, negative)
		point1 = Point(-1,0)
		self.assertEqual(point1.getX(), -1)

class TestLineSeg(unittest.TestCase):

	def test_lineseg_constructor_start(self):
		# Test start point x1,y1

		lineseg = LineSeg(0,0,1,1)

		x1 = lineseg.getStart().getX()
		self.assertEqual(x1,0)

		y1 = lineseg.getStart().getY()
		self.assertEqual(y1,0)

	def test_lineseg_constructor_end(self):
		# Test end point x2,y2

		lineseg = LineSeg(0,0,1,1)

		x2 = lineseg.getEnd().getX()
		self.assertEqual(x2,1)

		y2 = lineseg.getEnd().getY()
		self.assertEqual(y2,1)

	def test_lineseg_constructor_samepoints(self):
		# Test if the two points are identical, if so it should raise an exception.
		
		# This should raise an exception.
		with self.assertRaises(Exception):
    			lineseg = LineSeg(0,0,0,0)

if __name__ == '__main__':
	unittest.main()
