#Author: nickdirienzo
#Began on: 06.08.2011
import pygame
from menu import Menu

def main():
    pygame.init()

    screen_dimensions = pygame.display.list_modes()[0]
    frame = pygame.display.set_mode([screen_dimensions[0]/2, screen_dimensions[1]/2])
    pygame.display.set_caption("Menu Testing")
    pygame.mouse.set_visible(False)
   
    screen = pygame.Surface(frame.get_size()).convert()

    main_menu = Menu(screen)
    game_clock = pygame.time.Clock()
    while True:
        game_clock.tick(40)
        
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return
            
        frame.blit(main_menu.draw(event), [0, 0])
        stage = main_menu.get_stage()
        if stage == -1:
            return
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
