#! /usr/bin/env python
import pygame, pygame.font
from constants import Const

class level_select:
    def draw(self, event):
        self.screen.fill([0, 0, 0])
        
        square_width = self.width/5
        square_height = self.height/3
        spacing = 10
        for x in range(0, 5):
            for y in range(0, 3):
                if [x, y] == self.selected:
                    color = [255, 0, 0]
                else:
                    color = [255, 255, 255]
                
                self.screen.fill(color, 
                [x*square_width + spacing, y*square_height + spacing, 
                square_width - spacing*2, square_height - spacing*2])
                
                pygame.font.init()
                font = pygame.font.Font(None, 120)
                ren = font.render(str(y*5 + x + 1), 1, [0, 255, 0])
                self.screen.blit(ren, [x*square_width + 3*spacing, 
                    y*square_height + 3*spacing])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.selected[1] > 0:
                self.selected[1] -= 1
            if event.key == pygame.K_DOWN and self.selected[1] < 2:
                self.selected[1] += 1
            if event.key == pygame.K_LEFT and self.selected[0] > 0:
                self.selected[0] -= 1
            if event.key == pygame.K_RIGHT and self.selected[0] < 4:
                self.selected[0] += 1
            if event.key == pygame.K_RETURN:
                return (self.selected[1]*5 + self.selected[0] + 1)
            if event.key == pygame.K_BACKSPACE:
                return Const.EXIT
        pygame.display.flip()
        
    def __init__(self, screen):
        self.screen = screen
        self.width = 800
        self.height = 600
        self.selected = [0, 0]
