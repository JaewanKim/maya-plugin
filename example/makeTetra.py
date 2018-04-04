import maya.cmds as cmds
import random

def makeTetra(size):
    
    pointA = [0, 0, 0]
    pointB = [size, 0, 0]    
    pointC = [size/2.0, 0, 0]
    
    # set the Z position for C
    pointC[2] = math.sqrt((size*size) - (size/2.0 * size/2.0))
    pointE = [0, 0, 0]
    
    # average the A, B, and C to get E
    # first add all the values
    for i in range(0,3):
        pointE[i] += pointA[i]
        pointE[i] += pointB[i]
        pointE[i] += pointC[i]
    
    # now divide by 3
    for i in range(0,3):
        pointE[i] = pointE[i] / 3.0
        
    # start point D with the X and Z coordinates of point E
    pointD = [0, 0, 0]
    pointD[0] = pointE[0]
    pointD[2] = pointE[2]
    
    distanceAE = math.sqrt((pointE[0] * pointE[0]) + (pointE[2] * pointE[2]))
    
    # set the Y coordinate of point D
    pointD[1] = math.sqrt((size*size) - (distanceAE * distanceAE))
    
    faces = []
    faces.append(cmds.polyCreateFacet(p=[pointA, pointB, pointC], texture=1))
    faces.append(cmds.polyCreateFacet(p=[pointA, pointD, pointB], texture=1))
    faces.append(cmds.polyCreateFacet(p=[pointB, pointD, pointC], texture=1))
    faces.append(cmds.polyCreateFacet(p=[pointC, pointD, pointA], texture=1))

    cmds.select(faces[0], replace=True)
    for i in range(1, len(faces)):
        cmds.select(faces[i], add=True)

    obj = cmds.polyUnite()
    
    cmds.select(obj[0] + ".vtx[:]")
    cmds.polyMergeVertex(distance=0.0001)
    
    cmds.select(obj[0])
    
    cmds.move(-pointE[0], 0, -pointE[2])
    cmds.xform(pivots=(pointE[0], 0, pointE[2]))
    cmds.makeIdentity(apply=True)
    cmds.delete(ch=True)
    
makeTetra(5)