#!/usr/bin/env python
# coding=utf-8
import unittest
import sys
import colorOhms.colorOhms

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


class ColorOhmsTestCase(unittest.TestCase):
	def setUp(self):
		self.builder = gtk.Builder()
        self.builder.add_from_file("colorOhms2.glade")
        self.window = self.builder.get_object("main")
        self.builder.connect_signals(self)
        self.drawingarea1 = self.builder.get_object("resistorArea")
        
    def test_init(self):
    	
	
