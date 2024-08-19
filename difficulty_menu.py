import pygame

from config import *
from colors import WHITE, BLACK, GRAY


class DifficultyMenu:
    def __init__(self, app, screen):
        self.app = app
        self.screen = screen

        # Загрузка фона
        self.background_image_day = pygame.image.load("images/backgrounds/main_menu_day.png").convert()
        self.background_day_image = pygame.transform.scale(self.background_image_day, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_night_image = pygame.image.load("images/backgrounds/main_menu_night.png").convert()
        self.background_night_image = pygame.transform.scale(self.background_night_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Иконка настроек
        self.settings_icon_surface = pygame.Surface((60, 60))
        self.settings_icon_surface.fill(BLACK)
        self.settings_icon_rect = self.settings_icon_surface.get_rect(center=(
            SCREEN_WIDTH - 10 - self.settings_icon_surface.get_width() // 2,
            SCREEN_HEIGHT - 10 - self.settings_icon_surface.get_height() // 2,))

        self.font = pygame.font.Font(None, FONT_SIZE)
        self.button_font = pygame.font.Font(None, 36)

        # Основной текст меню
        self.text_maindifficulty_surface = self.font.render("Difficulty Settings", True, BLACK)
        self.text_maindifficulty_rect = self.text_maindifficulty_surface.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 170))

        # Размер и позиция кнопки "Easy"
        self.easy_button_texture = {
            1: pygame.image.load("images/buttons/easy_button_static.png").convert_alpha(),
            2: pygame.image.load("images/buttons/easy_button_hover.png").convert_alpha()
        }
        self.easy_button_status = 1
        self.easy_button_rect = self.easy_button_texture[self.easy_button_status].get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))

        # Размер и позиция кнопки "Medium"
        self.medium_button_texture = {
            1: pygame.image.load("images/buttons/medium_button_static.png").convert_alpha(),
            2: pygame.image.load("images/buttons/medium_button_hover.png").convert_alpha()
        }
        self.medium_button_status = 1
        self.medium_button_rect = self.medium_button_texture[self.medium_button_status].get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))

        # Размер и позиция кнопки "Hard"
        self.hard_button_texture = {
            1: pygame.image.load("images/buttons/hard_button_static.png").convert_alpha(),
            2: pygame.image.load("images/buttons/hard_button_hover.png").convert_alpha()
        }
        self.hard_button_status = 1
        self.hard_button_rect = self.hard_button_texture[self.hard_button_status].get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))
        
        # Создание кнопки "Назад" как Surface
        self.back_button_texture = {
            1: pygame.image.load("images/buttons/back_button_static.png").convert_alpha(),
            2: pygame.image.load("images/buttons/back_button_hover.png").convert_alpha()
        }
        self.back_button_status = 1
        self.back_button_rect = self.back_button_texture[self.back_button_status].get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))


    def check_for_clicks(self, mouse_pos, mouse_click):
        # Проверка нажатия кнопок сложности
        if self.easy_button_rect.collidepoint(mouse_pos):
            self.easy_button_status = 2
            if mouse_click:
                self.app.game_settings.difficulty = 1
        else:
            self.easy_button_status = 1

        if self.medium_button_rect.collidepoint(mouse_pos):
            self.medium_button_status = 2
            if mouse_click:
                self.app.game_settings.difficulty = 2
        else:
            self.medium_button_status = 1

        if self.hard_button_rect.collidepoint(mouse_pos):
            self.hard_button_status = 2
            if mouse_click:
                self.app.game_settings.difficulty = 3
        else:
            self.hard_button_status = 1

        if self.back_button_rect.collidepoint(mouse_pos):
            self.back_button_status = 2
            if mouse_click:
                self.app.is_menu = True
                self.app.is_difficulty = False
        else:
            self.back_button_status = 1

        if self.settings_icon_rect.collidepoint(mouse_pos):
            if mouse_click:
                print(f"Icon clicked!")  # Реализуйте здесь вашу логику отклика

    def check_keys(self):
        mouse_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.app.is_menu = True
                    self.app.is_difficulty_settings = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = True
            else:
                mouse_click = False
        mouse_pos = pygame.mouse.get_pos()
        self.check_for_clicks(mouse_pos, mouse_click)


    def draw(self):
        self.screen.blit(self.background_image_day, (0, 0))  # Отображаем фон
        self.screen.blit(self.settings_icon_surface, self.settings_icon_rect)
        self.screen.blit(self.text_maindifficulty_surface, self.text_maindifficulty_rect)

        # Рисуем кнопки используя их поверхности и прямоугольники
        self.screen.blit(self.easy_button_texture[self.easy_button_status], self.easy_button_rect)
        self.screen.blit(self.medium_button_texture[self.medium_button_status], self.medium_button_rect)
        self.screen.blit(self.hard_button_texture[self.hard_button_status], self.hard_button_rect)
        self.screen.blit(self.back_button_texture[self.back_button_status], self.back_button_rect)