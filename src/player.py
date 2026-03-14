import pygame


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.width = 40
        self.height = 60

        self.vel_y = 0
        self.gravity = 0.8
        self.jump_power = -15

        self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

    def update(self):

        self.vel_y += self.gravity
        self.y += self.vel_y

        if self.y >= 300:
            self.y = 300
            self.vel_y = 0
            self.on_ground = True

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            (0, 200, 0),
            (self.x, self.y - self.height, self.width, self.height)
        )