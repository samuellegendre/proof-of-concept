import math

import pyglet.shapes


def center_object(_object):
    if isinstance(_object, pyglet.shapes.Circle):
        _object.anchor_x = _object.radius / 2
        _object.anchor_y = _object.radius / 2
    else:
        _object.anchor_x = _object.width / 2
        _object.anchor_y = _object.height / 2


def distance_between(point_1=(0, 0), point_2=(0, 0)):
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)
