# coding: utf-8
import pygame
import platform

class Gomoku():

	def __init__(self):
		pygame.init()  # init a intance of pygame
		self.going = True # this is a signal of 
		self.screen = pygame.display.set_mode((800, 600)) # set up the initial window
	
	def loop(self):
		while self.going:
			self.update()
		pygame.quit()

	def update(self):
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				self.going = False

	def draw

if __name__ == '__main__':
	game = Gomoku()
	game.loop()
