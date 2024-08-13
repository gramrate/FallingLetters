import pygame
from game import Game
from menu import Menu


class App:
    def __init__(self, screen_width, screen_height, caption, FPS):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()

        self.game = Game()

        self.menu = Menu()

        self.FPS = FPS

        self.running = True
        self.is_menu = True
        self.is_settings = False
        self.is_game = False

    def run(self):
        while self.running:
            if self.is_game:
                self.game.check_keys(self)
                self.game.update()
                self.game.draw(self.screen)
            elif self.is_menu:
                self.menu.check_keys(self)
                self.menu.draw(self.screen)


            pygame.display.flip()
            self.clock.tick(self.FPS)

        pygame.quit()
