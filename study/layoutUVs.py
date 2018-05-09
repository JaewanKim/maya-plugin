import maya.cmds as cmds

def layoutUVs():
    
    selected = cmds.ls(selection=True)
    obj = selected[0]
    
    totalFaces = cmds.polyEvaluate(obj, face=True)
    
    oneThird = totalFaces/3
    
    startFace = 0
    endFace = oneThird - 1
    cmds.polyProjection(obj + '.f[' + str(startFace) + ':' + str(endFace) + ']', type="planar")
    
    startFace = oneThird
    endFace = (oneThird * 2) - 1
    cmds.polyProjection(obj + '.f[' + str(startFace) + ':' + str(endFace) + ']', type="cylindrical")
    
    startFace = (oneThird * 2)
    endFace = totalFaces - 1
    cmds.polyProjection(obj + '.f[' + str(startFace) + ':' + str(endFace) + ']', type="spherical")

'''
    # format command just can do on string
    # Refer to https://pyformat.info/
    cmds.select("{0}.f[{1}:{2}]".format(obj, startFace, endFace), replace=True)
    
'''

layoutUVs()