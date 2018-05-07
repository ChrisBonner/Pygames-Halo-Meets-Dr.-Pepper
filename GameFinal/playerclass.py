import pygame, os, sys, math
pygame.init()

class player(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        self.frame = 6
        self.delay = 5
        self.pause = 0
        self.reverseYES = 0
        self.forwardYES = 0
        self.justpressed = 1
        self.image = self.imgListFwd[6]
        self.rect = self.image.get_rect()
        self.rect.centerx = 300
        self.rect.centery = 380
        self.life = 10
        self.shield = 10
        self.x = 0
        self.jumping = -1
        self.gravityY = 0
        self.old_x = self.rect.centerx
        self.old_y = self.rect.centery
        self.shieldcap = 0
        self.offscreen = 0
        self.dx = 5
    def loadImages(self):
        try:
        ##forward image load
            imgForwardMaster = pygame.image.load(os.path.join('Sprites','masterchief.png'))
        except:
            sys.exit("could not load image files in 'Sprites' folder :-(")
        imgForwardMaster = imgForwardMaster.convert()
        
        self.imgListFwd = []
        
        imgSize = ((58, 65), (56, 65), (52,65), (54, 65), (52, 65), (52,65), (50, 67))
        offset = ((841, 168),(906, 168),(969, 168),(1027, 168),(1087,168),(1149,168), (841, 14))

        for i in range(7):
            fwdImage = pygame.Surface(imgSize[i])
            fwdImage.blit(imgForwardMaster, (0, 0), (offset[i], imgSize[i]))
            transColor = fwdImage.get_at((1, 1))
            fwdImage.set_colorkey(transColor)
            self.imgListFwd.append(fwdImage)
        try:
        ##reverse image load
            imgReverseMaster = pygame.image.load(os.path.join('Sprites','masterchief.png'))
        except:
            sys.exit("could not load image files in 'Sprites' folder :-(")
        imgReverseMaster = imgReverseMaster.convert()
        
        self.imgListRvs = []
        
        imgSize = ((58, 65), (56, 65), (52,65), (54, 65), (52, 65), (52,65), (50, 67))
        offset = ((841, 168),(906, 168),(969, 168),(1027, 168),(1087,168),(1149,168), (841, 14))

        for i in range(7):
            RvsImage = pygame.Surface(imgSize[i])
            RvsImage.blit(imgReverseMaster, (0, 0), (offset[i],imgSize[i]))
            transColor = RvsImage.get_at((0, 0))
            RvsImage.set_colorkey(transColor)
            self.imgListRvs.append(RvsImage)
        for i in range(7):
           self.imgListRvs[i] = pygame.transform.flip(self.imgListRvs[i], 1, 0)

    def update(self,floor):
        if self.offscreen == 0:
            if self.jumping == 1:
                self.jump(floor)
            self.shieldregen()
            if self.forwardYES == 1:
                if self.reverseYES == 0:
                    self.forward()
            elif self.forwardYES == 0:
                if self.reverseYES == 0:
                    self.stop()
            if self.reverseYES == 1:
                if self.forwardYES == 0:
                    self.reverse()
            elif self.reverseYES == 0:
                if self.forwardYES == 0:
                    self.stop()
        elif self.offscreen == 1:
            self.endlvl()
    def stop(self):
        ##forward
        if self.justpressed == 1:
            self.oldy = self.rect.centery
            self.image = self.imgListFwd[6]
            self.rect = self.image.get_rect()
            self.rect.centerx = 300
            self.rect.centery = self.oldy
        ##reverse
        elif self.justpressed == 2:
            self.oldy = self.rect.centery
            self.image = self.imgListRvs[6]
            self.rect = self.image.get_rect()
            self.rect.centerx = 300
            self.rect.centery = self.oldy
    def forward(self):
        self.oldy = self.rect.centery
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            if self.frame >= 5:  
                self.frame = 0
            else:
                self.frame += 1    
            self.image = self.imgListFwd[self.frame]
            self.rect = self.image.get_rect()
            self.rect.centerx = 300
            self.rect.centery = self.oldy
    def reverse(self):
        self.pause += 1
        self.oldy = self.rect.centery
        if self.pause >= self.delay:
            self.pause = 0
            if self.frame >= 5:  
                self.frame = 0
            else:
                self.frame += 1
            self.image = self.imgListRvs[self.frame]
            self.rect = self.image.get_rect()
            self.rect.centerx = 300
            self.rect.centery = self.oldy
 
    def jump(self,floor):
        collide = pygame.sprite.spritecollide(self, floor, False)
        if collide:
            self.jumping = 0
            self.rect.centery = 380
        else:
            self.old_y = self.rect.centery
            self.rect.centery -= self.gravityY
            self.gravityY -= .20
            
    def shieldregen(self):
        if self.x >= self.shieldcap:
            self.x = self.shieldcap
        elif self.x < self.shieldcap:
            self.x += 1
        if self.x >= self.shieldcap:
            if self.shield < 10:
                self.shield += 1
    
    def endlvl(self):
        self.oldy = self.rect.centery
        self.rect.centerx += self.dx
        self.oldx = self.rect.centerx
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            if self.frame >= 5:  
                self.frame = 0
            else:
                self.frame += 1    
            self.image = self.imgListFwd[self.frame]
            self.rect = self.image.get_rect()
            self.rect.centerx = self.oldx
            self.rect.centery = self.oldy
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, filename, StartPosx, StartPosy, dir):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()
        self.image = pygame.image.load(filename)
        self.transColor = self.image.get_at((0, 0))
        self.image.set_colorkey(self.transColor)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = StartPosx
        self.rect.centery = StartPosy
        self.dir = dir
        self.dx = 3
        self.dy = 0

    def update(self):
        if self.rect.centerx > self.screen.get_width():
            self.kill()
        elif self.rect.centerx < 0:
            self.kill()
        elif self.rect.centery > self.screen.get_height():
            self.kill()
        elif self.rect.centery < 0:
            self.kill()
        self.rect.move_ip((self.dir,0))
        
