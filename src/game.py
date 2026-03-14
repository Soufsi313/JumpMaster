import pygame


class Game:

    def __init__(self):
        pygame.init()

        self.width = 800
        self.height = 400

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("JumpMaster")

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((30, 30, 30))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()