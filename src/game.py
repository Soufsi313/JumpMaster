import pygame
from player import Player


class Game:

    def __init__(self):
        # Initialisation de Pygame
        pygame.init()

        # Dimensions de la fenêtre
        self.width = 800
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("JumpMaster")

        # Horloge pour FPS
        self.clock = pygame.time.Clock()
        self.running = True

        # Création du joueur
        self.player = Player(200, 300)

    def run(self):
        while self.running:

            # --- Gestion des événements ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                # Gestion du saut
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()

            # --- Mise à jour du jeu ---
            self.player.update()

            # --- Dessin ---
            self.screen.fill((30, 30, 30))  # Fond noir
            self.player.draw(self.screen)

            # Actualiser l'écran
            pygame.display.flip()
            self.clock.tick(60)  # Limiter à 60 FPS

        # Quitter Pygame proprement
        pygame.quit()