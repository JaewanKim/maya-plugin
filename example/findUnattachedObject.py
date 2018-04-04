import maya.cmds as cmds

def shadersFromObject(obj):
    cmds.select(obj, replace=True)
    cmds.hyperShade(obj, shaderNetworkSelectMaterialNode=True)
    shaders = cmds.ls(selection=True)
    return shaders

def isGeometry(obj):
    
    shapes = cmds.listRelatives(obj, shapes=True)
    shapeType = cmds.nodeType(shapes[0])
    geometryTypes = ['mesh', 'nurbsSurface', 'subdiv']
    
    if shapeType in geometryTypes:
        return True
    
    return False

def findUnattachedObjects():
    
    # Getting a list of all the obj in the scene
    objects = cmds.ls(type="transform")

    unShaded = []
   
    # Running through the list and  Checking whether a given node is geometry
    for i in range(0, len(objects)):
        # For geometric node, find the shaders applied to it
        if (isGeometry(objects)):
            shaders = shadersFromObject(objects[i])

            # Adding Non-shaded objects to non-shaded obj list
            if (len(shaders) < 1):
                unShaded.append(objects[i])

    # Create a new shader & Apply it to the shader-less obj
    newShader = cmds.shadingNode('blinn', asShader=True)
    cmds.setAttr(newShader + '.color', 0, 1, 1, type="double3")
    
    cmds.select(unShaded, replace=True)
    cmds.hyperShade(assign=newShader)
    
findUnattachedObjects()
