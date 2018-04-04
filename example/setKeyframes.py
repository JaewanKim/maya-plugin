'''
    Set keyframes of the first selected object like bouncing ball
'''

import maya.cmds as cmds

def setKeyframes():
    objs = cmds.ls(selection=True)
    obj = objs[0]
    
    xVal = 0
    yVal = 0
    frame = 0
    
    maxVal = 10
    
    tangentType = "auto"
    
    for i in range(0, 20):
        frame = i * 10
        xVal = i * 2
        
        if i % 2 == 1:
            yVal = 0
            tangentType = "linear"
        else:
            yVal = maxVal
            tangentType = "spline"
            maxVal *= 0.8
        
        cmds.setKeyframe(obj + '.translateY', value=yVal, time=frame, inTangentType=tangentType, outTangentType=tangentType)
        cmds.setKeyframe(obj + '.translateX', value=xVal, time=frame)

setKeyframes()
