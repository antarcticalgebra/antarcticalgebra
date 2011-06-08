#! /usr/bin/env python
import olpcgames, pygame
from menu import menu

def main():
    size = (800,600)
    if olpcgames.ACTIVITY:
        size = olpcgames.ACTIVITY.game_size
        
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    
    state = 0
    states = [menu(screen).draw]

    running = True
    while running:
        milliseconds = clock.tick(25) # maximum number of frames per second
        
        state = states[state]() # sets the state of the game.
        
        events = pygame.event.get()
        if events:
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            pygame.display.flip()

if __name__ == "__main__":
    main()
