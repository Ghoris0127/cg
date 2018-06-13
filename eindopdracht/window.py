from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import random
import time

class Window:

	def __init__(self, sizeX, sizeY):
		self.sizeX = sizeX
		self.sizeY = sizeY
		self.shapes = []
		self.interfaces = []
		self.rotation = 45
		self.old_time = time.time()
		self.iso = Isometric(self)
		glutInit()
		glutInitDisplayMode(GLUT_RGB)
		glutInitWindowSize(sizeX, sizeY)
		glutCreateWindow("Eindopdracht".encode("ascii"))
		glOrtho(0, sizeX, sizeY, 0, -1, 1)
		glutDisplayFunc(self.display)
		glutMouseFunc(self.mouse_func)
		#added timer func that will update after 2 seconds
		glutTimerFunc(50, self.update, 1)
		glutKeyboardFunc(self.end)

	def add_shape(self, shape):
		self.shapes.append(shape)

	def add_interface(self, interface):
		self.interfaces.append(interface)

	def update(self, value):
		new_time = time.time()
		dt = new_time - self.old_time
		self.old_time = new_time

		for shape in self.shapes:
			shape.update(dt)

		glutTimerFunc(50, self.update, 1)

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT)
		for shape in self.shapes:
			shape.draw(self.iso)
		for interface in self.interfaces:
			interface.draw()
		glFlush()
		glutPostRedisplay()

	def mouse_func(self, button, state, x, y):
		if state == 1:
			for interface in self.interfaces:
				interface.check_pressed(button, x, y, self)

	def end(self, key, x, y):
		exit()

	def draw(self):
		glutMainLoop()

#class to wrap the methods needed for isometric calculation
class Isometric():

	def __init__(self, window):
		self.window = window

	#method to multiply a matrix with a vector
	def mult_matrix_vector(self, matrix, vector):
		return_matrix = [0] * len(matrix)
		if len(matrix[0]) == len(vector):
			for i in range (0, len(matrix)):
				for j in range(0, len(vector)):
					return_matrix[i] += matrix[i][j] * vector[j]
		return return_matrix

	#method to multipy a matrix with a matrix
	def mult_matrix_matrix(self, matrix_one, matrix_two):
		return_matrix = []
		for i in range (0, len(matrix_one)):
			return_matrix.append([])
			for j in range (0, len(matrix_two[0])):
				return_matrix[i].append(0)

		if len(matrix_one[0]) == len(matrix_two):
			for h in range (0, len(matrix_one[0])):
				for i in range (0, len(matrix_one)):
					value = 0
					for j in range(0, len(matrix_one[0])):
						value += matrix_one[i][j] * matrix_two[j][h]
					return_matrix[i][h] = value
			return return_matrix

	''' in case of symmetry the rotational matrix that we need to implement is already used to create the view.
		with isometric you need to use 2 rotational matrixes. One for making the camera turn around the y axis and one around the x axis.
		we did the bonus excersize by multiplying our matrixes so that we only need to multiply the vector with one matrix.'''
	def isometricisize(self, coordinate_list, x, y, object_rotation):
		isometric_coordinates = []
		alpha = math.asin(math.tan(math.radians(30)))
		beta = math.radians(object_rotation + self.window.rotation)
		projection_matrix_one = ((math.cos(beta), 0, -1 * math.sin(beta)),
								 (0, 1, 0),
								 (math.sin(beta), 0, math.cos(beta)))
		projection_matrix_two = ((1, 0, 0),
								 (0, math.cos(alpha), math.sin(alpha)),
								 (0, -1 * math.sin(alpha), math.cos(alpha)))
		combined_matrix = self.mult_matrix_matrix(projection_matrix_two, projection_matrix_one)
		for coordinate in coordinate_list:
			matrix_calc = self.mult_matrix_vector(combined_matrix, coordinate)
			isometric_coordinates.append((matrix_calc[0] + 0.5 * self.window.sizeX + x, matrix_calc[1] + 0.5 * self.window.sizeY + y))
		return isometric_coordinates
