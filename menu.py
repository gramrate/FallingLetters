import pygame
from game import Game
from config import *
from colors import WHITE, BLACK, GRAY


class Menu:
    def __init__(self, app, screen):
        self.app = app
        self.screen = screen

        # Загрузка фона
        self.background_day_image = pygame.image.load("images/backgrounds/main_menu_day.png").convert()
        self.background_day_image = pygame.transform.scale(self.background_day_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_night_image = pygame.image.load("images/backgrounds/main_menu_night.png").convert()
        self.background_night_image = pygame.transform.scale(self.background_night_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Иконка настроек
        self.settings_icon_surface = pygame.Surface((60, 60))
        self.settings_icon_surface.fill(BLACK)
        self.settings_icon_rect = self.settings_icon_surface.get_rect(center=(
            SCREEN_WIDTH - 10 - self.settings_icon_surface.get_width() // 2,
            SCREEN_HEIGHT - 10 - self.settings_icon_surface.get_height() // 2,))

        self.font = pygame.font.Font(None, FONT_SIZE)

        # Основной текст меню
        self.text_mainmenu_surface = self.font.render("Main menu", True, BLACK)
        self.text_mainmenu_rect = self.text_mainmenu_surface.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))

        # кнопка "Play"
        self.play_button_texture = {
            1: pygame.image.load("images/buttons/play_button_static.png").convert_alpha(),
            2: pygame.image.load("images/buttons/play_button_hover.png").convert_alpha()
        }
        self.play_button_status = 1
        self.play_button_rect = self.play_button_texture[self.play_button_status].get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        # Создание кнопки "Difficulty" как Surface
        self.difficulty_button_texture = {
            1: pygame.image.load("images/buttons/difficulty_button_static.png").convert_alpha(),
            2: pygame.image.load("images/buttons/difficulty_button_hover.png").convert_alpha()
        }
        self.difficulty_button_status = 1
        self.difficulty_button_rect = self.difficulty_button_texture[self.difficulty_button_status].get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70))
        
        

        # Создание кнопки "Quit" как Surface
        self.quit_button_texture = {
            1: pygame.image.load("images/buttons/quit_button_static.png").convert_alpha(),
            2: pygame.image.load("images/buttons/quit_button_hover.png").convert_alpha()
        }
        self.quit_button_status = 1
        self.quit_button_rect = self.quit_button_texture[self.quit_button_status].get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 140))

    def check_for_clicks(self, mouse_pos, mouse_click):
        if self.play_button_rect.collidepoint(mouse_pos):
            self.play_button_status = 2
            if mouse_click:
                self.app.game.reset()
                self.app.is_game = True
                self.app.is_menu = False
        else:
            self.play_button_status = 1

        # Проверка нажатия кнопки "Difficulty"
        if self.difficulty_button_rect.collidepoint(mouse_pos):
            self.difficulty_button_status = 2
            if mouse_click:
                self.app.is_difficulty = True
                self.app.is_menu = False

        else:
            self.difficulty_button_status = 1

        # Проверка нажатия кнопки "Quit"
        if self.quit_button_rect.collidepoint(mouse_pos):
            self.quit_button_status = 2
            if mouse_click:
                self.app.running = False
        else:
            self.quit_button_status = 1

        if self.settings_icon_rect.collidepoint(mouse_pos):
            if mouse_click:
                print(f"Icon clicked!")  # Реализуйте здесь вашу логику отклика

    def check_keys(self):
        mouse_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.app.is_game = True
                    self.app.is_menu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = True
            else:
                mouse_click = False
        mouse_pos = pygame.mouse.get_pos()
        self.check_for_clicks(mouse_pos, mouse_click)

    def draw(self):
        self.screen.blit(self.background_day_image, (0, 0))  # Отображаем фон
        self.screen.blit(self.settings_icon_surface, self.settings_icon_rect)

        self.screen.blit(self.text_mainmenu_surface, self.text_mainmenu_rect)

        # Рисуем кнопки используя их поверхности и прямоугольники
        self.screen.blit(self.play_button_texture[self.play_button_status], self.play_button_rect)
        self.screen.blit(self.difficulty_button_texture[self.difficulty_button_status], self.difficulty_button_rect)
        self.screen.blit(self.quit_button_texture[self.quit_button_status], self.quit_button_rect)
