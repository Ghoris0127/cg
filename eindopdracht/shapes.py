from OpenGL.GL import *

class Curve:
	def __init__(self, p1, p2, p3, c):
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		self.c = c

	def update(self, dt):
		pass

	def get_coordinates(self):
		return_list = []
		for t in range(0, 10, 1):
			t *= 0.1
			x_coor = (1 - t) ** 2 * self.p1[0] + 2 * (1 - t) * t * self.p2[0] + t ** 2 * self.p3[0]
			y_coor = (1 - t) ** 2 * self.p1[1] + 2 * (1 - t) * t * self.p2[1] + t ** 2 * self.p3[1]
			return_list.append((int(x_coor), int(y_coor)))
		return return_list

	def draw(self, perspective):
		glBegin(GL_LINE_STRIP)
		glColor(self.c)
		for coordinate in self.get_coordinates():
			glVertex(coordinate)
		glEnd()

class Star:
	vertices = [[0, -1, 0],
				[-0.95, -0.31, 0],
				[-0.59, 0.81, 0],
				[0.59, 0.81, 0],
				[0.95, -0.31, 0]]

	edges = ((0, 2),
			 (2, 4),
			 (4, 1),
			 (1, 3),
			 (3, 0))

	def __init__(self, x, y, z, s, c, turning):
		self.x = x # x coordinate
		self.y = y # y coordinate
		self.z = z # z coordinate
		self.s = s # s (scale)
		self.c = c # c color (f, f, f)
		self.r = 0
		self.turning = turning

	# Converts vertices to coordinates in the world
	def return_vertex_coordinates(self):
		return_coordinates = []
		for vertex in self.vertices:
			new_x = vertex[0] * 0.5 * self.s
			new_y = vertex[1] * 0.5 * self.s
			new_z = vertex[2] * 0.5 * self.s
			return_coordinates.append((new_x, new_y, new_z))
		return return_coordinates

	#returns the list with edgess
	def return_edges(self):
		return self.edges

	def update(self, dt):
		if self.turning:
			self.r -= 100 * dt

	def draw(self, perspective):
		#makes the isometric representation for an array of coordinates taking the current rotation into account
		isometric_coordinates = perspective.isometricisize(self.return_vertex_coordinates(), self.x, self.y, self.r)
		#draws lines between the calculated coordinates
		glBegin(GL_LINES)
		glColor(self.c)
		for edge in self.edges:
			glVertex(isometric_coordinates[edge[0]])
			glVertex(isometric_coordinates[edge[1]])
		#increases rotation for one
		glEnd()

class Cube:
	# vertices related from the middle of the cube
	vertices = ((1, -1, -1),
				(1, 1, -1),
				(-1, 1, -1),
				(-1, -1, -1),
				(1, -1, 1),
				(1, 1, 1),
				(-1, -1, 1),
				(-1, 1, 1))

	# edges to show which vertex connects to which other vertex
	edges = ((0,1),
			 (0,3),
			 (0,4),
			 (2,1),
			 (2,3),
			 (2,7),
			 (6,3),
			 (6,4),
			 (6,7),
			 (5,1),
			 (5,4),
			 (5,7))

	surfaces = ((0,1,2,3),
				(3,2,7,6),
				(6,7,5,4),
				(4,5,1,0),
				(1,5,7,2),
				(4,0,3,6))

	def __init__(self, x, y, z, s, c, turning):
		self.x = x # x coordinate
		self.y = y # y coordinate
		self.z = z # z coordinate
		self.s = s # s (scale)
		self.c = c # c color (f, f, f)
		self.r = 45
		self.turning = turning

	# Converts vertices to coordinates in the world
	def return_vertex_coordinates(self):
		return_coordinates = []
		for vertex in self.vertices:
			new_x = vertex[0] * 0.5 * self.s
			new_y = vertex[1] * 0.5 * self.s
			new_z = vertex[2] * 0.5 * self.s
			return_coordinates.append((new_x, new_y, new_z))
		return return_coordinates

	#returns the list with edgess
	def return_edges(self):
		return self.edges

	def update(self, dt):
		if self.turning:
			self.r += 100 * dt

	def draw(self, perspective):
		#makes the isometric representation for an array of coordinates taking the current rotation into account
		isometric_coordinates = perspective.isometricisize(self.return_vertex_coordinates(), self.x, self.y, self.r)
		#draws lines between the calculated coordinates
		glBegin(GL_QUADS)
		glColor(self.c)
		for surface in self.surfaces:
			for vertex in surface:
				glVertex(isometric_coordinates[vertex])
		glEnd()

		glBegin(GL_LINES)
		glColor((1, 1, 1))
		for edge in self.edges:
			glVertex(isometric_coordinates[edge[0]])
			glVertex(isometric_coordinates[edge[1]])
		#increases rotation for one
		glEnd()
