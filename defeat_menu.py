import pygame
import time
from colors import WHITE, GRAY, BLACK, RED1
from config import *

class DefeatMenu:
    def __init__(self, app, screen):
        self.app = app
        self.screen = screen

        self.font = pygame.font.Font(None, 100)  # Увеличенный шрифт для надписи "DEFEAT"
        self.score_font = pygame.font.Font(None, 50)  # Шрифт для отображения счета
        self.button_font = pygame.font.Font(None, 36)  # Шрифт для кнопок

        # Загрузка фона
        self.background_image = pygame.image.load("images/main_menu.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Надпись "DEFEAT"
        self.defeat_text_surface = self.font.render("DEFEAT", True, RED1)  # Красный текст
        self.defeat_text_rect = self.defeat_text_surface.get_rect(center=(SCREEN_WIDTH // 2, -self.defeat_text_surface.get_height()))  # Начальная позиция сверху

        # Отображение счета
        self.final_score = self.app.game.score
        self.current_score = 0
        self.update_score_surface()

        # Кнопка "Retry"
        self.retry_button_surface = pygame.Surface((180, 50))
        self.retry_button_surface.fill(GRAY)  # Серый фон для кнопки
        self.retry_button_rect = self.retry_button_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120))  # Позиция кнопки "Retry"

        # Текст на кнопке "Retry"
        self.retry_button_text_surface = self.button_font.render("Retry", True, BLACK)
        self.retry_button_text_rect = self.retry_button_text_surface.get_rect(center=self.retry_button_rect.center)

        # Кнопка "Back"
        self.back_button_surface = pygame.Surface((180, 50))
        self.back_button_surface.fill(GRAY)  # Серый фон для кнопки
        self.back_button_rect = self.back_button_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 180))  # Позиция кнопки

        # Текст на кнопке "Back"
        self.back_button_text_surface = self.button_font.render("Back", True, BLACK)
        self.back_button_text_rect = self.back_button_text_surface.get_rect(center=self.back_button_rect.center)

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
        self.old_record = -2  # Замените это значение на ваш реальный рекорд

        self.last_blink_time = time.time()
        self.blink_interval = 0.5  # Интервал моргания в секундах
        self.show_record_text = False

    def check_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if self.can_check_keys:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.app.is_menu = True
                        self.app.is_game = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.check_for_buttons(mouse_pos, True)

    def check_for_buttons(self, mouse_pos, mouse_click):
        # Проверка нажатия кнопок
        if self.retry_button_rect.collidepoint(mouse_pos) and mouse_click:
            self.app.game.reset()
            self.app.is_game = True
            self.app.is_defeat = False
        elif self.back_button_rect.collidepoint(mouse_pos) and mouse_click:
            print('Back to menu')
            self.app.is_menu = True
            self.app.is_game = False

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
                if self.final_score > self.old_record:
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
        self.screen.blit(self.background_image, (0, 0))  # Отображаем фон
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
            self.screen.blit(self.retry_button_surface, self.retry_button_rect)
            self.screen.blit(self.retry_button_text_surface, self.retry_button_text_rect)
            self.screen.blit(self.back_button_surface, self.back_button_rect)
            self.screen.blit(self.back_button_text_surface, self.back_button_text_rect)
