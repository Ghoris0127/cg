from window import Window
from shapes import Cube, Star, Curve
from interface import Interface

width = 1080
height = 720

def toggle_turning(window):
	for shape in window.shapes:
		if not isinstance(shape, Curve):
			shape.turning = not shape.turning

l = Window(width, height)
cube1 = Cube(0, 0, 0, 200, (1, 0, 0), True)
l.add_shape(cube1)
cube2 = Cube(0, -150, 0, 100, (0, 1, 0), True)
l.add_shape(cube2)
star = Star(350, 0, 0, 100, (1, 0, 1), True)
l.add_shape(star)
interface = Interface(50, 25, 100, 50, (0, 1, 1), toggle_turning)
l.add_interface(interface)
curve1 = Curve((100, 100), (100, 200), (200, 200), (0.5, 0, 0.5))
curve2 = Curve((100, 100), (100, 200), (0, 200), (0.5, 0, 0.5))
curve3 = Curve((100, 300), (100, 200), (0, 200), (0.5, 0, 0.5))
curve4 = Curve((100, 300), (100, 200), (200, 200), (0.5, 0, 0.5))
l.add_shape(curve1)
l.add_shape(curve2)
l.add_shape(curve3)
l.add_shape(curve4)
l.draw()

#data for testing the matrix multiplier function.
#matrix_one = [[4, 0, 3], [1, -1, 7], [-3, 3, 2]]
#matrix_two = [[-2, 3, 1], [2, -3, -5], [4, 0, 7]]
#print(mult_matrix_matrix(matrix_one, matrix_two))
