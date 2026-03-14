import pygame
import math

class Rope:

    def __init__(self, player):
        self.player = player
        self.radius = 120
        self.angle = 0
        self.speed = 0.08

    def update(self):
        self.angle += self.speed

    def draw(self, screen):
        rope_x = self.player.x + self.player.width//2 + math.cos(self.angle) * self.radius
        rope_y = self.player.y - self.player.height//2 + math.sin(self.angle) * self.radius
        pygame.draw.line(screen, (200, 200, 255),
                         (self.player.x + self.player.width//2, self.player.y - self.player.height//2),
                         (rope_x, rope_y), 6)