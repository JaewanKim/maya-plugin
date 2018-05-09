import maya.cmds as cmds

# examine data for a currently-selected polygonal object
def getPolyData():
    
    # Accessing Object Recently selected Objects
    selectedObjects = cmds.ls(selection=True)
    obj = selectedObjects[-1]
    
    vertNum = cmds.polyEvaluate(obj, vertex=True)
    print('Vertex Number: ', vertNum)
    
    edgeNum = cmds.polyEvaluate(obj, edge=True)
    print('Edge Number: ', edgeNum)
    
    faceNum = cmds.polyEvaluate(obj, face=True)
    print('Vertex Number: ', faceNum)

    cmds.select(obj+'.vtx[0]', replace=True)
    cmds.select(obj+'.e[0]', replace=True)
    cmds.select(obj+'.f[0]', replace=True)

#    cmds.select(obj + '.vtx[0:4]', replace=True)
#    cmds.select(obj + '.vtx[' + str(startIndex) + ':' + str(endIndex) + ']', replace=True)

    # Accessing Object with objectName
    objectName = "pSphere1"    # pSphere1 == myObject
    startIndex = 0
    endIndex = 4

#    pSphere1.vtx[0:4]
#    cmds.select("{0}.vtx[{1}:{2}]".format(objectName, startIndex, endIndex), replace=True)

getPolyData()