#! /usr/bin/env python
import pygame
import random


class play_level:
    def draw(self, event, level):
        self.__screen.fill([0, 0, 0])
        pygame.font.init()
        font = pygame.font.Font(None, 120)
        ren = font.render("This is level " + str(level), 1, [0, 255, 0])
        self.__screen.blit(ren, [50, 50])
        self.__see_saw.draw()            
        pygame.display.flip()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.__see_saw.move_right(True)
            if event.key == pygame.K_LEFT:
                self.__see_saw.move_left(True)
            if event.key == pygame.K_RETURN:
                return 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.__see_saw.move_right(False)
            if event.key == pygame.K_LEFT:
                self.__see_saw.move_left(False)
        return level

    def __init__(self, screen):
        self.__screen = screen
        self.__see_saw = See_Saw(self.__screen)
        
class See_Saw:
    def __init__(self, parent_screen):
        self.__color = [255, 0, 0]
        self.__length = 200
        self.__height = 25
        self.__x = parent_screen.get_width()/2 - self.__length
        self.__y = parent_screen.get_height() - (self.__height + 10)
        self.__screen = parent_screen
        self.__move_right = False
        self.__move_left = False
        
    def draw(self):
        if self.__move_right:
            self.__x += 5
        if self.__move_left:
            self.__x -= 5
            
        pygame.draw.rect(self.__screen, self.__color, [self.__x, self.__y, self.__length, self.__height])
        
    def move_right(self, bool):
        self.__move_right = bool
        
    def move_left(self, bool):
        self.__move_left = bool
