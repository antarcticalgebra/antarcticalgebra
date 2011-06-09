#Author: nickdirienzo
#Began on: 06.08.2011
import pygame

class Menu:
    """
    Create a new Menu that controls which menu page is displayed. Takes in the 
    Surface object used in the Game class. 
    """
    def __init__(self, screen):
        self.__screen = screen
        self.__b1 = Button([255, 0, 0], [50, 50, 100, 100])
        self.__b2 = Button([255, 0, 0], [50, 200, 100, 100])
        self.__b3 = Button([255, 0, 0], [200, 50, 100, 100])
        self.__b4 = Button([255, 0, 0], [200, 200, 100, 100])
        self.__buttons = [self.__b1, self.__b2, self.__b3, self.__b4]
        self.__menu_selection = 0

    """
    This will take care of everything involved with user interaction and the
    menu. Returns a Surface object to be blit(ed) to the frame.
    """
    def draw(self, event):
        #Main menu selection
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                if self.__menu_selection < len(self.__buttons) - 1:
                    self.__menu_selection += 1
                else:
                    self.__menu_selection = 0
            elif event.key == pygame.K_UP:
                if self.__menu_selection > 0:
                    self.__menu_selection -= 1
                else:
                    self.__menu_selection = len(self.__buttons) - 1
            
        self.__screen.fill([0, 0, 0])
        
        #Draws the buttons
        for i in xrange(len(self.__buttons)):
            pygame.draw.rect(self.__screen, 
                             self.__buttons[i].getColor(),
                             self.__buttons[i].getArea())
        
        #Draws the 'selection outline'
        pygame.draw.rect(self.__screen, [0, 0, 255], 
                         self.__buttons[self.__menu_selection].getArea(), 5)
        return self.__screen

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
