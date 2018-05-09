import maya.cmds as cmds

def createNodes():
    
    # Creating the Nodes
    shaderNode = cmds.shadingNode('blinn', asShader=True)
    rampTexture = cmds.shadingNode('ramp', asTexture=True)
    samplerNode = cmds.shadingNode('samplerInfo', asUtility=True)
    
    # Setting their Attributes
    cmds.setAttr(rampTexture + '.interpolation', 0)
    cmds.setAttr(rampTexture + '.colorEntryList[0].position', 0)
    cmds.setAttr(rampTexture + '.colorEntryList[1].position', 0.45)
    cmds.setAttr(rampTexture + '.colorEntryList[0].color', 0, 0, 0, type="float3")
    cmds.setAttr(rampTexture + '.colorEntryList[1].color', 1, 0, 0, type="float3")
    
    # Connecting them
    cmds.connectAttr(samplerNode + '.facingRatio', rampTexture + '.vCoord')
    cmds.connectAttr(rampTexture + '.outColor', shaderNode + '.color')

createNodes()
