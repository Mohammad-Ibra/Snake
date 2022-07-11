import pygame

class Cube:

    rows = 20
    _width = 500

    def __init__(self, pos=(), color = (255,0,0), speed=(1,0)) -> None:
        self.pos = pos
        self.next = None
        self.color = color
        self.speed = speed

    def draw(self, surface) -> None:

        dis = self._width // self.rows
        
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1,dis-1,dis-1))

    def move(self, speed) -> None:
        self.speed = speed
        self.pos = (self.pos[0] + self.speed[0], self.pos[1] + self.speed[1])

    
