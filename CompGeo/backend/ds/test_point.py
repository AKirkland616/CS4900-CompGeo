import unittest
import cg
from cg import Point

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

if __name__ == '__main__':
	unittest.main()
