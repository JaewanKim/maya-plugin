import maya.cmds as cmds
import math

def makeSquare():    
    # Setting the Location of four points
    square = cmds.curve(degree=1, p=[(-0.5,-0.5,0), (0.5,-0.5,0), (0.5,0.5,0), (-0.5,0.5,0), (-0.5,-0.5,0)])
    
def curveFunction(i):
    
    x = math.sin(i)
    y = math.cos(i)
    
    x = math.pow(x, 3)
    y = math.pow(y, 3)
    
    return (x,y)

def complexCurve():
    theCurve = cmds.curve(degree=3, p=[0,0,0])
    
    for i in range(0, 32):
        val = (math.pi * 2)/32 * i
        newPoint = curveFunction(val)
        cmds.curve(theCurve, append=True, p=[(newPoint[0], newPoint[1], 0)])

makeSquare()
complexCurve()
