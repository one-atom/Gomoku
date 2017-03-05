# coding: utf-8

import pygame
from Button import Button

class Chessboard:
	def __init__(self, font):
		self.grid_size = 26  # the width of grid
		self.start_x, self.start_y = 30, 50 # the coordinate of the left-up-most check grid 
		self.edge_size = self.grid_size / 2 # the width of blank around the checkboard
		self.grid_count = 19  # the number of grid each column or row
		self.font = font
		# init a return button
		self.return_to_welcome = Button([600, 500], [150, 30], "Return", self.font)

	def draw(self, game):

		screen = game.screen

		# draw retrun button
		self.return_to_welcome.draw(screen)

		# draw a rectangle, using RGB(185, 122, 87)
		pygame.draw.rect(screen, (185, 122, 87),
						 [self.start_x - self.edge_size, 
						  self.start_y - self.edge_size,
						  (self.grid_count - 1) * self.grid_size + self.edge_size * 2,
						  (self.grid_count - 1) * self.grid_size + self.edge_size * 2],
						 0)  # boundary line width

		# draw horizontal grid line, using black
		for r in range(self.grid_count):
			y = self.start_y + r * self.grid_size
			pygame.draw.line(screen, 
							 (0,0,0), 
							 [self.start_x, y],
							 [self.start_x + self.grid_size * (self.grid_count - 1), y],
							 2) # line width

		# draw vertical grid line, using black
		for c in range(self.grid_count):
			x = self.start_x + c * self.grid_size
			pygame.draw.line(screen, 
							 (0,0,0),
							 [x, self.start_y],
							 [x, self.start_y + self.grid_size * (self.grid_count - 1)],
							 2)  

	def handle_return_event(self, e, game):
		pos = e.pos
		if (self.return_to_welcome.check(pos)):
			game.window = 0
		else:
			game.window = 1

