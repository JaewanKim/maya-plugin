import maya.cmds as cmds

def createSimpleSkeleton(joints):
    '''
    Creates a simple skeleton as a single chain of bones
    ARGS:
        joints - the number of bones to create
    '''
    
    cmds.select(clear=True)
    
    bones = []
    pos = [0, 0, 0]
    
    # Locating bones' joint
    for i in range(0, joints):
        pos[1] = i * 5
        bones.append(cmds.joint(p=pos))
        
    # Selecting the root bone
    cmds.select(bones[0], replace=True)


def createHand(fingers, joints):
    '''
    Creates a set of 'fingers', each with a set number of joints
    ARGS:
        fingers - the number of joint chains to create
        joints - the number of bones per finger
    '''
    
    cmds.select(clear=True)
    
    baseJoint = cmds.joint(name='wrist', p=(0, 0, 0))
    
    fingerSpacing = 2
    palmLen = 4
    jointLen = 2
    
    # Creating and Naming Joints
    for i in range(0, fingers):
        cmds.select(baseJoint, replace=True)
        pos = [0, palmLen, 0]
        
        pos[0] = (i * fingerSpacing) - ((fingers - 1) * fingerSpacing)/2
        
        cmds.joint(name='finger{0}base'.format(i+1), p=pos)
        
        for j in range(0, joints):
            cmds.joint(name='finger{0}joint{1}'.format((i+1), (j+1)), relative=True, p=(0, jointLen, 0))
    
    # Selecting the baseJoint, wrist
    cmds.select(baseJoint, replace=True)


createSimpleSkeleton(5)
createHand(5, 3)
