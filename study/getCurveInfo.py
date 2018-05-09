import maya.cmds as cmds

def getCurveInfo():
    
    # Accessing Object Recently selected Objects
    selectedObjects = cmds.ls(selection=True)
    obj = selectedObjects[-1]
    
    degree = cmds.getAttr(obj + '.degree')
    spans = cmds.getAttr(obj + '.spans')
    cvs = degree + spans
    print('CVs: ', cvs)
    
    # Accessing first and last Vertex points on Curve
    cmds.select(obj + '.cv[0]')
    cmds.select(obj + '.cv[' + str(cvs-1) + ']', add=True)
    
getCurveInfo()