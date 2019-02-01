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

class SlideShow:
    def __init__(self):
        self.cities = glob.glob("./citymaps/*/")
        self.city = random.choice(self.cities)
        self.images = ["1.jpg","2.jpg","3.jpg","6.jpg"]
        self.image_pos = 0
        self.window = pyglet.window.Window()
        self.img = pyglet.image.load(self.city+self.images[self.image_pos])
        self.sprite = pyglet.sprite.Sprite(self.img)
        
    def update_city(self, dt):
        self.city = random.choice(self.cities)

    def update_image(self, dt):
        print("updating")
        self.img = pyglet.image.load(self.city+self.images[self.image_pos])
        self.sprite.image = self.img
        self.sprite.scale = self.get_scale(self.window, self.img)
        self.sprite.x = 0
        self.sprite.y = 0
        if self.image_pos > 2:
            self.image_pos = 0
        else: 
            self.image_pos += 1
        
        self.window.clear()
        self.sprite.draw()


    def get_scale(self, window, image):
        if image.width > image.height:
            scale = float(window.width) / image.width
        else:
            scale = float(window.height) / image.height
        return scale




  # @self.window.event
  # def on_draw(self):
  #     self.sprite.draw()

    def run(self):
        self.sprite.scale = self.get_scale( self.window, self.img)
        print("got here")
        self.sprite.draw()
        pyglet.clock.schedule_interval(self.update_image, 2)
        pyglet.clock.schedule_interval(self.update_city, 300)
        pyglet.app.run()
