import pygame
from constants import Const

class Menu:
    
    def __init__(self, screen):
        self.__screen = screen
        self.__menu_items = [[About(self.__screen).draw, Button([255, 0, 0], [50, 50, 100, 100])],
                            [Help(self.__screen).draw, Button([255, 0, 0], [50, 200, 100, 100])]]
        self.__menu_state = 0
        self.__menu_selection = 1
        
    def draw(self, event):
        print str(self.__menu_state) + " " + str(self.__menu_selection)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if self.__menu_selection < len(self.__menu_items) - 1:
                    self.__menu_selection += 1
                else:
                    self.__menu_selection = 0
            elif event.key == pygame.K_UP:
                if self.__menu_selection > 0:
                    self.__menu_selection -= 1
                else:
                    self.__menu_selection = len(self.__menu_items) - 1
            elif event.key == pygame.K_RETURN:
                self.__menu_state = self.__menu_selection
            elif event.key == pygame.K_ESCAPE:
                return Const.EXIT
                
        if self.__menu_state > 0:
            self.__menu_state = self.__menu_items[self.__menu_state - 1][0](event)
        else:
            self.__screen.fill([0, 0, 0])            
            for i in xrange(len(self.__menu_items)):
                pygame.draw.rect(self.__screen, self.__menu_items[i][1].getColor(), self.__menu_items[i][1].getArea())
                                     
            pygame.draw.rect(self.__screen, [0, 0, 255], self.__menu_items[self.__menu_selection - 1][1].getArea(), 5)
                
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
