#! /usr/bin/env python
import olpcgames, pygame
from const import const

class menu:
	def draw(self):
		pygame.draw.rect(self.screen, [255, 255, 255], [20, 20, 20, 20], 2)
		return const.MENU

	def __init__(self, screen):
		self.screen = screen
