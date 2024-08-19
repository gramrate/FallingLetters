import pygame
import random
from letter import Letter
from defeat_menu import DefeatMenu
from difficulty import difficulty_map
from config import *
from colors import WHITE, BLACK


class Game:
    def __init__(self, app, screen):
        self.app = app
        self.screen = screen

        # Загрузка фона
        self.background_image_day = pygame.image.load("images/backgrounds/main_menu_day.png").convert()
        self.background_image_day = pygame.transform.scale(self.background_image_day, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_image_night = pygame.image.load("images/backgrounds/main_menu_night.png").convert()
        self.background_image_night = pygame.transform.scale(self.background_image_night, (SCREEN_WIDTH, SCREEN_HEIGHT))


        difficulty = difficulty_map[self.app.game_settings.difficulty]
        self.LINE_END = LINE_START + difficulty.target_zone
        self.HIT_FACTOR = difficulty.hit_factor
        self.MAX_MISTAKE_SERIES = difficulty.max_mistake_series
        self.spawn_rate = difficulty.spawn_rate
        self.MIN_SPAWN_RATE = difficulty.min_spawn_rate
        self.INCREMENT_SPAWN_RATE = difficulty.increment_spawn_rate
        self.falling_speed = difficulty.falling_speed
        self.MAX_FALLING_SPEED = difficulty.max_falling_speed
        self.INCREMENT_FALLING_SPEED = difficulty.increment_falling_speed


        self.letters = pygame.sprite.Group()
        self.score = 0
        self.mistakes = 0
        self.mistake_series = 0
        self.spawn_timer = self.spawn_rate - 5

        self.font = pygame.font.Font(None, FONT_SIZE)


    def reset(self):
        difficulty = difficulty_map[self.app.game_settings.difficulty]
        self.LINE_END = LINE_START + difficulty.target_zone
        self.HIT_FACTOR = difficulty.hit_factor
        self.MAX_MISTAKE_SERIES = difficulty.max_mistake_series
        self.spawn_rate = difficulty.spawn_rate
        self.MIN_SPAWN_RATE = difficulty.min_spawn_rate
        self.INCREMENT_SPAWN_RATE = difficulty.increment_spawn_rate
        self.falling_speed = difficulty.falling_speed
        self.MAX_FALLING_SPEED = difficulty.max_falling_speed
        self.INCREMENT_FALLING_SPEED = difficulty.increment_falling_speed

        self.letters = pygame.sprite.Group()
        self.score = 0
        self.mistakes = 0
        self.mistake_series = 0
        self.spawn_timer = self.spawn_rate - 5

    def spawn_letter(self):
        x = random.randint(0, SCREEN_WIDTH - FONT_SIZE)
        y = 0
        char = random.choice(LETTERS)
        new_letter = Letter(x, y, char, self.falling_speed)
        self.letters.add(new_letter)

    def check_misses(self):
        for letter in self.letters:
            if letter.rect.top > SCREEN_HEIGHT:
                self.mistakes += 1
                self.mistake_series += 1
                letter.kill()

    def check_for_hits(self, key):
        for letter in self.letters:
            if letter.char == key and LINE_START - FONT_SIZE // 2 <= letter.rect.centery <= self.LINE_END + FONT_SIZE // 2:
                letter.kill()
                self.score += 1 * self.HIT_FACTOR
                self.mistake_series = 0
                break
        else:
            self.mistakes += 1
            self.mistake_series += 1

    def check_lose(self):
        if self.mistake_series >= self.MAX_MISTAKE_SERIES:
            self.app.defeat_menu = DefeatMenu(self.app, self.screen)
            self.app.is_defeat = True
            self.app.is_game = False

    def difficulty_increment(self):
        if self.falling_speed <= self.MAX_FALLING_SPEED:
            self.falling_speed += self.INCREMENT_FALLING_SPEED
        if self.spawn_rate >= self.MIN_SPAWN_RATE:
            self.spawn_rate -= self.INCREMENT_SPAWN_RATE

    def update(self):
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_rate:
            self.spawn_letter()
            self.spawn_timer = 0

        self.letters.update()
        self.difficulty_increment()
        self.check_misses()
        self.check_lose()

    def check_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if event.type == pygame.KEYDOWN:
                self.check_for_hits(event.unicode.upper())

    def draw(self):
        self.screen.blit(self.background_image_day, (0, 0))  # Отображаем фон
        self.letters.draw(self.screen)
        pygame.draw.line(self.screen, BLACK, (0, LINE_START), (SCREEN_WIDTH, LINE_START), 2)
        pygame.draw.line(self.screen, BLACK, (0, self.LINE_END), (SCREEN_WIDTH, self.LINE_END), 2)
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_text, (10, 10))
        mistakes = self.font.render(f"Mistakes: {self.mistakes}", True, BLACK)
        self.screen.blit(mistakes, (10, 10 + FONT_SIZE))