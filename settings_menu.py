import pygame
from colors import BLACK, GRAY
from config import *

class SettingsMenu:
    def __init__(self, app, screen):
        self.app = app
        self.screen = screen

        # Загрузка фона
        self.background_image_day = pygame.image.load("images/main_menu_day.png").convert()
        self.background_image_day = pygame.transform.scale(self.background_image_day, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_image_night = pygame.image.load("images/main_menu_night.png").convert()
        self.background_image_night = pygame.transform.scale(self.background_image_night, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Иконка настроек
        self.settings_icon_surface = pygame.Surface((60, 60))
        self.settings_icon_surface.fill(BLACK)
        self.settings_icon_rect = self.settings_icon_surface.get_rect(center=(
            SCREEN_WIDTH - 10 - self.settings_icon_surface.get_width() // 2,
            SCREEN_HEIGHT - 10 - self.settings_icon_surface.get_height() // 2,))

        self.font = pygame.font.Font(None, FONT_SIZE)

        # Основной текст меню
        self.text_main_settings_menu_surface = self.font.render("Main menu", True, BLACK)
        self.text_main_settings_menu_rect = self.text_main_settings_menu_surface.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))

    def update(self):
        pass

    def check_for_clicks(self, mouse_pos, mouse_click):
        # Проверка нажатия кнопок сложности
        if self.easy_button_rect.collidepoint(mouse_pos) and mouse_click:
            self.app.game_settings.difficulty = 1

        elif self.medium_button_rect.collidepoint(mouse_pos) and mouse_click:
            self.app.game_settings.difficulty = 2


        elif self.hard_button_rect.collidepoint(mouse_pos) and mouse_click:
            self.app.game_settings.difficulty = 3

        # Проверка нажатия кнопки "Назад"
        elif self.back_button_rect.collidepoint(mouse_pos) and mouse_click:
            self.app.is_menu = True
            self.app.is_difficulty = False

        elif self.settings_icon_rect.collidepoint(mouse_pos) and mouse_click:
            print(f"Icon clicked!")  # Реализуйте здесь вашу логику отклика

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
                self.check_for_clicks(mouse_pos, True)

    def show(self):
        self.screen.blit(self.background_image_day, (0, 0))  # Отображаем фон
        self.screen.blit(self.settings_icon_surface, self.settings_icon_rect)

        self.screen.blit(self.text_main_settings_menu_surface, self.text_main_settings_menu_rect)
