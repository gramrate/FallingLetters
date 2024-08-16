import pygame
from game import Game
from menu import Menu
from difficulty import Difficulty



class App:
    def __init__(self, screen_width, screen_height, caption, FPS):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()

        self.game = Game(self, self.screen)
        self.menu = Menu(self, self.screen)
        self.difficulty = Difficulty(self, self.screen)

        self.running = True
        self.is_menu = True
        self.is_difficulty = False
        self.is_settings = False
        self.is_game = False

        self.FPS = FPS


    def run(self):
        while self.running:
            if self.is_game:
                self.game.check_keys()
                self.game.update()
                self.game.draw()
            elif self.is_menu:
                self.menu.check_keys()
                self.menu.draw()
            elif self.is_difficulty:
                self.difficulty.check_keys()
                self.difficulty.draw()

            pygame.display.flip()
            self.clock.tick(self.FPS)

        pygame.quit()
