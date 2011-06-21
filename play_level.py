#! /usr/bin/env python
import pygame
import random
import time
from equation import Equation

class play_level:
    def draw(self, event, level):
        self.__screen.fill([0, 0, 0])
        pygame.font.init()
        font = pygame.font.Font(None, 100)
        ren = font.render("This is level " + str(level), 1, [0, 255, 0])
        square_count_text = font.render("Squares caught: " + str(self.__square_count), 1, [0, 255, 0])
        eq_text = font.render(self.__eq, 1, [0, 255, 0])
        self.__screen.blit(ren, [25, 50])
        self.__screen.blit(square_count_text, [25, 200])
        self.__screen.blit(eq_text, [25, 350])
        self.__see_saw.draw()
        self.__cur_time = time.time()
        
        if (self.__cur_time - self.__start_time) < self.__drop_time:
            if self.__square.get_x() > self.__see_saw.get_upper_left_corner()[0] and self.__square.get_x() < self.__see_saw.get_upper_right_corner()[0]:
                if self.__square.get_height_constraint() < self.__see_saw.get_upper_left_corner()[1] and self.__square.get_height_constraint() > self.__see_saw.get_lower_right_corner()[1]:
                    self.__square_count += 1
                    self.__generate_square()
         
            self.__square.draw((self.__cur_time - self.__start_time), self.__drop_time, self.__drop_height)
        else:
            self.__generate_square()
            
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
        
    def __generate_square(self):
        self.__square = Droppable_Square(self.__screen)
        self.__start_time = time.time()

    def __init__(self, screen):
        self.__screen = screen
        self.__seesaw_gap = 10
        self.__see_saw = See_Saw(self.__screen, self.__seesaw_gap)
        self.__start_time = time.time()
        self.__cur_time = None
        self.__drop_time = 5 #in seconds
        self.__square =  Droppable_Square(self.__screen)
        self.__drop_height = self.__screen.get_height() - (self.__see_saw.get_height() + self.__seesaw_gap)
        self.__square_count = 0
        self.__eq = Equation().generateEquation(2)
        
        
class Droppable_Square:
    def __init__(self, parent_screen):
        colors = [[255,0,0], [0,255,0], [0,0,255]]
        self.__color = colors[random.randint(0, len(colors)-1)]
        self.__size = 50
        self.__x = random.randint(0, parent_screen.get_width() - self.__size)
        self.__y = 0
        self.__screen = parent_screen
        
    def draw(self, time_elapsed, drop_time, drop_height):
        self.__y = (time_elapsed / drop_time) * drop_height
        pygame.draw.rect(self.__screen, self.__color, [self.__x, self.__y, self.__size, self.__size])
        
    def get_size(self):
        return self.__size
        
    def get_x(self):
        return self.__x
        
    def get_y(self):
        return self.__y
        
    def get_height_constraint(self):
        return self.__y + (self.__size - 10)
        
        
class See_Saw:
    def __init__(self, parent_screen, gap):
        self.__color = [255, 0, 0]
        self.__length = 200
        self.__height = 25
        self.__x = parent_screen.get_width()/2 - self.__length
        self.__y = parent_screen.get_height() - (self.__height + gap)
        self.__screen = parent_screen
        self.__move_right = False
        self.__move_left = False
        
    def draw(self):
        if (self.__x + self.__length) > self.__screen.get_width():
            self.__x = self.__screen.get_width() - self.__length
        elif self.__move_right:
            self.__x += 5
            
        if self.__x < 0:
            self.__x = 0
        elif self.__move_left:
            self.__x -= 5
            
        pygame.draw.rect(self.__screen, self.__color, [self.__x, self.__y, self.__length, self.__height])
        
    def move_right(self, bool):
        self.__move_right = bool
        
    def move_left(self, bool):
        self.__move_left = bool
        
    def get_height(self):
        return self.__height
        
    def get_upper_left_corner(self):
        return [self.__x, self.__y]
        
    def get_upper_right_corner(self):
        return [self.__x + self.__length, self.__y]
        
    def get_lower_right_corner(self):
        return [self.__x + self.__length, self.__y - self.__height]
        
    def get_lower_left_corner(self):
        return [self.__x, self.__y - self.__height]
