# coding: utf-8

import pygame

class Chessboard:
	def __init__(self):
		self.grid_size = 26  # the width of grid
		self.start_x, self.start_y = 30, 50 # the coordinate of left-up-most corner of the left-up-most check grid 
		self.edge_size = self.grid_size / 2 # the width of blank around the checkboard
		self.grid_count = 19  # the number of grid each column or row


	def draw(self, screen):
		# draw a rectangle
		pygame.draw.rect(screen, (185, 122, 87),
						 [self.start_x - self.edge_size, 
						  self.start_y - self.edge_size,
						  (self.grid_count - 1) * self.grid_size + self.edge_size * 2,
						  (self.grid_count - 1) * self.grid_size + self.edge_size * 2],
						 0)
		