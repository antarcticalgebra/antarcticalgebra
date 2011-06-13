#! /usr/bin/env python
import olpcgames, pygame
from menu import menu
from game import game

def main():
    size = (800,600)
    if olpcgames.ACTIVITY:
        size = olpcgames.ACTIVITY.game_size
        
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    
    state = 1
    states = [menu(screen).draw, game(screen).draw]

    running = True
    while running:
        milliseconds = clock.tick(25) # maximum number of frames per second
        
        events = pygame.event.get()
        if events:
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            pygame.display.flip()
        
        state = states[state](events) # sets the state of the game.

if __name__ == "__main__":
    main()
