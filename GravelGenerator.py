import maya.cmds as cmds
import random

class GravelGenerator():
    '''
        Description : Generate gravels randomly on selected object
        Things to do
            1. 
            2. 
            . layout
    ''' 
    
    def __init__(self):
        
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

        # DirectionControl = cmds.radioCollection()
        # Direction0 = cmds.radioButton(label='Front')
        # Direction1 = cmds.radioButton(label='Back')
        # Direction2 = cmds.radioButton(label='Random')
        # DirectionControl = cmds.radioCollection( DirectionControl, edit=True, select=Direction0 )
        
#        self.radio_col = cmds.radioCollection()
#        cmds.radioButtonGrp(label="Generate Type", labelArray2=['File', 'Script'], numberOfRadioButtons=2)
#        self.radio_col = cmds.radioCollection(self.radio_col, edit=True, select='Script')

        cmds.setParent("..")
        
        self.amount_str = cmds.intSliderGrp(l="Amount", min=1, max=100, field=True)
        self.global_size_str = cmds.intSliderGrp(l="Global Size", min=1, max=3, field=True)
        self.max_size_str = cmds.floatSliderGrp(l="Max Size", min=1, max=3, field=True)
        self.min_size_str = cmds.floatSliderGrp(l="Min Size", min=1, max=3, field=True)
        
        cmds.columnLayout(adjustableColumn=True)
        
        cmds.setParent("..")
        cmds.button(label="Generate Gravels", command=self.get_values)
        cmds.button(label="Reset", command=self.reset)
        
        cmds.setParent("..")
        cmds.showWindow(self.win)

    def get_values(self, args):
        # Get value of Generate type
        self.amount = cmds.intSliderGrp(self.amount_str, query=True, value=True)
        self.global_size = cmds.intSliderGrp(self.global_size_str, query=True, value=True)
        self.max_size = floatSliderGrp(self.max_size_str, query=True, value=True)
        self.min_size = floatSliderGrp(self.min_size_str, query=True, value=True)
        
        # self.radioCol = cmds.radioCollection(DirectionControl, query=True, sl=True)
        # getSelectRadioVal = cmds.radioButton(self.radioCol, query=True, select=True)
        
#        self.radio_collect = cmds.radioCollection(self.radio_col, query=True, select=True)
#        getRadioVal = cmds.radioButton(self.radio_collect, query=True, select=True)

        print(self.amount + self.global_size)

    def make_gravel(self, args):
        # Generate gravels by script
        pass

    def get_gravel_file(self, args):
        # Get the files of gravel, size it randomly
        # I/O File obj, poly, 
        pass
        
    def recognize_map(self, args):
        # Recognize the selected object as a map
        self.selectedObjs = cmds.ls(selection=True)
        
        # Is it necessary exception for len(self.selectedObjs) negative ? Idon't think so..
        if (len(self.selectedObjs) == 0):
            self.scatter_gravel_grid(self)
        
        else:    # len(self.selectedObjs) > 0
            self.scatter_gravel_map(self)
        
        
    def scatter_gravel_grid(self, args):
        # Scatter gravels on grid
        pass
        
    def scatter_gravel_map(self, args):
        # Scatter gravels on map
        # Get vertex of the map
        pass
                
        
    def reset(self, args):
        # Reset the values set by a user
        pass

GravelGenerator()
