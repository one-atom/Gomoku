# coding: utf-8
import numpy as np
import pdb

class AI():

	def __init__(self, game):
		self.game = game
		self.color = (not game.AI_first) + 1
		self.rival_color = game.AI_first + 1
		self.grid_count = self.game.chessboard.grid_count

	def choose_according_to_position_evaluation(self):
		'''
		this algorithm is refering to http://www.cnblogs.com/goodness/archive/2010/05/27/1745756.html
		'''
		#pdb.set_trace()
		if self.game.chess_count == 0:
			self.game.chessboard.set_piece([9,9] , self.color, True)
			return
		evaluation_matrix = np.zeros((self.grid_count, self.grid_count),dtype = int)
		for r in range(self.grid_count):
			for c in range(self.grid_count):
				if self.game.current_game[r,c] == 0:
					self_evaluation = self.game.chessboard.position_evaluation(self.color, r, c)
					rival_evaluation = self.game.chessboard.position_evaluation(self.rival_color, r, c)
					evaluation_matrix[r,c] = max([self_evaluation + 1, rival_evaluation])
		for k in range(evaluation_matrix.shape[0]):
			print evaluation_matrix[k].tolist()
		i,j = np.unravel_index(evaluation_matrix.argmax(), evaluation_matrix.shape)
		self.game.chessboard.set_piece([i,j] , self.color, True)


	def selection(self):
		pass