import pygame

class Ship:
    '''clase para adminisitrar la nave'''

    def __init__(self, ia_game):
        '''inicializa la nave y estable la posicion inicial'''
        self.screen = ia_game.screen
        self.screen_rect = ia_game.screen.get_rect()

        '''carga la imagen'''
        self.image = pygame.image.load('/Users/aviantowebstudio/Downloads/Alexis/Universidad/1er_Cuatri/Hybridge_1/Universidad/1er_Cuatri/Python/Libro Python/Images/foto.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()

        '''empieza en la parte inferior centrada'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
    
    def update(self):
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        '''pone la imagen en la ubicacion actual'''
        self.screen.blit(self.image, self.rect)
        