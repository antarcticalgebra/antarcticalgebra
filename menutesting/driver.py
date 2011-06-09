#Author: nickdirienzo
#Began on: 06.08.2011
import pygame
from menu import Menu

def main():
    pygame.init()

    screenDimensions = pygame.display.list_modes()[0]
    frame = pygame.display.set_mode([screenDimensions[0]/2, screenDimensions[1]/2])
    pygame.display.set_caption("Menu Testing")
   
    screen = pygame.Surface(frame.get_size())

    mainMenu = Menu(screen)
    gameClock = pygame.time.Clock()
    while True:
        gameClock.tick(40)
        if pygame.event.poll().type == pygame.QUIT:
            return
        frame.blit(mainMenu.draw(), [0, 0])
        pygame.display.flip()

if __name__ == "__main__":
    main()
