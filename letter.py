from pygame.sprite import Sprite
from config import *
import colors


class Letter(Sprite):
    def __init__(self, x, y, char, speed):
        super().__init__()
        font = pygame.font.Font(None, FONT_SIZE)

        self.image = font.render(char, True, colors.BLACK)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.char = char
        self.speed = speed

    def update(self):
        self.rect.y += self.speed