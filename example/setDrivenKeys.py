import maya.cmds as cmds

def setDrivenKeys():
    '''
        Set driven key on rotateZ to all children bones of selected Joint
        Please select only one root joint. (If you select more, it can cause unexpected situation)
    '''
    
    # Grab the current selected object
    objs = cmds.ls(selection=True)    # Two root bones are on objs
    baseJoint = objs[0]    # First selected Root Joint
                           # objs[-1] : Last selected Root Joint
    
    driver = baseJoint + ".rotateZ"
    
    children = cmds.listRelatives(children=True, allDescendents=True)    # allDescendents=True : All of the list of children
                                                                         # All children selected, even if not linked each other
    
    # Go round all of children bones
    for bone in children:
        # Set driven to attribute, bone.rotateZ
        driven = bone + ".rotateZ"
        
        # Set minimum value 
        cmds.setAttr(driver, 0)
        cmds.setDrivenKeyframe(driven, cd=driver, value=0, driverValue=0)
        
        # Set maximum value 
        cmds.setAttr(driver, 30)
        cmds.setDrivenKeyframe(driven, cd=driver, value=30, driverValue=30)
        
    cmds.setAttr(driver, 0)
