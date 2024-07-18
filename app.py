import pygame
from game import Game


class App:
    def __init__(self, screen_width, screen_height, caption, FPS):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.game = Game()
        self.FPS = FPS
        self.running = True

    def run(self):
        while self.running:
            self.game.check_misses()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.game.check_for_hits(event.unicode.upper())

            self.game.update()
            self.game.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.FPS)

        pygame.quit()
