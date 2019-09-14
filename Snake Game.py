#########################################
# File Name: APPLE VS ANDROID
# Description: My snake game!
# Author: Paula Yuan
# Date: November 2018
#########################################
from random import randint
import pygame
import time

pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.init()
WIDTH = 800
HEIGHT= 600
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

TOP = 0
BOTTOM = HEIGHT
MIDDLE = int(WIDTH/2.0)
GAME_TOP = 40
RED  = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW =(255, 255, 0)
fill = 0
red1, green1, blue1 = 30, 144, 255
LIGHT_BLUE = (red1, green1, blue1)
red2, green2, blue2 = 253, 122, 83
SALMON = (red2, green2, blue2)
PINK = (255, 182, 193)
BRIGHT_GREEN = (127, 255, 0)
BRIGHT_BLUE =(82, 239, 255)
MIDNIGHT = (10, 10, 90)
ORANGE = (255, 140, 0)

#---------------------------------------#
# functions                             #
#---------------------------------------#
def drawText(font, text, colour, x, y):
    graphics = font.render(text, 1, colour)
    gameWindow.blit(graphics, (x, y))

def redrawGameWindow():
    gameWindow.blit(bkgd, (0, 0))
    for i in range(len(segX)):
        if i == 0:
            blueValue = 255
            redValue = 30
            greenValue = 144
            segmentCLR = LIGHT_BLUE
        else:
            redInt, greenInt, blueInt = abs(red2-red1), abs(green2-green1), abs(blue2-blue1)
            blueValue = blueValue - blueInt/(len(segX))
            redValue = redValue + redInt/(len(segX))
            greenValue = greenValue - greenInt/(len(segX))
            segmentCLR = (redValue, greenValue, blueValue)
        pygame.draw.circle(gameWindow, segmentCLR, (segX[i]*HSTEP, segY[i]*VSTEP), SEGMENT_R, fill)
    drawApple()
    drawClock()
    drawPoisonApple()
    drawObstacle()
    # drawing border
    pygame.draw.rect(gameWindow, BLACK, (0, 0, 800, 30), fill)
    pygame.draw.rect(gameWindow, SALMON, (0, 30, 800, 1), 1)
    # Display score and levels
    scoreGraphics = smallFont2.render("Score: " + str(score), 1, WHITE)
    timeGraphics = smallFont2.render("Time left: " + str(period-elapsed), 1, WHITE)
    levelGraphics = smallFont2.render(city +" : " +objective, 1, WHITE) 
    gameWindow.blit(scoreGraphics, (10, 6))
    gameWindow.blit(timeGraphics, (650, 6))
    gameWindow.blit(levelGraphics, (150, 6))
    pygame.display.update() 

def drawApple():
    for i in range(len(appleX)):
        pygame.draw.circle(gameWindow, RED, (appleX[i]*HSTEP, appleY[i]*VSTEP), appleR, fill)

def drawPoisonApple():
    for i in range(len(poisonX)):
        pygame.draw.circle(gameWindow, BRIGHT_GREEN, (poisonX[i]*HSTEP, poisonY[i]*VSTEP), appleR, fill)
        
def drawClock():
    for i in range(len(clockX)):
        gameWindow.blit(clocky, (clockX[i]*HSTEP-SEGMENT_R, clockY[i]*VSTEP-SEGMENT_R))
        
def drawMenu():
    gameWindow.blit(menuBkgd, (0,0))
    drawText(bigFont, "The Apple Wars", WHITE, 350, 100)
    drawText(medFont2, "(and you're a snake)", WHITE, 440, 200)
    drawText(bigFont2, "INSTRUCTIONS", WHITE, 440, 300)
    pygame.draw.rect(gameWindow, WHITE, (430, 300, 225, 40), 2)
    drawText(medFont, "PRESS SPACEBAR TO START", WHITE, 390, 440)

def drawPauseMenu():
    gameWindow.blit(pauseBkgd, (0, 0))
    drawText(bigFont, "PAUSED", BLACK, 300, 130)
    drawText(medFont2, "CRONCH. Are you having fun eating apples?", BLACK, 190, 400)
    drawText(medFont2, "Press U to Unpause.", BLACK, 290, 450)
    pygame.display.update()

