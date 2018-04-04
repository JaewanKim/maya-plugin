import maya.cmds as cmds
import maya.mel as mel

def runMEL():
	print("Running MEL from Python")
	mel.eval("source myMELScript;")
	mel.eval("myMELScript;")

runMEL()