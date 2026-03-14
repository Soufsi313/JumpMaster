import pygame
from player import Player
from rope import Rope


class Game:

    def __init__(self):
        pygame.init()

        # Dimensions de la fenêtre
        self.width = 800
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("JumpMaster")

        self.clock = pygame.time.Clock()
        self.running = True

        # Joueur
        self.player = Player(200, 300)

        # Corde
        self.rope = Rope(self.player)

    def run(self):
        while self.running:

            # --- Gestion des événements ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()

            # --- Mise à jour ---
            self.player.update()
            self.rope.update()

            # --- Dessin ---
            self.screen.fill((30, 30, 30))  # Fond noir
            self.player.draw(self.screen)
            self.rope.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()