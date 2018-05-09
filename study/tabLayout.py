import maya.cmds as cmds

class TabExample:

    def __init__(self):
        self.win = cmds.window(title="Tabbed Layout", widthHeight=(300, 300))
        
        self.tabs = cmds.tabLayout()
        
        # add first tab
        firstTab = cmds.columnLayout()
        cmds.tabLayout(self.tabs, edit=True, tabLabel=[firstTab, 'Simple Tab'])
        cmds.button(label="Button")
        cmds.setParent("..")
        
        # add second tab & setup scrolling
        newLayout = cmds.scrollLayout()
        cmds.tabLayout(self.tabs, edit=True, tabLabel=[newLayout, 'Scrolling Tab'])
        cmds.columnLayout()

        for i in range(20):
            cmds.button(label="Button " + str(i+1))

        cmds.setParent("..")
        cmds.setParent("..")
        
        cmds.showWindow(self.win)

        currTab = cmds.tabLayout(self.tabs, query=True, selectTabIndex=True)
        cmds.tabLayout(self.tabs, edit=True, selectTabIndex=2)
        
TabExample()