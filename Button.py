# coding:utf-8
import pygame

class Button():
	def __init__(self, pos, size, word, font):
		self.pos = pos
		self.size = size
		self.word = word
		self.font = font
		self.bound_color = (0,0,0)

	def set(self, color):
		self.bound_color = color

	def draw(self, screen):
		pygame.draw.rect(screen, 
						 self.bound_color,
						 [self.pos[0],
						  self.pos[1],
						  self.size[0],
						  self.size[1]],
						  2)  
		screen.blit(self.font.render(self.word, True, (0, 0, 0)), (self.pos[0]  + self.size[0] / 4, self.pos[1]))

	def check(self, pos):
		x = pos[0]
		y = pos[1]
		if self.pos[0] < x and self.pos[1] < y and x < self.pos[0] + self.size[0] and y < self.pos[1] + self.size[1]:
			return True
		else:
			return False