def drawLoseMenu():
    gameWindow.fill(MIDNIGHT)
    gameWindow.blit(pusheen, (400, 250))
    drawText(bigFont, "GAME OVER", WHITE, 80, 200)
    drawText(smallFont, "(Press Esc to close the game.)", WHITE, 80, 300)
    drawText(smallFont, "(Press Enter to retry.)", WHITE, 80, 330)
    pygame.display.update()

def drawWinMenu():
    gameWindow.blit(endBkgd, (0,0))
    drawText(bigFont, "YOU WIN!!!!!!", WHITE, 130, 200)
    drawText(smallFont, "(Press Esc to close the game.)", WHITE, 130, 300)
    drawText(smallFont, "(Press Enter to replay.)", WHITE, 130, 330)
    pygame.display.update()
    
def drawLore():
    drawText(medFont2, "iOS and Android have begun a digital OS war, and you, dear snake, are", WHITE, 50, 80)
    drawText(medFont2, "now a snake refugee, forced to flee your home. Luckily, there are", WHITE, 50, 110)
    drawText(medFont2, "objectives that will guide your way through five OS cities, until you", WHITE, 50, 140)
    drawText(medFont2, "finally reach your destination, the (relatively) peaceful city of", WHITE, 50, 170)
    drawText(medFont2, "Microsoft Windows. For food, collect iOS's spyware apples:", WHITE, 50, 200)
    pygame.draw.circle(gameWindow, RED, (640, 215), appleR, fill)
    drawText(medFont2, "However, there are also malware apples:", WHITE, 50, 230)
    pygame.draw.circle(gameWindow, BRIGHT_GREEN, (470, 245), appleR, fill)
    drawText(medFont2, "Avoid them, as they will slow you down while you deal with the malware.", WHITE, 50, 260)
    drawText(medFont2, "Furthermore, avoid the orange fences. They are extremely deadly.", WHITE, 50, 290)
    drawText(medFont2, "Lastly, don't forget about collecting clocks. They give you more time!", WHITE, 50, 320)
    drawText(medFont2, "Why? No idea. Good luck with your relocation!", WHITE, 50, 350)
   
def drawInstructionsMenu():
    gameWindow.fill(MIDNIGHT)
    drawLore()
    drawText(medFont2, "Controls: Arrow keys to move. Press 'p' to pause.", WHITE, 150, 400)
    drawText(medFont, "BACK", WHITE, 400, 450)
    pygame.draw.rect(gameWindow, WHITE, (390, 450, 80, 40), 2)

def drawObstacle():
    for i in range(len(obstacleX)):
        pygame.draw.rect(gameWindow, ORANGE, (obstacleX[i]*HSTEP-SEGMENT_R, obstacleY[i]*VSTEP-SEGMENT_R, obstacleW*HSTEP, obstacleH*HSTEP), fill)

def playMenuSong():
    pygame.mixer.music.load("stargazer.ogg")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)

def playMainSong():
    pygame.mixer.music.load("a real life.ogg")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loops=-1)

def playDrop():
    drop.set_volume(1)
    drop.play(0)

def countdownUnpause():
    pygame.draw.rect(gameWindow, BLACK, (390, 300, 50, 70), fill)
    drawText(bigFont, "3", WHITE, 400, 300)
    pygame.display.update()
    clock.tick(1)
    pygame.draw.rect(gameWindow, BLACK, (390, 300, 50, 70), fill)
    drawText(bigFont, "2", WHITE, 400, 300)
    pygame.display.update()
    clock.tick(1)
    pygame.draw.rect(gameWindow, BLACK, (390, 300, 50, 70), fill)
    drawText(bigFont, "1", WHITE, 400, 300)
    pygame.display.update()
    clock.tick(1)
    
#---------------------------------------#
# variables (that are only needed once) #
#---------------------------------------#
# snake's properties
SEGMENT_R = 10
HSTEP = 20
VSTEP = 20
stepX = 0
stepY = -VSTEP                          # initially the snake moves upards
segX = []
segY = []
for i in range(4):                      # add coordinates for the head and 3 segments
    segX.append(MIDDLE/HSTEP)
    segY.append((BOTTOM + i*VSTEP)/VSTEP)

