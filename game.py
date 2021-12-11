import pyglet

import config
import player
from lib.publisher import Publisher
from player import Player
from utils import util, load


class Game:
    # Static data
    EVENT_LEVEL_RESET = "EVENT_LEVEL_RESET"

    # Public defs
    def __init__(self):
        self._reset()

    def update(self, dt):
        for _object in self._game_objects:
            if isinstance(_object, player.Player):
                _object.update(dt)

    # - Behaviors or handlers or listeners -
    def on_player_moves_right(self):
        for _object in self._game_objects:
            if not isinstance(_object, player.Player):
                _object.x -= self._player.speed / config.FPS

    def on_player_moves_left(self):
        for _object in self._game_objects:
            if not isinstance(_object, player.Player):
                _object.x += self._player.speed / config.FPS

    def on_player_moves_up(self):
        for _object in self._game_objects:
            if not isinstance(_object, player.Player):
                _object.y -= self._player.speed / config.FPS

    def on_player_moves_down(self):
        for _object in self._game_objects:
            if not isinstance(_object, player.Player):
                _object.y += self._player.speed / config.FPS

    def _listen_to_events(self):
        self._player.get_publisher().register(self._player.EVENT_PLAYER_MOVES_RIGHT, self,
                                              self.on_player_moves_right)
        self._player.get_publisher().register(self._player.EVENT_PLAYER_MOVES_LEFT, self,
                                              self.on_player_moves_left)
        self._player.get_publisher().register(self._player.EVENT_PLAYER_MOVES_UP, self,
                                              self.on_player_moves_up)
        self._player.get_publisher().register(self._player.EVENT_PLAYER_MOVES_DOWN, self,
                                              self.on_player_moves_down)

    # - Utils -
    def get_publisher(self):
        return self._publisher

    def get_batch(self):
        return self._batch

    def get_handlers(self):
        return self._handlers

    def _reset(self):
        # Dynamic data
        self._publisher = Publisher([self.EVENT_LEVEL_RESET])
        self._batch = pyglet.graphics.Batch()

        self._reset_level()

    def _reset_level(self):
        self._player = Player(x=config.WINDOW_WIDTH // 2, y=config.WINDOW_HEIGHT // 2, width=50, height=50,
                              batch=self._batch, color=(0, 255, 0))
        util.center_object(self._player)
        self._objects = load.objects(15, self._player.position, self._batch)
        self._game_objects = [self._player] + self._objects
        self._handlers = [self, self._player, self._player.get_key_handler()]
        self._listen_to_events()
        self._publisher.dispatch(self.EVENT_LEVEL_RESET)
