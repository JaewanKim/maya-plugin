import maya.cmds as cmds

def startCtx():
    print("starting context")

def finalizeCtx():
    objs = cmds.ls(selection=True)
    
    numObjs = len(objs)
    xpos = 0
    ypos = 0
    zpos = 0
    
    for o in objs:
        # print(o)
        pos = cmds.xform(o, query=True, worldSpace=True, translation=True)
        # print(pos)
        xpos += pos[0]
        ypos += pos[1]
        zpos += pos[2]
    
    xpos /= numObjs
    ypos /= numObjs
    zpos /= numObjs
    
    newLoc = cmds.spaceLocator()
    cmds.move(xpos, ypos, zpos, newLoc)

def createContext():
    toolStartStr = 'python("customCtx.startCtx()");'
    toolFinishStr = 'python("customCtx.finalizeCtx");'
    
    newCtx = cmds.scriptCtx(i1='myTool.png', title='MyTool', setNoSelectionPrompt='Select at least two objects', toolStart=toolStartStr, finalCommandScript=toolFinishStr, totalSelectionSets=1, setSelectionCount=2, setAllowExcessCount=True, setAutoComplete=False, toolCursorType="create")
    
    cmds.setToolTo(newCtx)

createContext()

