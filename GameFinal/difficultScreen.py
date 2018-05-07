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
        
class ease(pygame.sprite.Sprite):
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
        self.rect.centerx = 100
        self.rect.centery = 200
        self.active = False
        
    def update(self,mouse):
        self.active = False
        
        #check for mouse input
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if pygame.sprite.collide_mask(self,mouse):
                self.active = True
                 
class medium(pygame.sprite.Sprite):
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
        self.rect.centerx = 300
        self.rect.centery = 200
        self.active = False

    def update(self,mouse):
        self.active = False
        
        #check for mouse input
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if pygame.sprite.collide_mask(self,mouse):
                self.active = True   
        
class hard(pygame.sprite.Sprite):
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
        self.rect.centerx = 500
        self.rect.centery = 200
        self.active = False

    def update(self,mouse):
        self.active = False
        
        #check for mouse input
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if pygame.sprite.collide_mask(self,mouse):
                self.active = True

class extreme(pygame.sprite.Sprite):
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
        self.rect.centerx = 700
        self.rect.centery = 200
        self.active = False

    def update(self,mouse):
        self.active = False
        
        #check for mouse input
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if pygame.sprite.collide_mask(self,mouse):
                self.active = True