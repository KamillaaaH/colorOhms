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

class colorohmsGUI:

    def init_multiple(self):
        self.liststore = gtk.ListStore(int,str)
        self.liststore.append([0,"selecione"])
        self.liststore.append([1,"Ω"])
        self.liststore.append([2,"kΩ"])
        self.liststore.append([3,"MΩ"])
        
        self.combobox = self.builder.get_object('multiple')
        self.combobox.set_model(self.liststore)
        self.cell = gtk.CellRendererText()
        self.combobox.pack_start(self.cell, True)
        self.combobox.add_attribute(self.cell, 'text', 1)
        self.combobox.set_active(0)

    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("colorohms.glade")
        self.window = self.builder.get_object ("main")
        if self.window:
            self.window.connect("destroy", gtk.main_quit)        
        self.builder.connect_signals(self)
        self.init_multiple()

app = colorohmsGUI()
gtk.main()
