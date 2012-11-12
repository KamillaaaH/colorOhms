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

    def init_combobox(self, objname, values):
        """
        inicia combobox, incluindo suas opções
        objname -- nome do objeto
        values  -- lista de opções
        """
        # @FIXME testar parâmetros e entender essa sobrescrita de instâncias
        self.liststore = gtk.ListStore(int,str)
        for i, value in enumerate(values):
            self.liststore.append([i, value])
        self.combobox = self.builder.get_object(objname)
        self.combobox.set_model(self.liststore)
        self.cell = gtk.CellRendererText()
        self.combobox.pack_start(self.cell, True)
        self.combobox.add_attribute(self.cell, 'text', 1)
        self.combobox.set_active(0)

    def init_objects(self):        
        # inicia combobox "multiple" (múltiplo de ohm)
        self.init_combobox("multiple", ["Ω", "kΩ", "MΩ"])
        # inicia combobox "restype"  (tipo de resistor/qtde listras)
#        self.init_combobox("restype",  ["4 bands", "5 bands", "6 bands"])

    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("colorohms.glade")
        self.window = self.builder.get_object ("colorohms")
        if self.window:
            self.window.connect("destroy", gtk.main_quit)        
        self.builder.connect_signals(self)
        self.init_objects()

app = colorohmsGUI()
gtk.main()
