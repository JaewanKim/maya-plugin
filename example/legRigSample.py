'''
    setup IK Rig
    # You should subordinate locators to joints!
'''

import maya.cmds as cmds

def showUI():
    myWin = cmds.window(title="IK Rig", widthHeight=(200, 200))
    cmds.columnLayout()
    cmds.button(label="1. Make Locators", command=makeLocators, width=200)
    cmds.button(label="2. Setup IK", command=setupIK, width=200)
    
    cmds.showWindow(myWin)

def makeLocators(args):
    global hipLoc
    global kneeLoc
    global ankleLoc
    global footLoc

    # Create Locators    
    hipLoc = cmds.spaceLocator(name="HipLoc")
    kneeLoc = cmds.spaceLocator(name="KneeLoc")
    ankleLoc = cmds.spaceLocator(name="AnkleLoc")
    footLoc = cmds.spaceLocator(name="FootLoc")
    
    # Position the Locators
    cmds.xform(hipLoc, absolute=True, translation=(0, 10, 0))
    cmds.xform(kneeLoc, absolute=True, translation=(0, 5, 0))
    cmds.xform(footLoc, absolute=True, translation=(2, 0, 0))

def setupIK(args):
    global hipLoc
    global kneeLoc
    global ankleLoc
    global footLoc
    
    cmds.select(clear=True)
    
    # Position the joints along the Locators
    pos = cmds.xform(hipLoc, query=True, translation=True, worldSpace=True)
    hipJoint = cmds.joint(position=pos)
    
    pos = cmds.xform(kneeLoc, query=True, translation=True, worldSpace=True)
    kneeJoint = cmds.joint(position=pos)
    
    pos = cmds.xform(ankleLoc, query=True, translation=True, worldSpace=True)
    ankleJoint = cmds.joint(position=pos)
    
    pos = cmds.xform(footLoc, query=True, translation=True, worldSpace=True)
    footJoint = cmds.joint(position=pos)
    
    cmds.ikHandle(startJoint=hipJoint, endEffector=ankleJoint)

showUI()

