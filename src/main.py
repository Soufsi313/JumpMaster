from game import Game
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("JumpMaster")
    font = pygame.font.SysFont(None, 60)
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((30, 30, 30))
        title_text = font.render("JumpMaster", True, (255, 255, 255))
        play_text = font.render("Jouer", True, (0, 255, 0))
        quit_text = font.render("Quitter", True, (255, 0, 0))

        screen.blit(title_text, (800//2 - title_text.get_width()//2, 50))
        screen.blit(play_text, (800//2 - play_text.get_width()//2, 150))
        screen.blit(quit_text, (800//2 - quit_text.get_width()//2, 250))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                # Jouer si clique sur "Jouer"
                if 150 <= my <= 150 + play_text.get_height():
                    game = Game()
                    game.run()
                # Quitter si clique sur "Quitter"
                if 250 <= my <= 250 + quit_text.get_height():
                    running = False

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()