import pygame
import os

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

        # Charger les sprites
        self.sprites = []
        self.load_sprites()
        self.frame = 0
        self.animation_speed = 0.2

    def load_sprites(self):
        path = os.path.join("assets", "images")
        for i in range(1, 5):  # 4 frames d'exemple
            img = pygame.image.load(os.path.join(path, f"player_{i}.png")).convert_alpha()
            self.sprites.append(pygame.transform.scale(img, (self.width, self.height)))

    def jump(self):
        if self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False
            # Jouer le son
            pygame.mixer.Sound(os.path.join("assets", "sounds", "jump.wav")).play()

    def update(self):
        self.vel_y += self.gravity
        self.y += self.vel_y

        if self.y >= 0.75 * pygame.display.get_surface().get_height():
            self.y = 0.75 * pygame.display.get_surface().get_height()
            self.vel_y = 0
            self.on_ground = True

        # Animation simple
        self.frame += self.animation_speed
        if self.frame >= len(self.sprites):
            self.frame = 0

    def draw(self, screen):
        screen.blit(self.sprites[int(self.frame)], (self.x, self.y - self.height))