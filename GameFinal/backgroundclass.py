import pygame, sys
pygame.init()

class Background(pygame.sprite.Sprite):
    def __init__(self, screen, filename):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()
        self.image = pygame.image.load(filename)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = 3995
        self.rect.centery = 300

        self.forwardYES = 0
        self.reverseYES = 0
        self.dx = 0
        self.dy = 0
  
    def update(self):
        if self.forwardYES == 1:
            if self.reverseYES == 0:
                self._move()
        elif self.forwardYES == 0:
            if self.reverseYES == 0:
                return
        if self.reverseYES == 1:
            if self.forwardYES == 0:
                self._move()
        elif self.reverseYES == 0:
            if self.forwardYES == 0:
                return

    def _move(self):
        if self.rect.centerx > 3990: 
            self.rect.centerx = 3990
        if self.rect.centerx < -3190:
            self.rect.centerx = -3190
        self.newpos = self.rect.move((self.dx,self.dy))
        self.rect = self.newpos
        
class ground(pygame.sprite.Sprite):
    def __init__(self, screen, PosX, PosY):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()
        self.image = pygame.Surface((800, 1))
        self.image = self.image.convert()
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = PosX
        self.rect.centery = PosY
        self.dx = 0
        self.dy = 0

    def update(self,lvlbackground):
        if lvlbackground.forwardYES == 1:
            if lvlbackground.reverseYES == 0:
               self._move(lvlbackground)
        elif lvlbackground.forwardYES == 0:
            if lvlbackground.reverseYES == 0:
                return
        if lvlbackground.reverseYES == 1:
            if lvlbackground.forwardYES == 0:
                self._move(lvlbackground)
        elif lvlbackground.reverseYES == 0:
            if lvlbackground.forwardYES == 0:
                return
    def _move(self,lvlbackground):
        if lvlbackground.rect.centerx > 3990: 
            self.dx = 0
        if lvlbackground.rect.centerx < -3190:
            self.dx = 0
        self.newpos = self.rect.move((self.dx,self.dy))
        self.rect = self.newpos

class BossBackground(pygame.sprite.Sprite):
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
  
class Bossground(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()
        self.image = pygame.Surface((800, 1))
        self.image = self.image.convert()
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 425