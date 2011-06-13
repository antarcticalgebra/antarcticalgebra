#Author: nickdirienzo
#Began on: 06.08.2011
import pygame
from menu import Menu

def main():
    pygame.init()

    screen_dimensions = pygame.display.list_modes()[0]
    screen = pygame.display.set_mode([screen_dimensions[0]/2, screen_dimensions[1]/2])
    pygame.display.set_caption("Menu Testing")
    pygame.mouse.set_visible(False)

    state = 0
    states = [Menu(screen).draw]

    game_clock = pygame.time.Clock()
    while True:
        game_clock.tick(40)
        
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            return
            
        state = states[state](event)
        if state == -1:
            pygame.quit()
            return
        pygame.display.flip()
    

if __name__ == "__main__":
    main()
