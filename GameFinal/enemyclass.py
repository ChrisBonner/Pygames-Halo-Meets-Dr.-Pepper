import pygame, os, sys, math, random
pygame.init()
class grunt(pygame.sprite.Sprite):
    def __init__(self, screen,Pos):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        self.image = self.imgGruntListRvs[0]
        self.rect = self.image.get_rect()
        PosX, PosY = Pos
        self.rect.centerx = PosX
        self.rect.centery = PosY
        self.hit = 0
        self.res = 0
        self.d = 15
        self.delay = 5
        self.p = 0
        self.pause = 0
        self.frame = 0
        self.f = 1
        self.speed = 5
        self.left = 0
        self.right = 0
        self.life = 0
        self.dx = 0
        self.deadrect = self.rect.centery + 40 
        self.shotat = 0
        self.gravityY = 5
        self.jumping = 0
        self.n = 0
    def loadImages(self):
        try:
        ##forward image load
            imgGruntForwardMaster = pygame.image.load(os.path.join('Sprites','grunt.png'))
        except:
            sys.exit("could not load image files in 'Sprites' folder :-(")
        imgGruntForwardMaster = imgGruntForwardMaster.convert()
        
        self.imgGruntListFwd = []
        
        imgSize = ((38, 60), (58, 54), (59, 29))
        offset = ((177, 962), (177, 10),(244, 35))

        for i in range(3):
            fwdGruntImage = pygame.Surface(imgSize[i])
            fwdGruntImage.blit(imgGruntForwardMaster, (0, 0), (offset[i], imgSize[i]))
            transColor = fwdGruntImage.get_at((1, 1))
            fwdGruntImage.set_colorkey(transColor)
            self.imgGruntListFwd.append(fwdGruntImage)
        ##reverse image load
        try:
            imgGruntReverseMaster = pygame.image.load(os.path.join('Sprites','grunt.png'))
        except:
            sys.exit("could not load image files in 'Sprites' folder :-(")
        imgGruntReverseMaster = imgGruntReverseMaster.convert()
        
        self.imgGruntListRvs = []
        
##        imgSize = ((34, 60), (36, 60), (38,60), (38, 60), (35, 62), (34,62), (58, 54), (59, 29))
##        offset = ((15, 962),(62, 962),(109, 962),(177, 962),(225,962),(273,962), (177, 10),(244, 35))
        imgSize = ((38, 60), (58, 54), (59, 29))
        offset = ((177, 962), (177, 10),(244, 35))
        
        for i in range(3):
            GruntRvsImage = pygame.Surface(imgSize[i])
            GruntRvsImage.blit(imgGruntReverseMaster, (0, 0), (offset[i],imgSize[i]))
            transColor = GruntRvsImage.get_at((1, 1))
            GruntRvsImage.set_colorkey(transColor)
            self.imgGruntListRvs.append(GruntRvsImage)
        for i in range(3):
           self.imgGruntListRvs[i] = pygame.transform.flip(self.imgGruntListRvs[i], 1, 0)
        
    def update(self,lvlbackground,floor):
        if self.shotat == 1:
            if self.n != 25:
                self.n = random.randint(1,50)
            elif self.n == 25:
                self.jump(floor)
              
                    
        self.checkpos()
        if self.life <= 0:
            self.killed()  
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
            
    def killed(self):
        if self.rect.centerx > 300:
            self.speed = 0
            self.p += 1
            if self.p >= self.d:
                self.p = 0
                if self.f >= 2:  
                    self.kill()
                else:
                    self.f += 1
            self.image = self.imgGruntListRvs[self.f]
        if self.f == 2:
            self.rect.centery = self.deadrect
        if self.rect.centerx < 300:
            self.speed = 0
            self.p += 1
            if self.p >= self.d:
                self.p = 0
                if self.f >= 2:  
                    self.kill()
                else:
                    self.f += 1
            self.image = self.imgGruntListFwd[self.f]
        if self.f == 2:
            self.rect.centery = self.deadrect
     
    def _move(self,lvlbackground):
        if lvlbackground.rect.centerx > 3990: 
            self.dx = 0
        elif lvlbackground.rect.centerx < -3190:
            self.dx = 0
        
        self.rect.centerx += self.dx
    
    def jump(self,floor):
        collide = pygame.sprite.spritecollide(self, floor, False)
        if collide:
            self.rect.centery = 385
            self.gravityY = 5
            self.shotat = 0
            self.n = 0
        else:
            self.rect.centery -= self.gravityY
            self.gravityY -= .20
            self.n = 25
            
    def checkpos(self):
        if self.rect.centerx < 300:
            self.image = self.imgGruntListFwd[0]
        elif self.rect.centerx > 300:
            self.image = self.imgGruntListRvs[0]

class laser(pygame.sprite.Sprite):
    def __init__(self, screen, laser, StartPosx, StartPosy, dir):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()
        self.image = pygame.image.load(laser)
        transColor = self.image.get_at((1, 1))
        self.image.set_colorkey(transColor)
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
            
class boss(pygame.sprite.Sprite):
    def __init__(self, screen, can):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()
        self.image = pygame.image.load(can)
        self.transColor = self.image.get_at((1, 1))
        self.image.set_colorkey(self.transColor)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.x = self.rect.centerx = 600
        self.y = self.rect.centery = 125
        self.ground = 330
        self.life = 0
        self.dx = 7
        self.shakedx = 15
        self.downdy = 20
        self.r = 0
        self.l = 0
        self.shaketime = 0
        self.downtime = 0
        self.movedir = 0
        self.n = 0
        self.moveU = 0
        self.hitground = 0
        
    def update(self):
        self.checkdeath()
        self.algo()
        
    def checkdeath(self):
        if self.life <= 0:
            self.kill()
    
    def algo(self):
        if self.n != 43:
            self.n = random.randint(1,150)
        if self.n != 43:
            self.moveing()
        elif self.n == 43:
            self.shake()
            
    def shake(self):
        self.shaketime += 1
        if self.shaketime < 30:
            if self.r != 3:
                self.rect.move_ip(self.shakedx,0)
                self.r += 1
                if self.l == 3 and self.l == 3:
                    self.l = 0
            if self.r == 3:
                if self.l !=3:
                    self.rect.move_ip(-self.shakedx,0)
                    self.l += 1
                if self.r == 3 and self.l == 3:
                    self.r = 0
        elif self.shaketime >= 30:
            self.down()
            
    def up(self):
        if self.rect.centery > 125:
            self.rect.move_ip(0,-self.downdy)
        elif self.rect.centery <= 125:
            self.downtime = 0
            self.shaketime = 0
            self.n = 0

    def down(self):
        self.downtime += 1
        if self.rect.centery < self.ground and self.downtime < 40:
            self.rect.move_ip(0,self.downdy)
        elif self.downtime >= 40:
            self.up()
        if self.downtime >= 40:
            self.downtime = 40
            
    def moveing(self):
        if self.rect.centerx < 740 and self.movedir == 1:
            self.rect.move_ip(self.dx,0)
        else:
            self.movedir = 0
        if self.rect.centerx > 60 and self.movedir == 0:
            self.rect.move_ip(-self.dx,0)
        else:
            self.movedir = 1