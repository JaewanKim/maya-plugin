import maya.cmds as cmds

print("Imported the script!")

def makeCube():
	cmds.polyCube()
	print("Make a cube!")

def makeObject():
	cmds.polySphere()
	print("Make a sphere!")
