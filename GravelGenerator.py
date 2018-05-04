import maya.cmds as cmds
import random

class GravelGenerator():
    '''
        Description : Generate gravels randomly on selected object
        Things to do
            1. Add funtion : get_gravel_script, reset
            2. layout
            3. refactoring
    ''' 
    
    def __init__(self):
        
        self.radio = 0
        self.radio_str = ''
        
        self.amount = 0
        self.amount_str = ''
        
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
        self.normal = []

        self.randVerts_pos = 0
        self.randVerts_pos_list = []

        # Window
        if (cmds.window("gravel generator", exists=True)):
            cmds.deleteUI("gravel generator")
        
        self.win = cmds.window("gravel generator", title="Gravel Generator", widthHeight=(500, 300))
        
        cmds.columnLayout(adjustableColumn=True)

        self.amount_str = cmds.intSliderGrp(l="Amount", min=1, max=100, field=True)
        self.global_size_str = cmds.floatSliderGrp(l="Global Size", min=1, max=3, field=True)
        self.max_size_str = cmds.floatSliderGrp(l="Max Size", min=1.0, max=3.0, field=True)
        self.min_size_str = cmds.floatSliderGrp(l="Min Size", min=0.1, max=1.0, field=True)
        
        cmds.button(label="Generate Gravels", command=self.get_values)
        cmds.button(label="Reset", )
        cmds.button(label="Test for scatter on grid", command=self.scatter_gravel_grid)
        cmds.button(label="Test for scatter on map", command=self.scatter_gravel_map)
        cmds.button(label="Test to get gravel script", command=self.get_gravel_script)
        
        cmds.setParent("..")
        cmds.showWindow(self.win)
        
        
    def get_values(self, args):
        # Get values of UI Component
        
        self.radio = cmds.radioButtonGrp(self.radio_str, query=True, select=True)
        
        self.amount = cmds.intSliderGrp(self.amount_str, query=True, value=True)
        self.global_size = cmds.floatSliderGrp(self.global_size_str, query=True, value=True)
        self.max_size = cmds.floatSliderGrp(self.max_size_str, query=True, value=True)
        self.min_size = cmds.floatSliderGrp(self.min_size_str, query=True, value=True)
        
        if (self.max_size < self.min_size):
            error("Please input min_size lower than max_size")
        
        if (self.radio == 1):    # File
            self.get_gravel_file(self)
        
        elif (self.radio == 2):  # Script
            self.get_gravel_script(self)
        
        
    def get_gravel_script(self, args):
        # Generate gravels by script
        print("get_gravel_script")
        
        self.amount = cmds.intSliderGrp(self.amount_str, query=True, value=True)
        self.global_size = cmds.floatSliderGrp(self.global_size_str, query=True, value=True)
        self.max_size = cmds.floatSliderGrp(self.max_size_str, query=True, value=True)
        self.min_size = cmds.floatSliderGrp(self.min_size_str, query=True, value=True)
        
        gravelGrp = cmds.group(empty=True, name="Gravel_Grp")
        
        for amount in range(0, self.amount):
            
            # Create nurbs sphere
            mysphere = cmds.sphere(r=1, n="randGravel#")
            cmds.scale(random.uniform(0.6,1.0), random.uniform(0.2,0.5), 1, mysphere)
            
            # Add noise for nurbsSurface
            shapeNode = cmds.listRelatives(mysphere, shapes=True)
            
            degU = cmds.getAttr('randGravel' + str(amount+1) + '.degreeU')
            spansU = cmds.getAttr('randGravel' + str(amount+1) + '.spansU')
            cvsU = degU + spansU
            
            degV = cmds.getAttr('randGravel' + str(amount+1) + '.degreeV')
            spansV = cmds.getAttr('randGravel' + str(amount+1) + '.spansV')
            cvsV = degV + spansV
            
            noiseAmt = 0.1
            randAmt = [0, 0, 0]
            
            for i in range(1, cvsU-1):
                
                for j in range(0, cvsV):
                    
                    for k in range(0, 3):
                        randAmt[k] = random.random() * (noiseAmt*2) - noiseAmt
                    
                    vertexStr = "{0}.cv[{1}][{2}]".format('randGravel'+str(amount+1), i, j)

                    cmds.select(vertexStr, replace=True)
                    cmds.move(randAmt[0], randAmt[1], randAmt[2], relative=True)
        
        cmds.select(gravelGrp, replace=True)        # finish up
        
        
    def recognize_map(self, args):
        # Recognize the selected object as a map
        print("recognize_map")
        
        self.selectedObjs = cmds.ls(selection=True)
        
        # Is it necessary exception for len(self.selectedObjs) negative ? Idon't think so..
        if (len(self.selectedObjs) == 0):
            self.scatter_gravel_grid(self)
        
        else:    # len(self.selectedObjs) > 0
            self.scatter_gravel_map(self)
        
        
    def scatter_gravel_grid(self, args):
        # Scatter gravels on grid
        
        self.amount = cmds.intSliderGrp(self.amount_str, query=True, value=True)    # Will be deleted
        self.global_size = cmds.floatSliderGrp(self.global_size_str, query=True, value=True)    # Will be deleted
        self.max_size = cmds.floatSliderGrp(self.max_size_str, query=True, value=True)
        self.min_size = cmds.floatSliderGrp(self.min_size_str, query=True, value=True)
        
        if (self.max_size < self.min_size):
            cmds.error("Please input min_size lower than max_size")
        
        gravelGrp = cmds.group(empty=True, name="Gravel_Grp")
        
        for i in range(0, self.amount):    # for obj in objlist: from get_gravel_~
        
            x = random.uniform(-10.0, 10.0)
            z = random.uniform(-10.0, 10.0)
            
            randomsize = random.uniform(self.min_size, self.max_size)*self.global_size
            
            mycube = cmds.polyCube(h=1, w=1, d=1, n="randPolyCube#")
            cmds.scale(randomsize, randomsize, randomsize, mycube)
            cmds.move(x, randomsize/2, z, mycube)    # obj in 
            cmds.move(x, 0, z, ".scalePivot", ".rotatePivot", absolute=True)
            cmds.rotate(0, random.uniform(-45.0, 45.0), 0, mycube)
            cmds.parent(mycube, gravelGrp)
            
        cmds.select(gravelGrp, replace=True)
        
        
    def scatter_gravel_map(self, args):
        # Scatter gravels on map
        print("scatter_gravel_map")

        self.amount = cmds.intSliderGrp(self.amount_str, query=True, value=True)    # Will be deleted
        self.global_size = cmds.floatSliderGrp(self.global_size_str, query=True, value=True)    # Will be deleted
        self.max_size = cmds.floatSliderGrp(self.max_size_str, query=True, value=True)
        self.min_size = cmds.floatSliderGrp(self.min_size_str, query=True, value=True)
        
        self.selectedObjs = cmds.ls(selection=True)
        
        # Exception when not selecting polygon
        for i in range(0, len(self.selectedObjs)):
            
            self.obj = self.selectedObjs[i]
            
            shapeNode = cmds.listRelatives(self.obj, shapes=True)
            nodeType = cmds.nodeType(shapeNode)
            
            if (nodeType != "mesh"):
                cmds.error('Please select polygon!')
        
        # Loop all maps
        for n in range(0, len(self.selectedObjs)):
            
            print("selectedObjs[", n, "]")
            print(self.obj)
            
            self.obj = self.selectedObjs[n]
            
            shapeNode = cmds.listRelatives(self.obj, shapes=True)
            nodeType = cmds.nodeType(shapeNode)
            
            # Initialize what 
            self.randVerts = []
            self.numVerts = cmds.polyEvaluate(self.obj, vertex=True)
            self.vertex_str_list = []
            
            # Select vertex randomly as many as amount and Save it to ranVerts list
            for j in range(0, self.amount):
                self.randVerts.append(random.randint(0, self.numVerts))
            
            # Combine the vertex of selected object to string
            for k in self.randVerts:
                self.vertex_str_list.append("{0}.vtx[{1}]".format(self.obj, k))
            
            # Save position of the vertex selected randomly
            vertPos = [0, 0, 0]
            gravelGrp = cmds.group(empty=True, name="Gravel_Grp#")

            for r in self.vertex_str_list:

                self.randVerts_pos = cmds.xform(r, q=True, ws=True, t=True)

                for j in range(0, 3):
                    vertPos[j] = self.randVerts_pos[j]
                
                # Get the normal vector on selected vertex
                self.normal = cmds.polyNormalPerVertex(r, query=True, xyz=True)[:3]
                
                # Create and Arrange the temporary cube.  # It will be changed to gravel
                randomsize = random.uniform(self.min_size, self.max_size)*self.global_size
                
                mycube = cmds.polyCube(axis=self.normal, h=1, w=1, d=1, n="randPolyCube#")
                cmds.scale(randomsize, randomsize, randomsize, mycube)
                cmds.move(vertPos[0], vertPos[1]+randomsize/2, vertPos[2], mycube)    # obj in 
                cmds.move(vertPos[0], vertPos[1], vertPos[2], ".scalePivot", ".rotatePivot", absolute=True)
                cmds.rotate(0, random.uniform(-45.0, 45.0), 0, mycube)

                cmds.parent(mycube, gravelGrp)
            
            cmds.select(gravelGrp, replace=True)
    
    
    def reset(self, args):
        # Reset the values set by a user
        print("reset")


GravelGenerator()