import pygame
from constants import Const

class Menu:
    def __init__(self, screen):
        self.__screen = screen
        self.__menu_actions = [About(self.__screen).draw, Help(self.__screen).draw]
        self.__menu_buttons = [Button([255, 0, 0], [50, 50, 100, 100], Const.Menu.ABOUT), Button([255, 0, 0], [50, 200, 100, 100], Const.Menu.HELP)] 
        self.__state = 0
    def draw(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.__state = 1
            if event.key == pygame.K_2:
                self.__state = 2
            if event.key == pygame.K_ESCAPE:
                return -1
        if self.__state > 0:
            self.__state = self.__menu_actions[self.__state - 1](event)
        else:
            print "Menu"
            self.__screen.fill([0, 0, 0])
            for i in xrange(len(self.__menu_buttons)):
                pygame.draw.rect(self.__screen, 
                                 self.__menu_buttons[i].getColor(),
                                 self.__menu_buttons[i].getArea())
        return Const.Menu.MAIN

class About:
    def __init__(self, screen):
        self.__screen = screen
        self.__page = 0
    def draw(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.__page -= 1
            if event.key == pygame.K_RIGHT:
                self.__page += 1
        print "About: " + str(self.__page)
        self.__screen.fill([255, 0, 0])
        if self.__page < 0:
            self.__page = 0
            return Const.EXIT
        return Const.Menu.ABOUT

class Help:
    def __init__(self, screen):
        self.__screen = screen
        self.__page = 0
    def draw(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.__page -= 1
            if event.key == pygame.K_RIGHT:
                self.__page += 1
        print "Help: " + str(self.__page)
        self.__screen.fill([0, 255, 0])
        if self.__page < 0:
            self.__page = 0
            return Const.EXIT
        return Const.Menu.HELP

class Button:
    """
    Create a new Menu Button. The parameter area takes in values as a List in 
    this order: [x, y, length, height]
    """
    def __init__(self, color, area, index):
        self.__color = color
        self.__area = area
        self.__index = index
    
    """
    Gets the area of this button.
    """
    def getArea(self):
        return self.__area
        
    """
    Gets the color of this button.
    """
    def getColor(self):
        return self.__color
        
    def get_index(self):
        return self.__index
