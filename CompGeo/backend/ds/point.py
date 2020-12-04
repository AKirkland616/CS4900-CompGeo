class Point:
	def __new__(cls, x, y):
		if isinstance(x, str) or isinstance(y, str) or isinstance(x, bool) or isinstance(y, bool):
			return -1
		if not isinstance(x, int) and not isinstance(x, float):
			return -1
		if not isinstance(y, int) and not isinstance(y, float):
			return -1

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	# prints point in an understandable way. can be rewritten easily
	def __str__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ")"

	# compares points. Returns true if equal, or false if not.
	def __eq__(self, other):
		if isinstance(other, Point):
			return (self.x == other.x and self.y == other.y) or (self.x == other.y and self.y == other.x)
		return False

