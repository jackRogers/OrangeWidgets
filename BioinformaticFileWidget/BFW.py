#bioinformatic file widget to be implemented
import BF		#this is where the functions for dealing with stuff go
import sys
sys.path.append("C:\\Python27\\Lib\\site-packages\\Orange\\OrangeWidgets")
from OWWidget import *
import OWGUI
import numpy as np

class Bio-file(OWWidget):
    
    def __init__(self, parent=None, signalManager=None):
        OWWidget.__init__(self, parent, signalManager, 'Bio-File')
        
        #self.inputs = [("Data", ExampleTable, self.data)]
        self.outputs = [("Sampled Data", ExampleTable)]

        # GUI
        box = OWGUI.widgetBox(self.controlArea, "Info")
        self.infoa = OWGUI.widgetLabel(box, 'File tool to help import, organize, and manipulate data of various file types from within orange.')
        self.infob = OWGUI.widgetLabel(box, '')
        self.resize(100,50)
        
        
#goals
	#take multiple files and merge them into single data table
	#be able to transpose matrix(switching from samples to genes as entries)
	#be able to deal with FASTA formats(WHY DOESNT ORANGE DO THIS?)
	
	
	
