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
        self.button_font = pygame.font.Font(None, 36)  # Шрифт для кнопки "Back"

        # Надпись "DEFEAT"
        self.defeat_text_surface = self.font.render("DEFEAT", True, RED1)  # Красный текст
        self.defeat_text_rect = self.defeat_text_surface.get_rect(center=(SCREEN_WIDTH // 2, -self.defeat_text_surface.get_height()))  # Начальная позиция сверху

        # Отображение счета
        self.final_score = self.app.game.score
        self.current_score = 0
        self.score_text_surface = self.score_font.render(f"Score: {self.current_score}", True, BLACK)  # Черный текст для счета
        self.score_text_rect = self.score_text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))  # Позиция счета

        # Кнопка "Back"
        self.back_button_surface = pygame.Surface((180, 50))
        self.back_button_surface.fill(GRAY)  # Серый фон для кнопки
        self.back_button_rect = self.back_button_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120))  # Позиция кнопки

        # Текст на кнопке "Back"
        self.back_button_text_surface = self.button_font.render("Back", True, BLACK)
        self.back_button_text_rect = self.back_button_text_surface.get_rect(center=self.back_button_rect.center)

        # Загрузка фона
        self.background_image = pygame.image.load("images/main_menu.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.can_check_keys = False

        self.state = "falling"  # Состояние анимации (падение или стояние)
        self.start_time = None  # Время, когда текст остановился
        self.score_increment_time = None  # Время для обновления счета

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
        # Проверка нажатия кнопки "Back"
        if self.back_button_rect.collidepoint(mouse_pos) and mouse_click:
            print('Back to menu')
            self.app.is_menu = True
            self.app.is_game = False

    def update(self):
        current_time = time.time()

        if self.state == "falling":
            self.defeat_text_rect.y += 5  # Скорость падения текста
            if self.defeat_text_rect.y >= SCREEN_HEIGHT // 2 - self.defeat_text_rect.height // 2:
                self.defeat_text_rect.y = SCREEN_HEIGHT // 2 - self.defeat_text_rect.height // 2
                self.state = "waiting_for_score"
                self.start_time = current_time

        elif self.state == "waiting_for_score":
            if current_time - self.start_time >= 1:  # Ждем 1 секунду
                self.state = "counting_score"
                self.current_score = 0  # Сбросить текущий счет до 0
                self.update_score_surface()

        elif self.state == "counting_score":
            if self.current_score < self.final_score:
                self.current_score += 1
                self.update_score_surface()
                self.score_increment_time = current_time
            else:
                self.end_counting_score = time.time()
                self.state = "waiting_for_show"

        elif self.state == "waiting_for_show":
            if current_time - self.end_counting_score >= 1:  # Ждем 1 секунду после окончания счета
                self.can_check_keys = True
                self.state = "waiting_for_input"

    def update_score_surface(self):
        self.score_text_surface = self.score_font.render(f"Score: {self.current_score}", True, BLACK)
        self.score_text_rect = self.score_text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))  # Отображаем фон
        self.screen.blit(self.defeat_text_surface, self.defeat_text_rect)

        if self.state in ("counting_score", "waiting_for_show", "waiting_for_input"):
            self.screen.blit(self.defeat_text_surface, self.defeat_text_rect)
            self.screen.blit(self.score_text_surface, self.score_text_rect)

        if self.state == "waiting_for_input":
            self.screen.blit(self.back_button_surface, self.back_button_rect)
            self.screen.blit(self.back_button_text_surface, self.back_button_text_rect)
