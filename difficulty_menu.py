import pygame

from config import *
from colors import WHITE, BLACK, GRAY


class DifficultyMenu:
    def __init__(self, app, screen):
        self.app = app
        self.screen = screen

        self.font = pygame.font.Font(None, FONT_SIZE)
        self.button_font = pygame.font.Font(None, 36)

        # Основной текст меню
        self.text_maindifficulty_surface = self.font.render("Difficulty Settings", True, BLACK)
        self.text_maindifficulty_rect = self.text_maindifficulty_surface.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 170))

        # Размер и позиция кнопки "Easy"
        self.easy_button_surface = pygame.Surface((180, 50))
        self.easy_button_surface.fill(GRAY)
        self.easy_button_rect = self.easy_button_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        self.easy_button_text_surface = self.button_font.render("Easy", True, BLACK)
        self.easy_button_text_rect = self.easy_button_text_surface.get_rect(center=self.easy_button_rect.center)

        # Размер и позиция кнопки "Medium"
        self.medium_button_surface = pygame.Surface((180, 50))
        self.medium_button_surface.fill(GRAY)
        self.medium_button_rect = self.medium_button_surface.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
        self.medium_button_text_surface = self.button_font.render("Medium", True, BLACK)
        self.medium_button_text_rect = self.medium_button_text_surface.get_rect(center=self.medium_button_rect.center)

        # Размер и позиция кнопки "Hard"
        self.hard_button_surface = pygame.Surface((180, 50))
        self.hard_button_surface.fill(GRAY)
        self.hard_button_rect = self.hard_button_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))
        self.hard_button_text_surface = self.button_font.render("Hard", True, BLACK)
        self.hard_button_text_rect = self.hard_button_text_surface.get_rect(center=self.hard_button_rect.center)

        # Создание кнопки "Назад" как Surface
        self.back_button_surface = pygame.Surface((180, 50))
        self.back_button_surface.fill(GRAY)
        self.back_button_rect = self.back_button_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        self.back_button_text_surface = self.button_font.render("Back", True, BLACK)
        self.back_button_text_rect = self.back_button_text_surface.get_rect(center=self.back_button_rect.center)

    def check_for_buttons(self, mouse_pos, mouse_click):
        # Проверка нажатия кнопок сложности
        if self.easy_button_rect.collidepoint(mouse_pos) and mouse_click:
            print('Easy difficulty selected')
            self.app.game_settings.difficulty = 1

        if self.medium_button_rect.collidepoint(mouse_pos) and mouse_click:
            print('Medium difficulty selected')
            self.app.game_settings.difficulty = 2


        if self.hard_button_rect.collidepoint(mouse_pos) and mouse_click:
            print('Hard difficulty selected')
            self.app.game_settings.difficulty = 3

        # Проверка нажатия кнопки "Назад"
        if self.back_button_rect.collidepoint(mouse_pos) and mouse_click:
            print('Back to menu')
            self.app.is_menu = True
            self.app.is_difficulty = False

    def check_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.app.is_menu = True
                    self.app.is_difficulty_settings = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_for_buttons(mouse_pos, True)


    def draw(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.text_maindifficulty_surface, self.text_maindifficulty_rect)

        # Рисуем кнопки используя их поверхности и прямоугольники
        self.screen.blit(self.easy_button_surface, self.easy_button_rect)
        self.screen.blit(self.easy_button_text_surface, self.easy_button_text_rect)
        self.screen.blit(self.medium_button_surface, self.medium_button_rect)
        self.screen.blit(self.medium_button_text_surface, self.medium_button_text_rect)
        self.screen.blit(self.hard_button_surface, self.hard_button_rect)
        self.screen.blit(self.hard_button_text_surface, self.hard_button_text_rect)
        self.screen.blit(self.back_button_surface, self.back_button_rect)
        self.screen.blit(self.back_button_text_surface, self.back_button_text_rect)
