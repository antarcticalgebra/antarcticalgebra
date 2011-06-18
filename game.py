#! /usr/bin/env python2
import pygame
from constants import Const
from level_select import level_select
from play_level import play_level

class game:
    def draw(self, event):
        #print self.level
        if self.level > 0:
            self.level = self.play_level(event, self.level)
        elif self.level == -1:
            self.level = 0
            return Const.MENU
        else:
            self.level = self.select(event)
            
        return Const.GAME

    def __init__(self, screen):
        self.screen = screen
        self.level = 0
        self.select = level_select(screen).draw
        self.play_level = play_level(screen).draw