class bossplayer(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.loadImages()
        self.frame = 6
        self.delay = 5
        self.pause = 0
        self.image = self.imgListFwd[self.frame]
        self.rect = self.image.get_rect()
        self.dx = 5
        self.justpressed = 1
        self.forwardYES = 0
        self.reverseYES = 0
        self.stunned = 0
        self.hit = 0
        self.count = 0
        self.rect.centerx = 100
        self.rect.centery = 390
        self.life = 10
        self.shield = 10
        self.x = 0
        self.jumping = -1
        self.gravityY = 0
        self.shieldcap = 0
        self.oldx = self.rect.centerx
        self.oldy = self.rect.centery
        self.offscreen = 0
        
    def loadImages(self):
        try:
        ##forward image load
            imgForwardMaster = pygame.image.load(os.path.join('Sprites','masterchief.png'))
        except:
            sys.exit("could not load image files in 'Sprites' folder :-(")
        imgForwardMaster = imgForwardMaster.convert()
        
        self.imgListFwd = []
        
        imgSize = ((58, 65), (56, 65), (52,65), (54, 65), (52, 65), (52,65), (50, 67))
        offset = ((841, 168),(906, 168),(969, 168),(1027, 168),(1087,168),(1149,168), (841, 14))

        for i in range(7):
            fwdImage = pygame.Surface(imgSize[i])
            fwdImage.blit(imgForwardMaster, (0, 0), (offset[i], imgSize[i]))
            transColor = fwdImage.get_at((1, 1))
            fwdImage.set_colorkey(transColor)
            self.imgListFwd.append(fwdImage)
        ##reverse image load
        try:
            imgReverseMaster = pygame.image.load(os.path.join('Sprites','masterchief.png'))
        except:
            sys.exit("could not load image files in 'Sprites' folder :-(")
        imgReverseMaster = imgReverseMaster.convert()
        
        self.imgListRvs = []
        
        imgSize = ((58, 65), (56, 65), (52,65), (54, 65), (52, 65), (52,65), (50, 67))
        offset = ((841, 168),(906, 168),(969, 168),(1027, 168),(1087,168),(1149,168), (841, 14))

        for i in range(7):
            RvsImage = pygame.Surface(imgSize[i])
            RvsImage.blit(imgReverseMaster, (0, 0), (offset[i],imgSize[i]))
            transColor = RvsImage.get_at((0, 0))
            RvsImage.set_colorkey(transColor)
            self.imgListRvs.append(RvsImage)
        for i in range(7):
           self.imgListRvs[i] = pygame.transform.flip(self.imgListRvs[i], 1, 0)

    def update(self, levelground):
        if self.offscreen == 0:
            if self.stunned == 0:
                self.checkbounds()
                if self.jumping == 1:
                    self.jump(levelground)
                self.shieldregen()
                if self.forwardYES == 1:
                    if self.reverseYES == 0:
                        self.forward()
                elif self.forwardYES == 0:
                    if self.reverseYES == 0:
                        self.stop()
                if self.reverseYES == 1:
                    if self.forwardYES == 0:
                        self.reverse()
                elif self.reverseYES == 0:
                    if self.forwardYES == 0:
                        self.stop()
            elif self.stunned == 1:
                self.stun()
        elif self.offscreen == 1:
            if self.jumping == 1:
                self.jump(levelground)
            elif self.jumping == 0:
                self.endboss()
    def stop(self):
        ##forward
        if self.justpressed == 1:
            self.oldy = self.rect.centery
            self.oldx = self.rect.centerx
            self.image = self.imgListFwd[6]
            self.rect = self.image.get_rect()
            self.rect.centerx = self.oldx
            self.rect.centery = self.oldy
            
        ##reverse
        elif self.justpressed == 2:
            self.oldy = self.rect.centery
            self.oldx = self.rect.centerx
            self.image = self.imgListRvs[6]
            self.rect = self.image.get_rect()
            self.rect.centerx = self.oldx
            self.rect.centery = self.oldy
    
    def forward(self):
        self.oldy = self.rect.centery
        self.rect.centerx += self.dx
        self.oldx = self.rect.centerx
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            if self.frame >= 5:  
                self.frame = 0
            else:
                self.frame += 1    
            self.image = self.imgListFwd[self.frame]
            self.rect = self.image.get_rect()
            self.rect.centerx = self.oldx
            self.rect.centery = self.oldy
        
    def reverse(self):
        self.oldy = self.rect.centery
        self.rect.centerx += -self.dx
        self.oldx = self.rect.centerx
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            if self.frame >= 5:  
                self.frame = 0
            else:
                self.frame += 1
            self.image = self.imgListRvs[self.frame]
            self.rect = self.image.get_rect()
            self.rect.centerx = self.oldx
            self.rect.centery = self.oldy
            
    def jump(self,levelground):
        collide = pygame.sprite.spritecollide(self, levelground, False)
        if collide:
            self.jumping = 0
            self.rect.centery = 390
        else:
            self.rect.centery -= self.gravityY
            self.gravityY -= .20
            
    def shieldregen(self):
        if self.x >= self.shieldcap:
            self.x = self.shieldcap
        elif self.x < self.shieldcap:
            self.x += 1
        if self.x >= self.shieldcap:
            if self.shield < 10:
                self.shield += 1
                
    def checkbounds(self):
        if self.rect.centerx +30 >= 800:
            self.rect.centerx = 770
        elif self.rect.centerx -30 <= 0:
            self.rect.centerx = 30
            
    def stun(self):
        self.count += 1
        if self.count == 50:
            self.count = 0
            
    def endboss(self):
        self.oldy = self.rect.centery
        self.rect.centerx += self.dx
        self.oldx = self.rect.centerx
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            if self.frame >= 5:  
                self.frame = 0
            else:
                self.frame += 1    
            self.image = self.imgListFwd[self.frame]
            self.rect = self.image.get_rect()
            self.rect.centerx = self.oldx
            self.rect.centery = self.oldy
            
class hud(pygame.sprite.Sprite):
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
        self.rect.centerx = 690
        self.rect.centery = 30
        
class healthpoint(pygame.sprite.Sprite):
    def __init__(self, screen, filename,pos):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()
        self.image = pygame.image.load(filename)
        self.transColor = self.image.get_at((0, 5))
        self.image.set_colorkey(self.transColor)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = pos
        self.scored = 0
        
class shieldpoint(pygame.sprite.Sprite):
    def __init__(self, screen, filename,pos):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()
        self.image = pygame.image.load(filename)
        self.transColor = self.image.get_at((1, 1))
        self.image.set_colorkey(self.transColor)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = pos
