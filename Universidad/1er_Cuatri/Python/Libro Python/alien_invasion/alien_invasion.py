
#? Empezando con el desarrollo del juego >> crear una ventana de pygame

import sys
import pygame
from settings import Settings

class AlienInvasion:
    '''Clase para definir el comportamiento de la ventana'''
    def __init__(self):
        '''Inicializa el juego y crea la ventana'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

    def run_game(self):
        '''Empezar el loop del juego'''
        while True:
            '''revisa teclado y mouse'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                '''Redibuja el fondo de pantalla'''
                self.screen.fill(self.settings.bg_color)

                '''refresca la pantalla'''
                pygame.display.flip()
                self.clock.tick(60)

if __name__ == '__main__':
    '''crea una instancia del juego'''
    ia = AlienInvasion()
    ia.run_game()