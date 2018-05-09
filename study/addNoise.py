import maya.cmds as cmds
import random

def addNoise(amt):
    
    # Selecting Object to be noised
    selectedObjs = cmds.ls(selection=True)
    obj = selectedObjs[-1]
    
    shapeNode = cmds.listRelatives(obj, shapes=True)
    
    # Exception for mesh
    if (cmds.nodeType(shapeNode) != 'mesh'):
        cmds.error('Select a mesh')
        return
    
    numVerts = cmds.polyEvaluate(obj, vertex=True)
    
    randAmt = [0, 0, 0]
    for i in range(0, numVerts):
        
        for j in range(0, 3):
            randAmt[j] = random.random() * (amt*2) - amt
            
        vertexStr = "{0}.vtx[{1}]".format(obj, i)
        cmds.select(vertexStr, replace=True)
        cmds.move(randAmt[0], randAmt[1], randAmt[2], relative=True)
    
        # Same as following, but faster than below
        # cmds.polyMoveVertex(vertexStr, t=randAmt)
            
    cmds.select(obj, replace=True)        # finish up 
    

addNoise(0.1)