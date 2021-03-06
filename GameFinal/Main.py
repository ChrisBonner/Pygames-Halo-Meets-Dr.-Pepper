import pygame, sys, os, math, random, easygui
import playerclass, backgroundclass, startscreenclass
import enemyclass, difficultScreen, miniGUI, Save
pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()                
#global
global scorehealth
global scoreenemystart
global scorebonus
global PlayerName

try:
#sound
    sndBoss = pygame.mixer.Sound(os.path.join('Sounds','boss.ogg'))
    sndLevel = pygame.mixer.Sound(os.path.join('Sounds','level.ogg'))
    sndMenu = pygame.mixer.Sound(os.path.join('Sounds','menu.ogg'))
    sndLaser = pygame.mixer.Sound(os.path.join('Sounds','Photon.ogg'))
    sndRifle = pygame.mixer.Sound(os.path.join('Sounds','Rifle.ogg'))
except:
    sys.exit("could not load or play soundfiles in 'Sprites' folder :-(")
#screen set up
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
try:
#file names for pictures
    level = os.path.join('Sprites','gamebackground.bmp')
    startscreen = os.path.join('Sprites','startscreen.png')
    filename = os.path.join('Sprites','bullet.png')
    laser = os.path.join('Sprites','laser.png')
    graphicname = os.path.join('Sprites', 'Graphic.bmp')
    mousepic = os.path.join('Sprites','mouse.bmp')
except:
    sys.exit("could not load image files in 'Sprites' folder :-(")
