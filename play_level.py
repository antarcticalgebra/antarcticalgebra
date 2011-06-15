#! /usr/bin/env python
import pygame,random,constants
pygame.font.init()
font = pygame.font.Font(None, 120)
BLACK = [0,0,0]

class play_level:
    def draw(self, event, level):
        self.screen.fill(BLACK)
        self.variables=level+1
        self.objectvalues=[0,0,0]
        self.equation=''
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
            self.objectvalues[i]=random.randint(1,10)
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
            elif complexity == 3:
                order=randon.randint(0,3)
                if order==0:
                    slope = self.objectvalues[0] / (self.objectvalues[1] + self.objectvalues[2])
                    slope = self.objectvalues[0] % (self.objectvalues[1] + self.objectvalues[2])
                    self.equation= 'O=' + str(slope) + '([]+/_\)+' + str(intercept)
                #elif
                    

    def __init__(self, screen):
        self.screen = screen
