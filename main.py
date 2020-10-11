import pyglet
from pyglet.gl import *

win = pyglet.window.Window()

@win.event
def on_draw():
    win.clear()

pyglet.app.run()