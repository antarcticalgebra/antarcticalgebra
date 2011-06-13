# Author: Nick DiRienzo nickdirienzo
# Began on: 06.08.2011
import pygame
from constants import Const

class Menu:
    
    def __init__(self, screen):
        self.__screen = screen
        self.__menu_items = [[About(self.__screen).draw, Button([255, 0, 0], [50, 50, 100, 100])],
                            [Help(self.__screen).draw, Button([255, 0, 0], [50, 200, 100, 100])]]
                            
        self.__menu_state = 0
        self.__menu_selection = Const.Menu.ABOUT
        
        self.__first_run = True
        self.__keypressed = False
        self.__item_selected = False
        
        self.__bg_color = [0, 0, 0]
        self.__select_color = [0, 0, 255]
        
    def draw(self, event):
        if event.type == pygame.KEYDOWN:
            self.__keypressed = True
            if event.key == pygame.K_DOWN:
                print "Key down"
                if self.__menu_selection < len(self.__menu_items) - 1:
                    self.__menu_selection += 1
                else:
                    self.__menu_selection = 0
            elif event.key == pygame.K_UP:
                print "Key Up"
                if self.__menu_selection > 0:
                    self.__menu_selection -= 1
                else:
                    self.__menu_selection = len(self.__menu_items) - 1
            elif event.key == pygame.K_RETURN:
                self.__menu_state = self.__menu_selection
                self.__item_selected = True
            elif event.key == pygame.K_ESCAPE:
                return Const.EXIT
                
        if self.__item_selected:
            print self.__menu_state
            self.__menu_state = self.__menu_items[self.__menu_state - 1][0](event)
            self.__first_run = True
        else:
            if self.__first_run:    
                self.__screen.fill(self.__bg_color)            
                for i in xrange(len(self.__menu_items)):
                    pygame.draw.rect(self.__screen, self.__menu_items[i][1].getColor(), self.__menu_items[i][1].getArea())
                    pygame.draw.rect(self.__screen, self.__bg_color, self.__menu_items[i][1].getArea(), 5)
                pygame.draw.rect(self.__screen, self.__select_color, self.__menu_items[0][1].getArea(), 5)
                self.__first_run = False
                
            if self.__keypressed:
                for i in xrange(len(self.__menu_items)):
                    pygame.draw.rect(self.__screen, self.__bg_color, self.__menu_items[i][1].getArea(), 5)
                pygame.draw.rect(self.__screen, self.__select_color, self.__menu_items[self.__menu_selection][1].getArea(), 5)
                        
        self.__keypressed = False
        return Const.Menu.MAIN

class About:
    
    def __init__(self, screen):
        self.__screen = screen
        self.__page = 0
        
        self.__first_run = True
        
    def draw(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.__page -= 1
            if event.key == pygame.K_RIGHT:
                self.__page += 1
                
        if self.__first_run:
            self.__screen.fill([255, 0, 0])
            
        if self.__page < 0:
            self.__page = 0
            return Const.EXIT
        else:
            return Const.Menu.ABOUT

class Help:
    
    def __init__(self, screen):
        self.__screen = screen
        self.__page = 0
        
        self.__first_run = True
        
    def draw(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.__page -= 1
            if event.key == pygame.K_RIGHT:
                self.__page += 1
                
        if self.__first_run:
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
