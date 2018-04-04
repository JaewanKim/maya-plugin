import maya.cmds as cmds
import random

class NoiseDeformer():

    def __init__(self):
        
        self.amount = 0.0
        self.amount_str = ''
        self.selectedObjs = []
        self.obj = ''
                
        if (cmds.window("noise", exists=True)):
            cmds.deleteUI("noise")
        
        # UI Component
        self.win = cmds.window("noise", title="Set Noise", widthHeight=(400, 100))
        cmds.columnLayout()
        cmds.rowLayout(numberOfColumns=2)
        
        self.amount_str = cmds.floatSliderGrp(l="Amount", min=0, max=3, field=True)
        cmds.button(label="Add Noise", command=self.classify_object)
        
        cmds.setParent("..")
        cmds.showWindow(self.win)
        
        
    def classify_object(self, args):
        
        self.selectedObjs = cmds.ls(selection=True)
        
        if (len(self.selectedObjs) < 1):
            cmds.error("Please select object at least one!")
        
        self.obj = self.selectedObjs[-1]
        
        # Get noise amount from slider group
        self.amount = cmds.floatSliderGrp(self.amount_str, query=True, value=True)
        
        shapeNode = cmds.listRelatives(self.obj, shapes=True)
        nodeType = cmds.nodeType(shapeNode)
        
        if (nodeType == "mesh"):
            self.noise_poly(self)
            
        elif (nodeType == "nurbsSurface" ):
            self.noise_nurbsSurface(self)
            
        else:    # (nodeType == "nurbsCurve")
            print("preparing for nurbsCurve")
    
    
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

NoiseDeformer()
