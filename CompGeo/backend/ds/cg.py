class Point:
	x, y = 0,0 # Two-dimensional point (x,y).

	def __init__(self, x1, y1): 
		self.x = x1
		self.y = y1

	def getX(self):
		return self.x

	def getY(self):
		return self.y

class LineSeg:
	start = Point(0,0) # Start end-point.
	end   = Point(1,1) # End end-point.

	def __init__(self, x1, y1, x2, y2): 
		# Check for identical points.
		if x1 == x2 and y1 == y2:
			raise Exception("Error: identical points!")
		else:
			self.start = Point(x1, y1)
			self.end   = Point(x2, y2)

	def getStart(self):
		return self.start

	def getEnd(self):
		return self.end

class Intersection:
	def findIntersection():
	# Will take as input a list of LineSeg objects.
	# Will output a list of Point objects.

		pass

	def handleEvent():
		pass
	
	def findNewEvent():
		pass

# Create a single line segment.
ls2 = LineSeg(0,0,1,1)
print(ls2.getStart().getX()) #x1
print(ls2.getStart().getY()) #y1
print(ls2.getEnd().getX()) #x2
print(ls2.getEnd().getY()) #y2