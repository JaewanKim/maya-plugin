import maya.cmds as cmds

def isSplitEdge(obj, index):

    result = cmds.polyListComponentConversion(obj + '.e[' + str(index) + ']', fromEdge=True, toUV=True)
    cmds.select(result, replace=True)
    vertNum = cmds.polyEvaluate(vertexComponent=True)

    result = cmds.polyListComponentConversion(obj + '.e[' + str(index) + ']', fromEdge=True, toVertex=True)
    cmds.select(result, replace=True)
    uvNum = cmds.polyEvaluate(uvComponent=True)
    
    if (uvNum == vertNum):
        return False
    
    return True

def uvInfo():
    
    sel = cmds.ls(selection=True)
    obj = sel[0]        # sel[-1] works well

    uvs = cmds.polyEvaluate(obj, uvComponent=True)
    uvPos = cmds.polyEditUV(obj + '.map[0]', query=True)
    isFirstEdgeSplit = isSplitEdge(obj, 0)
    
    print("Num UVs: " + str(uvs))
    print("Position of first UV: ", uvPos)
    print("First edge is split: ", isFirstEdgeSplit)
    
    cmds.select(obj, replace=True)

uvInfo()