# apple properties:
appleR = 8

# Time
clock = pygame.time.Clock()

#Whether to show various menus
showInstructionsMenu = False

#win?
win = False

#levels
obstacles = []
obstacleW = 20/HSTEP
obstacleH = 20/VSTEP

#Pausing
unpaused = False
            
#-----------------------------#
# Images, sound effects, font #
#-----------------------------#

#Backgrounds
pauseBkgd = pygame.image.load("pauseMenu.jpg").convert()
menuBkgd = pygame.image.load("android.png").convert()
endBkgd = pygame.image.load("endMenu.jpg").convert()
chromeBkgd = pygame.image.load("chromeos.png").convert()
macBkgd = pygame.image.load("macos.jpg").convert()
ubuntuBkgd = pygame.image.load("ubuntu.jpg").convert()
windowsBkgd = pygame.image.load("windows.jpg").convert()

#Clock
clocky = pygame.image.load("clocky.png").convert_alpha()
pusheen = pygame.image.load("pusheen.png").convert_alpha()
          
#sound effects
drop = pygame.mixer.Sound("drop.wav")

#font
smallFont = pygame.font.SysFont("Impact", 18)
medFont = pygame.font.SysFont("Impact", 30)
bigFont = pygame.font.SysFont("Impact", 60)
medFont2 = pygame.font.SysFont("Century Gothic", 20)
bigFont2 = pygame.font.SysFont("Century Gothic", 30)
smallFont2 = pygame.font.SysFont("Century Gothic", 20)

#---------------------------------------#
# main program                          #
#---------------------------------------#
print "Use the arrows and the space bar."
print "Hit ESC to end the program."

#---------------------------------------#

#display menu

