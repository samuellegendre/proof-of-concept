import pyglet.window

import config


class Window(pyglet.window.Window):
    # Public defs
    def __init__(self):
        super(Window, self).__init__(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)

        self._reset()

    # - Behaviors or handlers or listeners -
    def on_draw(self):
        self.clear()
        self._batch.draw()

    # - Utils -
    def set_batch(self, scene):
        self._batch = scene
        self.on_draw()

    def _reset(self):
        # Dynamic data
        self._batch = pyglet.graphics.Batch()
