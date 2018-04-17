import maya.cmds as cmds
import random

class GravelGenerator():
    '''
        Description : Generate gravels randomly on selected object
        Things to do
            1. funtion : get_gravel_file, get_gravel_script, scatter_gravel_map, reset
            2. layout
    ''' 
    
    def __init__(self):
        
        self.radio = 0
        self.radio_str = ''
        
        self.amount = 0
        self.amount_str = ''
        
        self.global_size = 0
        self.global_size_str = ''
        
        self.max_size = 0.0
        self.max_size_str = ''
        
        self.min_size = 0.0
        self.min_size_str = ''
        
        self.selectedObjs = []
        self.obj = ''
        
        # Window
        if (cmds.window("gravel generator", exists=True)):
            cmds.deleteUI("gravel generator")
        
        self.win = cmds.window("gravel generator", title="Gravel Generator", widthHeight=(500, 300))
        
        cmds.columnLayout(adjustableColumn=True)
        cmds.rowLayout(numberOfColumns=3)
        
        self.radio_str = cmds.radioButtonGrp(label="Generate Type", labelArray2=['File', 'Script'], numberOfRadioButtons=2, select=1)
        
        cmds.setParent("..")
        
        self.amount_str = cmds.intSliderGrp(l="Amount", min=1, max=100, field=True)
        self.global_size_str = cmds.intSliderGrp(l="Global Size", min=1, max=3, field=True)
        self.max_size_str = cmds.floatSliderGrp(l="Max Size", min=1, max=3, field=True)
        self.min_size_str = cmds.floatSliderGrp(l="Min Size", min=1, max=3, field=True)
        
        cmds.columnLayout(adjustableColumn=True)
        
        cmds.setParent("..")
        cmds.button(label="Generate Gravels", command=self.get_values)
        cmds.button(label="Reset", )
        cmds.button(label="Test for scatter on grid", command=self.scatter_gravel_grid)
        
        cmds.setParent("..")
        cmds.showWindow(self.win)
        
        
    def get_values(self, args):
        # Get values of UI Component
        
        self.radio = cmds.radioButtonGrp(self.radio_str, query=True, select=True)
        
        self.amount = cmds.intSliderGrp(self.amount_str, query=True, value=True)
        self.global_size = cmds.intSliderGrp(self.global_size_str, query=True, value=True)
        self.max_size = cmds.floatSliderGrp(self.max_size_str, query=True, value=True)
        self.min_size = cmds.floatSliderGrp(self.min_size_str, query=True, value=True)
        
        if (self.radio == 1):    # File
            self.get_gravel_file(self)
        
        elif (self.radio == 2):  # Script
            self.get_gravel_script(self)
        
        
    def get_gravel_file(self, args):
        # Get the files of gravel, size it randomly
        # I/O File obj, poly, 
        print("get_gravel_file")
        
        
    def get_gravel_script(self, args):
        # Generate gravels by script
        print("get_gravel_script")
        
        
    def recognize_map(self, args):
        # Recognize the selected object as a map
        print("recognize_map")
        
        self.selectedObjs = cmds.ls(selection=True)
        
        # Is it necessary exception for len(self.selectedObjs) negative ? Idon't think so..
        if (len(self.selectedObjs) == 0):
            self.scatter_gravel_grid(self)
        
        else:    # len(self.selectedObjs) > 0
            self.scatter_gravel_map(self)
        
        
    def scatter_gravel_grid(self, args):
        # Scatter gravels on grid
        
        print("scatter_gravel_grid")
        
        self.amount = cmds.intSliderGrp(self.amount_str, query=True, value=True)    # Will be deleted
        print(self.amount)
        
        gravelGrp = cmds.group(empty=True, name="Gravel_Grp")
        
        for i in range(0, self.amount):    # for obj in objlist:
            
            x = random.uniform(-10.0, 10.0)
            z = random.uniform(-10.0, 10.0)
            
            mycube = cmds.polyCube(h=3, w=3, d=3, n="randPolyCube#")
            cmds.move(x, 0.0, z, mycube)    # obj in 
            cmds.rotate(random.random()*1000, random.random()*1000, random.random()*1000, mycube)
            
            cmds.parent(mycube, gravelGrp)
        
        cmds.select(gravelGrp, replace=True)
        
        
    def scatter_gravel_map(self, args):
        # Scatter gravels on map
        print("scatter_gravel_map")
        
        # Get vertex of the map
        
        
    def reset(self, args):
        # Reset the values set by a user
        print("reset")
        

GravelGenerator()