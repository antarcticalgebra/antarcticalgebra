import pygame
from constants import Const

class Menu:
    def __init__(self, screen):
        self.__screen = screen
        self.__menu_actions = [None, About(self.__screen).draw, Help(self.__screen).draw]
        self.__menu_buttons = [Button([255, 0, 0], [50, 50, 100, 100]), Button([255, 0, 0], [50, 200, 100, 100]), Button([255, 0, 0], [200, 50, 100, 100])] 
        self.__state = 0
        self.__menu_selection = 1
    def draw(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                #self.__state = 1
                self.__menu_selection = 1
            if event.key == pygame.K_2:
                #self.__state = 2
                self.__menu_selection = 2
            if event.key == pygame.K_3:
                self.__menu_selection = 3
            if event.key == pygame.K_DOWN:
                if self.__menu_selection < len(self.__menu_buttons):
                    self.__menu_selection += 1
                else:
                    self.__menu_selection = 1
            if event.key == pygame.K_UP:
                if self.__menu_selection > 1:
                    self.__menu_selection -= 1
                else:
                    self.__menu_selection = len(self.__menu_buttons)
            if event.key == pygame.K_RETURN:
                self.__state = self.__menu_selection
            if event.key == pygame.K_ESCAPE:
                return Const.EXIT
        if self.__state > 0:
            if self.__state == 1:
                return Const.GAME
            else:
                self.__state = self.__menu_actions[self.__state - 1](event)
        else:
            self.__screen.fill([0, 0, 0])
            for i in xrange(len(self.__menu_buttons)):
                pygame.draw.rect(self.__screen, 
                                 self.__menu_buttons[i].getColor(),
                                 self.__menu_buttons[i].getArea())
            if self.__menu_selection > 0:
                pygame.draw.rect(self.__screen, [0, 0, 255], self.__menu_buttons[self.__menu_selection - 1].getArea(), 5)
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
    def __init__(self, color, area):
        self.__color = color
        self.__area = area
    
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
