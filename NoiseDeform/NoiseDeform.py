import maya.cmds as cmds
import random

class NoiseDeformer():
    '''
        Description : Add noise deformation to selected object(polygon, nurbsSurface)
        Things to do :
            1. Refactoring
    '''
    
    def __init__(self):
        
        self.amount = 0.0
        self.amount_str = ''
        self.selectedObjs = []
        self.obj = ''
        
        if (cmds.window("noise", exists=True)):
            cmds.deleteUI("noise")
        
        # UI Component
        if (cmds.window("noise", exists=True)):
            cmds.deleteUI("noise", window=True)
            
        self.win = cmds.window("noise", title="Set Noise", sizeable=False, menuBar=True)
        
        # Menu Bar
        fileMenu = cmds.menu(label="Edit")
        saveOption = cmds.menuItem(label="Save Settings", enable=False)
        resetOption = cmds.menuItem(label="Reset Settings", command=self.reset)
        
        helpMenu = cmds.menu(label="Help")
        helpOption = cmds.menuItem(label="Help on Gravel Generator", command=self.showHelp)
        cmds.setParent("..")
        
        # Slider Group
        cmds.columnLayout(h=200)
        self.amount_str = cmds.floatSliderGrp(l="Amount", min=0, max=2, field=True)
        cmds.setParent("..")
        
        cmds.columnLayout(h=40)
        cmds.separator(h=5, style='single', hr=True)
        cmds.setParent("..")
        
        # Button Layout
        cmds.rowColumnLayout(numberOfColumns=7, columnWidth=[(1,5),(2,164),(3,4),(4,164),(5,4),(6,164),(7,5)])
        cmds.separator(h=10, style='none')
        cmds.button(label="Apply and Close", h=27, command=self.classify_object_close)
        cmds.separator(h=10, style='none')
        cmds.button(label="Apply", h=27, command=self.classify_object)
        cmds.separator(h=10, style='none')
        cmds.button(label="Close", h=27, command=self.close)
        cmds.separator(h=10, style='none')
        cmds.setParent("..")
        
        cmds.showWindow(self.win)
        
        
    def classify_object_close(self, args):
        
        # Exception to prevent when nothing is selected
        self.selectedObjs = cmds.ls(selection=True)
        
        if (len(self.selectedObjs) < 1):
            cmds.error("Please select object at least one!")
        
        # Get noise amount from slider group
        self.amount = cmds.floatSliderGrp(self.amount_str, query=True, value=True)
        
        for i in range(0, len(self.selectedObjs)):
            
            self.obj = self.selectedObjs[i]
            
            shapeNode = cmds.listRelatives(self.obj, shapes=True)
            nodeType = cmds.nodeType(shapeNode)
            
            # Classify object nodeType and Call method
            if (nodeType == "mesh"):
                self.noise_poly(self)
                
            elif (nodeType == "nurbsSurface" ):
                self.noise_nurbsSurface(self)
                
            else:
                cmds.error("Please select mesh or nurbsSurface!")
        
        if cmds.window(self.win, exists=True): 
            cmds.deleteUI(self.win, window=True)
        
        
    def classify_object(self, args):
        
        # Exception to prevent when nothing is selected
        self.selectedObjs = cmds.ls(selection=True)
        
        if (len(self.selectedObjs) < 1):
            cmds.error("Please select object at least one!")
        
        # Get noise amount from slider group
        self.amount = cmds.floatSliderGrp(self.amount_str, query=True, value=True)
        
        for i in range(0, len(self.selectedObjs)):
            
            self.obj = self.selectedObjs[i]
            
            shapeNode = cmds.listRelatives(self.obj, shapes=True)
            nodeType = cmds.nodeType(shapeNode)
            
            # Classify object nodeType and Call method
            if (nodeType == "mesh"):
                self.noise_poly(self)
                
            elif (nodeType == "nurbsSurface" ):
                self.noise_nurbsSurface(self)
                
            else:
                cmds.error("Please select mesh or nurbsSurface!")
        
        
    def noise_poly(self, args):
        # Add noise for polygon
        
        shapeNode = cmds.listRelatives(self.obj, shapes=True)
        
        numVerts = cmds.polyEvaluate(self.obj, vertex=True)
        
        randAmt = [0, 0, 0]
        for i in range(0, numVerts):
            
            for j in range(0, 3):
                randAmt[j] = random.random() * (self.amount*2) - self.amount
            
            vertexStr = "{0}.vtx[{1}]".format(self.obj, i)
            cmds.select(vertexStr, replace=True)
            cmds.move(randAmt[0], randAmt[1], randAmt[2], relative=True)
        
        cmds.select(self.obj, replace=True)        # finish up
        
        
    def noise_nurbsSurface(self, args):
        # Add noise for nurbsSurface
        
        shapeNode = cmds.listRelatives(self.obj, shapes=True)
        
        degU = cmds.getAttr(self.obj + '.degreeU')
        spansU = cmds.getAttr(self.obj + '.spansU')
        cvsU = degU + spansU
        
        degV = cmds.getAttr(self.obj + '.degreeV')
        spansV = cmds.getAttr(self.obj + '.spansV')
        cvsV = degV + spansV
        
        randAmt = [0, 0, 0]
        for i in range(0, cvsU):
            
            for j in range(0, cvsV):
                
                for k in range(0, 3):
                    
                    randAmt[k] = random.random() * (self.amount*2) - self.amount
                
                vertexStr = "{0}.cv[{1}][{2}]".format(self.obj, i, j)
                
                cmds.select(vertexStr, replace=True)
                cmds.move(randAmt[0], randAmt[1], randAmt[2], relative=True)
        
        cmds.select(self.obj, replace=True)
        
        
    def reset(self, args):
        # Reset the values by default
        cmds.floatSliderGrp(self.amount_str, edit=True, value=True)
        
        
    def showHelp(self, args):
        cmds.showHelp("https://github.com/JaewanKim/maya-plugin", absolute=True)
        
        
    def close(self, args):
        # Close the window
        if cmds.window(self.win, exists=True): 
            cmds.deleteUI(self.win, window=True)


NoiseDeformer()