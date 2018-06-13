from OpenGL.GL import *
from OpenGL.GLUT import *
import ctypes

class Interface:
	def __init__(self, x, y, s_hor, s_ver, c, func):
		self.x = x
		self.y = y
		self.s_hor = s_hor
		self.s_ver = s_ver
		self.c = c
		self.func = func

	def check_pressed(self, button, x, y, window):
		if button == 0 and self.x - 0.5 * self.s_hor <= x <= self.x + 0.5 * self.s_hor and self.y - 0.5 * self.s_ver <= y <= self.y + 0.5 * self.s_ver:
			self.func(window)

	def draw(self):
		glBegin(GL_QUADS)
		glColor((1, 1, 1))
		glVertex((self.x - 0.5 * self.s_hor, self.y - 0.5 * self.s_ver))
		glVertex((self.x + 0.5 * self.s_hor, self.y - 0.5 * self.s_ver))
		glVertex((self.x + 0.5 * self.s_hor, self.y + 0.5 * self.s_ver))
		glVertex((self.x - 0.5 * self.s_hor, self.y + 0.5 * self.s_ver))
		glColor(self.c)
		glVertex((self.x - 0.5 * self.s_hor + 2, self.y - 0.5 * self.s_ver + 2))
		glVertex((self.x + 0.5 * self.s_hor - 2, self.y - 0.5 * self.s_ver + 2))
		glVertex((self.x + 0.5 * self.s_hor - 2, self.y + 0.5 * self.s_ver - 2))
		glVertex((self.x - 0.5 * self.s_hor + 2, self.y + 0.5 * self.s_ver - 2))
		glEnd()
