import pygame
from colors import BLACK
from config import SCREEN_WIDTH, SCREEN_HEIGHT


class MenuIcons:
    def __init__(self, app, screen):
        self.screen = screen

        self.settings_icon_surface = pygame.Surface((60, 60))
        self.settings_icon_surface.fill(BLACK)
        self.settings_icon_rect = self.settings_icon_surface.get_rect(center=(SCREEN_WIDTH - 10 - self.settings_icon_surface.get_width() // 2, SCREEN_HEIGHT - padding - self.settings_icon_surface.get_height() // 2, ))

    def check_for_buttons(self, mouse_pos, mouse_click):
        if self.settings_icon_rect.collidepoint(mouse_pos) and mouse_click:
            print(f"Icon clicked!")  # Реализуйте здесь вашу логику отклика

    def check_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('mousedown')
        mouse_pos = pygame.mouse.get_pos()
        self.check_for_buttons(mouse_pos, True)

    def draw(self):
        self.screen.blit(self.settings_icon_surface, self.settings_icon_rect)
