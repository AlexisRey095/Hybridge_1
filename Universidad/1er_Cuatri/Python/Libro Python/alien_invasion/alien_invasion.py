
#? Empezando con el desarrollo del juego >> crear una ventana de pygame

import sys
import pygame
from settings import Settings
from ship import Ship

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
        self.ship = Ship(self)

    def run_game(self):
        '''Empezar el loop del juego'''
        while True:
            '''revisa teclado y mouse'''
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        '''Responde al tocar teclas  '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                
           
    def _update_screen(self):
        '''Redibuja el fondo de pantalla'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()        

        '''refresca la pantalla'''
        pygame.display.flip()
        



if __name__ == '__main__':
    '''crea una instancia del juego'''
    ia = AlienInvasion()
    ia.run_game()