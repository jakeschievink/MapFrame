#!/usr/bin/env python
#
#  Copyright (c) 2013, 2015, Corey Goldberg
#
#  Dev: https://github.com/cgoldberg/py-slideshow
#  License: GPLv3


import argparse
import random
import os,pdb
import glob
import pyglet

cities = glob.glob("./citymaps/*/")
city = random.choice(cities)
images = ["1.jpg","2.jpg","3.jpg","6.jpg"]
image_pos = 0

def update_pan_zoom_speeds():
    global _pan_speed_x
    global _pan_speed_y
    global _zoom_speed
    _pan_speed_x = random.randint(-8, 8)
    _pan_speed_y = random.randint(-8, 8)
    _zoom_speed = random.uniform(-0.02, 0.02)
    return _pan_speed_x, _pan_speed_y, _zoom_speed


def update_pan(dt):
    sprite.x += dt * _pan_speed_x
    sprite.y += dt * _pan_speed_y


def update_zoom(dt):
    sprite.scale += dt * _zoom_speed

def update_city(dt):
    city = random.choice(cities)

def update_image(dt):
    global image_pos
    img = pyglet.image.load(city+images[image_pos])
    sprite.image = img
    sprite.scale = get_scale(window, img)
    sprite.x = 0
    sprite.y = 0
    update_pan_zoom_speeds()
    if image_pos > 2:
        image_pos = 0
    else: 
        image_pos += 1
    window.clear()


def get_scale(window, image):
    if image.width > image.height:
        scale = float(window.width) / image.width
    else:
        scale = float(window.height) / image.height
    return scale


window = pyglet.window.Window(fullscreen=True)


@window.event
def on_draw():
    sprite.draw()


if __name__ == '__main__':

    image_pos = 0
    img = pyglet.image.load(city+images[image_pos])
    image_pos+=1
    sprite = pyglet.sprite.Sprite(img)
    sprite.scale = get_scale(window, img)
    pyglet.clock.schedule_interval(update_image, 6)
    pyglet.clock.schedule_interval(update_city, 200)
    pyglet.app.run()
