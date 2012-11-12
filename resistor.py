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


class ResistorUI:

    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("resistor.glade")
        self.window = self.builder.get_object("main")
        if self.window:
            self.window.connect("destroy", gtk.main_quit)
        self.builder.connect_signals(self)
        
        self.drawingarea1 = self.builder.get_object("drawingarea1")

        # Definições de cores
        self.fg_gc  = gtk.gdk.GC(self.drawingarea1.window)
        self.bg_gc  = gtk.gdk.GC(self.drawingarea1.window)
        self.bg_gc1 = gtk.gdk.GC(self.drawingarea1.window)
        self.bg_gc2 = gtk.gdk.GC(self.drawingarea1.window)
        self.bg_gc3 = gtk.gdk.GC(self.drawingarea1.window)
        self.bg_gc4 = gtk.gdk.GC(self.drawingarea1.window)
        self.bg_gc5 = gtk.gdk.GC(self.drawingarea1.window)
        self.bg_gc6 = gtk.gdk.GC(self.drawingarea1.window)
        self.bg_gc.set_rgb_fg_color(gtk.gdk.color_parse('#BD987F'))
        self.fg_gc.set_rgb_fg_color(gtk.gdk.color_parse('black'))
        self.bg_gc1.set_rgb_fg_color(gtk.gdk.color_parse('Black'))
        self.bg_gc2.set_rgb_fg_color(gtk.gdk.color_parse('Red'))
        self.bg_gc3.set_rgb_fg_color(gtk.gdk.color_parse('Brown'))
        self.bg_gc4.set_rgb_fg_color(gtk.gdk.color_parse('Orange'))
        self.bg_gc5.set_rgb_fg_color(gtk.gdk.color_parse('Blue'))
        self.bg_gc6.set_rgb_fg_color(gtk.gdk.color_parse('Green'))

    # desenha o resistor dentro de drawingarea1
    def on_drawingarea1_expose_event(self, widget, * args):
        width, height = self.drawingarea1.window.get_size()
        x = y = 250/4
        w = (width-300) / 2
        h = 250/2
        # terminal esquerdo
        self.drawingarea1.window.draw_line(self.fg_gc, w+20, 107, w+40, 107)
        self.drawingarea1.window.draw_line(self.fg_gc, w+20, 107, w+20, 200)
        # terminal direito
        self.drawingarea1.window.draw_line(self.fg_gc, w+258, 107, w+278, 107)
        self.drawingarea1.window.draw_line(self.fg_gc, w+278, 107, w+278, 200)

        # ponta esquerda - borda
        self.drawingarea1.window.draw_arc(self.fg_gc, True, w+35, 65, 68, 85, 360, 360*64)
        # ponta esquerda - preenchimento
        self.drawingarea1.window.draw_arc(self.bg_gc, True, w+36, 66, 66, 83, 360, 360*64)
        # ponta direita - borda
        self.drawingarea1.window.draw_arc(self.fg_gc, True, w+190, 65, 68, 85, 360, 360*64)
        # ponta direita - preenchimento
        self.drawingarea1.window.draw_arc(self.bg_gc, True, w+191, 66, 66, 83, 360, 360*64)

        # meio - borda
        self.drawingarea1.window.draw_rectangle(self.fg_gc,  False, w+97,  82, 99, 50)
        # meio - preenchimento
        self.drawingarea1.window.draw_rectangle(self.bg_gc,  True,  w+97,  83, 100, 49)
        # 1a listra
        self.drawingarea1.window.draw_rectangle(self.bg_gc1, True,  w+63,  67, 10, 83)
        # 2a listra
        self.drawingarea1.window.draw_rectangle(self.bg_gc2, True,  w+110, 83, 10, 49)
        # 3a listra
        self.drawingarea1.window.draw_rectangle(self.bg_gc3, True,  w+130, 83, 10, 49)
        # 4a listra
        self.drawingarea1.window.draw_rectangle(self.bg_gc4, True,  w+150, 83, 10, 49)
        # 5a listra
        self.drawingarea1.window.draw_rectangle(self.bg_gc5, True,  w+170, 83, 10, 49)
        # 6a listra
        self.drawingarea1.window.draw_rectangle(self.bg_gc6, True,  w+215, 67, 10, 83)

ResistorUI()
gtk.main()
