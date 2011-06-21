#! /usr/bin/env python2
import pygame,constants
from random import randint
from fractions import gcd

class Equation:
    
    def __init__(self):
        self.objectvalues=[0,0,0]
    
    def generateEquation(self, complexity=None):
        if complexity == None:
            complexity=self.variables
        if complexity > 3:
            complexity = 3
        for i in range(0,complexity):
            self.objectvalues[i]=randint(1,15)
        equationtype=randint(0,3)
        
        if equationtype==constants.EquationForm.SLOPEINTERCEPT:
            
            if complexity == 2:
                
                if randint(0,1):
                    slope = self.objectvalues[0] / self.objectvalues[1]
                    intercept = self.objectvalues[0] % self.objectvalues[1]
                    self.equation = '[]=' + str(slope) + 'O+' + str(intercept)
                    return self.equation
                else:
                    slope = self.objectvalues[1] / self.objectvalues[0]
                    intercept= self.objectvalues[1] % self.objectvalues[0]
                    self.equation= 'O=' + str(slope) + '[]+' + str(intercept)
                    return self.equation
            elif complexity == 3:
                order=randint(0,2)
                if order==0:
                    slope = self.objectvalues[0] / (self.objectvalues[1] \
                     + self.objectvalues[2])
                    intercept = self.objectvalues[0] % (self.objectvalues[1] \
                     + self.objectvalues[2])
                    self.equation= '[]=' + str(slope) + '(O+/_\)+' + str(intercept)
                    return self.equation
                elif order == 1:
                    slope = self.objectvalues[1] / (self.objectvalues[0] \
                     + self.objectvalues[2])
                    intercept = self.objectvalues[1] % (self.objectvalues[0] \
                     + self.objectvalues[2])
                    self.equation= 'O=' + str(slope) + '([]+/_\)+' + str(intercept)
                    return self.equation
                elif order == 2:
                    slope = self.objectvalues[2] / (self.objectvalues[1] \
                     + self.objectvalues[0])
                    intercept = self.objectvalues[2] % (self.objectvalues[1] \
                     + self.objectvalues[0])
                    self.equation= '/_\=' + str(slope) + '([]+O)+' + str(intercept)
                    return self.equation
        elif equationtype==constants.EquationForm.STANDARD:
            if complexity==2:
                coefficients=[randint(1,5),randint(1,5)]
                sumofvalues=(self.objectvalues[0] * coefficients[0]) \
                 + (self.objectvalues[1] * coefficients[1])
                self.equation= str(coefficients[0]) + 'O+' \
                 + str(coefficients[1]) + '[]=' + str(sumofvalues)
                return self.equation
            elif complexity==3:
                coefficients=[randint(1,5),randint(1,5), \
                 randint(1,5)]
                sumofvalues=(self.objectvalues[0] * coefficients[0]) \
                 + (self.objectvalues[1] * coefficients[1]) \
                 + (self.objectvalues[2] * coefficients[2])
                self.equation= str(coefficients[0]) + 'O+' \
                 + str(coefficients[1]) + '[]+' + str(coefficients[2]) \
                 + '/_\=' + str(sumofvalues)
                return self.equation
                
                
        elif equationtype==constants.EquationForm.UNSIMPLIFIEDSI:
            
            
            if complexity == 2:
                if randint(0,1):
                    slope = self.objectvalues[0] / self.objectvalues[1]
                    intercept = self.objectvalues[0] % self.objectvalues[1]
                    coefficient = randint(1,5)
                    slope *= coefficient
                    intercept *=coefficient
                    self.equation = str(coefficient) + '[]=' + str(slope) \
                     + 'O+' + str(intercept)
                    return self.equation
                else:
                    slope = self.objectvalues[1] / self.objectvalues[0]
                    intercept= self.objectvalues[1] % self.objectvalues[0]
                    coefficient = randint(1,5)
                    slope *= coefficient
                    intercept *=coefficient
                    self.equation = str(coefficient) + '[]=' + str(slope) \
                     + 'O+' + str(intercept)
                    return self.equation
            elif complexity == 3:
                order=randint(0,2)
                if order==0:
                    slope = self.objectvalues[0] / (self.objectvalues[1] \
                     + self.objectvalues[2])
                    intercept = self.objectvalues[0] % (self.objectvalues[1] \
                     + self.objectvalues[2])
                    coefficient = randint(1,5)
                    slope *= coefficient
                    intercept *=coefficient
                    self.equation= str(coefficient) + '[]=' + str(slope) \
                     + '(O+/_\)+' + str(intercept)
                    return self.equation
                elif order == 1:
                    slope = self.objectvalues[1] / (self.objectvalues[0] \
                     + self.objectvalues[2])
                    intercept = self.objectvalues[1] % (self.objectvalues[0] \
                     + self.objectvalues[2])
                    coefficient = randint(1,5)
                    slope *= coefficient
                    intercept *=coefficient
                    self.equation= str(coefficient) + 'O=' + str(slope) \
                     + '([]+/_\)+' + str(intercept)
                    return self.equation
                elif order == 2:
                    slope = self.objectvalues[2] / (self.objectvalues[1] \
                     + self.objectvalues[0])
                    intercept = self.objectvalues[2] % (self.objectvalues[1] \
                     + self.objectvalues[0])
                    coefficient = randint(1,5)
                    slope *= coefficient
                    intercept *=coefficient
                    self.equation= str(coefficient) + '/_\=' + str(slope) \
                     + '([]+O)+' + str(intercept)
                    return self.equation
        elif equationtype==constants.EquationForm.NOCONSTANTS:
            if complexity == 2:
                greatestdivisor=gcd(self.objectvalues[0],self.objectvalues[1])
                self.equation=str(self.objectvalues[1]/greatestdivisor) + '[]=' \
                 + str(self.objectvalues[0]/greatestdivisor) + 'O'
                return self.equation
            elif complexity == 3:
                sumofvalues=self.objectvalues[1]+self.objectvalues[2]
                greatestdivisor=gcd(self.objectvalues[0],sumofvalues)
                self.equation=str(sumofvalues/greatestdivisor) + '[]=' \
                 + str(self.objectvalues[0]/greatestdivisor) + '(O+/_\)'
                return self.equation
