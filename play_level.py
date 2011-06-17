#! /usr/bin/env python
import pygame,random,constants
from fractions import gcd
pygame.font.init()
font = pygame.font.Font(None, 120)
BLACK = [0,0,0]

class play_level:
    def draw(self, event, level):
        self.screen.fill(BLACK)
        self.variables=level+1
        self.objectvalues=[0,0,0]
        if level != self.lastlevel:
            self.lastlevel=level
            self.generateEquation()
        ren = font.render("This is level " + str(level), 1, [0, 255, 0])
        self.screen.blit(ren, [50, 50])
        pygame.display.flip()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return 0
        return level

    def generateEquation(self, complexity=None):
        if complexity == None:
            complexity=self.variables
        if complexity > 3:
            complexity = 3
        for i in range(0,complexity):
            self.objectvalues[i]=random.randint(1,15)
        equationtype=random.randint(0,3)
        
        if equationtype==constants.Const.EquationForm.SLOPEINTERCEPT:
            
            if complexity == 2:
                
                if random.randint(0,1):
                    slope = self.objectvalues[0] / self.objectvalues[1]
                    intercept = self.objectvalues[0] % self.objectvalues[1]
                    self.equation = '[]=' + str(slope) + 'O+' + str(intercept)
                    print self.equation
                else:
                    slope = self.objectvalues[1] / self.objectvalues[0]
                    intercept= self.objectvalues[1] % self.objectvalues[0]
                    self.equation= 'O=' + str(slope) + '[]+' + str(intercept)
                    print self.equation
            elif complexity == 3:
                order=random.randint(0,2)
                if order==0:
                    slope = self.objectvalues[0] / (self.objectvalues[1] \
                     + self.objectvalues[2])
                    intercept = self.objectvalues[0] % (self.objectvalues[1] \
                     + self.objectvalues[2])
                    self.equation= '[]=' + str(slope) + '(O+/_\)+' + str(intercept)
                    print self.equation
                elif order == 1:
                    slope = self.objectvalues[1] / (self.objectvalues[0] \
                     + self.objectvalues[2])
                    intercept = self.objectvalues[1] % (self.objectvalues[0] \
                     + self.objectvalues[2])
                    self.equation= 'O=' + str(slope) + '([]+/_\)+' + str(intercept)
                    print self.equation
                elif order == 2:
                    slope = self.objectvalues[2] / (self.objectvalues[1] \
                     + self.objectvalues[0])
                    intercept = self.objectvalues[2] % (self.objectvalues[1] \
                     + self.objectvalues[0])
                    self.equation= '/_\=' + str(slope) + '([]+O)+' + str(intercept)
                    print self.equation
        elif equationtype==constants.Const.EquationForm.STANDARD:
            if complexity==2:
                coefficients=[random.randint(1,5),random.randint(1,5)]
                sumofvalues=(self.objectvalues[0] * coefficients[0]) \
                 + (self.objectvalues[1] * coefficients[1])
                self.equation= str(coefficients[0]) + 'O+' \
                 + str(coefficients[1]) + '[]=' + str(sumofvalues)
                print self.equation
            elif complexity==3:
                coefficients=[random.randint(1,5),random.randint(1,5), \
                 random.randint(1,5)]
                sumofvalues=(self.objectvalues[0] * coefficients[0]) \
                 + (self.objectvalues[1] * coefficients[1]) \
                 + (self.objectvalues[2] * coefficients[2])
                self.equation= str(coefficients[0]) + 'O+' \
                 + str(coefficients[1]) + '[]+' + str(coefficients[2]) \
                 + '/_\=' + str(sumofvalues)
                print self.equation
                
                
        elif equationtype==constants.Const.EquationForm.UNSIMPLIFIEDSI:
            
            
            if complexity == 2:
                if random.randint(0,1):
                    slope = self.objectvalues[0] / self.objectvalues[1]
                    intercept = self.objectvalues[0] % self.objectvalues[1]
                    coefficient = random.randint(1,5)
                    slope *= coefficient
                    intercept *=coefficient
                    self.equation = str(coefficient) + '[]=' + str(slope) \
                     + 'O+' + str(intercept)
                    print self.equation
                else:
                    slope = self.objectvalues[1] / self.objectvalues[0]
                    intercept= self.objectvalues[1] % self.objectvalues[0]
                    coefficient = random.randint(1,5)
                    slope *= coefficient
                    intercept *=coefficient
                    self.equation = str(coefficient) + '[]=' + str(slope) \
                     + 'O+' + str(intercept)
                    print self.equation
            elif complexity == 3:
                order=random.randint(0,2)
                if order==0:
                    slope = self.objectvalues[0] / (self.objectvalues[1] \
                     + self.objectvalues[2])
                    intercept = self.objectvalues[0] % (self.objectvalues[1] \
                     + self.objectvalues[2])
                    coefficient = random.randint(1,5)
                    slope *= coefficient
                    intercept *=coefficient
                    self.equation= str(coefficient) + '[]=' + str(slope) \
                     + '(O+/_\)+' + str(intercept)
                    print self.equation
                elif order == 1:
                    slope = self.objectvalues[1] / (self.objectvalues[0] \
                     + self.objectvalues[2])
                    intercept = self.objectvalues[1] % (self.objectvalues[0] \
                     + self.objectvalues[2])
                    coefficient = random.randint(1,5)
                    slope *= coefficient
                    intercept *=coefficient
                    self.equation= str(coefficient) + 'O=' + str(slope) \
                     + '([]+/_\)+' + str(intercept)
                    print self.equation
                elif order == 2:
                    slope = self.objectvalues[2] / (self.objectvalues[1] \
                     + self.objectvalues[0])
                    intercept = self.objectvalues[2] % (self.objectvalues[1] \
                     + self.objectvalues[0])
                    coefficient = random.randint(1,5)
                    slope *= coefficient
                    intercept *=coefficient
                    self.equation= str(coefficient) + '/_\=' + str(slope) \
                     + '([]+O)+' + str(intercept)
                    print self.equation
        elif equationtype==constants.Const.EquationForm.NOCONSTANTS:
            if complexity == 2:
                greatestdivisor=gcd(self.objectvalues[0],self.objectvalues[1])
                self.equation=str(self.objectvalues[1]/greatestdivisor) + '[]=' \
                 + str(self.objectvalues[0]/greatestdivisor) + 'O'
                print self.equation
            elif complexity == 3:
                sumofvalues=self.objectvalues[1]+self.objectvalues[2]
                greatestdivisor=gcd(self.objectvalues[0],sumofvalues)
                self.equation=str(sumofvalues/greatestdivisor) + '[]=' \
                 + str(self.objectvalues[0]/greatestdivisor) + '(O+/_\)'
                print self.equation

    def __init__(self, screen):
        self.screen = screen
        self.lastlevel = 0
