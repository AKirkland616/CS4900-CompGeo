class Point:
	x, y = 0,0 # Two-dimensional point (x,y).

	def __init__(self, x1, y1): 
		self.x = x1
		self.y = y1

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	# prints point in an understandable way. can be rewritten easily
	def __str__(self):
		return ("(" + str(self.x) + ", " + str(self.y) + ")")

	# compares points. Returns true if equal, or false if not.
	def __eq__(self, other):
		if (isinstance(other, Point)):
			return ((self.x == other.x and self.y == other.y) or (self.x == other.y and self.y == other.x))
		return False


