import pygame
from player import Player
from rope import Rope
from score_manager import ScoreManager
import os

class Game:

    def __init__(self, width=800, height=400):
        pygame.init()
        pygame.mixer.init()  # Initialiser le son

        # Fenêtre responsive
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption("JumpMaster")

        self.clock = pygame.time.Clock()
        self.running = True

        # Joueur
        self.player = Player(self.width * 0.25, self.height * 0.75)

        # Corde
        self.rope = Rope(self.player)

        # Score et erreurs
        self.score = 0
        self.misses = 0
        self.font = pygame.font.SysFont(None, 40)

        # Gestion des scores
        self.score_manager = ScoreManager()

        # Sons
        self.sound_fail = pygame.mixer.Sound(os.path.join("assets", "sounds", "fail.wav"))

    def run(self):
        while self.running:

            # --- Gestion des événements ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()
                if event.type == pygame.VIDEORESIZE:
                    self.width, self.height = event.size
                    self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

            # --- Mise à jour ---
            self.player.update()
            self.rope.update()

            # Collision simple : corde sous le joueur
            rope_bottom_y = self.player.y - self.player.height//2 + self.rope.radius * pygame.math.sin(self.rope.angle)
            if rope_bottom_y > self.player.y and not self.player.on_ground:
                self.misses += 1
                self.player.y = self.height * 0.75
                self.player.vel_y = 0
                self.player.on_ground = True
                self.sound_fail.play()

            # Score et difficulté progressive
            if self.player.on_ground:
                self.score += 1
                if self.score % 10 == 0:
                    self.rope.speed += 0.01

            # --- Dessin ---
            self.screen.fill((30, 30, 30))

            # Joueur
            self.player.draw(self.screen)

            # Corde animée
            rope_x = self.player.x + self.rope.radius * pygame.math.cos(self.rope.angle)
            rope_y = self.player.y - self.player.height//2 + self.rope.radius * pygame.math.sin(self.rope.angle)
            pygame.draw.line(self.screen, (200, 200, 255),
                             (self.player.x + self.player.width//2, self.player.y - self.player.height//2),
                             (rope_x, rope_y), 6)

            # Affichage score et erreurs
            score_text = self.font.render(f"Score : {self.score}", True, (255, 255, 255))
            miss_text = self.font.render(f"Erreurs : {self.misses}/3", True, (255, 100, 100))
            high_score_text = self.font.render(f"Meilleur score : {self.score_manager.get_high_score()}", True, (255, 255, 0))
            self.screen.blit(score_text, (20, 20))
            self.screen.blit(miss_text, (20, 60))
            self.screen.blit(high_score_text, (20, 100))

            # Game Over
            if self.misses >= 3:
                self.score_manager.save_score(self.score)
                game_over = self.font.render("GAME OVER", True, (255, 0, 0))
                self.screen.blit(game_over, (self.width//2 - 100, self.height//2))
                pygame.display.flip()
                pygame.time.wait(3000)
                self.running = False

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()