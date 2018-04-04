import maya.cmds as cmds

def currentSelectionPolygonal(obj):
    
    shapeNode = cmds.listRelatives(obj, shapes=True)
    nodeType = cmds.nodeType(shapeNode)

    if nodeType == "mesh":    # nurbsCurve, nurbsSurface
        return True

    return False

#    return(nodeType == "mesh")

def checkSelection():
    selectedObjs = cmds.ls(selection=True)    # ls : list
    
    if (len(selectedObjs) < 1):
        cmds.error('Please select an object')
    
    lastSelected = selectedObjs[-1]        # Recently selected object
    
    isPolygon = currentSelectionPolygonal(lastSelected)

    if (isPolygon):
        print('FOUND POLYGON')
    else:
        cmds.error('Please select a polygonal object')

checkSelection()
