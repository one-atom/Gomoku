# coding: utf-8
import pygame
import platform
from Chessboard import Chessboard  # from file Chessboard.py import class Chesboard
from Welcome import Welcome
from AI import AI
import numpy as np
import pdb

class Gomoku():

	def __init__(self):
		pygame.init()  # init a intance of pygame
		self.window = 0
		self.going = True # this is a signal of 
		self.with_AI = False
		self.AI_first = True


		#self.parameters = {'window':self.window, 
		#				   'with_AI':self.with_AI, 
		#				   'AI_first':self.AI_first}

		self.screen = pygame.display.set_mode((800, 600)) # set up the initial window
		pygame.display.set_caption("Gomoku")
		
		
		if 'Windows' in platform.system():
			self.font = pygame.font.Font(r"C:\\Windows\\Fonts\\consola.ttf", 24)
		else:
			self.font = pygame.font.Font(r"/Library/Fonts/Courier New.ttf", 24)
        
		self.welcome = Welcome(self)

	def loop(self):
		while self.going:
			self.update()
			self.draw()
		pygame.quit()

	def update(self):

		if self.with_AI and self.current_color == (not self.AI_first) + 1:
			self.AI.choose_according_to_position_evaluation()


		for e in pygame.event.get():

			# QUIT
			if e.type == pygame.QUIT:
				self.going = False

			# Click event
			elif e.type == pygame.MOUSEBUTTONDOWN:
				
				# if on welcome screen
				if(self.window == 0):
					self.welcome.handle_key_event(e)
					if (self.window == 1):
						self.init_game()

				# if on checkboard screen
				elif(self.window == 1):
					if not self.game_over:
						if not self.with_AI:
							posi = True
						else:
							if self.current_color == self.AI_first + 1:
								posi = True
							else:
								posi = False
						
						self.chessboard.handle_key_event(e, posi)
					else:
						self.init_game()

	def draw(self):

		self.screen.fill((255, 255, 255))  # fill all screen as white
		
		if self.window == 0:
			self.welcome.draw()
		
		if self.window == 1:
			self.chessboard.draw()  # call draw function with parameter self.screen in class chessborad
			if self.with_AI:
				if self.AI_first:
					to_show = 'Black'
				else:
					to_show = 'White'
			else:
				to_show = 'OFF'
			self.screen.blit(self.font.render("AI: {}".format(to_show) , True, (0, 0, 0)), (600, 100))
			if self.current_color == 1:
				to_show = "Black"
			else:
				to_show = "White"
			self.screen.blit(self.font.render("Current Color", True, (0,0,0)), (570, 200))
			self.screen.blit(self.font.render("    {}".format(to_show) , True, (0, 0, 0)), (570, 230))

			if self.game_over:
				if self.win == 1:
					to_show = "Black"
				elif self.win == 2:
					to_show = "White"
				elif self.win == 3:
					to_show = "No One"

				self.screen.blit(self.font.render("{} Win!".format(to_show), True, (0,0,0)), (350, 10))
		
		pygame.display.update()


	def init_game(self):
		try:
			del self.chessboard
			self.chessboard = Chessboard(self)
		except:
			self.chessboard = Chessboard(self)		
		self.current_color = 1
		self.current_game = np.zeros((self.chessboard.grid_count,self.chessboard.grid_count), dtype = int)
		self.win = 0
		self.game_over = False
		self.chess_count = 0
		if (self.with_AI):
			try:
				del self.AI
				self.AI = AI(self)
			except:
				self.AI = AI(self)

	def AI_select(self):
		pass




if __name__ == '__main__':
	game = Gomoku()
	game.loop()
