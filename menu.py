import pygame
from game import Game
from config import *
from colors import WHITE, BLACK, GRAY

class Menu:
    def __init__(self, app, screen):
        self.app = app
        self.screen = screen


        self.font = pygame.font.Font(None, FONT_SIZE)

        # Основной текст меню
        self.text_mainmenu_surface = self.font.render("Main menu", True, BLACK)
        self.text_mainmenu_rect = self.text_mainmenu_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))

        # Размер и позиция кнопки "Play Button"
        self.play_button_surface = pygame.Surface((180, 50))
        self.play_button_surface.fill(GRAY)
        self.play_button_rect = self.play_button_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        # Создание кнопки "Play Button" как Surface
        self.button_font = pygame.font.Font(None, 36)
        self.play_button_text_surface = self.button_font.render("Play", True, BLACK)
        self.play_button_text_rect = self.play_button_text_surface.get_rect(center=self.play_button_rect.center)

        # Создание кнопки "Difficulty" как Surface
        self.difficulty_button_surface = pygame.Surface((180, 50))
        self.difficulty_button_surface.fill(GRAY)
        self.difficulty_button_rect = self.difficulty_button_surface.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70))
        self.difficulty_button_text_surface = self.button_font.render("Difficulty", True, BLACK)
        self.difficulty_button_text_rect = self.difficulty_button_text_surface.get_rect(center=self.difficulty_button_rect.center)

        # Создание кнопки "Quit" как Surface
        self.quit_button_surface = pygame.Surface((180, 50))
        self.quit_button_surface.fill(GRAY)
        self.quit_button_rect = self.quit_button_surface.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 140))
        self.quit_button_text_surface = self.button_font.render("Quit", True, BLACK)
        self.quit_button_text_rect = self.quit_button_text_surface.get_rect(center=self.quit_button_rect.center)

    def check_for_buttons(self, mouse_pos, mouse_click):
        # Проверка нажатия кнопки "Play Button"
        if self.play_button_rect.collidepoint(mouse_pos) and mouse_click:
            print('Start game')
            self.app.game = Game(self.app, self.screen)
            self.app.is_game = True
            self.app.is_menu = False

        # Проверка нажатия кнопки "Difficulty"
        if self.difficulty_button_rect.collidepoint(mouse_pos) and mouse_click:
            print('Open difficulty settings')
            self.app.is_difficulty = True
            self.app.is_menu = False

        # Проверка нажатия кнопки "Quit"
        if self.quit_button_rect.collidepoint(mouse_pos) and mouse_click:
            print('Quit game')
            self.app.running = False

    def check_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.app.is_game = True
                    self.app.is_menu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_for_buttons(mouse_pos, True)

    def draw(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.text_mainmenu_surface, self.text_mainmenu_rect)

        # Рисуем кнопки используя их поверхности и прямоугольники
        self.screen.blit(self.play_button_surface, self.play_button_rect)
        self.screen.blit(self.play_button_text_surface, self.play_button_text_rect)
        self.screen.blit(self.difficulty_button_surface, self.difficulty_button_rect)
        self.screen.blit(self.difficulty_button_text_surface, self.difficulty_button_text_rect)
        self.screen.blit(self.quit_button_surface, self.quit_button_rect)
        self.screen.blit(self.quit_button_text_surface, self.quit_button_text_rect)