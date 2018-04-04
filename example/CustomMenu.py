import maya.cmds as cmds

class CustomMenu:

    def __init__(self):
        self.win = cmds.window(title="Menu Example", menuBar=True, widthHeight=(300, 200))
        
        # Menu Definition
        fileMenu = cmds.menu(label="File")
        loadOption = cmds.menuItem(label="Load")
        saveOption = cmds.menuItem(label="Save")
        cmds.setParent("..")
        
        objectsMenu = cmds.menu(label="Objects")
        sphereOption = cmds.menuItem(label="Make Sphere", command=self.makeSphere)
        cubeOption = cmds.menuItem(label="Make Cube", command=self.makeCube)
        cmds.setParent("..")

        # Menu Item & Menu Item Option Box        # What's differences from UP & DOWN
        self.menu = cmds.menu(label="OptionBox")
        sphereCommandMI = cmds.menuItem(label="make Sphere", command=self.myCommand)
        sphereCommandMIOption = cmds.menuItem(optionBox=True, command=self.myCommandOptions)    # Please Change the Command correctly

        cmds.columnLayout()
        cmds.text(label="Put the rest of your interface here")
        
        cmds.showWindow(self.win)

    def myCommand(self, *args):
        self.makeSphere(1)
        
    def myCommandOptions(self, *args):
        promptInput = cmds.promptDialog(title="Sphere Radius", message='Specify Radius:', button=['OK', 'CANCEL'], defaultButton='OK', cancelButton='CANCEL', dismissString='CANCEL')
        
        if (promptInput == 'OK'):
            radiusInput = cmds.promptDialog(query=True, text=True)
            self.makeSphere(radiusInput)
        
    def makeSphere(self, sphereRadius):
        cmds.polySphere(radius=sphereRadius)
        
    def makeCube(self, *args):
        cmds.polyCube()


CustomMenu()