#sets up sprites
Player = playerclass.player(screen)
StartPosx = Player.rect.centerx
StartPosy = Player.rect.centery 
lvlbackground = backgroundclass.Background(screen,level)
startscreen = startscreenclass.startscreen(screen,startscreen)
Halo = startscreenclass.HaloGraphic(screen,graphicname)
#def main loop
def main():
    #globals
    global playerhealth
    global scorehealth
    global scoreenemystart
    global scorebonus
    global score
    #screen load
    pygame.display.set_caption("Halo - Chris Bonner")
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    #sound
    sndLevel.play(-1)
    sndLaser.set_volume(0.6)
    sndRifle.set_volume(0.2)
    
    #file names for picutres
    lvl = os.path.join('Sprites','gamebackground.bmp')
    filename = os.path.join('Sprites','bullet.png')
    laser = os.path.join('Sprites','laser.png')
    hudpic = os.path.join('Sprites','hud.bmp')
    healthpic = os.path.join('Sprites','healthpoint.bmp')
    shieldpic1 = os.path.join('Sprites','shield1pic.bmp')
    shieldpic2 = os.path.join('Sprites','shield2pic.bmp')
    shieldpic3 = os.path.join('Sprites','shield3pic.bmp')
    shieldpic4 = os.path.join('Sprites','shield4pic.bmp')
    shieldpic5 = os.path.join('Sprites','shield5pic.bmp')
    #class sprites
    Player = playerclass.player(screen)
    StartPosx = Player.rect.centerx
    StartPosy = Player.rect.centery
    lvlbackground = backgroundclass.Background(screen, level)
    Hud = playerclass.hud(screen, hudpic)
    healthpoint1 = playerclass.healthpoint(screen,healthpic,(732,45))
    healthpoint2 = playerclass.healthpoint(screen,healthpic,(718,45))
    healthpoint3 = playerclass.healthpoint(screen,healthpic,(705,45))
    healthpoint4 = playerclass.healthpoint(screen,healthpic,(691,45))
    healthpoint5 = playerclass.healthpoint(screen,healthpic,(678,45))
    healthpoint6 = playerclass.healthpoint(screen,healthpic,(665,45))
    healthpoint7 = playerclass.healthpoint(screen,healthpic,(652,45))
    healthpoint8 = playerclass.healthpoint(screen,healthpic,(638,45))
    healthpoint9 = playerclass.healthpoint(screen,healthpic,(625,45))
    healthpoint10 = playerclass.healthpoint(screen,healthpic,(611,45))

    shieldpoint1 = playerclass.shieldpoint(screen,shieldpic1,(768,47))
    shieldpoint2 = playerclass.shieldpoint(screen,shieldpic2,(759,35))
    shieldpoint3 = playerclass.shieldpoint(screen,shieldpic3,(759,16))
    shieldpoint4 = playerclass.shieldpoint(screen,shieldpic4,(729,16))
    shieldpoint5 = playerclass.shieldpoint(screen,shieldpic4,(710,16))
    shieldpoint6 = playerclass.shieldpoint(screen,shieldpic4,(691,16))
    shieldpoint7 = playerclass.shieldpoint(screen,shieldpic4,(672,16))
    shieldpoint8 = playerclass.shieldpoint(screen,shieldpic4,(653,16))
    shieldpoint9 = playerclass.shieldpoint(screen,shieldpic4,(634,16))
    shieldpoint10 = playerclass.shieldpoint(screen,shieldpic5,(614,16))
    
    #sprite groups
    friend = pygame.sprite.Group(Player,Hud)
    ammo = pygame.sprite.Group()
    enemyammo = pygame.sprite.Group()
    lvl = pygame.sprite.Group(lvlbackground)
    health = pygame.sprite.Group(
    healthpoint1,healthpoint2,healthpoint3,healthpoint4,healthpoint5,
    healthpoint6,healthpoint7,healthpoint8,healthpoint9,healthpoint10)
    
    shield = pygame.sprite.Group(
    shieldpoint1,shieldpoint2,shieldpoint3,shieldpoint4,shieldpoint5,
    shieldpoint6,shieldpoint7,shieldpoint8,shieldpoint9,shieldpoint10)
    
    floor = pygame.sprite.Group(
    backgroundclass.ground(screen,400,415), backgroundclass.ground(screen,1200,415),
    backgroundclass.ground(screen,2000,415),backgroundclass.ground(screen,2800,415),
    backgroundclass.ground(screen,3600,415),backgroundclass.ground(screen,4400,415),
    backgroundclass.ground(screen,5200,415),backgroundclass.ground(screen,6000,415),
    backgroundclass.ground(screen,6800,415),backgroundclass.ground(screen,7600,415))

    enemy = pygame.sprite.Group(enemyclass.grunt(screen,(1000,385)),
    enemyclass.grunt(screen,(1300,385)),enemyclass.grunt(screen,(1500,385)),
    enemyclass.grunt(screen,(1700,385)),enemyclass.grunt(screen,(1900,385)),
    enemyclass.grunt(screen,(2300,385)),enemyclass.grunt(screen,(2500,385)),
    enemyclass.grunt(screen,(2700,385)),enemyclass.grunt(screen,(2900,385)),
    enemyclass.grunt(screen,(3300,385)),enemyclass.grunt(screen,(3500,385)),
    enemyclass.grunt(screen,(3700,385)),enemyclass.grunt(screen,(3900,385)),
    enemyclass.grunt(screen,(4300,385)),enemyclass.grunt(screen,(4500,385)),
    enemyclass.grunt(screen,(4700,385)),enemyclass.grunt(screen,(4900,385)),
    enemyclass.grunt(screen,(5300,385)),enemyclass.grunt(screen,(5500,385)),
    enemyclass.grunt(screen,(5700,385)),enemyclass.grunt(screen,(5900,385)),
    enemyclass.grunt(screen,(6300,385)),enemyclass.grunt(screen,(6500,385)),
    enemyclass.grunt(screen,(6700,385)),enemyclass.grunt(screen,(6900,385)),
    enemyclass.grunt(screen,(7200,385)),enemyclass.grunt(screen,(7500,385)))
    
    #checks difficulty settings
    if difficulty == 0:
        scoreenemystart = 13500
        scorehealth = 0
        scorebonus = 3000
        # cap score == 16500
        for x in enemy:
            x.life = 3
        Player.shieldcap = 300
    elif difficulty == 1:
        scoreenemystart = 27000
        scorehealth = 0
        scorebonus = 6000
        # cap score == 35500
        for x in enemy:
            x.life = 5
        Player.shieldcap = 500
    elif difficulty == 2:
        scoreenemystart = 40500
        scorehealth = 0
        scorebonus = 9000
        # cap score == 52000
        for x in enemy:
            x.life = 10
        Player.shieldcap = 1000
    elif difficulty == 3:
        scoreenemystart = 54000
        scorehealth = 0
        scorebonus = 12000
        # cap score == 68500
        for x in enemy:
            x.life = 20
        Player.shieldcap = 2000
        
    #exit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Keepgoing = False
            pygame.display.quit()
            pygame.quit()
            sys.exit()
    # set clock and game loop
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        if Player.life <= 0:
            sndLevel.stop()
            GameOver()
        if lvlbackground.rect.centerx <= -3185:
            if Player.rect.centery == 380:
                lvlbackground.dx = 0
                Player.offscreen = 1
            if Player.rect.centerx > 825:
                for x in floor:
                    x.dx = 0
                for item in enemy:
                    scoreenemystart -= 500
                playerhealth = Player.life
                sndLevel.stop()
                BOSS()    
        # game ticks
        clock.tick(60)
        #mouse visibility set false
        pygame.mouse.set_visible(False)
        #key event checks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if Player.offscreen == 0:
                    if event.key == pygame.K_ESCAPE:
                        Keepgoing = False
                        pygame.display.quit()
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_a:
                        lvlbackground.dx = 5
                        for x in floor: 
                            x.dx = 5
                        for x in enemy:
                            x.dx = 5
                        lvlbackground.reverseYES = 1
                        Player.reverseYES = 1
                        Player.justpressed = 0
                    elif event.key == pygame.K_d:
                        lvlbackground.dx = -5
                        for x in floor: 
                            x.dx = -5
                        for x in enemy:
                            x.dx = -5
                        lvlbackground.forwardYES = 1
                        Player.forwardYES = 1
                        Player.justpressed = 0
                    elif event.key == pygame.K_SPACE:
                        if Player.offscreen == 0:
                            if Player.jumping <= 0:
                                Player.jumping = 1
                                Player.gravityY = 5
            #key up events
            elif event.type == pygame.KEYUP:
                if Player.offscreen == 0:
                    if event.key == pygame.K_a:
                        Player.justpressed = 2
                        lvlbackground.reverseYES = 0
                        lvlbackground.dx = 0
                        for x in floor: 
                            x.dx = 0
                        for x in enemy:
                            x.dx = 0
                        Player.reverseYES = 0
                    elif event.key == pygame.K_d:
                        Player.justpressed = 1                    
                        lvlbackground.dx = 0
                        for x in floor: 
                            x.dx = 0
                        for x in enemy:
                            x.dx = 0
                        Player.forwardYES = 0
                        lvlbackground.forwardYES = 0
            #mouse Events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Player.offscreen == 0:
                    sndRifle.play()
                    if Player.forwardYES == 1 or Player.justpressed == 1:
                        StartPosx = Player.rect.centerx + 25
                        StartPosy = Player.rect.centery - 9
                        dir = 10
                        for x in enemy:
                            x.shotat = 1
                    elif Player.reverseYES == 1 or Player.justpressed == 2:
                        StartPosx = Player.rect.centerx - 25
                        StartPosy = Player.rect.centery - 9
                        dir = -10
                        for x in enemy:
                            x.shotat = 1
                    ammo.add(playerclass.Bullet(screen, filename, StartPosx, StartPosy, dir))
                
        # each enemy check if he is on the screen to shoot and what direction to face
        for e in enemy:
            if e.life >= 1:
                if e.rect.centerx < 800 and e.rect.centerx > 0:
                    if e.rect.centery == 385 or e.rect.centery < 345:
                        n = random.randint(1,75)
                        Posx = e.rect.centerx
                        Posy = e.rect.centery + 3
                        if e.rect.centerx < 300:
                            dir = 10
                        elif e.rect.centerx > 300:
                            dir = -10
                        if n == 25:
                            sndLaser.play()
                            enemyammo.add(enemyclass.laser(screen,laser,Posx,Posy,dir))
                        
        #health and shield check 
        if Player.life == 9:
            health.remove(healthpoint10)
        elif Player.life == 8:
            health.remove(healthpoint9)
        elif Player.life == 7:
            health.remove(healthpoint8)
        elif Player.life == 6:
            health.remove(healthpoint7)
        elif Player.life == 5:
            health.remove(healthpoint6)
        elif Player.life == 4:
            health.remove(healthpoint5)
        elif Player.life == 3:
            health.remove(healthpoint4)
        elif Player.life == 2:
            health.remove(healthpoint3)
        elif Player.life == 1:
            health.remove(healthpoint2)
        elif Player.life == 0:
            health.remove(healthpoint1)

        if Player.x != Player.shieldcap:
            if Player.shield == 9:
                shield.remove(shieldpoint10)
            elif Player.shield == 8:
                shield.remove(shieldpoint9)
            elif Player.shield == 7:
                shield.remove(shieldpoint8)
            elif Player.shield == 6:
                shield.remove(shieldpoint7)
            elif Player.shield == 5:
                shield.remove(shieldpoint6)
            elif Player.shield == 4:
                shield.remove(shieldpoint5)
            elif Player.shield == 3:
                shield.remove(shieldpoint4)
            elif Player.shield == 2:
                shield.remove(shieldpoint3)
            elif Player.shield == 1:
                shield.remove(shieldpoint2)
            elif Player.shield == 0:
                shield.remove(shieldpoint1)
        
        if Player.x > Player.shieldcap - 2:
            if Player.shield == 9:
                shield.add(shieldpoint10)
            elif Player.shield == 8:
                shield.add(shieldpoint9)
            elif Player.shield == 7:
                shield.add(shieldpoint8)
            elif Player.shield == 6:
                shield.add(shieldpoint7)
            elif Player.shield == 5:
                shield.add(shieldpoint6)
            elif Player.shield == 4:
                shield.add(shieldpoint5)
            elif Player.shield == 3:
                shield.add(shieldpoint4)
            elif Player.shield == 2:
                shield.add(shieldpoint3)
            elif Player.shield == 1:
                shield.add(shieldpoint2)
            elif Player.shield == 0:
                shield.add(shieldpoint1)
                
        #updates
        lvl.update()
        Player.update(floor)
        ammo.update()
        floor.update(lvlbackground)
        enemyammo.update()
        enemy.update(lvlbackground,floor)
         
        #check for collisions
        for e in enemy:
            for a in ammo:
                if pygame.sprite.collide_mask(e,a):
                    e.life -= 1
                    a.kill()
                    
        for p in friend:
            for e in enemyammo:
                if pygame.sprite.collide_mask(e,p):
                    p.x = 0
                    scorebonus -= 100
                    if scorebonus <= 0:
                        scorebonus = 0
                    if p.shield > 0:
                        p.shield -= 1
                    elif p.shield <= 0:
                        p.life -= 1
                    e.kill()
        
        #blit screen
        screen.blit(background, (0, 0))
        
        # draw everything
        floor.draw(screen)
        lvl.draw(screen)
        ammo.draw(screen)
        enemyammo.draw(screen)
        friend.draw(screen)
        enemy.draw(screen)
        health.draw(screen)
        shield.draw(screen)
        
        # flip display
        pygame.display.flip()
