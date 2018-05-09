import maya.cmds as cmds

def getNURBSInfo():
    
    # Accessing Object Recently selected Objects
    selectedObjects = cmds.ls(selection=True)
    obj = selectedObjects[-1]
    
    degU = cmds.getAttr(obj + '.degreeU')
    spansU = cmds.getAttr(obj + '.spansU')
    cvsU = degU + spansU
    print('CVs (U): ', cvsU)

    degV = cmds.getAttr(obj + '.degreeV')
    spansV = cmds.getAttr(obj + '.spansV')
    cvsV = degV + spansV
    print('CVs (V): ', cvsV)

    cmds.select(obj + '.cv[0][0]')    # Selecting first CV
#    cmds.select(obj + '.cv[' + str(cvsU-1) + '][' + str(cvsV-1) + ']', add=True)    # Selecting last CV

    # Accessing object with objectName
#    cmds.select('nurbsSphere1.cv[0][0]')

#    objectName = "nurbsSphere1"
#    cmds.select("{0}.cv[{1}][{2}]".format(objectName, (cvsU-1), (cvsV-1), add=True)

getNURBSInfo()