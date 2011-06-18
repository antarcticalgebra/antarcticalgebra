#! /usr/bin/env python2
import pygame
from menu import Menu
from game import game

def main():
    pygame.init()
    size = (800,600)
        
    pygame.display.set_caption("Antarctic Algebra Proof of Concept")
    pygame.mouse.set_visible(False)
    
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    
    state = 0
    states = [Menu(screen).draw, game(screen).draw]

    running = True
    while running:
        milliseconds = clock.tick(60) # maximum number of frames per second
        
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        pygame.display.flip()
        
        state = states[state](event) # sets the state of the game.
    pygame.quit()

if __name__ == "__main__":
    main()
