import JH, pygame


class Map:
    def __init__(self, scale):
        
        wallSize = [25, 5]
        wall_NS = pygame.Surface((wallSize[1], wallSize[0]))
        wall_NS.fill((0, 0, 0))


        wall_WE = pygame.Surface(wallSize)
        wall_WE.fill((0, 0, 0))

        

        wall_NS_WE = pygame.Surface((wallSize[0], wallSize[0])).convert_alpha()
        wall_NS_WE.fill((0, 0, 0, 0))
        wall_NS_WE.blit(wall_WE, (0, 0))
        wall_NS_WE.blit(wall_NS, (0, 0))

        wall_Small = pygame.Surface((wallSize[1], wallSize[1])).convert_alpha()
        wall_Small.fill((0, 0, 0))
        self.wallsSurfs = {"wall_WE": wall_WE,
                           "wall_NS": wall_NS,
                           "wall_NS-WE": wall_NS_WE,
                           "wall_Small" : wall_Small
                               }
        self.scale = scale
        self.folder = "data/json/map.json"
        self.Json = JH.JsonReader(self.folder)
        self.mapName = "Map 1"
        self.map = self.Json[self.mapName] 
        self.LoadedMap = None
    def loadMap(self, name="Map 1"):
        self.mapName = name
        self.map = self.Json[self.mapName] 
        chunkSize = 25
        self.LoadedMap: pygame.Surface = pygame.Surface((len(self.map)*chunkSize*self.scale, len(self.map[0])*chunkSize*self.scale)).convert_alpha()
        self.LoadedMap.fill((0, 0, 0, 0))
        Yint = 0
        for y in self.map:
            Xint = 0
            for x in y:
                if x == 0:
                    Xint+=1
                    continue
                if x == 1:
                    self.LoadedMap.blit(self.wallsSurfs["wall_NS"], (Xint*chunkSize*self.scale, Yint*chunkSize*self.scale))
                if x == 2:
                    self.LoadedMap.blit(self.wallsSurfs["wall_WE"], (Xint*chunkSize*self.scale, Yint*chunkSize*self.scale))
                if x == 3:
                    self.LoadedMap.blit(self.wallsSurfs["wall_NS-WE"], (Xint*chunkSize*self.scale, Yint*chunkSize*self.scale))
                if x == 4:
                    self.LoadedMap.blit(self.wallsSurfs["wall_Small"], (Xint*chunkSize*self.scale, Yint*chunkSize*self.scale))
                Xint += 1
            Yint += 1
        return self.LoadedMap
    def draw(self, screen:pygame.Surface):
        if self.LoadedMap == None:
            print("No map Loaded")
            return 1
        screen.blit(self.LoadedMap, (0, 0))