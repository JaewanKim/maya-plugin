import maya.cmds as cmds
import random

class PeddleGenerator():

    def __init__(self):
        
        self.amount = 0
        self.amount_str = ''
        self.size = 0.0
        self.size_str = ''
        
        self.selectedObjs = []
        self.obj = ''
        
        if (cmds.window("peddle generator", exists=True)):
            cmds.deleteUI("peddle generator")
        
        # UI Component
        self.win = cmds.window("peddle generator", title="Peddle Generator", widthHeight=(400, 100))
        cmds.columnLayout()
        
        self.amount_str = cmds.intSliderGrp(l="Amount", min=1, max=100, field=True)
        self.size_str = cmds.floatSliderGrp(l="Size", min=1, max=3, field=True)
        
        cmds.button(label="Generate Peddles", command=self.classify_object)
        
        cmds.showWindow(self.win)

    def 


PeddleGenerator()