import maya.cmds as cmds
import math

def makeFace():
    # Setting the Location of four points
    newFace = cmds.polyCreateFacet(p=[(-1,-1,0), (1,-1,0), (1,1,0), (-1,1,0), (-1,-1,0)])

def makeFaceWithHole():
    points = []
    
    # Create the initial square
    points.append((-5, -5, 0))
    points.append((5, -5, 0))
    points.append((5, 5, 0))
    points.append((-5, 5, 0))

    # Add empty point to start a hole
    points.append(())
    
    for i in range(32):
        theta = (math.pi * 2) / 32 * i
        x = math.cos(theta)
        y = math.sin(theta)
        points.append((2*x, 2*y, 0))
        
    newFace = cmds.polyCreateFacet(p=points)
    cmds.polyTriangulate()
    cmds.polyQuad()        # Generally doesn't hurt anything

def makePolyNormal():
    cmds.polyNormal(normalMode=4)

makeFace()
makeFaceWithHole()