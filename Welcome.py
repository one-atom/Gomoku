# coding: utf-8

import pygame
from Button import Button
import pdb

class Welcome():
	def __init__(self, font):
		self.font = font
		self.one_player_button = Button([300, 350], [200, 30], "1P VS AI", self.font)
		self.one_player_button2 = Button([300, 400], [200, 30], "AI VS 1P", self.font)
		self.two_player_button = Button([300, 450], [200, 30], "1P VS 2P", self.font)

	def draw(self, screen):
		self.one_player_button.draw(screen)
		self.one_player_button2.draw(screen)
		self.two_player_button.draw(screen)

	def handle_key_event(self, e, game):
		
		pos = e.pos
		
		if self.one_player_button.check(pos):
			game.window = 1
			game.with_AI = True
			game.AI_first = True
 			

		elif self.one_player_button2.check(pos):
			game.window = 1
			game.with_AI = True
			game.AI_first = False
			
		elif self.two_player_button.check(pos):
			game.window = 1
			game.with_AI = False


