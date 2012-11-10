#!/usr/bin/env python

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

class colorohmsGUI:

    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("colorohms.glade")
        self.window = self.builder.get_object ("main")
        if self.window:
            self.window.connect("destroy", gtk.main_quit)        
        self.builder.connect_signals(self)

app = colorohmsGUI()
gtk.main()