#def start screen
def StartScreen():
    #globals
    global userStart
    global PlayerName
    userStart = 0
    #screen setup
    pygame.display.set_caption("Halo - Chris Bonner")
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    #sound
    sndMenu.play(-1)
    #picture for sprite class
    pygame.mouse.set_visible(True)
    try:
        startscreen = os.path.join('Sprites','startscreen.png')
        graphicname = os.path.join('Sprites','Graphic.bmp')
        mousepic = os.path.join('Sprites','mouse.bmp')
    except:
        sys.exit("could not load image files in 'Sprites' folder :-(")
    #sprite class
    startscreen = startscreenclass.startscreen(screen, startscreen)
    Halo = startscreenclass.HaloGraphic(screen,graphicname)
    Mouse = startscreenclass.tempMouse(screen,mousepic)
    #Player Name
    PlayerName = easygui.enterbox("Enter Player Name", ' ', "Player", True, None, None)
    #button start
    btnStart = miniGUI.Button()
    btnStart.text = "Start"
    btnStart.center = (400,300)
    btnStart.size = (60,21)
    btnStart.bgColor = (0x00,0x00,0x00)
    btnStart.fgColor = (0xFF, 0xFF, 0xFF)

    #button difficulty 
    btnDifficulty = miniGUI.Button()
    btnDifficulty.text = "Difficulty"
    btnDifficulty.center = (400, 350)
    btnDifficulty.size = (110,21)
    btnDifficulty.bgColor = (0x00,0x00,0x00)
    btnDifficulty.fgColor = (0xFF,0xff,0xff)
    
    #button Exit
    btnExit = miniGUI.Button()
    btnExit.text = "Exit"
    btnExit.center = (400,400)
    btnExit.size = (50,21)
    btnExit.bgColor = (0x00,0x00,0x00)
    btnExit.fgColor = (0xff,0xff,0xff)
    
    #sprite ordered update
    allsprites = pygame.sprite.OrderedUpdates(startscreen,Halo,btnStart,btnDifficulty,btnExit,Mouse)
    #set clock and game loop
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        #clock ticks
        clock.tick(60)
        #mouse visibily off
        pygame.mouse.set_visible(False)
        #exit event or game start
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Keepgoing = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
            if btnStart.active == True:
                if 'difficulty' in globals():
                    sndMenu.stop()
                    main()
                else:
                    userStart = 1
                    difficultyScreen()
            elif btnDifficulty.active == True:
                difficultyScreen()
            elif btnExit.active == True:
                Keepgoing = False
                pygame.display.quit()
                pygame.quit()
                sys.exit()
                
        #clear, updates and flip
        allsprites.clear(screen,background)
        allsprites.update()
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()
        
