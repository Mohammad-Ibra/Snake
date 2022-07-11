from tkinter import LEFT
from cube import Cube
import pygame

class Snake:
    def __init__(self, head: Cube) -> None:
        self.head = head
        self.dirx = 0
        self.diry = 1
        self.moves = {}
        
    
    def __iter__(self) -> Cube:
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def _add_cube(self, pos) -> None:
        cube = Cube(pos)
        for current_cube in self:
            pass
        current_cube.next = cube

    def tail(self) -> Cube:
        for node in self:
            if node.next == None:
                return node

    def eat(self) -> None:
        tail = self.tail()
        dx, dy = tail.speed[0], tail.speed[1]

        if dx == 1 and dy == 0:
            self._add_cube(((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self._add_cube(((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self._add_cube(((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self._add_cube(((tail.pos[0],tail.pos[1]+1)))

        for node in self:
            if node.next == None:
                node.speed = (dx, dy)

    def move(self) -> None:
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_LEFT]:
                self.dirx = -1
                self.diry = 0
                self.moves[self.head.pos[:]] = [self.dirx, self.diry]
            if keys[pygame.K_RIGHT]:
                self.dirx = 1
                self.diry = 0
                self.moves[self.head.pos[:]] = [self.dirx, self.diry]
            if keys[pygame.K_UP]:
                self.dirx = 0
                self.diry = -1
                self.moves[self.head.pos[:]] = [self.dirx, self.diry]
            if keys[pygame.K_DOWN]:
                self.dirx = 0
                self.diry = 1
                self.moves[self.head.pos[:]] = [self.dirx, self.diry]
        
        for c in self:
            p = c.pos[:]
            if p in self.moves:
                turn = self.moves[p]
                c.move((turn[0],turn[1]))
                if c.next == None:
                    self.moves.pop(p)
            else:
                if c.speed[0] == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.speed[0] == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.speed[1] == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.speed[1] == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move((c.speed[0],c.speed[1]))

    def draw(self, surface) -> None:
        for cube in self:
            cube.draw(surface)

    def reset(self,pos):
        self.head = Cube(pos)
        self.moves = {}
        self.dirx = 0
        self.diry = 1
        self.body = []


    