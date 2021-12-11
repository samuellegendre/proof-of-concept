import random

import pyglet.shapes

import config
from utils import util


def objects(_number_objects, _player_position, _batch):
    _objects = []

    for i in range(_number_objects):
        _x, _y = _player_position

        while util.distance_between((_x, _y), _player_position) < 100:
            _x = random.randint(-config.WINDOW_WIDTH - 100, config.WINDOW_WIDTH + 200)
            _y = random.randint(-config.WINDOW_HEIGHT - 100, config.WINDOW_HEIGHT + 200)

        _object = pyglet.shapes.Circle(x=_x, y=_y, radius=25, batch=_batch, color=(0, 0, 255))
        util.center_object(_object)
        _objects.append(_object)

    return _objects
