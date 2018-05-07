import pygame, sys
pygame.init()

class startscreen(pygame.sprite.Sprite):
    def __init__(self, screen, filename):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()
        self.image = pygame.image.load(filename)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 300
        
class HaloGraphic(pygame.sprite.Sprite):
    def __init__(self, screen, graphicname):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()
        self.image = pygame.image.load(graphicname)
        self.transColor = self.image.get_at((5, 5))
        self.image.set_colorkey(self.transColor)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.left = 325
        self.rect.top = 0
        
class tempMouse(pygame.sprite.Sprite):
    def __init__(self, screen, filename):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()
        self.image = pygame.image.load(filename)
        self.transColor = self.image.get_at((1, 1))
        self.image.set_colorkey(self.transColor)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = (1,1)


    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.topleft = pos