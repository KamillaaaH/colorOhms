#!/usr/bin/env python
# coding=utf-8

import sys
try:
 	import pygtk
  	pygtk.require("2.0")
except:
  	pass
try:
	import gtk
  	import gtk.glade
except:
	sys.exit(1)

class main:
    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("resistor.glade")
        self.window = self.builder.get_object("main")
        if self.window:
            self.window.connect("destroy", gtk.main_quit)
        self.builder.connect_signals(self)
        self.resistor = self.builder.get_object("drawingarea1")

    def on_drawingarea1_expose_event(self, widget, * args):
        Band().render(self.resistor)


class Band(object):
    def __init__(self, order=1, color=1):        
        #@FIXME alguns desses nomes podem não ser aceitos no color parser
        colors = ['Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green',
                  'Blue', 'Violet', 'Grey', 'White', 'Gold', 'Silver']
        self.order  = order
        self.color  = colors[color]
        self.active = True
        self.width  = 100
        self.height = 49 if 1<order else 83
        self.left   = 50
        self.top    = 10

    def render(self, drawingarea):
        #@FIXME como é operador not?? xD
        if (not self.active):
            return False
        color = gtk.gdk.GC(drawingarea.window)
        color.set_rgb_fg_color(gtk.gdk.color_parse(self.color))
        drawingarea.window.draw_rectangle(color, True, self.left, self.top,
                                          self.width, self.height)

main()
gtk.main()
