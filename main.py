import pyglet.window

import config
from config import FPS
from game import Game
from window import Window


class Main:
    # Public defs
    def __init__(self):
        self._reset()

    def start(self):
        pyglet.clock.schedule_interval(self._game.update, 1 / FPS)
        pyglet.app.run()

    # Shunting or routing or wiring
    def _listen_to_events(self):
        self._game.get_publisher().register(self._game.EVENT_LEVEL_RESET, self, self._listen_to_handlers)

    def _listen_to_handlers(self):
        self._window.remove_handlers()

        for handler in self._state.get_handlers():
            self._window.push_handlers(handler)

    # - Utils -
    def _reset(self):
        # Dynamic data
        self._window = Window()
        self._window.set_caption(config.GAME_TITLE)
        self._game = Game()
        self._set_state(self._game)
        self._listen_to_events()

    def _set_state(self, state):
        self._state = state
        self._listen_to_handlers()
        self._window.set_batch(self._get_state().get_batch())

    def _get_state(self):
        return self._state