replaying = True
while replaying:    
    #--------------------------------------------#
    #(re)define needed variables for each replay #
    #--------------------------------------------#
    stepX = 0
    stepY = -VSTEP                          # initially the snake moves upwards
    segX = []
    segY = []
    for i in range(4):                      # add coordinates for the head and 3 segments
        segX.append(MIDDLE/HSTEP)
        segY.append((BOTTOM + i*VSTEP)/VSTEP)

    # apple properties:
    appleX = [randint(appleR, (WIDTH-appleR)/HSTEP)]
    appleY = [randint(GAME_TOP, (HEIGHT-appleR))/VSTEP]

    # poison apple properties:
    poisonX = [randint(appleR, (WIDTH-appleR)/HSTEP)]
    poisonY = [randint(GAME_TOP, (HEIGHT-appleR))/VSTEP]

    # Counter for clocks, apples, and poison apples generated/eaten
    applesGenerated = 1
    poisonGenerated = 1
    clocksGenerated = 1
    poisonEaten = 0
    clocksEaten = 0
    applesEaten = 0

    # Scoring
    score = 0

    # Time
    period = 30
    elapsed = 0
    pauseElapsed = 0
    fps = 15

    # Clock properties
    clockX = [randint(5, (WIDTH-5)/HSTEP)]
    clockY = [randint(5, (HEIGHT-5)/VSTEP)]

    # keyboard
    left, right, up, down = False, False, True, False

    # Levels:
    level = 1
    
    #-----------------#
    # Starting menus  #
    #-----------------#
    
    #play menu music
    playMenuSong()
    
    #draw starting menu
    showMenu = True
    while showMenu:
        drawMenu()
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            showMenu = False
            
        clock.tick(10)
        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseX >= 430 and mouseX <= 655 and mouseY >= 300 and mouseY <= 340:
            pygame.draw.rect(gameWindow, BRIGHT_BLUE, (430, 300, 225, 40), 2)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    showInstructionsMenu = True
        else:
            pygame.event.clear()
        pygame.display.update()

        # draw instructions menu
        while showInstructionsMenu:
            drawInstructionsMenu()
            clock.tick(10)
            mouseX, mouseY = pygame.mouse.get_pos()
            if mouseX >= 390 and mouseX <= 470 and mouseY >= 450 and mouseY <= 490:
                pygame.draw.rect(gameWindow, BRIGHT_BLUE, (390, 450, 80, 40), 2)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        showInstructionsMenu = False
            else:
                pygame.event.clear()
            pygame.display.update()
                                    
    #stop menu music, load and play main game music        
    pygame.mixer.music.stop()
    playMainSong()
    
    # Start Timing:
    isTiming = True
    if isTiming:
        BEGIN = time.time()
        referenceTime = BEGIN

    #-------------------#
    # Start main game:  #
    #-------------------#
    
    inPlay = True
    while inPlay:

    # levels, with respective objectives and obstacles
        if level == 1:
            city = "Chrome OS"
            bkgd = chromeBkgd
            obstacleX = [MIDDLE/HSTEP]
            obstacleY = [TOP/VSTEP]
            for i in range(20):
                obstacleX.append(MIDDLE/HSTEP)
                obstacleY.append((obstacleW + i*VSTEP)/VSTEP)
            objective = "Collect 10 apples."
        elif level == 2:
            city = "Mac OS"
            bkgd = macBkgd
            objective = "Collect 10 clocks."
            for i in range(10):
                obstacleX.append(MIDDLE/2/HSTEP)
                obstacleY.append((obstacleW + i*VSTEP)/VSTEP)
        elif level == 3:
            city = "Ubuntu"
            bkgd = ubuntuBkgd
            objective = "Collect 1 poison apple and 10 apples."
        elif level == 4:
            city = "Windows"
            bkgd = windowsBkgd
            objective = "Collect 10 apples and 3 poison apples."
            for i in range(10):
                obstacleX.append((MIDDLE+MIDDLE/2)/HSTEP)
                obstacleY.append((obstacleW + i*VSTEP)/VSTEP)

        redrawGameWindow()

    # Countdown after unpausing
        while unpaused:
            countdownUnpause()
            unpaused = False

        clock.tick(fps)
        if elapsed > period:
            inPlay = False
            referenceTime = time.time()

    # pause menu 
        if keys[pygame.K_p]:
            pause = True
            pauseStart = time.time()
            while pause:
                drawPauseMenu()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_u]:
                    pause = False
                    unpaused = True
                else:
                    pygame.event.clear()
            pauseElapsed = round(time.time() - pauseStart, 1)
        elapsed = round(time.time() - referenceTime, 1)
        elapsed = elapsed - pauseElapsed
       
    # keyboard stuff
        pygame.event.clear()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            inPlay = False
        if keys[pygame.K_UP] and not down:
            stepX = 0
            stepY = -VSTEP
            up, left, right = True, False, False
        elif keys[pygame.K_DOWN] and not up:
            stepX = 0
            stepY = VSTEP
            down, left, right = True, False, False
        elif keys[pygame.K_LEFT] and not right:
            stepX = -HSTEP
            stepY = 0
            left, up, down = True, False, False
        elif keys[pygame.K_RIGHT] and not left:
            stepX = HSTEP
            stepY = 0
            right, up, down = True, False, False
       
    # move the segments
        lastIndex = len(segX)-1
        for i in range(lastIndex,0,-1):     # starting from the tail, and going backwards:
            segX[i] = segX[i-1]               # every segment takes the coordinates
            segY[i] = segY[i-1]               # of the previous one

    # move the head
        segX[0] = segX[0] + stepX/HSTEP
        segY[0] = segY[0] + stepY/VSTEP

    # Keeping the snake in the window
        if segX[0] > WIDTH/HSTEP or segX[0] < 0 or segY[0] > HEIGHT/VSTEP or segY[0] < GAME_TOP/VSTEP:
            inPlay = False
            
    # Detecting if the snake goes into itself
        for i in range(1,len(segX)):
            if segX[0] == segX[i] and segY[0] == segY[i]:
                inPlay = False

    # Eating apples
        for i in range(len(appleX)-1, -1, -1):
            if segX[0] == appleX[i] and segY[0] == appleY[i]:
                playDrop()
                appleX.pop(i)
                appleY.pop(i)
                segX.append(segX[-1])           
                segY.append(segY[-1])
                score = score + 1
                applesEaten = applesEaten + 1
                # FASTERRRRRR
                if score % 3 == 0:
                    fps = fps + 2
                
    # Generating more apples
        if elapsed / applesGenerated > 2: # use CONSTANTS
            appleX.append(randint(appleR, (WIDTH-appleR)/HSTEP))
            appleY.append(randint(GAME_TOP, (HEIGHT-appleR))/VSTEP)
            applesGenerated = applesGenerated + 1

    # Generating/eating clocks
        if elapsed / clocksGenerated > 6: # USE CONSTANTS
            clockX.append(randint(5, (WIDTH-5)/HSTEP))
            clockY.append(randint(GAME_TOP, (HEIGHT-5))/VSTEP)
            clocksGenerated = clocksGenerated + 1
            
        for i in range(len(clockX)-1, -1, -1):
            if segX[0] == clockX[i] and segY[0] == clockY[i]:
                playDrop()
                clockX.pop(i)
                clockY.pop(i)
                clocksEaten = clocksEaten + 1
                period = period + 6
                
    # Generating/eating poison apples
        if elapsed / poisonGenerated > 3:# USE CONSTANTS
            poisonX.append(randint(5, (WIDTH-5)/HSTEP))
            poisonY.append(randint(GAME_TOP, (HEIGHT-5))/VSTEP)
            poisonGenerated = poisonGenerated + 1
            
        for i in range(len(poisonX)-1, -1, -1):
            if segX[0] == poisonX[i] and segY[0] == poisonY[i]:
                playDrop()
                poisonX.pop(i)
                poisonY.pop(i)
                poisonEaten = poisonEaten + 1
                fps = 0.5*fps
                
    # Checking apples/poison apples/clocks (if they're in the obstacle)
        for i in range(len(obstacleX)):
            for j in range(len(appleX)):
                if appleX[j] == obstacleX[i] and appleY[j] == obstacleY[i]:
                    appleX[j] = appleX[j] + 1
            for j in range(len(clockX)):
                if clockX[j] in range(obstacleX[i], obstacleX[i]+obstacleW) and clockY[j] in range(obstacleY[i], obstacleY[i]+obstacleH):
                    clockX[j] = clockX[j] + 1
            for j in range(len(poisonX)):
                if poisonX[j] == obstacleX[i] and poisonY[j] == obstacleY[i]:
                    poisonX[j] = poisonX[j] + 1
                
    # Running into obstacles
        for i in range(len(obstacleY)):
            if segX[0] == obstacleX[i]:
                if segY[0] >= obstacleY[i] and segY[0] <= obstacleY[i]+obstacleH/20:
                    inPlay = False
            if segX[0] == obstacleX[i]+obstacleW/20:
                if segY[0] >= obstacleY[i] and segY[0] <= obstacleY[i]+obstacleH/20:
                    inPlay = False
                    
    # Meeting objectives
        if level == 1:
            if score == 10:
                level = level + 1
                applesEaten = 0
                poisonEaten = 0
                clocksEaten = 0
                if keys[pygame.K_a]:
                    level = 2
        if level == 2:
            if clocksEaten == 10:
                level = level + 1
                applesEaten = 0
                poisonEaten = 0
                clocksEaten = 0
                if keys[pygame.K_s]:
                    level = 3
        if level == 3:
            if poisonEaten >= 1 and applesEaten >= 10:
                level = level + 1
                applesEaten = 0
                poisonEaten = 0
                clocksEaten = 0
                if keys[pygame.K_d]:
                    level = 4
        if level == 4:
            if poisonEaten >=3 and applesEaten >= 10:
                win = True
                inPlay = False

# display respective end menus if win/lose
    if win == True:
        showWinEnd = True
        while showWinEnd:
            drawWinMenu()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                showWinEnd = False
                replaying = False
            if keys[pygame.K_RETURN]:
                showWinEnd = False
            else:
                pygame.event.clear()
    else:
        showLoseEnd = True
        while showLoseEnd:
            drawLoseMenu()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                showLoseEnd = False
                replaying = False
            if keys[pygame.K_RETURN]:
                showLoseEnd = False
            else:
                pygame.event.clear()
#---------------------------------------#    
pygame.quit()
