import maya.cmds as cmds

def keepCentered():
    '''
        Move the last selected object on the weight center(xz-axis) & Connect the attribute translate XZ
    '''
    
    objects = cmds.ls(selection=True)
    
    if (len(objects) < 3):
        cmds.error('Please select at least three objects')

    avgNode = cmds.shadingNode('plusMinusAverage', asUtility=True)
    cmds.setAttr(avgNode + '.operation', 3)
    
    for i in range(0, len(objects) - 1):
        cmds.connectAttr(objects[i] + '.translateX', avgNode + '.input3D[{0}].input3Dx'.format(i))
#        cmds.connectAttr(objects[i] + '.translateY', avgNode + '.input3D[{0}].input3Dy'.format(i))
        cmds.connectAttr(objects[i] + '.translateZ', avgNode + '.input3D[{0}].input3Dz'.format(i))
    
    controlledObjIndex = len(objects) - 1
    
    cmds.connectAttr(avgNode + '.output3D.output3Dx', objects[controlledObjIndex] + '.translateX')
#    cmds.connectAttr(avgNode + '.output3D.output3Dy', objects[controlledObjIndex] + '.translateY')
    cmds.connectAttr(avgNode + '.output3D.output3Dz', objects[controlledObjIndex] + '.translateZ')

keepCentered()
