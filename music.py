import pygame, math

class music:
    def __init__(self) -> None:
        self.Music = pygame.mixer.Channel(0)
        self.soundEffect = pygame.mixer.Channel(1)
        self.musicFolder = "data/Music/"
        self.backroundMusic = pygame.mixer.Sound(self.musicFolder + "Backround.mp3")
    def loopBackround(self):
        self.Music.play(self.backroundMusic, 2000000)
