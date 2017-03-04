# coding: utf-8
import pygame
import platform
from Chessboard import Chessboard  # from file Chessboard.py import class Chesboard

class Gomoku():

	def __init__(self):
		pygame.init()  # init a intance of pygame
		self.going = True # this is a signal of 
		self.screen = pygame.display.set_mode((800, 600)) # set up the initial window
		self.chessboard = Chessboard()
	def loop(self):
		while self.going:
			self.update()
			self.draw()
		pygame.quit()

	def update(self):
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				self.going = False

	def draw(self):
		self.screen.fill((255, 255, 255))  # fill all screen as white
		self.chessboard.draw(self.screen)  # call draw function with parameter self.screen in class chessborad

		pygame.display.update()


if __name__ == '__main__':
	game = Gomoku()
	game.loop()
