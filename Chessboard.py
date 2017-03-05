# coding: utf-8

import pygame
from Button import Button
import numpy as np
import pdb

class Chessboard:
	def __init__(self, game):

		self.font = game.font
		self.game = game
		self.grid_size = 26  # the width of grid
		self.start_x, self.start_y = 30, 50 # the coordinate of the left-up-most check grid 
		self.edge_size = self.grid_size / 2 # the width of blank around the checkboard
		self.grid_count = 19  # the number of grid each column or row
		# init a return button
		self.return_to_welcome = Button([600, 500], [150, 30], "Return", self.font)
		self.win_num = 5


	def draw(self):

		game = self.game
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

		# draw pieces
		for r in range(self.grid_count):
			for c in range(self.grid_count):
				piece = game.current_game[r,c]
				if piece != 0:
					if piece == 1:
						color = (0, 0, 0)
					else:
						color = (255, 255, 255)

					x = self.start_x + r * self.grid_size
					y = self.start_y + c * self.grid_size
					pygame.draw.circle(screen, color, [x, y], self.grid_size // 2)

	def set_piece(self, pos, color, AI):
		game = self.game
		#pdb.set_trace()
		if AI:
			absolute_r = pos[0]
			absolute_c = pos[1]
		else:
			absolute_r = pos[0] - (self.start_x - self.grid_size / 2)
			absolute_c = pos[1] - (self.start_y - self.grid_size / 2)
			absolute_r = absolute_r / self.grid_size
			absolute_c = absolute_c / self.grid_size
		#relative_x, relative_y = absolute_to_relative(absolute_nx, absolute_ny)
		if (absolute_r < 0 or absolute_r >= self.grid_count or absolute_c < 0 or absolute_c > self.grid_count):
			return
		
		# check if this position have been positioned a piece

		check = game.current_game[absolute_r, absolute_c]
		
		if(check == 0):
			game.current_game[absolute_r, absolute_c] = game.current_color
			game.chess_count += 1
			self.check_win(absolute_r, absolute_c)
			game.current_color %= 2
			game.current_color += 1

	def handle_key_event(self, e, whether_posi):
		game = self.game
		pos = e.pos
		if (self.return_to_welcome.check(pos)):
			game.window = 0
		else:
			game.window = 1
		if(whether_posi):
			self.set_piece(pos, game.current_color, False)
		

	def get_continuous_count(self, piece, r, c, dr, dc):
		game = self.game

		result = 0
		end_empty = False
		i = 1
		while True:
			new_r = r + dr * i
			new_c = c + dc * i
			if 0 <= new_r < self.grid_count and 0 <= new_c < self.grid_count:
				if game.current_game[new_r, new_c] == piece:
					result += 1
				else:
					if game.current_game[new_r, new_c] == 0:
						end_empty = True
					break
			else:
				break
			i += 1
		return result, end_empty

	def check_win(self, r, c):
		game = self.game
		piece = game.current_game[r, c]
		n_count, _ = self.get_continuous_count(piece, r, c, -1, 0)
		s_count, _ = self.get_continuous_count(piece, r, c, 1, 0)

		e_count, _ = self.get_continuous_count(piece, r, c, 0, 1)
		w_count, _ = self.get_continuous_count(piece, r, c, 0, -1)

		se_count, _ = self.get_continuous_count(piece, r, c, 1, 1)
		nw_count, _ = self.get_continuous_count(piece, r, c, -1, -1)

		ne_count, _ = self.get_continuous_count(piece, r, c, -1, 1)
		sw_count, _ = self.get_continuous_count(piece, r, c, 1, -1)

		if (n_count + s_count + 1 >= self.win_num ) or (e_count + w_count + 1 >= self.win_num ) or \
			(se_count + nw_count + 1 >= self.win_num ) or (ne_count + sw_count + 1 >= self.win_num ):
			game.win = game.current_game[r, c]
			game.game_over = True

		if game.chess_count == self.grid_count ** 2:

			game.win = 3
			game.game_over = True

	def position_evaluation(self, piece, r, c):
		game = self.game
		game = self.game

		count = []
		empty = []

		n_count, n_empty = self.get_continuous_count(piece, r, c, -1, 0)
		s_count, s_empty = self.get_continuous_count(piece, r, c, 1, 0)
		ns_count = n_count + s_count
		ns_empty = n_empty + s_empty
		count.append(ns_count)
		empty.append(ns_empty)

		e_count, e_empty = self.get_continuous_count(piece, r, c, 0, 1)
		w_count, w_empty = self.get_continuous_count(piece, r, c, 0, -1)
		ew_count = e_count + w_count
		ew_empty = e_empty + w_empty
		count.append(ew_count)
		empty.append(ew_empty)

		se_count, se_empty = self.get_continuous_count(piece, r, c, 1, 1)
		nw_count, nw_empty = self.get_continuous_count(piece, r, c, -1, -1)
		senw_count = se_count + nw_count
		senw_empty = se_empty + nw_empty
		count.append(senw_count)
		empty.append(senw_empty)

		ne_count, ne_empty = self.get_continuous_count(piece, r, c, -1, 1)
		sw_count, sw_empty = self.get_continuous_count(piece, r, c, 1, -1)
		nesw_count = ne_count + sw_count
		nesw_empty = ne_empty + sw_empty
		count.append(nesw_count)
		empty.append(nesw_empty)

		count = np.array(count, dtype = int)
		empty = np.array(empty, dtype = int)
		print count
		print empty

		
		chengwu = sum(count == 4)
		huosi = sum((count == 3) * (empty == 2))
		sisi = sum((count == 3) * (empty == 1))
		huosan = sum((count == 2) * (empty == 2))
		sisan = sum((count == 2) * (empty == 1))
		huoer = sum((count == 1) * (empty == 2))
		sier = sum((count == 1) * (empty == 1))
		danzi = sum((count == 0) * (empty == 2))

		# 100
		if chengwu > 0:
			return 100
		elif huosi > 0 or sisi >= 1 or (sisi > 0 and huosan > 0):
			return 90
		elif huosan >= 2:
			return 80
		elif huosan > 0 and sisan > 0:
			return 70
		elif huosan > 0:
			return 50
		elif huoer >= 2:
			return 40
		elif sisan > 0:
			return 30
		elif huoer > 0:
			return 20
		elif sier > 0:
			return 10
		else:
			return 0




		






