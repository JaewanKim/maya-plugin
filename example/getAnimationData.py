import maya.cmds as cmds

def getAnimationData():
    '''
        Get Animation Data about selected object
    '''

    # Grab first selected object
    objs = cmds.ls(selection=True)
    obj = objs[0]
    
    # Get the Animation Data on List
    animAttributes = cmds.listAnimatable(obj)
    
    # Go round the list
    for attribute in animAttributes:
        
        # Count the Keyframes
        numKeyframes = cmds.keyframe(attribute, query=True, time=(1,100), keyframeCount=True)
        
        if (numKeyframes > 0):    # Could Key frames be negative?
            print("---------------------------")
            print("Found ", numKeyframes, " keyframes on ", attribute)
            
            times = cmds.keyframe(attribute, query=True, index=(0,numKeyframes), timeChange=True)
            values = cmds.keyframe(attribute, query=True, index=(0,numKeyframes), valueChange=True)
            
            print("frame#, time, value")
            for i in range(0, numKeyframes):
                print(i, times[i], values[i])
            
            print("---------------------------")

getAnimationData()
