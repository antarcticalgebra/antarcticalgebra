#! /usr/bin/env python
import pygame

class play_level:
    def draw(self, event, level):
        self.screen.fill([0, 0, 0])
        pygame.font.init()
        font = pygame.font.Font(None, 120)
        ren = font.render("This is level " + str(level), 1, [0, 255, 0])
        self.screen.blit(ren, [50, 50])
        pygame.display.flip()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return 0
        return level

    def __init__(self, screen):
        self.screen = screen
