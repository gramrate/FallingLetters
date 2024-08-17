from config import *

class Easy:
    falling_speed = 2
    spawn_rate = FPS
    hit_factor = 1
    target_zone = 100
    max_mistake_series = 5
    max_falling_speed = 5
    min_spawn_rate = 3
    increment_falling_speed = (max_falling_speed - falling_speed) / 15000
    increment_spawn_rate = (spawn_rate - min_spawn_rate) / 15000


class Medium:
    falling_speed = 3.5
    spawn_rate = FPS // 1.5
    hit_factor = 2
    target_zone = 75
    max_mistake_series = 5
    max_falling_speed = 8
    min_spawn_rate = 5
    increment_falling_speed = (max_falling_speed - falling_speed) / 15000
    increment_spawn_rate = (spawn_rate - min_spawn_rate) / 15000


class Hard:
    falling_speed = 5
    spawn_rate = FPS // 3
    hit_factor = 3
    target_zone = 50
    max_mistake_series = 5
    max_falling_speed = 10
    min_spawn_rate = 10
    increment_falling_speed = (max_falling_speed - falling_speed) / 15000
    increment_spawn_rate = (spawn_rate - min_spawn_rate) / 15000


# soon
class Nightmare:
    falling_speed = 7
    spawn_rate = FPS // 6
    hit_factor = 5
    target_zone = 25
    max_mistake_series = 5
    max_falling_speed = 12
    min_spawn_rate = 15
    increment_falling_speed = (max_falling_speed - falling_speed) / 15000
    increment_spawn_rate = (spawn_rate - min_spawn_rate) / 15000


difficulty_map = {
    1: Easy,
    2: Medium,
    3: Hard,
    4: Nightmare
}