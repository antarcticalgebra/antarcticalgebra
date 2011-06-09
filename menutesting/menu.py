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
        self.__menu_items = [
            [self.__b1, About(self.__screen)],
            [self.__b2, Scores(self.__screen)],
            [self.__b3, None],
            [self.__b4, None]
        ]
        self.__main_menu_selection = 0
        self.__menu_stage = -1
        self.__stage = 0
        
    def get_stage(self):
        return self.__stage

    """
    This will take care of everything involved with user interaction and the
    menu. Returns a Surface object to be blit(ed) to the frame.
    """
    def draw(self, event):
              
        if self.__menu_stage == -1:
            #Main menu selection
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    if self.__main_menu_selection < len(self.__menu_items) - 1:
                        self.__main_menu_selection += 1
                    else:
                        self.__main_menu_selection = 0
                elif event.key == pygame.K_UP:
                    if self.__main_menu_selection > 0:
                        self.__main_menu_selection -= 1
                    else:
                        self.__main_menu_selection = len(self.__menu_items) - 1
                elif event.key == pygame.K_ESCAPE:
                    self.__stage = -1
                elif event.key == pygame.K_RETURN:
                    self.__menu_stage = self.__main_menu_selection
                
            self.__screen.fill([0, 0, 0])
            
            #Draws the buttons
            for i in xrange(len(self.__menu_items)):
                pygame.draw.rect(self.__screen, 
                                 self.__menu_items[i][0].getColor(),
                                 self.__menu_items[i][0].getArea())
            
            #Draws the 'selection outline'
            pygame.draw.rect(self.__screen, [0, 0, 255], 
                             self.__menu_items[self.__main_menu_selection][0].getArea(), 5)
         
        else:
            self.__screen = self.__menu_items[self.__menu_stage][1].draw(event)
            self.__menu_stage = self.__menu_items[self.__menu_stage][1].get_stage()
            
        return self.__screen
        
class About:
    
    def __init__(self, screen):
        self.__screen = screen
        self.__font = pygame.font.Font(None, 36)
        self.__stage = 0
        
    def draw(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.__stage -= 1
            elif event.key == pygame.K_RIGHT:
                self.__stage += 1
                
        self.__screen.fill([255, 0, 0])
        return self.__screen
        
    def get_stage(self):
        if self.__stage < 0:
            temp = -1
            self.__stage = 0
            return temp
        return self.__stage
        
class Scores:
    
    def __init__(self, screen):
        self.__screen = screen
        self.__font = pygame.font.Font(None, 36)
        self.__stage = 1
        
    def draw(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.__stage -= 1
            elif event.key == pygame.K_RIGHT:
                self.__stage += 1
                
        self.__screen.fill([0, 255, 0])
        return self.__screen
        
    def get_stage(self):
        if self.__stage < 1:
            temp = -1
            self.__stage = 0
            return temp
        return self.__stage

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
