'''
    Copy animation from one object to anothers
    First selected object - for copy
    Others - for paste
'''

import maya.cmds as cmds

def getAttrName(fullname):    # get the full name (ex. |group1|obj.translateX)
    parts = fullname.split('.')
    return parts[-1]          # return only attribute name after the (ex. translateX)
    

def copyKeyframes():
    objs = cmds.ls(selection=True)
    
    if(len(objs) < 2):
        cmds.error("Please select at least two Objects")
    
    sourceObj = objs[0]    # First selected object is for copy
    
    # Find animated attributes and put on a list
    animAttributes = cmds.listAnimatable(sourceObj)
    
    # Go round the list
    for attribute in animAttributes:
        # Get the key frame numbers of animated attributes
        numKeyframes = cmds.keyframe(attribute, query=True, keyframeCount=True)

        if (numKeyframes > 0):
            # Copy keyframes where animated attribute is existed
            cmds.copyKey(attribute)    # Hold keyframes temporarily in memory
                                       # No additional flag, grabbing all keyframes for the specified attribute

            # Paste keyframes to other objects
            for obj in objs[1:]:
                cmds.pasteKey(obj, attribute=getAttrName(attribute), option="replace")

copyKeyframes()
