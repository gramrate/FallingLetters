import pygame
import random
import string
from letter import Letter
from config import *
from colors import WHITE, BLACK


class Game:
    def __init__(self):
        self.letters = pygame.sprite.Group()
        self.score = 0
        self.mistakes = 0
        self.spawn_timer = 0
        self.font = pygame.font.Font(None, FONT_SIZE)

    def spawn_letter(self):
        x = random.randint(0, SCREEN_WIDTH - FONT_SIZE)
        y = 0
        char = random.choice(LETTERS)
        new_letter = Letter(x, y, char, FALL_SPEED)
        self.letters.add(new_letter)

    def update(self):
        self.spawn_timer += 1
        if self.spawn_timer >= LETTER_SPAWN_RATE:
            self.spawn_letter()
            self.spawn_timer = 0

        self.letters.update()
    def check_misses(self):
        for letter in self.letters:
            if letter.rect.top > SCREEN_HEIGHT:
                self.mistakes += 1
                letter.kill()

    def check_for_hits(self, key):
        for letter in self.letters:
            if letter.char == key and LINE_START - FONT_SIZE // 2 <= letter.rect.centery <= LINE_END + FONT_SIZE // 2:
                letter.kill()
                self.score += 1
                break
        else:
            self.mistakes += 1

    def draw(self, screen):
        screen.fill(WHITE)
        self.letters.draw(screen)
        pygame.draw.line(screen, BLACK, (0, LINE_START), (SCREEN_WIDTH, LINE_START), 2)
        pygame.draw.line(screen, BLACK, (0, LINE_END), (SCREEN_WIDTH, LINE_END), 2)
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        mistakes = self.font.render(f"Mistakes: {self.mistakes}", True, BLACK)
        screen.blit(mistakes, (10, 10 + FONT_SIZE))
