from config import *


class Easy:
    falling_speed = 2
    spawn_rate = FPS
    hit_factor = 1
    target_zone = 100


class Medium:
    falling_speed = 4
    spawn_rate = FPS // 1.5
    hit_factor = 2
    target_zone = 75


class Hard:
    falling_speed = 5
    spawn_rate = FPS // 3
    hit_factor = 3
    target_zone = 50


# soon
class Nightmare:
    falling_speed = 7
    spawn_rate = FPS // 6
    hit_factor = 5
    target_zone = 25


difficulty_map = {
    1: Easy,
    2: Medium,
    3: Hard,
    4: Nightmare
}
