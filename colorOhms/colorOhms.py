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
    
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):    	
        self.builder = gtk.Builder()
        try:
        	self.builder.add_from_file("colorOhms.glade")
        except:
        	print "Can't load glade file"

        self.window = self.builder.get_object("main_window")
        self.window.set_title("ColorOhms")
        	
        if self.window:
            self.window.connect("delete_event", self.delete_event)
        
        self.builder.connect_signals(self)
        
        self.drawingarea = self.builder.get_object("drawingarea")
        
        print self.drawingarea.window
    
        self.drawingarea.show()
        
        self.window.show()

    # desenha o resistor dentro de drawingarea
    def on_drawingarea_expose_event(self, widget, * args):
        width, height = self.drawingarea.get_size()
        x = y = 250/4
        w = (width-300) / 2
        h = 250/2
        # terminal esquerdo
        self.drawingarea.draw_line(self.fg_gc, w+20, 107, w+40, 107)
        self.drawingarea.draw_line(self.fg_gc, w+20, 107, w+20, 200)
        # terminal direito
        self.drawingarea.draw_line(self.fg_gc, w+258, 107, w+278, 107)
        self.drawingarea.draw_line(self.fg_gc, w+278, 107, w+278, 200)

        # ponta esquerda - borda
        self.drawingarea.draw_arc(self.fg_gc, True, w+35, 65, 68, 85, 360, 360*64)
        # ponta esquerda - preenchimento
        self.drawingarea.draw_arc(self.bg_gc, True, w+36, 66, 66, 83, 360, 360*64)
        # ponta direita - borda
        self.drawingarea.draw_arc(self.fg_gc, True, w+190, 65, 68, 85, 360, 360*64)
        # ponta direita - preenchimento
        self.drawingarea.draw_arc(self.bg_gc, True, w+191, 66, 66, 83, 360, 360*64)

        # meio - borda
        self.drawingarea.draw_rectangle(self.fg_gc,  False, w+97,  82, 99, 50)
        # meio - preenchimento
        self.drawingarea.draw_rectangle(self.bg_gc,  True,  w+97,  83, 100, 49)
        # 1a listra
        self.drawingarea.draw_rectangle(self.listra1, True,  w+63,  67, 10, 83)
        # 2a listra
        self.drawingarea.draw_rectangle(self.listra2, True,  w+110, 83, 10, 49)
        # 3a listra
        self.drawingarea.draw_rectangle(self.listra3, True,  w+130, 83, 10, 49)
        # 4a listra
        self.drawingarea.draw_rectangle(self.listra4, True,  w+150, 83, 10, 49)
        # 5a listra
        self.drawingarea.draw_rectangle(self.listra5, True,  w+170, 83, 10, 49)
        # 6a listra
        self.drawingarea.draw_rectangle(self.listra6, True,  w+215, 67, 10, 83)


if __name__ == "__main__":
	ResistorUI()
	gtk.main()