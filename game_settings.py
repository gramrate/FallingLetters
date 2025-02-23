import json
import os


class GameSettings:
    def __init__(self):
        with open("data.json", 'r') as file:
            data = json.load(file)

        # Инициализация внутренних переменных
        self._player_secret_key = data["player"].get("player-secret-key")
        self._nickname = data["player"].get("nickname")
        self._last_played = data["player"].get("last_played")
        self._highscore = data["player"].get("highscore")
        self._record_set = data["player"].get("record_set")

        self._game_secret_key = data["game_settings"].get("game-secret-key")
        self._difficulty = data["game_settings"].get("difficulty")

        self._session_secret_key = data["session"].get("session-secret-key")
        self._session = data["session"].get("session")

    # Свойства для player_secret_key
    @property
    def player_secret_key(self):
        return self._player_secret_key

    @player_secret_key.setter
    def player_secret_key(self, value):
        self._player_secret_key = value

    # Свойства для nickname
    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, value):
        self._nickname = value

    # Свойства для last_played
    @property
    def last_played(self):
        return self._last_played

    @last_played.setter
    def last_played(self, value):
        self._last_played = value

    # Свойства для highscore
    @property
    def highscore(self):
        return self._highscore

    @highscore.setter
    def highscore(self, value):
        self._highscore = value

    # Свойства для record_set
    @property
    def record_set(self):
        return self._record_set

    @record_set.setter
    def record_set(self, value):
        self._record_set = value

    # Свойства для game_secret_key
    @property
    def game_secret_key(self):
        return self._game_secret_key

    @game_secret_key.setter
    def game_secret_key(self, value):
        self._game_secret_key = value

    # Свойства для difficulty
    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value):
        self._difficulty = value

    # Свойства для session_secret_key
    @property
    def session_secret_key(self):
        return self._session_secret_key

    @session_secret_key.setter
    def session_secret_key(self, value):
        self._session_secret_key = value

    # Свойства для session
    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, value):
        self._session = value

    def save(self):
        data = {
            "player": {"player-secret-key": self._player_secret_key,
                       "nickname": self._nickname,
                       "last_played": self._last_played,
                       "highscore": self._highscore,
                       "record_set": self._record_set, },
            "game_settings": {"game-secret-key": self._game_secret_key,
                              "difficulty": self._difficulty, },
            "session": {"session-secret-key": self._session_secret_key,
                        "session": self._session},
        }
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2)
