import pygame
import math


class Rope:

    def __init__(self, player):
        self.player = player  # Référence au joueur

        self.radius = 120       # Rayon de rotation de la corde
        self.angle = 0          # Angle initial
        self.speed = 0.08       # Vitesse de rotation de la corde

    def update(self):
        # Faire tourner la corde
        self.angle += self.speed

    def draw(self, screen):
        # Calcul de la position de la corde
        rope_x = self.player.x + math.cos(self.angle) * self.radius
        rope_y = self.player.y + math.sin(self.angle) * self.radius

        # Dessiner la corde
        pygame.draw.line(screen, (200, 200, 200),
                         (self.player.x + self.player.width // 2, self.player.y - self.player.height // 2),
                         (rope_x, rope_y), 5)