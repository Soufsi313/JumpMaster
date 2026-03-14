import pygame
from player import Player
from rope import Rope

class Game:

    def __init__(self, width=800, height=400):
        pygame.init()

        # Dimensions adaptables
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption("JumpMaster")

        self.clock = pygame.time.Clock()
        self.running = True

        # Joueur positionné proportionnellement
        self.player = Player(self.width * 0.25, self.height * 0.75)

        # Corde
        self.rope = Rope(self.player)

        # Score et erreurs
        self.score = 0
        self.misses = 0
        self.font = pygame.font.SysFont(None, 40)

    def run(self):
        while self.running:

            # --- Gestion des événements ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()
                # Gérer redimensionnement
                if event.type == pygame.VIDEORESIZE:
                    self.width, self.height = event.size
                    self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

            # --- Mise à jour ---
            self.player.update()
            self.rope.update()

            # Collision simple : corde passe sous le joueur
            rope_bottom_y = self.player.y - self.player.height//2 + self.rope.radius * pygame.math.sin(self.rope.angle)
            if rope_bottom_y > self.player.y and not self.player.on_ground:
                self.misses += 1
                self.player.y = self.height * 0.75
                self.player.vel_y = 0
                self.player.on_ground = True

            # Augmenter score quand le joueur saute correctement
            if self.player.on_ground:
                self.score += 1
                # Augmentation difficulté : vitesse corde
                if self.score % 10 == 0:
                    self.rope.speed += 0.01

            # --- Dessin ---
            self.screen.fill((30, 30, 30))
            self.player.draw(self.screen)
            self.rope.draw(self.screen)

            # Afficher score et erreurs
            score_text = self.font.render(f"Score : {self.score}", True, (255, 255, 255))
            miss_text = self.font.render(f"Erreurs : {self.misses}/3", True, (255, 100, 100))
            self.screen.blit(score_text, (20, 20))
            self.screen.blit(miss_text, (20, 60))

            # Game Over
            if self.misses >= 3:
                game_over = self.font.render("GAME OVER", True, (255, 0, 0))
                self.screen.blit(game_over, (self.width//2 - 100, self.height//2))
                pygame.display.flip()
                pygame.time.wait(3000)
                self.running = False

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()