class Point:
	def __new__(cls, x, y):
		if not (isinstance(x, (int, float))) or isinstance(x, bool):
			return -1

		if not (isinstance(y, (int, float))) or isinstance(y, bool):
			return -1

		return super(Point, cls).__new__(cls)

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def __str__(self):
		'''
		Prints point in an understandable way. can be rewritten easily.
		'''
		return "(" + str(self.x) + ", " + str(self.y) + ")"
	
	def __eq__(self, other):
		'''
		Compares points. Returns true if equal, or false if not.
		'''
		if isinstance(other, Point):
			return self.x == other.x and self.y == other.y

		return False

