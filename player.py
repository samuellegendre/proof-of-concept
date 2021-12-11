import pyglet.clock
from pyglet.window import key

from config import PLAYER_SPEED, PLAYER_MOVE_RIGHT_KEY, PLAYER_MOVE_LEFT_KEY, WINDOW_WIDTH, PLAYER_MOVE_UP_KEY, \
    WINDOW_HEIGHT, PLAYER_MOVE_DOWN_KEY
from lib.publisher import Publisher


class Player(pyglet.shapes.Rectangle):
    # Static data
    EVENT_PLAYER_MOVES_DOWN = "EVENT_PLAYER_MOVES_DOWN"
    EVENT_PLAYER_MOVES_LEFT = "EVENT_PLAYER_MOVES_LEFT"
    EVENT_PLAYER_MOVES_RIGHT = "EVENT_PLAYER_MOVES_RIGHT"
    EVENT_PLAYER_MOVES_UP = "EVENT_PLAYER_MOVES_UP"

    # Public defs
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)

        self._key_handler = key.KeyStateHandler()
        self._publisher = Publisher(
            [self.EVENT_PLAYER_MOVES_RIGHT, self.EVENT_PLAYER_MOVES_LEFT, self.EVENT_PLAYER_MOVES_UP,
             self.EVENT_PLAYER_MOVES_DOWN])
        self.speed = PLAYER_SPEED

    def update(self, dt):
        if self._key_handler[PLAYER_MOVE_RIGHT_KEY]:
            if self.x <= WINDOW_WIDTH // 8 * 6:
                self.x += PLAYER_SPEED * dt
            else:
                self._publisher.dispatch(self.EVENT_PLAYER_MOVES_RIGHT)

        if self._key_handler[PLAYER_MOVE_LEFT_KEY]:
            if self.x >= WINDOW_WIDTH // 8 * 2:
                self.x -= PLAYER_SPEED * dt
            else:
                self._publisher.dispatch(self.EVENT_PLAYER_MOVES_LEFT)

        if self._key_handler[PLAYER_MOVE_UP_KEY]:
            if self.y <= WINDOW_HEIGHT // 8 * 6:
                self.y += PLAYER_SPEED * dt
            else:
                self._publisher.dispatch(self.EVENT_PLAYER_MOVES_UP)

        if self._key_handler[PLAYER_MOVE_DOWN_KEY]:
            if self.y >= WINDOW_HEIGHT // 8 * 2:
                self.y -= PLAYER_SPEED * dt
            else:
                self._publisher.dispatch(self.EVENT_PLAYER_MOVES_DOWN)

    # - Utils -
    def get_key_handler(self):
        return self._key_handler

    def get_publisher(self):
        return self._publisher
