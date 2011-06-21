#! /usr/bin/env python2
import pygame
from constants import *
from level_select import level_select
from play_level import play_level

class Game:
    def draw(self, event):
        print self.level
        if self.level > 0:
            self.level = self.play_level(self.level, event)
        elif self.level == -1:
            self.level = 0
            return State.MAIN
        else:
            self.level = self.select(event)
            
        return State.GAME

    def __init__(self, screen):
        self.screen = screen
        self.level = 0
        self.select = level_select(screen).draw
        self.play_level = play_level(screen).draw