#def difficultyScreen
def difficultyScreen():
    #screen setup
    pygame.display.set_caption("Halo - Chris Bonner")
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    #picture for sprite class
    pygame.mouse.set_visible(True)
    try:
        startscreen = os.path.join('Sprites','startscreen.png')
        graphicname = os.path.join('Sprites','Graphic.bmp')
        easepic = os.path.join('Sprites','ease.png')
        medpic = os.path.join('Sprites','medium.png')
        hardpic = os.path.join('Sprites','hard.png')
        extremepic = os.path.join('Sprites','extreme.png')
        mousepic = os.path.join('Sprites','mouse.bmp')
    except:
        sys.exit("could not load image files in 'Sprites' folder :-(")
    #sprite class
    startscreen = startscreenclass.startscreen(screen, startscreen)
    Halo = startscreenclass.HaloGraphic(screen, graphicname)
    Ease = difficultScreen.ease(screen, easepic)
    Medium = difficultScreen.medium(screen, medpic)
    Hard = difficultScreen.hard(screen, hardpic)
    Extreme = difficultScreen.extreme(screen, extremepic)
    Mouse = startscreenclass.tempMouse(screen, mousepic)
    
    #button Ease
    btnEase = miniGUI.Button()
    btnEase.text = "Ease"
    btnEase.center = (100,400)
    btnEase.size = (75,21)
    btnEase.bgColor = (0x00,0x00,0x00)
    btnEase.fgColor = (0xff,0xff,0xff)
    
    #button Medium
    btnMed = miniGUI.Button()
    btnMed.text = "Medium"
    btnMed.center = (300,400)
    btnMed.size = (100,21)
    btnMed.bgColor = (0x00,0x00,0x00)
    btnMed.fgColor = (0xff,0xff,0xff)
    
    #button hard
    btnHard = miniGUI.Button()
    btnHard.text = "Hard"
    btnHard.center = (500,400)
    btnHard.size = (75,21)
    btnHard.bgColor = (0x00,0x00,0x00)
    btnHard.fgColor = (0xff,0xff,0xff)
    
    #button Extreme
    btnExtreme = miniGUI.Button()
    btnExtreme.text = "Extreme"
    btnExtreme.center = (700,400)
    btnExtreme.size = (100,21)
    btnExtreme.bgColor = (0x00,0x00,0x00)
    btnExtreme.fgColor = (0xff,0xff,0xff)
    
    #button Back
    btnBack = miniGUI.Button()
    btnBack.text = "Back"
    btnBack.center = (400,500)
    btnBack.size = (75,21)
    btnBack.bgColor = (0x00,0x00,0x00)
    btnBack.fgColor = (0xff,0xff,0xff)

    #sprite group ordered updates
    allsprites = pygame.sprite.OrderedUpdates(startscreen,Halo,btnEase,btnMed,btnHard,btnExtreme,btnBack)
    difficultySprites = pygame.sprite.OrderedUpdates(Ease,Medium,Hard,Extreme)
    mouseSprite = pygame.sprite.Group(Mouse)
    #set clock and game loop
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        #clock ticks
        clock.tick(60)
        #exit event or game start
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Keepgoing = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
        
            #sets difficulty variable if button pressed
            if btnEase.active == True or Ease.active == True:
                if 'difficulty' in globals():
                    difficulty = 0
                    if userStart == 1:
                        sndMenu.stop()
                        main()
                    elif userStart == 0:
                        StartScreen()
                elif  'difficulty' not in globals():
                    global difficulty
                    difficulty = 0
                    if userStart == 1:
                        sndMenu.stop()
                        main()
                    elif userStart == 0:
                        StartScreen()
            elif btnMed.active == True or Medium.active == True:
                if 'difficulty' in globals():
                    difficulty = 1
                    if userStart == 1:
                        sndMenu.stop()
                        main()
                    elif userStart == 0:
                        StartScreen()
                elif  'difficulty' not in globals():
                    global difficulty
                    difficulty = 1
                    if userStart == 1:
                        sndMenu.stop()
                        main()
                    elif userStart == 0:
                        StartScreen()
            elif btnHard.active == True or Hard.active == True:
                if 'difficulty' in globals():
                    difficulty = 2
                    if userStart == 1:
                        sndMenu.stop()
                        main()
                    elif userStart == 0:
                        StartScreen()
                elif  'difficulty' not in globals():
                    global difficulty
                    difficulty = 2
                    if userStart == 1:
                        sndMenu.stop()
                        main()
                    elif userStart == 0:
                        StartScreen()
            elif btnExtreme.active == True or Extreme.active == True:
                if 'difficulty' in globals():
                    difficulty = 3
                    if userStart == 1:
                        sndMenu.stop()
                        main()
                    elif userStart == 0:
                        StartScreen()
                elif  'difficulty' not in globals():
                    global difficulty
                    difficulty = 3
                    if userStart == 1:
                        sndMenu.stop()
                        main()
                    elif userStart == 0:
                        StartScreen()
            elif btnBack.active == True:
                StartScreen()

        #clear, updates and flip
        allsprites.clear(screen,background)
        difficultySprites.clear(screen,background)
        mouseSprite.clear(screen,background)
        allsprites.update()
        difficultySprites.update(Mouse)
        mouseSprite.update()
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        difficultySprites.draw(screen)
        mouseSprite.draw(screen)
        pygame.display.flip()

