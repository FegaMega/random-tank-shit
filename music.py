import pygame, math

class music:
    def __init__(self) -> None:
        self.Music = pygame.mixer.Channel(0)
        self.shoot1 = pygame.mixer.Channel(1)
        self.shoot2 = pygame.mixer.Channel(2)
        self.soundEffect = pygame.mixer.Channel(1)
        self.musicFolder = "data/Music/"
        self.shootSound = pygame.mixer.Sound(self.musicFolder + "shoot(4).mp3")
        self.backroundMusic = pygame.mixer.Sound(self.musicFolder + "Backround.mp3")
    def loopBackround(self):
        self.Music.play(self.backroundMusic, 2000000)
    def playShoot(self, n):
        if n == 0:
            self.shoot1.play(self.shootSound)
        if n == 1:
            self.shoot2.play(self.shootSound)