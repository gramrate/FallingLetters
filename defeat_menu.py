import pygame
import time
from colors import WHITE, GRAY, BLACK, RED1
from config import *

class DefeatMenu:
    def __init__(self, app, screen):
        self.app = app
        self.screen = screen

        # Загрузка фона
        self.background_image_day = pygame.image.load("images/backgrounds/main_menu_day.png").convert()
        self.background_image_day = pygame.transform.scale(self.background_image_day, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_image_night = pygame.image.load("images/backgrounds/main_menu_night.png").convert()
        self.background_image_night = pygame.transform.scale(self.background_image_night, (SCREEN_WIDTH, SCREEN_HEIGHT))


        self.font = pygame.font.Font(None, 100)  # Увеличенный шрифт для надписи "DEFEAT"
        self.score_font = pygame.font.Font(None, 50)  # Шрифт для отображения счета

        # Надпись "DEFEAT"
        self.defeat_text_surface = self.font.render("DEFEAT", True, RED1)  # Красный текст
        self.defeat_text_rect = self.defeat_text_surface.get_rect(center=(SCREEN_WIDTH // 2, -self.defeat_text_surface.get_height()))  # Начальная позиция сверху

        # Отображение счета
        self.final_score = self.app.game.score
        self.current_score = 0
        self.update_score_surface()

        # Кнопка "Retry"
        self.retry_button_texture = {
            1: pygame.image.load("images/buttons/retry_button_static.png").convert_alpha(),
            2: pygame.image.load("images/buttons/retry_button_hover.png").convert_alpha()
        }
        self.retry_button_status = 1
        self.retry_button_rect = self.retry_button_texture[self.retry_button_status].get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120))

        # Кнопка "Back"
        self.back_button_texture = {
            1: pygame.image.load("images/buttons/back_button_static.png").convert_alpha(),
            2: pygame.image.load("images/buttons/back_button_hover.png").convert_alpha()
        }
        self.back_button_status = 1
        self.back_button_rect = self.back_button_texture[self.back_button_status].get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 180))


        # Текст для рекорда
        self.record_font = pygame.font.Font(None, 40)
        self.record_text_surface = None
        self.record_text_rect = None

        self.can_check_keys = False
        self.state = "falling"  # Состояние анимации (падение или стояние)
        self.start_time = None  # Время, когда текст остановился
        self.score_increment_time = None  # Время для обновления счета
        self.record_beaten = False  # Флаг для проверки, побит ли рекорд

        # Пример старого рекорда, это должно быть заменено на логику загрузки рекорда из файла или базы данных
        self.highscore = self.app.game_settings.highscore

        self.last_blink_time = time.time()
        self.blink_interval = 0.5  # Интервал моргания в секундах
        self.show_record_text = False
        
        # Сохраняемся
        if self.final_score > self.highscore:
            self.app.game_settings.highscore = self.final_score
        self.app.game_settings.save()
        
    def check_keys(self):
        mouse_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if self.can_check_keys:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.app.is_menu = True
                        self.app.is_game = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_click = True
                else:
                    mouse_click = False
        mouse_pos = pygame.mouse.get_pos()
        self.check_for_clicks(mouse_pos, mouse_click)

    def check_for_clicks(self, mouse_pos, mouse_click):
        # Проверка нажатия кнопок
        if self.retry_button_rect.collidepoint(mouse_pos):
            self.retry_button_status = 2
            if mouse_click:
                self.app.game.reset()
                self.app.is_game = True
                self.app.is_defeat = False
        else:
            self.retry_button_status = 1

        if self.back_button_rect.collidepoint(mouse_pos):
            self.back_button_status = 2
            if mouse_click:
                self.app.is_menu = True
                self.app.is_game = False
        else:
            self.back_button_status = 1

    def update(self):
        current_time = time.time()

        if self.state == "falling":
            self.defeat_text_rect.y += 5  # Скорость падения текста
            if self.defeat_text_rect.y >= SCREEN_HEIGHT // 2 - self.defeat_text_surface.get_height() - 50:  # Останавливаем выше центра
                self.defeat_text_rect.y = SCREEN_HEIGHT // 2 - self.defeat_text_surface.get_height() - 50
                self.state = "waiting_for_score"
                self.start_time = current_time

        elif self.state == "waiting_for_score":
            if current_time - self.start_time >= 1:  # Ждем 1 секунду
                self.state = "counting_score"
                self.current_score = 0  # Сбросить текущий счет до 0
                self.update_score_surface()
                self.score_increment_time = current_time

        elif self.state == "counting_score":
            if self.current_score < self.final_score:
                self.current_score += 1
                self.update_score_surface()
                self.score_increment_time = current_time
            else:
                self.end_counting_score = time.time()
                self.state = "waiting_for_show"

                # Проверяем, побит ли рекорд
                if self.final_score > self.highscore:
                    self.record_beaten = True
                    self.record_text_surface = self.record_font.render("New Record!", True, RED1)
                    self.update_record_surface()

        elif self.state == "waiting_for_show":
            if current_time - self.end_counting_score >= 1:  # Ждем 1 секунду после окончания счета
                self.can_check_keys = True
                self.state = "waiting_for_input"

    def update_score_surface(self):
        self.score_text_surface = self.score_font.render(f"Score: {self.current_score}", True, BLACK)
        self.score_text_rect = self.score_text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

    def update_record_surface(self):
        # Позиционирование рекорда между счетом и кнопками
        record_y = (self.score_text_rect.top + self.defeat_text_rect.bottom) // 2
        self.record_text_rect = self.record_text_surface.get_rect(center=(SCREEN_WIDTH // 2, record_y))

    def draw(self):
        self.screen.blit(self.background_image_day, (0, 0))  # Отображаем фон
        self.screen.blit(self.defeat_text_surface, self.defeat_text_rect)
        self.screen.blit(self.score_text_surface, self.score_text_rect)

        if self.record_beaten:
            current_time = time.time()
            if current_time - self.last_blink_time >= self.blink_interval:
                self.show_record_text = not self.show_record_text
                self.last_blink_time = current_time

            if self.show_record_text:
                self.screen.blit(self.record_text_surface, self.record_text_rect)

        if self.state == "waiting_for_input":
            self.screen.blit(self.retry_button_texture[self.retry_button_status], self.retry_button_rect)
            self.screen.blit(self.back_button_texture[self.back_button_status], self.back_button_rect)