#boss battle
def BOSS():
    #globals
    global playerhealth
    global bossstartlife
    global scorehealth
    global scorebonus
    
    #screen set up
    pygame.display.set_caption("Halo - Chris Bonner")
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    #sound
    sndBoss.play(-1)
    sndRifle.set_volume(0.2)
    print sndLaser.get_buffer()
    print sndRifle.get_buffer()
    
    try:
    #sprite pics
        bosspic = os.path.join('Sprites','DrPepper.bmp')
        bossbackgroundpic = os.path.join('Sprites','bossbattle.png')
        bulletpic = os.path.join('Sprites','bullet.png')
        hudpic = os.path.join('Sprites','hud.bmp')
        healthpic = os.path.join('Sprites','healthpoint.bmp')
        shieldpic1 = os.path.join('Sprites','shield1pic.bmp')
        shieldpic2 = os.path.join('Sprites','shield2pic.bmp')
        shieldpic3 = os.path.join('Sprites','shield3pic.bmp')
        shieldpic4 = os.path.join('Sprites','shield4pic.bmp')
        shieldpic5 = os.path.join('Sprites','shield5pic.bmp')
    except:
        sys.exit("could not load image files in 'Sprites' folder :-(")
    #sprites defined
    PlayerBoss = playerclass.bossplayer(screen)
    backgroundBoss = backgroundclass.BossBackground(screen, bossbackgroundpic)
    groundBoss = backgroundclass.Bossground(screen)
    BossNPC = enemyclass.boss(screen, bosspic)
    Hud = playerclass.hud(screen, hudpic)
    healthpoint1 = playerclass.healthpoint(screen,healthpic,(732,45))
    healthpoint2 = playerclass.healthpoint(screen,healthpic,(718,45))
    healthpoint3 = playerclass.healthpoint(screen,healthpic,(705,45))
    healthpoint4 = playerclass.healthpoint(screen,healthpic,(691,45))
    healthpoint5 = playerclass.healthpoint(screen,healthpic,(678,45))
    healthpoint6 = playerclass.healthpoint(screen,healthpic,(665,45))
    healthpoint7 = playerclass.healthpoint(screen,healthpic,(652,45))
    healthpoint8 = playerclass.healthpoint(screen,healthpic,(638,45))
    healthpoint9 = playerclass.healthpoint(screen,healthpic,(625,45))
    healthpoint10 = playerclass.healthpoint(screen,healthpic,(611,45))

    shieldpoint1 = playerclass.shieldpoint(screen,shieldpic1,(768,47))
    shieldpoint2 = playerclass.shieldpoint(screen,shieldpic2,(759,35))
    shieldpoint3 = playerclass.shieldpoint(screen,shieldpic3,(759,16))
    shieldpoint4 = playerclass.shieldpoint(screen,shieldpic4,(729,16))
    shieldpoint5 = playerclass.shieldpoint(screen,shieldpic4,(710,16))
    shieldpoint6 = playerclass.shieldpoint(screen,shieldpic4,(691,16))
    shieldpoint7 = playerclass.shieldpoint(screen,shieldpic4,(672,16))
    shieldpoint8 = playerclass.shieldpoint(screen,shieldpic4,(653,16))
    shieldpoint9 = playerclass.shieldpoint(screen,shieldpic4,(634,16))
    shieldpoint10 = playerclass.shieldpoint(screen,shieldpic5,(614,16))
    
    #Sprite grouping
    player = pygame.sprite.Group(PlayerBoss)
    level = pygame.sprite.Group(backgroundBoss)
    levelground = pygame.sprite.Group(groundBoss)
    enemy = pygame.sprite.Group(BossNPC)
    ammo = pygame.sprite.Group()
    HUD = pygame.sprite.Group(Hud)
    health = pygame.sprite.Group(
    healthpoint1,healthpoint2,healthpoint3,healthpoint4,healthpoint5,
    healthpoint6,healthpoint7,healthpoint8,healthpoint9,healthpoint10)
    
    shield = pygame.sprite.Group(
    shieldpoint1,shieldpoint2,shieldpoint3,shieldpoint4,shieldpoint5,
    shieldpoint6,shieldpoint7,shieldpoint8,shieldpoint9,shieldpoint10)
    
    #difficulty check
    if difficulty == 0:
        BossNPC.life = 20
        bossstartlife = 20
        PlayerBoss.shieldcap = 300
    elif difficulty == 1:
        BossNPC.life = 40
        bossstartlife = 40
        PlayerBoss.shieldcap = 500
    elif difficulty == 2:
        BossNPC.life = 75
        bossstartlife = 75
        PlayerBoss.shieldcap = 1000
    elif difficulty == 3:
        BossNPC.life = 100
        bossstartlife = 100
        PlayerBoss.shieldcap = 2000
        
    #setting player health
    PlayerBoss.life = playerhealth 
    if PlayerBoss.life == 10:
        health = pygame.sprite.Group(
        healthpoint1,healthpoint2,healthpoint3,healthpoint4,healthpoint5,
        healthpoint6,healthpoint7,healthpoint8,healthpoint9,healthpoint10)
    elif PlayerBoss.life == 9:
        health = pygame.sprite.Group(
        healthpoint1,healthpoint2,healthpoint3,healthpoint4,healthpoint5,
        healthpoint6,healthpoint7,healthpoint8,healthpoint9)   
    elif PlayerBoss.life == 8:
        health = pygame.sprite.Group(
        healthpoint1,healthpoint2,healthpoint3,healthpoint4,healthpoint5,
        healthpoint6,healthpoint7,healthpoint8)
    elif PlayerBoss.life == 7:
        health = pygame.sprite.Group(
        healthpoint1,healthpoint2,healthpoint3,healthpoint4,healthpoint5,
        healthpoint6,healthpoint7)
    elif PlayerBoss.life == 6:
        health = pygame.sprite.Group(healthpoint1,
        healthpoint2,healthpoint3,healthpoint4,healthpoint5,healthpoint6)
    elif PlayerBoss.life == 5:
        health = pygame.sprite.Group(
        healthpoint1,healthpoint2,healthpoint3,healthpoint4,healthpoint5)
    elif PlayerBoss.life == 4:
        health = pygame.sprite.Group(healthpoint1,healthpoint2,healthpoint3,healthpoint4)
    elif PlayerBoss.life == 3:
        health = pygame.sprite.Group(healthpoint1,healthpoint2,healthpoint3)
    elif PlayerBoss.life == 2:
        health = pygame.sprite.Group(healthpoint1,healthpoint2)
    elif PlayerBoss.life == 1:
        health = pygame.sprite.Group(healthpoint1)
    
        
    # set clock and game loop
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        if PlayerBoss.life <= 0:
            sndBoss.stop()
            GameOver()
        if BossNPC.life <= 0:
            if PlayerBoss.stunned == 1:
                PlayerBoss.stunned = 0  
            if PlayerBoss.hit == 1:
                PlayerBoss.hit = 0
            PlayerBoss.offscreen = 1
            if PlayerBoss.rect.centerx > 825:
                for x in health:
                    scorehealth += 250
                sndBoss.stop()
                ScoreScreen()
        # game ticks
        clock.tick(60)
        #mouse visibility set false
        pygame.mouse.set_visible(False)
        #key event checks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if PlayerBoss.offscreen == 0:
                    if event.key == pygame.K_ESCAPE:
                        Keepgoing = False
                        pygame.display.quit()
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_a:
                        PlayerBoss.reverseYES = 1
                        PlayerBoss.justpressed = 0
                    elif event.key == pygame.K_d:
                        PlayerBoss.forwardYES = 1
                        PlayerBoss.justpressed = 0
                    elif event.key == pygame.K_SPACE:
                            if PlayerBoss.jumping <= 0:
                                PlayerBoss.jumping = 1
                                PlayerBoss.gravityY = 5
            elif event.type == pygame.KEYUP:
                if PlayerBoss.offscreen == 0:
                    if event.key == pygame.K_a:
                        PlayerBoss.reverseYES = 0
                        PlayerBoss.justpressed = 2
                    elif event.key == pygame.K_d:
                        PlayerBoss.justpressed = 1 
                        PlayerBoss.forwardYES = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if PlayerBoss.offscreen == 0:
                    if PlayerBoss.stunned != 1:
                        sndRifle.play()
                        if PlayerBoss.forwardYES == 1 or PlayerBoss.justpressed == 1:
                            StartPosx = PlayerBoss.rect.centerx + 25
                            StartPosy = PlayerBoss.rect.centery - 9
                            dir = 10
                        elif PlayerBoss.reverseYES == 1 or PlayerBoss.justpressed == 2:
                            StartPosx = PlayerBoss.rect.centerx - 25
                            StartPosy = PlayerBoss.rect.centery - 9
                            dir = -10
                        ammo.add(playerclass.Bullet(screen, bulletpic, StartPosx, StartPosy, dir))
                
        #screen blit
        screen.blit(background, (0, 0))

        #sprite update
        enemy.update()
        ammo.update()
        player.update(levelground)
        
        #checks ammo hit boss
        if PlayerBoss.offscreen == 0:
            for b in enemy:
                for a in ammo:
                    if pygame.sprite.collide_mask(b,a):
                        b.life -= 1
                        a.kill()
                        
            #checks boss hp and sets faster movement
            if BossNPC.life <= bossstartlife / 2:
                BossNPC.dx = 12
                
            #checks if boss hits ground and player on ground
            if pygame.sprite.collide_rect(BossNPC,groundBoss):
                if PlayerBoss.rect.centery >= 390:
                    if PlayerBoss.stunned == 0:
                        PlayerBoss.stunned = 1
                        PlayerBoss.x = 0 
                        if BossNPC.hitground == 0:
                            BossNPC.hitground = 1
                            if PlayerBoss.shield > 0:
                                PlayerBoss.shield -= 3
                            elif PlayerBoss.shield <= 0:
                                PlayerBoss.life -= 3
        
            #checks if boss hits player                 
            if pygame.sprite.collide_mask(PlayerBoss,BossNPC):
                if PlayerBoss.stunned == 0:
                    PlayerBoss.stunned = 1
                    if PlayerBoss.hit == 0:
                        PlayerBoss.hit = 1
                        PlayerBoss.x = 0
                        if PlayerBoss.shield > 0:
                            PlayerBoss.shield = 0
                        elif PlayerBoss.shield <= 0:
                            PlayerBoss.life -= 3
                        
        #boss at top of screen reset variables
        if BossNPC.rect.centery <= 125:
            PlayerBoss.hit= 0
            PlayerBoss.stunned = 0
            BossNPC.hitground = 0
        #health and shield checks
        if healthpoint10 in health:
            if PlayerBoss.life <= 9:
                health.remove(healthpoint10)
        if healthpoint9 in health:
            if PlayerBoss.life <= 8:
                health.remove(healthpoint9)
        if healthpoint8 in health:
            if PlayerBoss.life <= 7:
                health.remove(healthpoint8)
        if healthpoint7 in health:
            if PlayerBoss.life <= 6:
                health.remove(healthpoint7)
        if healthpoint6 in health:
            if PlayerBoss.life <= 5:
                health.remove(healthpoint6)
        if healthpoint5 in health:
            if PlayerBoss.life <= 4:
                health.remove(healthpoint5)
        if healthpoint4 in health:
            if PlayerBoss.life <= 3:
                health.remove(healthpoint4)
        if healthpoint3 in health:
            if PlayerBoss.life <= 2:
                health.remove(healthpoint3)
        if healthpoint2 in health:
            if PlayerBoss.life <= 1:
                health.remove(healthpoint2)
        if healthpoint1 in health:
            if PlayerBoss.life <= 0:
                health.remove(healthpoint1)
                
        if PlayerBoss.x < PlayerBoss.shieldcap: 
            if shieldpoint10 in shield:
                if PlayerBoss.shield <= 9:
                    shield.remove(shieldpoint10)
            if shieldpoint9 in shield:
                if PlayerBoss.shield <= 8:
                    shield.remove(shieldpoint9)
            if shieldpoint8 in shield:
                if PlayerBoss.shield <= 7:
                    shield.remove(shieldpoint8)
            if shieldpoint7 in shield:
                if PlayerBoss.shield <= 6:
                    shield.remove(shieldpoint7)
            if shieldpoint6 in shield:
                if PlayerBoss.shield <= 5:
                    shield.remove(shieldpoint6)
            if shieldpoint5 in shield:
                if PlayerBoss.shield <= 4:
                    shield.remove(shieldpoint5)
            if shieldpoint4 in shield:
                if PlayerBoss.shield <= 3:
                    shield.remove(shieldpoint4)
            if shieldpoint3 in shield:
                if PlayerBoss.shield <= 2:
                    shield.remove(shieldpoint3)
            if shieldpoint2 in shield:
                if PlayerBoss.shield <= 1:
                    shield.remove(shieldpoint2)
            if shieldpoint1 in shield:
                if PlayerBoss.shield <= 0:
                    shield.remove(shieldpoint1)
            
        if PlayerBoss.x > PlayerBoss.shieldcap - 2:
            if PlayerBoss.shield == 9:
                shield.add(shieldpoint10)
            if PlayerBoss.shield == 8:
                shield.add(shieldpoint9)
            if PlayerBoss.shield == 7:
                shield.add(shieldpoint8)
            if PlayerBoss.shield == 6:
                shield.add(shieldpoint7)
            if PlayerBoss.shield == 5:
                shield.add(shieldpoint6)
            if PlayerBoss.shield == 4:
                shield.add(shieldpoint5)
            if PlayerBoss.shield == 3:
                shield.add(shieldpoint4)
            if PlayerBoss.shield == 2:
                shield.add(shieldpoint3)
            if PlayerBoss.shield == 1:
                shield.add(shieldpoint2)
            if PlayerBoss.shield == 0:
                shield.add(shieldpoint1)            
                        
        #sprite drawing
        levelground.draw(screen)
        level.draw(screen)
        ammo.draw(screen)
        player.draw(screen)
        enemy.draw(screen)
        health.draw(screen)
        shield.draw(screen)
        HUD.draw(screen)
        
        #screen flip
        pygame.display.flip()
