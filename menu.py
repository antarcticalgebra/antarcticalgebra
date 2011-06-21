#! /usr/bin/env python2
import pygame
from constants import *
from game import Game

class Menu:
    def __init__(self, screen):
        self.__screen = screen
        self.__menu_actions = [Game(self.__screen).draw, About(self.__screen).draw, Help(self.__screen).draw]
        
        # init buttons
        w = self.__screen.get_width()/2
        self.__menu_buttons = [Button([255, 0, 0], [w/2, 100, w, 100], "Play"), 
            Button([255, 0, 0], [w/2, 250, w, 100], "About"), 
            Button([255, 0, 0], [w/2, 400, w, 100], "Help")] 
            
        self.__state = -1
        self.__menu_selection = 0
        
        # init font
        pygame.font.init()
        self.__font = pygame.font.Font(None, 100)
        
    def draw(self, event):
        if self.__state == -1:
            self.__screen.fill([0, 0, 0])
            for i in xrange(len(self.__menu_buttons)):
                area = self.__menu_buttons[i].getArea() # [x, y, width, height]
                
                # draws rectangle for button
                pygame.draw.rect(self.__screen, self.__menu_buttons[i].getColor(), area)
                                 
                # renders the text into label
                label = self.__font.render(self.__menu_buttons[i].getText(), 1, [255, 255, 255])
                
                # calculates centering of the text within the rectangle
                text_width = tuple(label.get_rect())[2]
                x = area[0] + (area[2] - text_width)/2
                y = area[1] + ((area[3] - self.__font.get_height())/2)
                
                # draws the text
                self.__screen.blit(label, [x, y])
            
            if self.__menu_selection > -1:
                pygame.draw.rect(self.__screen, [0, 0, 255], self.__menu_buttons[self.__menu_selection].getArea(), 5)
                
            if event.type == pygame.KEYDOWN:
                # pressing 1, 2, or 3 to go to menu options
                if event.key == pygame.K_1:
                    self.__menu_selection = 0
                if event.key == pygame.K_2:
                    self.__menu_selection = 1
                if event.key == pygame.K_3:
                    self.__menu_selection = 2
                    
                # scrolling through menu options
                if event.key == pygame.K_DOWN:
                    if self.__menu_selection < len(self.__menu_buttons)-1:
                        self.__menu_selection += 1
                if event.key == pygame.K_UP:
                    if self.__menu_selection > 0:
                        self.__menu_selection -= 1
                        
                # selecting a menu option
                if event.key == pygame.K_RETURN:
                    self.__state = self.__menu_selection
                    
                # exiting game
                if event.key == pygame.K_ESCAPE:
                    return Const.EXIT
        else:
            self.__state = self.__menu_actions[self.__state](event)
        
        return Const.MENU

class About:
    def __init__(self, screen):
        self.__screen = screen
        
    def draw(self, event):
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                return State.MAIN
        self.__screen.fill([255, 0, 0])
        return State.ABOUT

class Help:
    def __init__(self, screen):
        self.__screen = screen
        
    def draw(self, event):
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                return State.MAIN
        self.__screen.fill([0, 255, 0])
        return State.HELP

class Button:
    """
    Create a new Menu Button. The parameter area takes in values as a List in 
    this order: [x, y, length, height]
    """
    def __init__(self, color, area, text):
        self.__color = color
        self.__area = area
        self.__text = text
    
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
        
    """
    Gets the text of this button.
    """
    def getText(self):
        return self.__text
