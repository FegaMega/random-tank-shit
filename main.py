import pygame, sys
from pygame.locals import *
import playerScript
import setup
def rectCollision(Ax, Ay, Awidth, Aheight, Bx, By, Bwidth, Bheight):
    return (Ax + Awidth > Bx) and (Ax < Bx + Bwidth) and (Ay + Aheight > By) and (Ay < By + Bheight)


class gameClass:
    def __init__(self) -> None:
        self.Clock = pygame.time.Clock()
        self.r = True
        self.screenSize = [700, 700]
        self.screen = pygame.display.set_mode(self.screenSize)
        self.player = playerScript.Player(400, 400, 1, True, [])
        self.player2 = playerScript.Player(200, 200, 1, False, [])
        self.deltaTime = 0
        self.MapObj = setup.Map(1)
        self.MapObj.loadMap()
    def handleEvent(self):
        if pygame.event.get(QUIT):
            self.r = False
        keys = pygame.key.get_pressed()
        if keys[K_w] == True:
            self.player.updateVal(speed=.25)
        elif keys[K_s] == True:
            self.player.updateVal(speed=-.25)
        else:
            self.player.updateVal(speed=0)
        if keys[K_a] == True:
            self.player.updateVal(angle=.125)
        elif keys[K_d] == True:
            self.player.updateVal(angle=-.125)
        else:
            self.player.updateVal(angle=0)
        
        if keys[K_UP] == True:
            self.player2.updateVal(speed=.25)
        elif keys[K_DOWN] == True:
            self.player2.updateVal(speed=-.25)
        else:
            self.player2.updateVal(speed=0)
        if keys[K_LEFT] == True:
            self.player2.updateVal(angle=.125)
        elif keys[K_RIGHT] == True:
            self.player2.updateVal(angle=-.125)
        else:
            self.player2.updateVal(angle=0) 
        for event in pygame.event.get(KEYDOWN):
            #player1
            if event.key == K_SPACE:
                self.player.shoot()

            #player2
            if event.key == K_RSHIFT:
                self.player2.shoot()

    def mapPlayerCollision(self, player):
        playerPos = player.getVal(pos=1)
        playerSize = player.getVal(size=1)
        for y in range(round(round(playerPos[1]-25)/25), 
                       round(round(playerPos[1]+playerSize[1]+25)/25)):
            if y < 0:
                y = 0
            if y > len(self.MapObj.map)-1:
                y = len(self.MapObj.map)-1
            for x in range(round(round(playerPos[0]-25)/25), 
                           round(round(playerPos[0]+playerSize[0]+25)/25)):
                if x < 0:
                    x = 0
                if x > len(self.MapObj.map[y])-1:
                    x = len(self.MapObj.map[y])-1

                if self.MapObj.map[y][x] == 0:
                    continue

                if self.MapObj.map[y][x] == 1:
                    if True == rectCollision(x*25, y*25, 5, 25, 
                                             playerPos[0], playerPos[1], 
                                             playerSize[0], playerSize[1]):
                        midpos = player.getVal(Midpos=1)
                        if midpos[0] < x*25:
                            if player.angle < 90 or player.angle > 270 or player.speed < 0:
                                player.speed = 0
                        
                        elif midpos[0] > x*25 + 5:
                            if player.angle > 90 and player.angle < 270 or player.speed < 0:
                                player.speed = 0
                        if y+1 != len(self.MapObj.map):
                            if self.MapObj.map[y+1][x] != 1 and self.MapObj.map[y+1][x] != 2 and self.MapObj.map[y+1][x] != 3:
                                if midpos[1] > y*25 + 25:
                                    if player.angle < 180 or player.speed < 0:
                                        player.speed = 0
                        if y-1 != -1:
                            if self.MapObj.map[y-1][x] != 1 and self.MapObj.map[y-1][x] != 3:
                                if midpos[1] < y*25:
                                    if player.angle > 180 or player.speed < 0:
                                        player.speed = 0


                if self.MapObj.map[y][x] == 2:
                    if True == rectCollision(x*25, y*25, 25, 5, 
                                             playerPos[0], playerPos[1], 
                                             playerSize[0], playerSize[1]):
                        midpos = player.getVal(Midpos=1)
                        if midpos[1] < y*25:
                            if player.angle > 180 or player.speed < 0:
                                player.speed = 0
                        elif midpos[1] > y*25 + 25:
                            if player.angle < 180 or player.speed < 0:
                                player.speed = 0
                        if x+1 != len(self.MapObj.map[y]):
                            if self.MapObj.map[y][x+1] != 1 and self.MapObj.map[y][x+1] != 2 and self.MapObj.map[y][x+1] != 3:
                                if midpos[0] > x*25+5:
                                    if player.angle > 90 and player.angle < 270 or player.speed < 0:
                                        player.speed = 0
                        if x-1 != -1:
                            if self.MapObj.map[y][x+1] != 2 and self.MapObj.map[y][x+1] != 3:
                                if midpos[0] < x*25:
                                    if player.angle < 90 or player.angle > 270 or player.speed < 0:
                                        player.speed = 0
                if self.MapObj.map[y][x] == 3:
                    if True == rectCollision(x*25, y*25, 25, 5, 
                                             playerPos[0], playerPos[1], 
                                             playerSize[0], playerSize[1]):
                        midpos = player.getVal(Midpos=1)
                        if midpos[1] < y*25:
                            if player.angle > 180 or player.speed < 0:
                                player.speed = 0
                        elif midpos[1] > y*25:
                            if player.angle < 180 or player.speed < 0:
                                player.speed = 0
                        if x+1 != len(self.MapObj.map[y]):
                            if self.MapObj.map[y][x+1] != 1 and self.MapObj.map[y][x+1] != 2 and self.MapObj.map[y][x+1] != 3:
                                if midpos[0] > x*25+5:
                                    if player.angle > 90 and player.angle < 270 or player.speed < 0:
                                        player.speed = 0
                        if x-1 != -1:
                            if self.MapObj.map[y][x+1] != 2 and self.MapObj.map[y][x+1] != 3:
                                if midpos[0] < x*25:
                                    if player.angle < 90 or player.angle > 270 or player.speed < 0:
                                        player.speed = 0
                    if True == rectCollision(x*25, y*25, 5, 25, 
                                             playerPos[0], playerPos[1], 
                                             playerSize[0], playerSize[1]):
                        midpos = player.getVal(Midpos=1)
                        if midpos[0] < x*25:
                            if player.angle < 90 or player.angle > 270 or player.speed < 0:
                                player.speed = 0
                        
                        elif midpos[0] > x*25:
                            if player.angle > 90 and player.angle < 270 or player.speed < 0:
                                player.speed = 0
                        if y+1 != len(self.MapObj.map):
                            if self.MapObj.map[y+1][x] != 1 and self.MapObj.map[y+1][x] != 2 and self.MapObj.map[y+1][x] != 3:
                                if midpos[1] > y*25 + 25:
                                    if player.angle < 180 or player.speed < 0:
                                        player.speed = 0
                        if y-1 != -1:
                            if self.MapObj.map[y-1][x] != 1 and self.MapObj.map[y-1][x] != 3:
                                if midpos[1] < y*25:
                                    if player.angle > 180 or player.speed < 0:
                                        player.speed = 0
    def mapBulletCollision(self, bullets):
        bulletwaitTime = 5
        for bullet in bullets:
            for y in range(round(round(bullet.pos[1]-25)/25), 
                        round(round(bullet.pos[1]+bullet.getVal(size=1)[1]+25)/25)):
                if y < 0:
                    y = 0
                if y > len(self.MapObj.map)-1:
                    y = len(self.MapObj.map)-1
                for x in range(round(round(bullet.pos[0]-25)/25), 
                            round(round(bullet.pos[0]+bullet.getVal(size=1)[0]+25)/25)):
                    if x < 0:
                        x = 0
                    if x > len(self.MapObj.map[y])-1:
                        x = len(self.MapObj.map[y])-1

                    if self.MapObj.map[y][x] == 0:
                        continue

                    if self.MapObj.map[y][x] == 1:
                        #CUBE
                        # #
                        # #
                        # #
                        # #
                        #Right or Left Side hit
                        if bullet.flippedTime[0] < 0:
                            if True == rectCollision(x*25+3, y*25, 3, 25, 
                                                bullet.pos[0], bullet.pos[1], 
                                                bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]) or True == rectCollision(x*25, y*25, 2, 25, 
                                                bullet.pos[0], bullet.pos[1], 
                                                bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):    
                                bullet.flipped[0] = not bullet.flipped[0]
                                bullet.flippedTime[0] = bulletwaitTime
                        #Bottom Side hit 
                        if bullet.flippedTime[1] < 0:
                            if y+1 != len(self.MapObj.map):
                                if self.MapObj.map[y+1][x] != 1 and self.MapObj.map[y+1][x] != 2 and self.MapObj.map[y+1][x] != 3: 
                                    if True == rectCollision(x*25, y*25+23, 5, 3, 
                                                        bullet.pos[0], bullet.pos[1], 
                                                        bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):
                                        bullet.flipped[1] = not bullet.flipped[1]
                                        bullet.flippedTime[1] = bulletwaitTime
                            else:
                                if True == rectCollision(x*25, y*25+23, 5, 3, 
                                                        bullet.pos[0], bullet.pos[1], 
                                                        bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):
                                    bullet.flipped[1] = not bullet.flipped[1]
                                    bullet.flippedTime[1] = bulletwaitTime
                            #Top Side hit
                            if y-1 != -1:
                                if self.MapObj.map[y-1][x] != 1 and self.MapObj.map[y-1][x] != 3: 
                                    if True == rectCollision(x*25, y*25, 5, 3, 
                                                        bullet.pos[0], bullet.pos[1], 
                                                        bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):
                                        bullet.flipped[1] = not bullet.flipped[1]
                                        bullet.flippedTime[1] = bulletwaitTime
                            else:
                                if True == rectCollision(x*25, y*25, 5, 3, 
                                                    bullet.pos[0], bullet.pos[1], 
                                                    bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):
                                    bullet.flipped[1] = not bullet.flipped[1]
                                    bullet.flippedTime[1] = bulletwaitTime

                    if self.MapObj.map[y][x] == 2:
                        #CUBE 
                        # ####
                        #Right or Left Side hit
                        if bullet.flippedTime[0] < 0:
                            if x+1 != len(self.MapObj.map[y]):
                                if self.MapObj.map[y][x+1] != 1 and self.MapObj.map[y][x+1] != 2 and self.MapObj.map[y][x+1] != 3: 
                                    if True == rectCollision(x*25+23, y*25, 2, 5, 
                                                        bullet.pos[0], bullet.pos[1], 
                                                        bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):
                                        bullet.flipped[0] = not bullet.flipped[0]
                                        bullet.flippedTime[0] = bulletwaitTime
                            else:
                                if True == rectCollision(x*25+23, y*25, 2, 5, 
                                                        bullet.pos[0], bullet.pos[1], 
                                                        bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):
                                    bullet.flipped[0] = not bullet.flipped[0]
                                    bullet.flippedTime[0] = bulletwaitTime
                            if x-1 != -1:
                                if self.MapObj.map[y][x-1] != 2 and self.MapObj.map[y][x-1] != 3:     
                                    if True == rectCollision(x*25, y*25, 2, 5, 
                                                        bullet.pos[0], bullet.pos[1], 
                                                        bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):    
                                        bullet.flipped[0] = not bullet.flipped[0]
                                        bullet.flippedTime[0] = bulletwaitTime
                            else:
                                if True == rectCollision(x*25, y*25, 2, 5, 
                                                        bullet.pos[0], bullet.pos[1], 
                                                        bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):    
                                        bullet.flipped[0] = not bullet.flipped[0]
                                        bullet.flippedTime[0] = bulletwaitTime
                        
                        #Bottom Side hit
                        #Top Side hit
                        if bullet.flippedTime[1] < 0:
                            if True == rectCollision(x*25, y*25+3, 25, 2, 
                                                bullet.pos[0], bullet.pos[1], 
                                                bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]) or True == rectCollision(x*25, y*25, 25, 2, 
                                                bullet.pos[0], bullet.pos[1], 
                                                bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):
                                bullet.flipped[1] = not bullet.flipped[1]
                                bullet.flippedTime[1] = bulletwaitTime

                    if self.MapObj.map[y][x] == 3:
                        #CUBE
                        # #
                        # #
                        # #
                        # #
                        #Right or Left Side hit
                        if bullet.flippedTime[0] < 0:
                            if True == rectCollision(x*25+3, y*25+5, 2, 20, 
                                                bullet.pos[0], bullet.pos[1], 
                                                bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]) or True == rectCollision(x*25, y*25, 2, 25, 
                                                bullet.pos[0], bullet.pos[1], 
                                                bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):    
                                bullet.flipped[0] = not bullet.flipped[0]
                                bullet.flippedTime[0] = bulletwaitTime
                        
                        #Bottom Side hit 
                        if bullet.flippedTime[1] < 0:
                            if y+1 != len(self.MapObj.map):
                                if self.MapObj.map[y+1][x] != 1 and self.MapObj.map[y+1][x] != 2 and self.MapObj.map[y+1][x] != 3: 
                                    if True == rectCollision(x*25, y*25+23, 5, 2, 
                                                        bullet.pos[0], bullet.pos[1], 
                                                        bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):
                                        bullet.flipped[1] = not bullet.flipped[1]
                                        bullet.flippedTime[1] = bulletwaitTime
                            else:
                                if True == rectCollision(x*25, y*25+23, 5, 2, 
                                                        bullet.pos[0], bullet.pos[1], 
                                                        bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):
                                    bullet.flipped[1] = not bullet.flipped[1]
                                    bullet.flippedTime[1] = bulletwaitTime
                            #Top Side hit
                            if y-1 != -1:
                                if self.MapObj.map[y-1][x] != 1 and self.MapObj.map[y-1][x] != 3: 
                                    if True == rectCollision(x*25, y*25, 5, 2, 
                                                        bullet.pos[0], bullet.pos[1], 
                                                        bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):
                                        bullet.flipped[1] = not bullet.flipped[1]
                                        bullet.flippedTime[1] = bulletwaitTime
                            else:
                                if True == rectCollision(x*25, y*25, 5, 2, 
                                                    bullet.pos[0], bullet.pos[1], 
                                                    bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):
                                    bullet.flipped[1] = not bullet.flipped[1]
                                    bullet.flippedTime[1] = bulletwaitTime
                        
                        #other one 

                        #CUBE 
                        # ####
                        #Right or Left Side hit
                        if bullet.flippedTime[0] < 0:
                            if x+1 != len(self.MapObj.map[y]):
                                if self.MapObj.map[y][x+1] != 1 and self.MapObj.map[y][x+1] != 2 and self.MapObj.map[y][x+1] != 3: 
                                    if True == rectCollision(x*25+23, y*25, 2, 5, 
                                                        bullet.pos[0], bullet.pos[1], 
                                                        bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):
                                        bullet.flipped[0] = not bullet.flipped[0]
                                        bullet.flippedTime[0] = bulletwaitTime
                            else:
                                if True == rectCollision(x*25+23, y*25, 2, 5, 
                                                        bullet.pos[0], bullet.pos[1], 
                                                        bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):
                                    bullet.flipped[0] = not bullet.flipped[0]
                                    bullet.flippedTime[0] = bulletwaitTime
                            if x-1 != -1:
                                if self.MapObj.map[y][x-1] != 2 and self.MapObj.map[y][x-1] != 3:     
                                    if True == rectCollision(x*25, y*25, 2, 5, 
                                                        bullet.pos[0], bullet.pos[1], 
                                                        bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):    
                                        bullet.flipped[0] = not bullet.flipped[0]
                                        bullet.flippedTime[0] = bulletwaitTime
                            else:
                                if True == rectCollision(x*25, y*25, 2, 5, 
                                                        bullet.pos[0], bullet.pos[1], 
                                                        bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):    
                                        bullet.flipped[0] = not bullet.flipped[0]
                                        bullet.flippedTime[0] = bulletwaitTime
                        
                        #Bottom Side hit
                        #Top Side hit
                        if bullet.flippedTime[1] < 0:
                            if True == rectCollision(x*25+5, y*25+3, 20, 2, 
                                                bullet.pos[0], bullet.pos[1], 
                                                bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]) or True == rectCollision(x*25, y*25, 25, 2, 
                                                bullet.pos[0], bullet.pos[1], 
                                                bullet.getVal(size=1)[0], bullet.getVal(size=1)[1]):
                                bullet.flipped[1] = not bullet.flipped[1]
                            bullet.flippedTime[1] = bulletwaitTime

    def bulletCollision(self, bullets, player):
        playerPos = player.getVal(pos=1)
        playerSize = player.getVal(size=1)
        for bullet in bullets:
            if True == rectCollision(bullet.pos[0], bullet.pos[1], bullet.size[0], bullet.size[1],
                            playerPos[0], playerPos[1], playerSize[0], playerSize[1]) and bullet.age > 5:
                player = playerScript.Player(300, 300, player.scale, player.one, [])
        return player
    def update(self):

        self.mapPlayerCollision(self.player)
        self.mapPlayerCollision(self.player2)

        self.mapBulletCollision(self.player.bullets)
        self.mapBulletCollision(self.player2.bullets)

        self.player.update(self.deltaTime)
        
        self.player2.update(self.deltaTime)
        
        self.player2 = self.bulletCollision(self.player.bullets, self.player2)
        self.player2 = self.bulletCollision(self.player2.bullets, self.player2)
        
        self.player = self.bulletCollision(self.player2.bullets, self.player)
        self.player = self.bulletCollision(self.player.bullets, self.player)
        

        return 0 
    def render(self):
        self.screen.fill((255, 255, 255))
        
        self.MapObj.draw(self.screen)
        
        self.player.draw(self.screen)
        self.player2.draw(self.screen)

        self.deltaTime = self.Clock.get_time()

        self.Clock.tick(60)
        
        pygame.display.update()

def main():
    game = gameClass()
    game.player.updateVal(x=400, y=400)
    while game.r == True:
        game.handleEvent()
        game.update()
        game.render()
    pygame.quit()
    return 0 
sys.exit(main())