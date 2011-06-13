#! /usr/bin/env python
import olpcgames, pygame
from const import const
from level_select import level_select
from play_level import play_level

class game:
	def draw(self, events):
		if self.level > 0:
			self.level = self.play_level(events, self.level)
		elif self.level == -1:
			self.level = 0
			return const.MENU
		else:
			self.level = self.select(events)
			
		return const.GAME

	def __init__(self, screen):
		self.screen = screen
		self.level = 0
		self.select = level_select(screen).draw
		self.play_level = play_level(screen).draw
