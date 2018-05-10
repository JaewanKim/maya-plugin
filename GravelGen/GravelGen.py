import maya.cmds as cmds
import random

class GravelGenerator():
    '''
        Description : Generate gravels randomly on grid or selected polygon map
        Things to do
            1. gravels on hill
            2. gravels shape
    ''' 
    
    def __init__(self):
        
        self.amount = 0
        self.amount_str = ''
        self.amount_idx = 0
        
        self.global_size = 0
        self.global_size_str = ''
        
        self.max_size = 0.0
        self.max_size_str = ''
        
        self.min_size = 0.0
        self.min_size_str = ''
        
        self.selectedObjs = []
        self.obj = ''
        
        self.randVerts = []
        self.numVerts = 0
        self.vertex_str_list = []
        self.normal = [0, 0, 0]
        
        self.randVerts_pos = 0
        self.randVerts_pos_list = []
        
        # Window
        if (cmds.window("gravel generator", exists=True)):
            cmds.deleteUI("gravel generator", window=True)
        
        self.win = cmds.window("gravel generator", title="Gravel Generator", sizeable=False, resizeToFitChildren=True, menuBar=True)
        
        # Menu Bar
        fileMenu = cmds.menu(label="Edit")
        saveOption = cmds.menuItem(label="Save Settings", enable=False)
        resetOption = cmds.menuItem(label="Reset Settings", command=self.reset)
        
        helpMenu = cmds.menu(label="Help")
        helpOption = cmds.menuItem(label="Help on Gravel Generator", command=self.showHelp)
        cmds.setParent("..")
        
        # Slider Group
        cmds.columnLayout(h=200)
        cmds.separator(h=5, style='single', hr=True)
        
        self.amount_str = cmds.intSliderGrp(l="Amount:", min=1, max=100, value=1, field=True)
        self.global_size_str = cmds.floatSliderGrp(l="Global Size:", min=1.0, max=2.0, value=1.0, field=True)
        self.max_size_str = cmds.floatSliderGrp(l="Max Size:", min=1.5, max=2.0, value=1.5, field=True)
        self.min_size_str = cmds.floatSliderGrp(l="Min Size:", min=1.0, max=1.5, value=1.0, field=True)
        cmds.setParent("..")
        
        cmds.columnLayout(h=40)
        cmds.separator(h=5, style='single', hr=True)
        cmds.setParent("..")
        
        # Button Layout
        cmds.rowColumnLayout(numberOfColumns=7, columnWidth=[(1,5),(2,164),(3,4),(4,164),(5,4),(6,164),(7,5)])
        cmds.separator(h=10, style='none')
        cmds.button(label="Apply and Close", h=27, command=self.get_values_close)
        cmds.separator(h=10, style='none')
        cmds.button(label="Apply", h=27, command=self.get_values)
        cmds.separator(h=10, style='none')
        cmds.button(label="Close", h=27, command=self.close)
        cmds.separator(h=10, style='none')
        cmds.setParent("..")
        
        cmds.showWindow(self.win)
        
        
    def get_values_close(self, args):
        # Get values of UI Component and Close the window
        
        self.amount = cmds.intSliderGrp(self.amount_str, query=True, value=True)
        self.global_size = cmds.floatSliderGrp(self.global_size_str, query=True, value=True)
        self.max_size = cmds.floatSliderGrp(self.max_size_str, query=True, value=True)
        self.min_size = cmds.floatSliderGrp(self.min_size_str, query=True, value=True)
        
        self.recognize_map(self)
        self.close(self)
        
        
    def get_values(self, args):
        # Get values of UI Component
        
        self.amount = cmds.intSliderGrp(self.amount_str, query=True, value=True)
        self.global_size = cmds.floatSliderGrp(self.global_size_str, query=True, value=True)
        self.max_size = cmds.floatSliderGrp(self.max_size_str, query=True, value=True)
        self.min_size = cmds.floatSliderGrp(self.min_size_str, query=True, value=True)
        
        self.recognize_map(self)
        
        
    def recognize_map(self, args):
        # Recognize the selected object as a map
        
        self.selectedObjs = cmds.ls(selection=True)
        
        # Exception when not selecting polygon
        for i in range(0, len(self.selectedObjs)):
            
            self.obj = self.selectedObjs[i]
            
            shapeNode = cmds.listRelatives(self.obj, shapes=True)
            nodeType = cmds.nodeType(shapeNode)
            
            if (nodeType != "mesh"):
                cmds.error('Please select polygon or nothing!')
        
        # Recognize map
        if (len(self.selectedObjs) == 0):
            self.scatter_grid(self)
        
        else:
            self.scatter_map(self)
        
        
    def get_gravel(self, args):
        # Generate gravels by script
        
        # Create nurbs sphere and Add noise for nurbsSurface
        gravel = cmds.sphere(axis=self.normal, r=1, n="randGravel#")[0]

        shapeNode = cmds.listRelatives(gravel, shapes=True)
        
        degU = cmds.getAttr('randGravel' + str(self.amount_idx+1) + '.degreeU')
        spansU = cmds.getAttr('randGravel' + str(self.amount_idx+1) + '.spansU')
        cvsU = degU + spansU
        
        degV = cmds.getAttr('randGravel' + str(self.amount_idx+1) + '.degreeV')
        spansV = cmds.getAttr('randGravel' + str(self.amount_idx+1) + '.spansV')
        cvsV = degV + spansV
        
        noiseAmt = 0.05
        randAmt = [0, 0, 0]
        
        for i in range(1, cvsU-1):
            
            for j in range(0, cvsV):
                
                for k in range(0, 3):
                    randAmt[k] = random.random() * (noiseAmt*2) - noiseAmt
                
                vertexStr = "{0}.cv[{1}][{2}]".format('randGravel'+str(self.amount_idx+1), i, j)
                
                cmds.select(vertexStr, replace=True)
                cmds.move(randAmt[0], randAmt[1], randAmt[2], relative=True)
        
        cmds.select(gravel, replace=True)
        return gravel
        
        
    def scatter_grid(self, args):
        # Scatter gravels on grid
        
        gravelGrp = cmds.group(empty=True, name="Gravel_Grp#")
        
        for self.amount_idx in range(0, self.amount):
        
            x = random.uniform(-10.0, 10.0)
            z = random.uniform(-10.0, 10.0)
            
            randomsize = random.uniform(self.min_size, self.max_size)*self.global_size
            
            gravel = self.get_gravel(self)
            temp = random.uniform(0.2,0.5)
            
            cmds.scale(random.uniform(0.6,1.0)*randomsize, temp*randomsize, randomsize, gravel)
            cmds.move(x, temp*randomsize/2, z, gravel)
            cmds.move(x, 0, z, ".scalePivot", ".rotatePivot", absolute=True)
            cmds.rotate(0, random.uniform(-45.0, 45.0), 0, gravel)
            cmds.parent(gravel, gravelGrp)
        
        cmds.select(gravelGrp, replace=True)
        
        
    def scatter_map(self, args):
        # Scatter gravels on map
        
        self.selectedObjs = cmds.ls(selection=True)
         
        # Loop all maps
        for n in range(0, len(self.selectedObjs)):
            
            self.obj = self.selectedObjs[n]
            
            shapeNode = cmds.listRelatives(self.obj, shapes=True)
            nodeType = cmds.nodeType(shapeNode)
            
            # Initialize vertex variables
            self.randVerts = []
            self.numVerts = cmds.polyEvaluate(self.obj, vertex=True)
            self.vertex_str_list = []
            self.amount_idx = 0
            
            # Select vertex randomly as many as amount and Save it to ranVerts list
            for i in range(0, self.amount):
                self.randVerts.append(random.randint(0, self.numVerts))
            
            # Combine the vertex of selected object to string
            for k in self.randVerts:
                self.vertex_str_list.append("{0}.vtx[{1}]".format(self.obj, k))
            
            # Make group for gravels and Move group position to selected map
            gravelGrp = cmds.group(empty=True, name="Gravel_Grp#")
            obj_pos = cmds.xform(self.obj, q=True, ws=True, t=True)
            cmds.move(obj_pos[0], obj_pos[1], obj_pos[2], gravelGrp)
            
            # Save position of the vertex selected randomly
            vertPos = [0, 0, 0]
            for r in self.vertex_str_list:
                
                self.randVerts_pos = cmds.xform(r, q=True, ws=True, t=True)
                
                for j in range(0, 3):
                    vertPos[j] = self.randVerts_pos[j]
                
                # Get the normal vector on selected vertex
                self.normal = cmds.polyNormalPerVertex(r, query=True, xyz=True)[:3]
                
                # Create and Arrange the gravels.
                randomsize = random.uniform(self.min_size, self.max_size)*self.global_size
                
                gravel = self.get_gravel(self)
                temp = random.uniform(0.2,0.5)
                cmds.scale(random.uniform(0.6,1.0)*randomsize, temp*randomsize, randomsize, gravel)
                cmds.move(vertPos[0], vertPos[1]+temp*randomsize/2, vertPos[2], gravel)
                cmds.move(vertPos[0], vertPos[1], vertPos[2], ".scalePivot", ".rotatePivot", absolute=True)
                cmds.rotate(0, random.uniform(-45.0, 45.0), 0, gravel)
                cmds.parent(gravel, gravelGrp)
                self.amount_idx += 1
            
            cmds.select(gravelGrp, replace=True)
        
        
    def reset(self, args):
        # Reset the values by default
        
        cmds.intSliderGrp(self.amount_str, edit=True, value=True)
        cmds.floatSliderGrp(self.global_size_str, edit=True, value=True)
        cmds.floatSliderGrp(self.max_size_str, edit=True, value=True)
        cmds.floatSliderGrp(self.min_size_str, edit=True, value=True)
        
        
    def showHelp(self, args):
        cmds.showHelp("https://github.com/JaewanKim/maya-plugin", absolute=True)
        
        
    def close(self, args):
        # Close the window
        if cmds.window(self.win, exists=True): 
            cmds.deleteUI(self.win, window=True)


GravelGenerator()