# def GameOver
def GameOver():
    #globals
    global userStart
    userStart = 0
    #screen setup
    pygame.display.set_caption("Halo - Chris Bonner")
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    #sound
    sndMenu.play(-1)
    #picture for sprite class
    pygame.mouse.set_visible(True)
    try:
        startscreen = os.path.join('Sprites','startscreen.png')
        graphicname = os.path.join('Sprites','Graphic.bmp')
        mousepic = os.path.join('Sprites','mouse.bmp')
    except:
        sys.exit("could not load image files in 'Sprites' folder :-(")
    #sprite class
    startscreen = startscreenclass.startscreen(screen, startscreen)
    Halo = startscreenclass.HaloGraphic(screen,graphicname)
    Mouse = startscreenclass.tempMouse(screen,mousepic)
    
    #label GameOver
    lblGameOver = miniGUI.Label()
    lblGameOver.font =  pygame.font.SysFont(None, 50)
    lblGameOver.text = "Game Over"
    lblGameOver.center = (400,200)
    lblGameOver.size = (250,40)
    lblGameOver.bgColor = ((0x00, 0x00, 0x00))
    lblGameOver.fgColor = ((0xFF, 0xFF, 0xFF))
    
    #button Retry
    btnRetry = miniGUI.Button()
    btnRetry.text = "Retry?"
    btnRetry.center = (400,300)
    btnRetry.size = (75,21)
    btnRetry.bgColor = (0x00,0x00,0x00)
    btnRetry.fgColor = (0xFF, 0xFF, 0xFF)

    #button Menu
    btnMenu = miniGUI.Button()
    btnMenu.text = "Main Menu"
    btnMenu.center = (400, 350)
    btnMenu.size = (120,21)
    btnMenu.bgColor = (0x00,0x00,0x00)
    btnMenu.fgColor = (0xFF,0xff,0xff)
    
    #button Exit
    btnExit = miniGUI.Button()
    btnExit.text = "Exit"
    btnExit.center = (400,400)
    btnExit.size = (50,21)
    btnExit.bgColor = (0x00,0x00,0x00)
    btnExit.fgColor = (0xff,0xff,0xff)
    
    #sprite ordered update
    allsprites = pygame.sprite.OrderedUpdates(startscreen,Halo,lblGameOver,btnRetry,btnMenu,btnExit,Mouse)
    #set clock and game loop
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        #clock ticks
        clock.tick(60)
        #mouse visibily off
        pygame.mouse.set_visible(False)
        #exit event or game start
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Keepgoing = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
            if btnRetry.active == True:
                sndMenu.stop()
                main()
            elif btnMenu.active == True:
                StartScreen()
            elif btnExit.active == True:
                Keepgoing = False
                pygame.display.quit()
                pygame.quit()
                sys.exit()
                
        #clear, updates and flip
        allsprites.clear(screen,background)
        allsprites.update()
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()
#def ScoreScreen  
def ScoreScreen():
    #globals
    global userStart
    global scorehealth
    global scoreenemystart
    global scorebonus
    global PlayerName
    userStart = 0
    #screen setup
    pygame.display.set_caption("Halo - Chris Bonner")
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    #sound
    sndMenu.play(-1)
    sndLaser.set_volume(0.7)
    sndRifle.set_volume(0.3)
    #picture for sprite class
    pygame.mouse.set_visible(True)
    
    try:
        startscreen = os.path.join('Sprites','startscreen.png')
        graphicname = os.path.join('Sprites','Graphic.bmp')
        mousepic = os.path.join('Sprites','mouse.bmp')
    except:
        sys.exit("could not load image files in 'Sprites' folder :-(")
        
    #sprite class
    startscreen = startscreenclass.startscreen(screen, startscreen)
    Halo = startscreenclass.HaloGraphic(screen,graphicname)
    Mouse = startscreenclass.tempMouse(screen,mousepic)
    
    #score
    score = "%s" %(scorehealth + scoreenemystart + scorebonus)
    #saving score
    HighScoreOld = []
    HighScoreOld = Save.Scores()
    HighScoreNew = []
    NameScore = []
    NameScore = Save.Names()
    a = 0
    try:
        if PlayerName == None:
            PlayerName = "Player"
    except:
        PlayerName = "Player"
        
    for (i, item) in enumerate(HighScoreOld):
        if int(item) < int(score):
            HighScoreNew.append(item)
        elif int(item) >= int(score) and a == 0:
            HighScoreNew.append(score)
            NameScore.remove(NameScore[i])
            NameScore.insert(i, PlayerName)
            a = 1
        else:
            HighScoreNew.append(item)
    Save.WriteScores(HighScoreNew)
    Save.WriteNames(NameScore)
    HighScoreNew.reverse()
    NameScore.reverse()
    #label Score
    lblScore = miniGUI.Label()
    lblScore.font =  pygame.font.SysFont(None, 50)
    lblScore.text = "Your Score %s" % score
    lblScore.center = (400,200)
    lblScore.size = (350,40)
    lblScore.bgColor = ((0x00, 0x00, 0x00))
    lblScore.fgColor = ((0xFF, 0xFF, 0xFF))

    lblHighScores = miniGUI.Label()
    lblHighScores.font =  pygame.font.SysFont(None, 50)
    lblHighScores.text = "High Scores"
    lblHighScores.center = (100,50)
    lblHighScores.size = (200,40)
    lblHighScores.bgColor = ((0x00, 0x00, 0x00))
    lblHighScores.fgColor = ((0xFF, 0xFF, 0xFF))

    lblScore1 = miniGUI.Label()
    lblScore1.font =  pygame.font.SysFont(None, 30)
    lblScore1.text = "%s" % NameScore[0] + " " +  "%s" %  HighScoreNew[0]
    lblScore1.center = (100,100)
    lblScore1.size = (150,25)
    lblScore1.bgColor = ((0x00, 0x00, 0x00))
    lblScore1.fgColor = ((0xFF, 0xFF, 0xFF))

    lblScore2 = miniGUI.Label()
    lblScore2.font =  pygame.font.SysFont(None, 30)
    lblScore2.text = "%s" % NameScore[1] + " " +  "%s" %  HighScoreNew[1]
    lblScore2.center = (100,150)
    lblScore2.size = (150,25)
    lblScore2.bgColor = ((0x00, 0x00, 0x00))
    lblScore2.fgColor = ((0xFF, 0xFF, 0xFF))

    lblScore3 = miniGUI.Label()
    lblScore3.font =  pygame.font.SysFont(None, 30)
    lblScore3.text = "%s" % NameScore[2] + " " +  "%s" %  HighScoreNew[2]
    lblScore3.center = (100,200)
    lblScore3.size = (150,25)
    lblScore3.bgColor = ((0x00, 0x00, 0x00))
    lblScore3.fgColor = ((0xFF, 0xFF, 0xFF))

    lblScore4 = miniGUI.Label()
    lblScore4.font =  pygame.font.SysFont(None, 30)
    lblScore4.text = "%s" % NameScore[3] + " " +  "%s" %  HighScoreNew[3]
    lblScore4.center = (100,250)
    lblScore4.size = (150,25)
    lblScore4.bgColor = ((0x00, 0x00, 0x00))
    lblScore4.fgColor = ((0xFF, 0xFF, 0xFF))

    lblScore5 = miniGUI.Label()
    lblScore5.font =  pygame.font.SysFont(None, 30)
    lblScore5.text = "%s" % NameScore[4] + " " +  "%s" %  HighScoreNew[4]
    lblScore5.center = (100,300)
    lblScore5.size = (150,25)
    lblScore5.bgColor = ((0x00, 0x00, 0x00))
    lblScore5.fgColor = ((0xFF, 0xFF, 0xFF))

    lblScore6 = miniGUI.Label()
    lblScore6.font =  pygame.font.SysFont(None, 30)
    lblScore6.text = "%s" % NameScore[5] + " " +  "%s" %  HighScoreNew[5]
    lblScore6.center = (100,350)
    lblScore6.size = (150,25)
    lblScore6.bgColor = ((0x00, 0x00, 0x00))
    lblScore6.fgColor = ((0xFF, 0xFF, 0xFF))

    lblScore7 = miniGUI.Label()
    lblScore7.font =  pygame.font.SysFont(None, 30)
    lblScore7.text = "%s" % NameScore[6] + " " +  "%s" %  HighScoreNew[6]
    lblScore7.center = (100,400)
    lblScore7.size = (150,25)
    lblScore7.bgColor = ((0x00, 0x00, 0x00))
    lblScore7.fgColor = ((0xFF, 0xFF, 0xFF))
    
    lblScore8 = miniGUI.Label()
    lblScore8.font =  pygame.font.SysFont(None, 30)
    lblScore8.text = "%s" % NameScore[7] + " " +  "%s" %  HighScoreNew[7]
    lblScore8.center = (100,450)
    lblScore8.size = (150,25)
    lblScore8.bgColor = ((0x00, 0x00, 0x00))
    lblScore8.fgColor = ((0xFF, 0xFF, 0xFF))

    lblScore9 = miniGUI.Label()
    lblScore9.font =  pygame.font.SysFont(None, 30)
    lblScore9.text = "%s" % NameScore[8] + " " +  "%s" %  HighScoreNew[8]
    lblScore9.center = (100,500)
    lblScore9.size = (150,25)
    lblScore9.bgColor = ((0x00, 0x00, 0x00))
    lblScore9.fgColor = ((0xFF, 0xFF, 0xFF))
    
    lblScore10 = miniGUI.Label()
    lblScore10.font =  pygame.font.SysFont(None, 30)
    lblScore10.text = "%s" % NameScore[9] + " " +  "%s" %  HighScoreNew[9]
    lblScore10.center = (100,550)
    lblScore10.size = (150,25)
    lblScore10.bgColor = ((0x00, 0x00, 0x00))
    lblScore10.fgColor = ((0xFF, 0xFF, 0xFF))
    
    #button retry
    btnRetry = miniGUI.Button()
    btnRetry.text = "Retry?"
    btnRetry.center = (400,300)
    btnRetry.size = (75,21)
    btnRetry.bgColor = (0x00,0x00,0x00)
    btnRetry.fgColor = (0xFF, 0xFF, 0xFF)

    #button Menu 
    btnMenu = miniGUI.Button()
    btnMenu.text = "Main Menu"
    btnMenu.center = (400, 350)
    btnMenu.size = (120,21)
    btnMenu.bgColor = (0x00,0x00,0x00)
    btnMenu.fgColor = (0xFF,0xff,0xff)
    
    #button Exit
    btnExit = miniGUI.Button()
    btnExit.text = "Exit"
    btnExit.center = (400,400)
    btnExit.size = (50,21)
    btnExit.bgColor = (0x00,0x00,0x00)
    btnExit.fgColor = (0xff,0xff,0xff)
    
    #sprite ordered update
    allsprites = pygame.sprite.OrderedUpdates(startscreen,Halo,lblScore,lblHighScores,
    lblScore1,lblScore2,lblScore3,lblScore4,lblScore5,lblScore6,lblScore7,
    lblScore8,lblScore9,lblScore10,btnRetry,btnMenu,btnExit,Mouse)
    #set clock and game loop
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        #clock ticks
        clock.tick(60)
        #mouse visibily off
        pygame.mouse.set_visible(False)
        #exit event or game start
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Keepgoing = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
            if btnRetry.active == True:
                sndMenu.stop()
                main()
            elif btnMenu.active == True:
                StartScreen()
            elif btnExit.active == True:
                Keepgoing = False
                pygame.display.quit()
                pygame.quit()
                sys.exit()
                
        #clear, updates and flip
        allsprites.clear(screen,background)
        allsprites.update()
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

#if name = main run startscreen
if __name__ == "__main__":
    StartScreen()



