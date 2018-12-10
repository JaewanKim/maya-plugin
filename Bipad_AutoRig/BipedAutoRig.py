import maya.cmds as cmds
import math

class BipedAutoRig():
    '''
        Description : Biped_AutoRig.py made by JW
            STEP 1. Create Joints
            STEP 2. Check Joint Orientation
            STEP 3. Create Controllers
            STEP 4. Build
            STEP 5. Import Weight
        
        Doing :
            - Layout
            - Refactoring
        
        Things to do :
            - arm PoleVector causes positional deviation of bone (CHECK ROTATION VALUE)
            - Build (In progress)
                - Head, Jaw, Neck Constrain
                - Root Constrain
                - Set Attributes
                    - Shoulder/Pelvis Rot
                    - Wrist Rot
            - Import Weight (fileDialog2/fileBrowseDialog)
    '''
    
    def __init__(self):
        
        # Window
        if (cmds.window("Biped_AutoRig", exists=True)):
            cmds.deleteUI("Biped_AutoRig", window=True)
        
        self.win = cmds.window("Biped_AutoRig", title="Biped_AutoRig", sizeable=True, resizeToFitChildren=True, menuBar=True)
        
        # Menu Bar
        fileMenu = cmds.menu(label="Edit")
        saveOption = cmds.menuItem(label="Save Settings", enable=False)
        resetOption = cmds.menuItem(label="Reset Settings", enable=False)
        
        helpMenu = cmds.menu(label="Help")
        helpOption = cmds.menuItem(label="Help on JWAutoRig.py", command=self.showHelp)
        cmds.setParent("..")
        
        # Button Group
        cmds.rowColumnLayout()
        cmds.separator(h=5, style='single', hr=True)
        
        cmds.button(label="STEP 1: Create Dummy Joint", command=self.dummy_jnt)
        cmds.text("Please adjust dummy joint")
        cmds.separator(h=15, style='none', hr=True)
        
        cmds.button(label="Check Joint Orientation", command=self.confirm_orient_joint)
        cmds.text("Toggle All Joint")
        cmds.separator(h=15, style='none', hr=True)
        
        cmds.button(label="STEP 2: Fix the Joint", command=self.fix_jnt)
        cmds.text("Generate IK,FK,BIND joint referred to dummy joint")
        cmds.separator(h=15, style='none', hr=True)
        
        cmds.button(label="STEP 3: Create CTRLs", command=self.create_ctrl)
        cmds.text("CTRLs will be created by following JO(YZZ)")
        cmds.text("Please adjust CTRLs in component mode")
        cmds.separator(h=15, style='none', hr=True)
        
        cmds.button(label="STEP 4: Fix the CTRLs", command=self.fix_ctrl)
        cmds.text("Connect Joints and CTRLs")
        cmds.separator(h=15, style='none', hr=True)
        
        cmds.button(label="STEP 5: Bind Skin", command=self.bind)
        cmds.text("Bind")
        cmds.separator(h=15, style='none', hr=True)
        
        cmds.button(label="Import Skin Weight", en=False, command=self.import_weight)
        cmds.text(" ")
        cmds.separator(h=10, style='none', hr=True)
        
        cmds.separator(h=5, style='single', hr=True)
        cmds.setParent("..")
        
        cmds.showWindow(self.win)
    
    
    def dummy_jnt(self, args):
        '''
            STEP 1. Create Dummy Joint
            # Please adjust dummy joint
        '''
        
        cmds.select(clear=True)
        
        # Head Joint
        head_jnt_grp = cmds.group(empty=True, n="head_jnt_grp")
        cmds.move(0, 14.447, -0.066, head_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        
        cmds.joint(a=True, p=[0, 14.447, -0.066], rad=0.6, n='head_001_jnt')
        cmds.joint(a=True, p=[0, 15.963, -0.066], rad=0.6, n='head_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('head_001_jnt', hi=True)
        cmds.joint(e=True, oj='yzx', sao='zup', ch=True, zso=True)
        cmds.select(clear=True)
        
        
        # Jaw Joint
        jaw_jnt_grp = cmds.group(empty=True, n="jaw_jnt_grp")
        cmds.move(0, 14.447, -0.066, jaw_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        
        cmds.joint(a=True, p=[0, 14.447, -0.066], rad=0.6, n='jaw_001_jnt')
        cmds.joint(a=True, p=[0, 14.094, 0.707], rad=0.6, n='jaw_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('jaw_001_jnt', hi=True)
        cmds.joint(e=True, oj='zxy', sao='xup', ch=True, zso=True)
        cmds.select(clear=True)
        
        
        # Neck Joint
        neck_jnt_grp = cmds.group(empty=True, n="neck_jnt_grp")
        cmds.move(0, 13.322, -0.366, neck_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        
        cmds.joint(a=True, p=[0, 13.322, -0.366], rad=0.6, n='neck_001_jnt')
        cmds.joint(a=True, p=[0, 13.91, -0.209], rad=0.6, n='neck_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0, 14.447, -0.066], rad=0.6, n='neck_003_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('neck_001_jnt', hi=True)
        cmds.joint(e=True, oj='yzx', sao='zup', ch=True, zso=True)
        cmds.select(clear=True)
        
        
        # Left Shoulder Joint
        shoulder_jnt_grp = cmds.group(empty=True, n="shoulder_jnt_grp")
        cmds.move(0, 12.965, -0.251, shoulder_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        
        cmds.joint(a=True, p=[0.232, 12.965, -0.251], rad=0.6, n='shoulder_lf_001_jnt')
        cmds.joint(a=True, p=[1.135, 13.093, -0.504], rad=0.6, n='shoulder_lf_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('shoulder_lf_001_jnt', hi=True)
        cmds.joint(e=True, oj='yzx', sao='zup', ch=True, zso=True) #
        cmds.select(clear=True)
        
        
        # Left Arm Joint
        arm_jnt_grp = cmds.group(empty=True, n="arm_jnt_grp")
        cmds.move(0, 13.093, -0.504, arm_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        
        cmds.joint(a=True, p=[1.135, 13.093, -0.504], rad=0.6, n='arm_lf_ik_shoulder_jnt')
        cmds.joint(a=True, p=[2.992, 11.146, -0.809], rad=0.6, n='arm_lf_ik_elbow_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[4.556, 9.612, -0.458], rad=0.6, n='arm_lf_ik_wrist_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.824, 8.343, -0.32], rad=0.6, n='arm_lf_ik_hand_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('arm_lf_ik_shoulder_jnt', hi=True)
        cmds.joint(e=True, oj='yzx', sao='zup', ch=True, zso=True)
        cmds.select(clear=True)
        
        
        # Left Hand Joint
        # Thumb
        hand_jnt_grp = cmds.group(empty=True, n="hand_jnt_grp")
        cmds.move(0, 9.612, -0.458, hand_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        
        cmds.joint(a=True, p=[4.691, 9.483, -0.228], rad=0.1, n='thumb_lf_001_jnt')
        cmds.joint(a=True, p=[4.851, 9.195, 0.036], rad=0.1, n='thumb_lf_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.024, 8.925, 0.138], rad=0.1, n='thumb_lf_003_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.186, 8.694, 0.144], rad=0.1, n='thumb_lf_004_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('thumb_lf_001_jnt', hi=True)
        cmds.joint(e=True, oj='yzx', sao='zup', ch=True, zso=True)
        cmds.select(clear=True)
        
        # Index
        cmds.select(hand_jnt_grp, replace=True)
        cmds.joint(a=True, p=[5.272, 9.168, -0.203], rad=0.1, n='index_lf_001_jnt')
        cmds.joint(a=True, p=[5.548, 8.913, -0.07], rad=0.1, n='index_lf_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.61, 8.694, -0.004], rad=0.1, n='index_lf_003_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.63, 8.49, 0.046], rad=0.1, n='index_lf_004_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('index_lf_001_jnt', hi=True)
        cmds.joint(e=True, oj='yzx', sao='zup', ch=True, zso=True)
        cmds.select(clear=True)
        
        # Middle
        cmds.select(hand_jnt_grp, replace=True)
        cmds.joint(a=True, p=[5.286, 9.176, -0.423], rad=0.1, n='middle_lf_001_jnt')
        cmds.joint(a=True, p=[5.605, 8.834, -0.376], rad=0.1, n='middle_lf_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.678, 8.604, -0.354], rad=0.1, n='middle_lf_003_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.702, 8.373, -0.336], rad=0.1, n='middle_lf_004_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('middle_lf_001_jnt', hi=True)
        cmds.joint(e=True, oj='yzx', sao='zup', ch=True, zso=True)
        cmds.select(clear=True)
        
        # Ring
        cmds.select(hand_jnt_grp, replace=True)
        cmds.joint(a=True, p=[5.206, 9.126, -0.574], rad=0.1, n='ring_lf_001_jnt')
        cmds.joint(a=True, p=[5.501, 8.846, -0.639], rad=0.1, n='ring_lf_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.508, 8.61, -0.619], rad=0.1, n='ring_lf_003_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.477, 8.378, -0.586], rad=0.1, n='ring_lf_004_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('ring_lf_001_jnt', hi=True)
        cmds.joint(e=True, oj='yzx', sao='zup', ch=True, zso=True)
        cmds.select(clear=True)
        
        # Pinky
        cmds.select(hand_jnt_grp, replace=True)
        cmds.joint(a=True, p=[5.069, 9.116, -0.734], rad=0.1, n='pinky_lf_001_jnt')
        cmds.joint(a=True, p=[5.209, 8.834, -0.826], rad=0.1, n='pinky_lf_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.233, 8.673, -0.842], rad=0.1, n='pinky_lf_003_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.236, 8.465, -0.843], rad=0.1, n='pinky_lf_004_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('pinky_lf_001_jnt', hi=True)
        cmds.joint(e=True, oj='yzx', sao='zup', ch=True, zso=True)
        cmds.select(clear=True)
        
        
        # Spine Joint
        spine_jnt_grp = cmds.group(empty=True, n="spine_jnt_grp")
        cmds.move(0, 8.869, 0.316, spine_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        
        cmds.joint(a=True, p=[0, 8.869, 0.316], rad=0.6, n='spine_ik_bind_001_jnt')
        cmds.joint(a=True, p=[0, 9.742, 0.404], rad=0.6, n='spine_ik_bind_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0, 10.017, 0.414], rad=0.6, n='spine_ik_bind_003_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0, 10.306, 0.414], rad=0.6, n='spine_ik_bind_004_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0, 10.593, 0.402], rad=0.6, n='spine_ik_bind_005_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0, 10.862, 0.379], rad=0.6, n='spine_ik_bind_006_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0, 11.124, 0.345], rad=0.6, n='spine_ik_bind_007_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0, 11.406, 0.295], rad=0.6, n='spine_ik_bind_008_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0, 11.847, 0.188], rad=0.6, n='spine_ik_bind_009_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('spine_ik_bind_001_jnt', hi=True)
        cmds.joint(e=True, oj='yzx', sao='zup', ch=True, zso=True)
        cmds.select(clear=True)
        
        
        # Left Pelvis Joint
        pelvis_jnt_grp = cmds.group(empty=True, n="pelvis_jnt_grp")
        cmds.move(0, 8.85, 0.266, pelvis_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        
        cmds.joint(a=True, p=[0.181, 8.85, 0.266], rad=0.6, n='pelvis_lf_001_jnt')
        cmds.joint(a=True, p=[0.967, 8.495, 0.266], rad=0.6, n='pelvis_lf_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('pelvis_lf_001_jnt', hi=True)
        cmds.joint(e=True, oj='yzx', sao='zup', ch=True, zso=True)
        cmds.select(clear=True)
        
        
        # Left Leg Joint
        leg_jnt_grp = cmds.group(empty=True, n="leg_jnt_grp")
        cmds.move(0, 8.495, 0.266, leg_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.joint(a=True, p=[0.967, 8.495, 0.266], rad=0.6, n='leg_lf_ik_tight_jnt')
        cmds.joint(a=True, p=[0.967, 5.156, 0.344], rad=0.6, n='leg_lf_ik_shin_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0.967, 0.785, -0.193], rad=0.6, n='leg_lf_ik_ankle_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0.967, 0.186, 0.733], rad=0.6, n='leg_lf_ik_ball_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0.967, 0.186, 1.418], rad=0.6, n='leg_lf_ik_toe_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('leg_lf_ik_tight_jnt', hi=True)
        cmds.joint(e=True, oj='yzx', sao='zup', ch=True, zso=True)    # Orient Joint Options
        cmds.select(clear=True)
         
        ### Left Foot Joint    # When create controllers
        
        # Mirror Joint
        cmds.mirrorJoint('shoulder_lf_001_jnt', myz=True, mb=True, sr=('lf', 'rt'))
        cmds.mirrorJoint('arm_lf_ik_shoulder_jnt', myz=True, mb=True, sr=('lf', 'rt'))
        cmds.mirrorJoint('pelvis_lf_001_jnt', myz=True, mb=False, sr=('lf', 'rt'))
        cmds.mirrorJoint('leg_lf_ik_tight_jnt', myz=True, mb=True, sr=('lf', 'rt'))
        cmds.mirrorJoint('thumb_lf_001_jnt', myz=True, mb=True, sr=('lf', 'rt'))
        cmds.mirrorJoint('index_lf_001_jnt', myz=True, mb=True, sr=('lf', 'rt'))
        cmds.mirrorJoint('middle_lf_001_jnt', myz=True, mb=True, sr=('lf', 'rt'))
        cmds.mirrorJoint('ring_lf_001_jnt', myz=True, mb=True, sr=('lf', 'rt'))
        cmds.mirrorJoint('pinky_lf_001_jnt', myz=True, mb=True, sr=('lf', 'rt'))
        cmds.select(clear=True)
        
        cmds.select('pelvis_rt_001_jnt', hi=True)
        cmds.joint(e=True, oj='yzx', sao='zdown', ch=True, zso=True)
        cmds.select(clear=True)
        
        # Make up the Joint Groups
        shoulder_lf_jnt_grp = cmds.group(empty=True, parent='shoulder_jnt_grp', n="shoulder_lf_jnt_grp")
        cmds.move(0.232, 12.965, -0.251, shoulder_lf_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('shoulder_lf_001_jnt', shoulder_lf_jnt_grp)
        
        shoulder_rt_jnt_grp = cmds.group(empty=True, parent='shoulder_jnt_grp', n="shoulder_rt_jnt_grp")
        cmds.move(-0.232, 12.965, -0.251, shoulder_rt_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('shoulder_rt_001_jnt', shoulder_rt_jnt_grp)
        
        arm_lf_jnt_grp = cmds.group(empty=True, parent='arm_jnt_grp', n="arm_lf_jnt_grp")
        cmds.move(1.135, 13.093, -0.504, arm_lf_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('arm_lf_ik_shoulder_jnt', arm_lf_jnt_grp)
        
        arm_rt_jnt_grp = cmds.group(empty=True, parent='arm_jnt_grp', n="arm_rt_jnt_grp")
        cmds.move(-1.135, 13.093, -0.504, arm_rt_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('arm_rt_ik_shoulder_jnt', arm_rt_jnt_grp)
        
        hand_lf_jnt_grp = cmds.group(empty=True, parent='hand_jnt_grp', n="hand_lf_jnt_grp")
        cmds.move(4.556, 9.612, -0.458, hand_lf_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('thumb_lf_001_jnt', hand_lf_jnt_grp)
        cmds.parent('index_lf_001_jnt', hand_lf_jnt_grp)
        cmds.parent('middle_lf_001_jnt', hand_lf_jnt_grp)
        cmds.parent('ring_lf_001_jnt', hand_lf_jnt_grp)
        cmds.parent('pinky_lf_001_jnt', hand_lf_jnt_grp)
        
        hand_rt_jnt_grp = cmds.group(empty=True, parent='hand_jnt_grp', n="hand_rt_jnt_grp")
        cmds.move(-4.556, 9.612, -0.458, hand_rt_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('thumb_rt_001_jnt', hand_rt_jnt_grp)
        cmds.parent('index_rt_001_jnt', hand_rt_jnt_grp)
        cmds.parent('middle_rt_001_jnt', hand_rt_jnt_grp)
        cmds.parent('ring_rt_001_jnt', hand_rt_jnt_grp)
        cmds.parent('pinky_rt_001_jnt', hand_rt_jnt_grp)
        
        pelvis_lf_jnt_grp = cmds.group(empty=True, parent='pelvis_jnt_grp', n="pelvis_lf_jnt_grp")
        cmds.move(0.181, 8.85, 0.266, pelvis_lf_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('pelvis_lf_001_jnt', pelvis_lf_jnt_grp)
        
        pelvis_rt_jnt_grp = cmds.group(empty=True, parent='pelvis_jnt_grp', n="pelvis_rt_jnt_grp")
        cmds.move(-0.181, 8.85, 0.266, pelvis_rt_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('pelvis_rt_001_jnt', pelvis_rt_jnt_grp)
        
        leg_lf_jnt_grp = cmds.group(empty=True, parent='leg_jnt_grp', n="leg_lf_jnt_grp")
        cmds.move(0.967, 8.495, 0.266, leg_lf_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('leg_lf_ik_tight_jnt', leg_lf_jnt_grp)
        
        leg_rt_jnt_grp = cmds.group(empty=True, parent='leg_jnt_grp', n="leg_rt_jnt_grp")
        cmds.move(-0.967, 8.495, 0.266, leg_rt_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('leg_rt_ik_tight_jnt', leg_rt_jnt_grp)
        
        cmds.select(clear=True)
        
        jnt_grp = cmds.group(empty=True, n="jnt_grp")
        cmds.parent(head_jnt_grp, jnt_grp)
        cmds.parent(jaw_jnt_grp, jnt_grp)
        cmds.parent(neck_jnt_grp, jnt_grp)
        cmds.parent(shoulder_jnt_grp, jnt_grp)
        cmds.parent(arm_jnt_grp, jnt_grp)
        cmds.parent(hand_jnt_grp, jnt_grp)
        cmds.parent(spine_jnt_grp, jnt_grp)
        cmds.parent(pelvis_jnt_grp, jnt_grp)
        cmds.parent(leg_jnt_grp, jnt_grp)
        
        ch_grp = cmds.group(empty=True, n="ch_grp")
        cmds.parent(jnt_grp, ch_grp)
        
        # Change name with 'dummy_'
        cmds.select(ch_grp, hi=True)
        sel = cmds.ls(sl=True)
        
        for s in sel:
            name = 'dummy_' + str(s)
            cmds.rename(s, name)
        
        cmds.select(clear=True)
        
        cmds.pointConstraint('dummy_neck_003_jnt', 'dummy_head_001_jnt', w=1, mo=True)
        cmds.pointConstraint('dummy_neck_003_jnt', 'dummy_jaw_001_jnt', w=1, mo=True)
        
        cmds.pointConstraint('dummy_shoulder_lf_002_jnt', 'dummy_arm_lf_ik_shoulder_jnt', w=1, mo=True)
        cmds.pointConstraint('dummy_shoulder_rt_002_jnt', 'dummy_arm_rt_ik_shoulder_jnt', w=1, mo=True)
        
        cmds.parentConstraint('dummy_arm_lf_ik_hand_jnt', 'dummy_hand_lf_jnt_grp', w=1, mo=True)
        cmds.parentConstraint('dummy_arm_rt_ik_hand_jnt', 'dummy_hand_rt_jnt_grp', w=1, mo=True)
        
        cmds.pointConstraint('dummy_pelvis_lf_002_jnt', 'dummy_leg_lf_ik_tight_jnt', w=1, mo=True)
        cmds.pointConstraint('dummy_pelvis_rt_002_jnt', 'dummy_leg_rt_ik_tight_jnt', w=1, mo=True)
        
        self.ctrl_gen(self)
        self.root_ctrl(self)
        cmds.group('root_ctrl', n='dummy_ctrl_grp')
        cmds.rename('root_ctrl', 'dummy_root_ctrl')
        cmds.parent('dummy_ctrl_grp', 'dummy_ch_grp')
        cmds.scaleConstraint('dummy_root_ctrl', 'dummy_jnt_grp', w=1, mo=True)
        cmds.parentConstraint('dummy_root_ctrl', 'dummy_jnt_grp', w=1, mo=True)
        
        self.color = 'PURPLE'
        cmds.select('dummy*')
        self.coloring_ctrl(self)
        
        cmds.select(clear=True)
        
        
    def confirm_orient_joint(self, args):
        '''
            STEP 1-1: Check Joint Orientation
        '''
        
        cmds.select(all=True, hi=True)
        selectedObjs = cmds.ls(sl=True)
        
        for obj in selectedObjs:
            if (cmds.objectType(obj) == 'joint'):
                cmds.toggle(obj, localAxis=True)
        
        cmds.select(clear=True)
        
        
    def fix_jnt(self, args):
        '''
            STEP 2: Fix the Joint
            # Generate IK,FK,BIND joint referred to dummy joint
        '''
        
        cmds.select('*jnt')
        
        jnt_list = cmds.ls(sl=True)
        
        # Create new JNT with new name
        t = [0,0,0]
        for i in range(0, len(jnt_list)):
            jnt_name = jnt_list[i].replace('dummy_', '')
            cmds.select(cl=True)
            cmds.joint(a=True, p=[0,0,0], rad=0.6, n=jnt_name)
            constraint = cmds.parentConstraint(jnt_list[i], jnt_name, w=1, mo=False)
            cmds.delete(constraint)
            
        cmds.select(cl=True)
        
        # Adjust Joint Orientation
        cmds.select('*jnt')
        cmds.select('dummy*', d=True)
        
        sel = cmds.ls(sl=True)
        
        for s in sel:
            cmds.setAttr( s+'.jox', cmds.getAttr(s+'.rx') )
            cmds.setAttr( s+'.joy', cmds.getAttr(s+'.ry') )
            cmds.setAttr( s+'.joz', cmds.getAttr(s+'.rz') )
            cmds.setAttr( s+'.rotateX', 0 )
            cmds.setAttr( s+'.rotateY', 0 )
            cmds.setAttr( s+'.rotateZ', 0 )
        
        # Set joint hierarchy
        cmds.parent('head_002_jnt', 'head_001_jnt')
        
        cmds.parent('jaw_002_jnt', 'jaw_001_jnt')
        
        cmds.parent('neck_002_jnt', 'neck_001_jnt')
        cmds.parent('neck_003_jnt', 'neck_002_jnt')
        
        cmds.parent('shoulder_lf_002_jnt', 'shoulder_lf_001_jnt')
        cmds.parent('shoulder_rt_002_jnt', 'shoulder_rt_001_jnt')
        
        cmds.parent('arm_lf_ik_elbow_jnt', 'arm_lf_ik_shoulder_jnt')
        cmds.parent('arm_lf_ik_wrist_jnt', 'arm_lf_ik_elbow_jnt')
        cmds.parent('arm_lf_ik_hand_jnt', 'arm_lf_ik_wrist_jnt')
        cmds.parent('arm_rt_ik_elbow_jnt', 'arm_rt_ik_shoulder_jnt')
        cmds.parent('arm_rt_ik_wrist_jnt', 'arm_rt_ik_elbow_jnt')
        cmds.parent('arm_rt_ik_hand_jnt', 'arm_rt_ik_wrist_jnt')
        
        finger = ['thumb', 'index', 'middle', 'ring', 'pinky']
        lf_rt = ['lf', 'rt']
        for lr in lf_rt:
            for f in finger:
                for i in range(1,4):
                    cmds.parent(f+'_'+lr+'_00'+str(i+1)+'_jnt', f+'_'+lr+'_00'+str(i)+'_jnt')
        
        for i in range(1,9):
            cmds.parent('spine_ik_bind_00'+str(i+1)+'_jnt', 'spine_ik_bind_00'+str(i)+'_jnt')
        
        cmds.parent('pelvis_lf_002_jnt', 'pelvis_lf_001_jnt')
        cmds.parent('pelvis_rt_002_jnt', 'pelvis_rt_001_jnt')
        
        cmds.parent('leg_lf_ik_shin_jnt', 'leg_lf_ik_tight_jnt')
        cmds.parent('leg_lf_ik_ankle_jnt', 'leg_lf_ik_shin_jnt')
        cmds.parent('leg_lf_ik_ball_jnt', 'leg_lf_ik_ankle_jnt')
        cmds.parent('leg_lf_ik_toe_jnt', 'leg_lf_ik_ball_jnt')
        cmds.parent('leg_rt_ik_shin_jnt', 'leg_rt_ik_tight_jnt')
        cmds.parent('leg_rt_ik_ankle_jnt', 'leg_rt_ik_shin_jnt')
        cmds.parent('leg_rt_ik_ball_jnt', 'leg_rt_ik_ankle_jnt')
        cmds.parent('leg_rt_ik_toe_jnt', 'leg_rt_ik_ball_jnt')
        
        
        # Group jnt_grp
        parts = ['head', 'jaw', 'neck', 'shoulder_lf', 'shoulder_rt', 'pelvis_lf', 'pelvis_rt']
        for part in parts:
            cmds.group(em=True, n=part+'_jnt_grp')    # head_jnt_grp
            t = cmds.xform(part+'_001_jnt', r=True, q=True, t=True)
            cmds.move(t[0], t[1], t[2], part+'_jnt_grp')
            cmds.makeIdentity(apply=True, t=True, r=True, s=True)
            cmds.parent(part+'_001_jnt', part+'_jnt_grp')
        
        for lr in lf_rt:
            # Arm 
            cmds.group(em=True, n='arm_'+lr+'_jnt_grp')
            t = cmds.xform('arm_'+lr+'_ik_shoulder_jnt', r=True, q=True, t=True)
            cmds.move(t[0], t[1], t[2], 'arm_'+lr+'_jnt_grp')
            cmds.makeIdentity(apply=True, t=True, r=True, s=True)
            cmds.parent('arm_'+lr+'_ik_shoulder_jnt', 'arm_'+lr+'_jnt_grp')
        
            # Hand 
            cmds.group(em=True, n='hand_'+lr+'_jnt_grp')
            t = cmds.joint('arm_'+lr+'_ik_wrist_jnt', q=True, p=True)
            cmds.move(t[0], t[1], t[2], 'hand_'+lr+'_jnt_grp')
            cmds.makeIdentity(apply=True, t=True, r=True, s=True)
            
            for f in finger:
                cmds.parent(f+'_'+lr+'_001_jnt', 'hand_'+lr+'_jnt_grp')
            
            # Leg
            cmds.group(em=True, n='leg_'+lr+'_jnt_grp')
            t = cmds.xform('leg_'+lr+'_ik_tight_jnt', r=True, q=True, t=True)
            cmds.move(t[0], t[1], t[2], 'leg_'+lr+'_jnt_grp')
            cmds.makeIdentity(apply=True, t=True, r=True, s=True)
            cmds.parent('leg_'+lr+'_ik_tight_jnt', 'leg_'+lr+'_jnt_grp')
        
        # Spine
        cmds.group(em=True, n='spine_jnt_grp')
        t = cmds.xform('spine_ik_bind_001_jnt', r=True, q=True, t=True)
        cmds.move(t[0], t[1], t[2], 'spine_jnt_grp')
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('spine_ik_bind_001_jnt', 'spine_jnt_grp')
        
        cmds.group(em=True, n='jnt_grp')
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        
        cmds.select('*jnt_grp')
        cmds.select('jnt_grp', d=True)
        cmds.select('dummy*', d=True)
        sel = cmds.ls(sl=True)
        for s in sel:
            cmds.parent(s, 'jnt_grp')
            
        cmds.select(cl=True)
        
        cmds.group(em=True, n='ch_grp')
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('jnt_grp', 'ch_grp')
        
        cmds.hide('dummy_ch_grp')
        
        #
        cmds.group(empty=True, n='shoulder_jnt_grp')
        constraint = cmds.parentConstraint('shoulder_lf_jnt_grp', 'shoulder_rt_jnt_grp', 'shoulder_jnt_grp', w=1, mo=False)
        cmds.delete(constraint)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('shoulder_lf_jnt_grp', 'shoulder_jnt_grp')
        cmds.parent('shoulder_rt_jnt_grp', 'shoulder_jnt_grp')
        cmds.parent('shoulder_jnt_grp', 'jnt_grp')
        
        cmds.group(empty=True, n='arm_jnt_grp')
        constraint = cmds.parentConstraint('arm_lf_jnt_grp', 'arm_rt_jnt_grp', 'arm_jnt_grp', w=1, mo=False)
        cmds.delete(constraint)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('arm_lf_jnt_grp', 'arm_jnt_grp')
        cmds.parent('arm_rt_jnt_grp', 'arm_jnt_grp')
        cmds.parent('arm_jnt_grp', 'jnt_grp')
        
        cmds.group(empty=True, n='hand_jnt_grp')
        constraint = cmds.parentConstraint('hand_lf_jnt_grp', 'hand_rt_jnt_grp', 'hand_jnt_grp', w=1, mo=False)
        cmds.delete(constraint)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('hand_lf_jnt_grp', 'hand_jnt_grp')
        cmds.parent('hand_rt_jnt_grp', 'hand_jnt_grp')
        cmds.parent('hand_jnt_grp', 'jnt_grp')
        
        cmds.group(em=True, n='pelvis_jnt_grp')
        constraint = cmds.parentConstraint('pelvis_lf_jnt_grp', 'pelvis_rt_jnt_grp', 'pelvis_jnt_grp', w=1, mo=False)
        cmds.delete(constraint)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('pelvis_lf_jnt_grp', 'pelvis_jnt_grp')
        cmds.parent('pelvis_rt_jnt_grp', 'pelvis_jnt_grp')
        cmds.parent('pelvis_jnt_grp', 'jnt_grp')
        
        cmds.group(empty=True, n='leg_jnt_grp')
        constraint = cmds.parentConstraint('leg_lf_jnt_grp', 'leg_rt_jnt_grp', 'leg_jnt_grp', w=1, mo=False)
        cmds.delete(constraint)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('leg_lf_jnt_grp', 'leg_jnt_grp')
        cmds.parent('leg_rt_jnt_grp', 'leg_jnt_grp')
        cmds.parent('leg_jnt_grp', 'jnt_grp')
        
        cmds.reorder('spine_jnt_grp', r=3)
        
        cmds.select(cl=True)
        
        
        # Duplicate IK Joints for FK,BIND
        # Left Arm
        cmds.duplicate('arm_lf_ik_shoulder_jnt', rc=True)
        
        cmds.select('arm_lf_ik_shoulder_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_bind = [0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_bind[i] = tmp_ik[i].replace('ik', 'fk')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_bind[i].split("|")[-1])
        
        cmds.select('arm_lf_fk_shoulder_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_fk[i] = tmp_ik[i].replace('t1', 't')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_fk[i].split("|")[-1])
        #
        cmds.duplicate('arm_lf_ik_shoulder_jnt', rc=True)
        
        cmds.select('arm_lf_ik_shoulder_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_bind = [0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_bind[i] = tmp_ik[i].replace('ik', 'bind')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_bind[i].split("|")[-1])
        
        cmds.select('arm_lf_bind_shoulder_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_fk[i] = tmp_ik[i].replace('t1', 't')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_fk[i].split("|")[-1])
        #
        # Right Arm
        cmds.duplicate('arm_rt_ik_shoulder_jnt', rc=True)
        
        cmds.select('arm_rt_ik_shoulder_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_bind = [0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_bind[i] = tmp_ik[i].replace('ik', 'fk')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_bind[i].split("|")[-1])
        
        cmds.select('arm_rt_fk_shoulder_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_fk[i] = tmp_ik[i].replace('t1', 't')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_fk[i].split("|")[-1])
        #
        cmds.duplicate('arm_rt_ik_shoulder_jnt', rc=True)
        
        cmds.select('arm_rt_ik_shoulder_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_bind = [0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_bind[i] = tmp_ik[i].replace('ik', 'bind')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_bind[i].split("|")[-1])
        
        cmds.select('arm_rt_bind_shoulder_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_fk[i] = tmp_ik[i].replace('t1', 't')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_fk[i].split("|")[-1])
        #
        
        # Spine
        cmds.duplicate('spine_ik_bind_001_jnt', rc=True)
        
        cmds.select('spine_ik_bind_001_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        tmp_bind = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_bind[i] = tmp_ik[i].replace('ik_bind', 'fk')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_bind[i].split("|")[-1])
        
        cmds.select('spine_fk_001_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_fk[i] = tmp_ik[i].replace('t1', 't')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_fk[i].split("|")[-1])
        #
        cmds.select('spine_fk_001_jnt', hi=True)
        sel = cmds.ls(sl=True)
        for s in sel:
            cmds.parent(s, w=True)
        cmds.delete('spine_fk_003_jnt', 'spine_fk_004_jnt', 'spine_fk_005_jnt', 'spine_fk_007_jnt', 'spine_fk_008_jnt')
        cmds.parent('spine_fk_002_jnt', 'spine_fk_001_jnt')
        cmds.parent('spine_fk_006_jnt', 'spine_fk_002_jnt')
        cmds.parent('spine_fk_009_jnt', 'spine_fk_006_jnt')
        
        cmds.parent('spine_fk_001_jnt', 'spine_jnt_grp')
        
        '''
        cmds.joint(a=True, p=[0, 8.869, 0.316], rad=0.6, n='spine_fk_001_jnt')
        cmds.joint(a=True, p=[0, 9.742, 0.404], rad=0.6, n='spine_fk_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0, 10.862, 0.379], rad=0.6, n='spine_fk_006_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0, 11.847, 0.188], rad=0.6, n='spine_fk_009_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('spine_fk_001_jnt', hi=True)'''
        cmds.joint(e=True, oj='yzx', sao='zup', ch=True, zso=True)
        
        # Left Leg
        cmds.duplicate('leg_lf_ik_tight_jnt', rc=True)
        
        cmds.select('leg_lf_ik_tight_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_bind = [0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_bind[i] = tmp_ik[i].replace('ik', 'fk')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_bind[i].split("|")[-1])
        
        cmds.select('leg_lf_fk_tight_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_fk[i] = tmp_ik[i].replace('t1', 't')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_fk[i].split("|")[-1])
        #
        cmds.duplicate('leg_lf_ik_tight_jnt', rc=True)
        
        cmds.select('leg_lf_ik_tight_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_bind = [0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_bind[i] = tmp_ik[i].replace('ik', 'bind')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_bind[i].split("|")[-1])
        
        cmds.select('leg_lf_bind_tight_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_fk[i] = tmp_ik[i].replace('t1', 't')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_fk[i].split("|")[-1])
        #
        # Right Leg
        cmds.duplicate('leg_rt_ik_tight_jnt', rc=True)
        
        cmds.select('leg_rt_ik_tight_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_bind = [0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_bind[i] = tmp_ik[i].replace('ik', 'fk')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_bind[i].split("|")[-1])
        
        cmds.select('leg_rt_fk_tight_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_fk[i] = tmp_ik[i].replace('t1', 't')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_fk[i].split("|")[-1])
        #
        cmds.duplicate('leg_rt_ik_tight_jnt', rc=True)
        
        cmds.select('leg_rt_ik_tight_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_bind = [0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_bind[i] = tmp_ik[i].replace('ik', 'bind')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_bind[i].split("|")[-1])
        
        cmds.select('leg_rt_bind_tight_jnt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_fk[i] = tmp_ik[i].replace('t1', 't')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_fk[i].split("|")[-1])
        
        
        # Arm, Hand, Leg Joint Constraint
        cmds.orientConstraint('arm_lf_ik_shoulder_jnt', 'arm_lf_fk_shoulder_jnt', 'arm_lf_bind_shoulder_jnt', w=1, mo=True)
        cmds.orientConstraint('arm_lf_ik_elbow_jnt', 'arm_lf_fk_elbow_jnt', 'arm_lf_bind_elbow_jnt', w=1, mo=True)
        cmds.orientConstraint('arm_lf_ik_wrist_jnt', 'arm_lf_fk_wrist_jnt', 'arm_lf_bind_wrist_jnt', w=1, mo=True)
        cmds.orientConstraint('arm_rt_ik_shoulder_jnt', 'arm_rt_fk_shoulder_jnt', 'arm_rt_bind_shoulder_jnt', w=1, mo=True)
        cmds.orientConstraint('arm_rt_ik_elbow_jnt', 'arm_rt_fk_elbow_jnt', 'arm_rt_bind_elbow_jnt', w=1, mo=True)
        cmds.orientConstraint('arm_rt_ik_wrist_jnt', 'arm_rt_fk_wrist_jnt', 'arm_rt_bind_wrist_jnt', w=1, mo=True)
        
        cmds.parentConstraint('arm_lf_bind_wrist_jnt', 'hand_lf_jnt_grp', w=1, mo=True)
        cmds.parentConstraint('arm_rt_bind_wrist_jnt', 'hand_rt_jnt_grp', w=1, mo=True)
        
        cmds.orientConstraint('leg_lf_ik_tight_jnt', 'leg_lf_fk_tight_jnt', 'leg_lf_bind_tight_jnt', w=1, mo=True)
        cmds.orientConstraint('leg_lf_ik_shin_jnt', 'leg_lf_fk_shin_jnt', 'leg_lf_bind_shin_jnt', w=1, mo=True)
        cmds.orientConstraint('leg_lf_ik_ankle_jnt', 'leg_lf_fk_ankle_jnt', 'leg_lf_bind_ankle_jnt', w=1, mo=True)
        cmds.orientConstraint('leg_lf_ik_ball_jnt', 'leg_lf_fk_ball_jnt', 'leg_lf_bind_ball_jnt', w=1, mo=True)
        cmds.orientConstraint('leg_rt_ik_tight_jnt', 'leg_rt_fk_tight_jnt', 'leg_rt_bind_tight_jnt', w=1, mo=True)
        cmds.orientConstraint('leg_rt_ik_shin_jnt', 'leg_rt_fk_shin_jnt', 'leg_rt_bind_shin_jnt', w=1, mo=True)
        cmds.orientConstraint('leg_rt_ik_ankle_jnt', 'leg_rt_fk_ankle_jnt', 'leg_rt_bind_ankle_jnt', w=1, mo=True)
        cmds.orientConstraint('leg_rt_ik_ball_jnt', 'leg_rt_fk_ball_jnt', 'leg_rt_bind_ball_jnt', w=1, mo=True)
        
        cmds.select(cl=True)
        
        
    def create_ctrl(self, args):
        '''
            STEP 3: Create Controllers
        '''
        
        # Select hirarchy of jnt_grp 
        cmds.select('jnt_grp', hi=True)
        selectedGrps = cmds.ls(sl=True)
        cmds.select(clear=True)
        
        # Select Only Joints of jnt_grp(NOT group or sth)
        jointGrps = []
        selectedJnts = []
        
        for grps in selectedGrps:    	# Save jnt_grp & bodypart_grp in jointGrps
            if (cmds.objectType(grps) == 'transform'):
                jointGrps.append(grps)
        
        for idx in range(1, len(jointGrps)):    # Acces to bodypart_grp in order except jnt_grp 
            obj = jointGrps[idx]
            
            # Create Controllers by site
            if (obj == 'head_jnt_grp'):
                self.shape = 'HEAD'
                
                cmds.select('head_001_jnt', hi=True)
                ctrl = self.ctrl_gen(self)
                
                head_ctrl_grp = cmds.group(empty=True, n="head_ctrl_grp")
                cmds.move(0, 14.447, -0.066, head_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                cmds.parent('head_001_jnt_ctrl_grp', head_ctrl_grp)
            
            elif (obj == 'jaw_jnt_grp'):
                self.shape = 'JAW'
                
                cmds.select('jaw_001_jnt', hi=True)
                ctrl = self.ctrl_gen(self)
                
                jaw_ctrl_grp = cmds.group(empty=True, n="jaw_ctrl_grp")
                cmds.move(0, 14.447, -0.066, jaw_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                cmds.parent('jaw_001_jnt_ctrl_grp', jaw_ctrl_grp)
            
            elif (obj == 'neck_jnt_grp'):
                self.shape = 'NECK'
                
                cmds.select('neck_001_jnt', hi=True)
                self.ctrl_gen(self)
                
                neck_ctrl_grp = cmds.group(empty=True, n="neck_ctrl_grp")
                cmds.move(0, 13.322, -0.366, neck_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                cmds.parent('neck_001_jnt_ctrl_grp', neck_ctrl_grp)
            
            elif (obj == 'shoulder_jnt_grp'):
                self.shape = 'SHOULDER_L'
                cmds.select('shoulder_lf_001_jnt', hi=True)
                ctrl = self.ctrl_gen(self)
                self.shape = 'SHOULDER_R'
                cmds.select('shoulder_rt_001_jnt', hi=True)
                ctrl = self.ctrl_gen(self)
                
                shoulder_ctrl_grp = cmds.group(empty=True, n="shoulder_ctrl_grp")
                cmds.move(0, 12.965, -0.251, shoulder_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                shoulder_lf_ctrl_grp = cmds.group(empty=True, p="shoulder_ctrl_grp", n="shoulder_lf_ctrl_grp")
                cmds.move(0.232, 12.965, -0.251, shoulder_lf_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                shoulder_rt_ctrl_grp = cmds.group(empty=True, p="shoulder_ctrl_grp", n="shoulder_rt_ctrl_grp")
                cmds.move(-0.232, 12.965, -0.251, shoulder_rt_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                cmds.parent('shoulder_lf_001_jnt_ctrl_grp', shoulder_lf_ctrl_grp)
                cmds.parent('shoulder_rt_001_jnt_ctrl_grp', shoulder_rt_ctrl_grp)
            
            elif (obj == 'arm_jnt_grp'):
                self.shape = 'SPHERE'
                
                cmds.select('arm_lf_ik_elbow_jnt', hi=True)
                self.ctrl_gen(self)
                cmds.select('arm_rt_ik_elbow_jnt', hi=True)
                self.ctrl_gen(self)
                
                cmds.select('arm_lf_ik_elbow_jnt_ctrl_grp')
                cmds.select('arm_rt_ik_elbow_jnt_ctrl_grp', add=True)
                cmds.move(0, 0, -3, r=True)
                cmds.makeIdentity(apply=True, t=True, s=True)
                
                cmds.select('arm_lf_ik_wrist_jnt_ctrl_grp')
                cmds.select('arm_rt_ik_wrist_jnt_ctrl_grp', add=True)
                cmds.move(0, 0, 3, r=True)
                cmds.makeIdentity(apply=True, t=True, s=True)
                
                self.shape = 'MIDDLE_CIRCLE'
                cmds.select('arm_lf_fk_shoulder_jnt', hi=True)
                self.ctrl_gen(self)
                cmds.select('arm_rt_fk_shoulder_jnt', hi=True)
                self.ctrl_gen(self)
                #
                ctrl = self.arrow_ctrl(self)
                constraint = cmds.pointConstraint('arm_lf_bind_wrist_jnt', ctrl, w=1, mo=False)
                cmds.delete(constraint)
                cmds.rename(ctrl, 'arm_lf_switch')
                ctrl = self.arrow_ctrl(self)
                constraint = cmds.pointConstraint('arm_rt_bind_wrist_jnt', ctrl, w=1, mo=False)
                cmds.delete(constraint)
                cmds.rename(ctrl, 'arm_rt_switch')
                cmds.select('arm_lf_switch', 'arm_rt_switch')
                cmds.makeIdentity(apply=True, t=True, s=True)
                
                arm_switch_grp = cmds.group(empty=True, n="arm_switch_grp")
                cmds.move(0, 9.612, -0.458, arm_switch_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                arm_lf_switch_grp = cmds.group(empty=True, p="arm_switch_grp", n="arm_lf_switch_grp")
                cmds.move(4.556, 9.612, -0.458, arm_lf_switch_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                arm_rt_switch_grp = cmds.group(empty=True, p="arm_switch_grp", n="arm_rt_switch_grp")
                cmds.move(-4.556, 9.612, -0.458, arm_rt_switch_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                cmds.parent('arm_lf_switch', 'arm_lf_switch_grp')
                cmds.parent('arm_rt_switch', 'arm_rt_switch_grp')
                #
                
                arm_ctrl_grp = cmds.group(empty=True, n="arm_ctrl_grp")
                cmds.move(0, 13.093, -0.504, arm_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                arm_lf_ctrl_grp = cmds.group(empty=True, p="arm_ctrl_grp", n="arm_lf_ctrl_grp")
                cmds.move(1.135, 13.093, -0.504, arm_lf_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                arm_rt_ctrl_grp = cmds.group(empty=True, p="arm_ctrl_grp", n="arm_rt_ctrl_grp")
                cmds.move(-1.135, 13.093, -0.504, arm_rt_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                cmds.parent('arm_lf_ik_elbow_jnt_ctrl_grp', arm_lf_ctrl_grp)
                cmds.parent('arm_rt_ik_elbow_jnt_ctrl_grp', arm_rt_ctrl_grp)
                cmds.parent('arm_lf_ik_wrist_jnt_ctrl_grp', arm_lf_ctrl_grp)
                cmds.parent('arm_rt_ik_wrist_jnt_ctrl_grp', arm_rt_ctrl_grp)
                cmds.parent('arm_lf_fk_shoulder_jnt_ctrl_grp', arm_lf_ctrl_grp)
                cmds.parent('arm_rt_fk_shoulder_jnt_ctrl_grp', arm_rt_ctrl_grp)
                
                cmds.rename('arm_lf_ik_elbow_jnt_ctrl', 'arm_lf_pv_ctrl')
                cmds.rename('arm_rt_ik_elbow_jnt_ctrl', 'arm_rt_pv_ctrl')
                cmds.rename('arm_lf_ik_elbow_jnt_ctrl_grp', 'arm_lf_pv_ctrl_grp')
                cmds.rename('arm_rt_ik_elbow_jnt_ctrl_grp', 'arm_rt_pv_ctrl_grp')
            
            elif (obj == 'hand_jnt_grp'):
                self.shape = 'SMALL_CIRCLE'
                
                cmds.select('thumb_lf_001_jnt', hi=True)
                self.ctrl_gen(self)
                cmds.select('index_lf_001_jnt', hi=True)
                self.ctrl_gen(self)
                cmds.select('middle_lf_001_jnt', hi=True)
                self.ctrl_gen(self)
                cmds.select('ring_lf_001_jnt', hi=True)
                self.ctrl_gen(self)
                cmds.select('pinky_lf_001_jnt', hi=True)
                self.ctrl_gen(self)
                
                cmds.select('thumb_rt_001_jnt', hi=True)
                self.ctrl_gen(self)
                cmds.select('index_rt_001_jnt', hi=True)
                self.ctrl_gen(self)
                cmds.select('middle_rt_001_jnt', hi=True)
                self.ctrl_gen(self)
                cmds.select('ring_rt_001_jnt', hi=True)
                self.ctrl_gen(self)
                cmds.select('pinky_rt_001_jnt', hi=True)
                self.ctrl_gen(self)
                
                hand_ctrl_grp = cmds.group(empty=True, n="hand_ctrl_grp")
                cmds.move(0, 9.612, -0.458, hand_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                hand_lf_ctrl_grp = cmds.group(empty=True, p="hand_ctrl_grp", n="hand_lf_ctrl_grp")
                cmds.move(4.556, 9.612, -0.458, hand_lf_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                hand_rt_ctrl_grp = cmds.group(empty=True, p="hand_ctrl_grp", n="hand_rt_ctrl_grp")
                cmds.move(-4.556, 9.612, -0.458, hand_rt_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                cmds.parent('thumb_lf_001_jnt_ctrl_grp', hand_lf_ctrl_grp)
                cmds.parent('index_lf_001_jnt_ctrl_grp', hand_lf_ctrl_grp)
                cmds.parent('middle_lf_001_jnt_ctrl_grp', hand_lf_ctrl_grp)
                cmds.parent('ring_lf_001_jnt_ctrl_grp', hand_lf_ctrl_grp)
                cmds.parent('pinky_lf_001_jnt_ctrl_grp', hand_lf_ctrl_grp)
                
                cmds.parent('thumb_rt_001_jnt_ctrl_grp', hand_rt_ctrl_grp)
                cmds.parent('index_rt_001_jnt_ctrl_grp', hand_rt_ctrl_grp)
                cmds.parent('middle_rt_001_jnt_ctrl_grp', hand_rt_ctrl_grp)
                cmds.parent('ring_rt_001_jnt_ctrl_grp', hand_rt_ctrl_grp)
                cmds.parent('pinky_rt_001_jnt_ctrl_grp', hand_rt_ctrl_grp)
            
            elif (obj == 'spine_jnt_grp'):
                self.shape = 'BODY'
                cmds.select('spine_ik_bind_001_jnt', hi=True)
                self.ctrl_gen(self)
                
                cmds.parent('spine_ik_bind_008_jnt_ctrl_grp' ,w=True)
                cmds.delete('spine_ik_bind_002_jnt_ctrl_grp')
                
                
                self.shape = 'CIRCLE'
                cmds.select('spine_fk_001_jnt', hi=True)
                self.ctrl_gen(self)
                
                spine_ctrl_grp = cmds.group(empty=True, n="spine_ctrl_grp")
                cmds.move(0, 8.869, 0.316, spine_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                cmds.parent('spine_ik_bind_001_jnt_ctrl_grp', spine_ctrl_grp)
                cmds.parent('spine_ik_bind_008_jnt_ctrl_grp', spine_ctrl_grp)
                cmds.parent('spine_fk_001_jnt_ctrl_grp', spine_ctrl_grp)
                
                cmds.rename('spine_ik_bind_001_jnt_ctrl_grp', 'lower_body_ctrl_grp')
                cmds.rename('spine_ik_bind_001_jnt_ctrl', 'lower_body_ctrl')
                cmds.rename('spine_ik_bind_008_jnt_ctrl_grp', 'upper_body_ctrl_grp')
                cmds.rename('spine_ik_bind_008_jnt_ctrl', 'upper_body_ctrl')
                
                '''
                
                cmds.group(em=True, n='spine_jnt_grp')
                t = cmds.xform('spine_ik_bind_001_jnt', r=True, q=True, t=True)
                cmds.move(t[0], t[1], t[2], 'spine_jnt_grp')
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                cmds.parent('spine_ik_bind_001_jnt', 'spine_jnt_grp')
                '''
                #cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                t = cmds.xform('spine_ik_bind_001_jnt', r=True, q=True, t=True)
                cmds.joint(a=True, p=[t[0], t[1], t[2]], rad=0.6, n='lower_body_jnt')
                cmds.parent('lower_body_jnt', 'lower_body_ctrl')
                
                t = cmds.xform('spine_ik_bind_001_jnt', r=True, q=True, t=True)
                cmds.joint(a=True, p=[t[0], t[1], t[2]], rad=0.6, n='upper_body_jnt')
                cmds.parent('upper_body_jnt', 'upper_body_ctrl')
                cmds.select('upper_body_ctrl')
                cmds.move(0, 11.847, 0.188, ".scalePivot", ".rotatePivot", a=True)
            
            elif (obj == 'pelvis_jnt_grp'):
                self.shape = 'PELVIS'
                
                cmds.select('pelvis_lf_001_jnt', hi=True)
                ctrl = self.ctrl_gen(self)
                cmds.select('pelvis_rt_001_jnt', hi=True)
                ctrl = self.ctrl_gen(self)
                
                pelvis_ctrl_grp = cmds.group(empty=True, n="pelvis_ctrl_grp")
                cmds.move(0, 8.85, 0.266, pelvis_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                pelvis_lf_ctrl_grp = cmds.group(empty=True, p="pelvis_ctrl_grp", n="pelvis_lf_ctrl_grp")
                cmds.move(0.181, 8.85, 0.266, pelvis_lf_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                pelvis_rt_ctrl_grp = cmds.group(empty=True, p="pelvis_ctrl_grp", n="pelvis_rt_ctrl_grp")
                cmds.move(-0.181, 8.85, 0.266, pelvis_rt_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                cmds.parent('pelvis_lf_001_jnt_ctrl_grp', pelvis_lf_ctrl_grp)
                cmds.parent('pelvis_rt_001_jnt_ctrl_grp', pelvis_rt_ctrl_grp)
            
            elif (obj == 'leg_jnt_grp'):
                self.shape = 'SPHERE'
                
                cmds.select('leg_lf_ik_shin_jnt', hi=True)
                self.ctrl_gen(self)
                cmds.select('leg_rt_ik_shin_jnt', hi=True)
                self.ctrl_gen(self)
                
                cmds.delete('leg_lf_ik_ankle_jnt_ctrl_grp')
                cmds.delete('leg_rt_ik_ankle_jnt_ctrl_grp')
                
                cmds.select('leg_lf_ik_shin_jnt_ctrl_grp')
                cmds.select('leg_rt_ik_shin_jnt_ctrl_grp', add=True)
                cmds.move(0, 0, 4, r=True)
                cmds.makeIdentity(apply=True, t=True, s=True)
                
                self.shape = 'MIDDLE_CIRCLE'
                
                cmds.select('leg_lf_fk_tight_jnt', hi=True)
                self.ctrl_gen(self)
                cmds.select('leg_rt_fk_tight_jnt', hi=True)
                self.ctrl_gen(self)
                
                ctrl = self.arrow_ctrl(self)
                constraint = cmds.pointConstraint('leg_lf_bind_ankle_jnt', ctrl, w=1, mo=False)
                cmds.delete(constraint)
                cmds.rename(ctrl, 'leg_lf_switch')
                ctrl = self.arrow_ctrl(self)
                constraint = cmds.pointConstraint('leg_rt_bind_ankle_jnt', ctrl, w=1, mo=False)
                cmds.delete(constraint)
                cmds.rename(ctrl, 'leg_rt_switch')
                cmds.select('leg_lf_switch', 'leg_rt_switch')
                cmds.makeIdentity(apply=True, t=True, s=True)
                
                ctrl = self.foot_lf_ctrl(self)
                '''
                t = cmds.xform('joint1', a=True, q=True, t=True)
                cmds.move(t[0], t[1], t[2], ".scalePivot", ".rotatePivot", a=True)
                cmds.move(0.967, 0, 0.3, rpr=True)
                t = cmds.xform('joint1', a=True, q=True, t=True)
                cmds.move(t[0], t[1], t[2], ".scalePivot", ".rotatePivot", r=True)
                cmds.move(0.967, 0.785, -0.193, ".scalePivot", ".rotatePivot", a=True)
                '''
                cmds.rename(ctrl, 'foot_lf_ik_ctrl')
                ctrl = self.foot_rt_ctrl(self)
                cmds.rename(ctrl, 'foot_rt_ik_ctrl')
                cmds.select('foot_lf_ik_ctrl', 'foot_rt_ik_ctrl')
                cmds.makeIdentity(apply=True, t=True, s=True)
                
                leg_switch_grp = cmds.group(empty=True, n="leg_switch_grp")
                cmds.move(0, 0.785, -0.193, leg_switch_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                leg_lf_switch_grp = cmds.group(empty=True, p="leg_switch_grp", n="leg_lf_switch_grp")
                cmds.move(0.967, 0.785, -0.193, leg_lf_switch_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                leg_rt_switch_grp = cmds.group(empty=True, p="leg_switch_grp", n="leg_rt_switch_grp")
                cmds.move(-0.967, 0.785, -0.193, leg_rt_switch_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                cmds.parent('leg_lf_switch', 'leg_lf_switch_grp')
                cmds.parent('leg_rt_switch', 'leg_rt_switch_grp')
                
                leg_ctrl_grp = cmds.group(empty=True, n="leg_ctrl_grp")
                cmds.move(0, 8.495, 0.266, leg_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                leg_lf_ctrl_grp = cmds.group(empty=True, p="leg_ctrl_grp", n="leg_lf_ctrl_grp")
                cmds.move(0.967, 8.495, 0.266, leg_lf_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                leg_rt_ctrl_grp = cmds.group(empty=True, p="leg_ctrl_grp", n="leg_rt_ctrl_grp")
                cmds.move(-0.967, 8.495, 0.266, leg_rt_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                
                foot_ctrl_grp = cmds.group(empty=True, n="foot_ctrl_grp")
                cmds.move(0, 0.785, -0.193, foot_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                foot_lf_ik_ctrl_grp = cmds.group(empty=True, p="foot_ctrl_grp", n="foot_lf_ik_ctrl_grp")
                cmds.move(0.967, 0.785, -0.193, foot_lf_ik_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                foot_rt_ik_ctrl_grp = cmds.group(empty=True, p="foot_ctrl_grp", n="foot_rt_ik_ctrl_grp")
                cmds.move(-0.967, 0.785, -0.193, foot_rt_ik_ctrl_grp)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                cmds.parent('foot_lf_ik_ctrl', 'foot_lf_ik_ctrl_grp')
                cmds.parent('foot_rt_ik_ctrl', 'foot_rt_ik_ctrl_grp')
                
                cmds.parent('leg_lf_fk_tight_jnt_ctrl_grp', leg_lf_ctrl_grp)
                cmds.parent('leg_rt_fk_tight_jnt_ctrl_grp', leg_rt_ctrl_grp)
                cmds.parent('leg_lf_ik_shin_jnt_ctrl_grp', leg_lf_ctrl_grp)
                cmds.parent('leg_rt_ik_shin_jnt_ctrl_grp', leg_rt_ctrl_grp)
                
                cmds.rename('leg_lf_ik_shin_jnt_ctrl_grp', 'leg_lf_pv_ctrl_grp')
                cmds.rename('leg_rt_ik_shin_jnt_ctrl_grp', 'leg_rt_pv_ctrl_grp')
                cmds.rename('leg_lf_ik_shin_jnt_ctrl', 'leg_lf_pv_ctrl')
                cmds.rename('leg_rt_ik_shin_jnt_ctrl', 'leg_rt_pv_ctrl')
        
        # Root CTRL
        cmds.group(em=True, n='root_x_ctrl_grp', p='ch_grp')
        root_x_ctrl = cmds.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=5, d=3, ut=0, tol=0.01, s=8, ch=1, n='root_x_ctrl')[0]
        cmds.group(em=True, n='root_y_ctrl_grp', p='ch_grp')
        root_y_ctrl = cmds.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=5.5, d=3, ut=0, tol=0.01, s=8, ch=1, n='root_y_ctrl')[0]
        cmds.group(em=True, n='root_z_ctrl_grp', p='ch_grp')
        root_z_ctrl = cmds.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=6, d=3, ut=0, tol=0.01, s=8, ch=1, n='root_z_ctrl')[0]
        cmds.parent('root_x_ctrl', 'root_x_ctrl_grp')
        cmds.parent('root_y_ctrl', 'root_y_ctrl_grp')
        cmds.parent('root_z_ctrl', 'root_z_ctrl_grp')
        cmds.parent('root_x_ctrl_grp', 'root_y_ctrl')
        cmds.parent('root_y_ctrl_grp', 'root_z_ctrl')
        
        # CTRL Grouping
        ctrl_grp = cmds.group(empty=True, p="ch_grp", n="ctrl_grp")
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        
        cmds.parent(head_ctrl_grp, ctrl_grp)
        cmds.parent(jaw_ctrl_grp, ctrl_grp)
        cmds.parent(neck_ctrl_grp, ctrl_grp)
        cmds.parent(shoulder_ctrl_grp, ctrl_grp)
        cmds.parent(arm_ctrl_grp, ctrl_grp)
        cmds.parent(arm_switch_grp, ctrl_grp)
        cmds.parent(hand_ctrl_grp, ctrl_grp)
        cmds.parent(spine_ctrl_grp, ctrl_grp)
        cmds.parent(pelvis_ctrl_grp, ctrl_grp)
        cmds.parent(leg_ctrl_grp, ctrl_grp)
        cmds.parent(leg_switch_grp, ctrl_grp)
        cmds.parent(foot_ctrl_grp, ctrl_grp)
        cmds.select(clear=True)
        
        # CTRL Coloring
        self.color = 'WHITE'
        cmds.select('*_001_jnt_ctrl', '*_fk_*_ctrl')
        self.coloring_ctrl(self)
        
        self.color = 'YELLOW'
        cmds.select('*_pv_ctrl', '*_ik*_ctrl')
        self.coloring_ctrl(self)
        
        self.color = 'PINK'
        cmds.select('*_switch')
        self.coloring_ctrl(self)
        
        self.color = 'SKYBLUE'
        cmds.select('*_body_ctrl', 'root*ctrl')
        self.coloring_ctrl(self)
    
    
    # Generate CTRL
    def ctrl_gen(self, args):
        
        selectedObjs = cmds.ls(sl=True)
        
        jntPostion = [0,0,0]
        jntAngle = [0,0,0]
        jntAngleSum = [0,0,0]
        ctrl_list = []
        named_ctrl = ''
        
        for idx in range(0, len(selectedObjs)-1):    # Except Tip of Joint
            
            jntPosition = cmds.joint(selectedObjs[idx], q=True, p=True)
            jntAngle = cmds.joint(selectedObjs[idx], q=True, o=True)
            for jdx in range(0, 3):
                jntAngleSum[jdx] = jntAngleSum[jdx] + jntAngle[jdx]
            ctrl_name = selectedObjs[idx] + '_ctrl'
            ctrl_grp_name = ctrl_name +'_grp'
            
            if (self.shape == 'HEAD'):
                ctrl = self.head_ctrl(self)
            elif(self.shape == 'JAW'):
                ctrl = self.jaw_ctrl(self)
            elif(self.shape == 'NECK'):
                ctrl = self.neck_ctrl(self)
            elif(self.shape == 'SHOULDER_L'):
                ctrl = self.shoulder_lf_ctrl(self)
            elif(self.shape == 'SHOULDER_R'):
                ctrl = self.shoulder_rt_ctrl(self)
            elif(self.shape == 'ARM'):
                ctrl = self.circle_ctrl(self)
            elif(self.shape == 'BODY'):
                ctrl = self.body_ctrl(self)
            elif(self.shape == 'PELVIS'):
                ctrl = self.pelvis_ctrl(self)
            elif (self.shape == 'CIRCLE'):
                ctrl = self.circle_ctrl(self)
            elif (self.shape == 'MIDDLE_CIRCLE'):
                ctrl = self.middle_circle_ctrl(self)
            elif (self.shape == 'SMALL_CIRCLE'):
                ctrl = self.small_circle_ctrl(self)
            elif (self.shape == 'CURVED_CIRCLE'):
                ctrl = self.curved_circle_ctrl(self)
            elif (self.shape == 'SQUARE'):
                ctrl = self.square_ctrl(self)
            elif (self.shape == 'CUBE'):
                ctrl = self.cube_ctrl(self)
            elif (self.shape == 'ARROW'):
                ctrl = self.arrow_ctrl(self)
            elif (self.shape == 'SPHERE'):
                ctrl = self.sphere_ctrl(self)
            elif (self.shape == 'ROOT'):
                ctrl = self.root_ctrl(self)
            
            cmds.move(jntPosition[0], jntPosition[1], jntPosition[2], ctrl)
            cmds.rotate(jntAngleSum[0], jntAngleSum[1], jntAngleSum[2], ctrl)
            
            grp = cmds.group(empty=True, n=ctrl_grp_name)
            s = cmds.xform('dummy_root_ctrl', r=True, q=True, s=True)
            
            cmds.scale(s[0], s[1], s[2], ctrl)
            cmds.makeIdentity(apply=True, t=True, r=True, s=True)
            
            cmds.move(jntPosition[0], jntPosition[1], jntPosition[2], grp)
            cmds.rotate(jntAngleSum[0], jntAngleSum[1], jntAngleSum[2], grp)
            cmds.parent(ctrl, grp)
            
            # Freeze CTRL
            cmds.select(grp)
            cmds.makeIdentity(apply=True, t=True, s=True)
            
            named_ctrl = cmds.rename(ctrl, ctrl_name)
            ctrl_list.append(named_ctrl)
        
        # Set Hirarchy of CTRL
        for cdx in range(0, len(ctrl_list)):
            if cdx+1 >= len(ctrl_list):
                break
            cmds.parent(ctrl_list[cdx+1]+'_grp', ctrl_list[cdx])
        
        return named_ctrl
    
    # CTRL Shapes
    def head_ctrl(self, args):
        ctrl = cmds.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=0.75, d=3, ut=0, tol=0.01, s=8, ch=1)[0]
        cmds.select(ctrl+'.cv[0:7]')
        cmds.move(0, 0, -0.9, r=True, os=True, wd=True)
        cmds.rotate(90, 0, 0)
        return ctrl
    
    def jaw_ctrl(self, args):
        ctrl = cmds.curve(d=1, p=[(-0.6, 0, 0), (0.6, 0, 0), (0.4, 0, 1.0), (-0.4, 0, 1.0), (-0.6, 0, 0)])
        return ctrl
    
    def neck_ctrl(self, args):
        ctrl = cmds.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=0.6, d=3, ut=0, tol=0.01, s=8, ch=1)[0]
        cmds.softSelect(sse=1)
        cmds.select(str(ctrl) + '.cv[3]')
        cmds.select(str(ctrl) + '.cv[7]', add=True)
        cmds.move(0, 0.2, 0, r=True)
        cmds.select(str(ctrl) + '.cv[1]')
        cmds.select(str(ctrl) + '.cv[5]', add=True)
        cmds.move(0, -0.2, 0, r=True)
        cmds.select(clear=True)
        return ctrl
    
    def shoulder_lf_ctrl(self, args):
        ctrl = cmds.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=0.2, d=3, ut=0, tol=0.01, s=8, ch=1)[0]
        cmds.softSelect(sse=1)
        cmds.select(str(ctrl) + '.cv[3]')
        cmds.select(str(ctrl) + '.cv[7]', add=True)
        cmds.move(0, 0.2, 0, r=True)
        cmds.select(str(ctrl) + '.cv[1]')
        cmds.select(str(ctrl) + '.cv[5]', add=True)
        cmds.move(0, -0.2, 0, r=True)
        cmds.select(clear=True)
        cmds.softSelect(sse=0)
        cmds.select(str(ctrl) + '.cv[0:7]')
        cmds.move(0, 2, 0, r=True)
        cmds.select(clear=True)
        return ctrl
    
    def shoulder_rt_ctrl(self, args):
        ctrl = cmds.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=0.2, d=3, ut=0, tol=0.01, s=8, ch=1)[0]
        cmds.softSelect(sse=1)
        cmds.select(str(ctrl) + '.cv[3]')
        cmds.select(str(ctrl) + '.cv[7]', add=True)
        cmds.move(0, -0.2, 0, r=True)
        cmds.select(str(ctrl) + '.cv[1]')
        cmds.select(str(ctrl) + '.cv[5]', add=True)
        cmds.move(0, 0.2, 0, r=True)
        cmds.select(clear=True)
        cmds.softSelect(sse=0)
        cmds.select(str(ctrl) + '.cv[0:7]')
        cmds.move(0, -2, 0, r=True)
        cmds.select(clear=True)
        return ctrl
    
    def body_ctrl(self, args):
        ctrl = cmds.curve(d=1, p=[-1.2, 1, -1.3], k=0)
        cmds.curve(ctrl, a=True, d=1, p=[ (-1.2, 1, -1.3), (-1.2, 1, 1), (1.2, 1, 1), (1.2, 1, -1.3), (-1.2, 1, -1.3), (-1.5, -0.66, -1.6), (-1.5, -0.66, 1.3), (-1.2, 1, 1), (-1.5, -0.66, 1.3), (1.5, -0.66, 1.3), (1.2, 1, 1), (1.5, -0.66, 1.3), (1.5, -0.66, -1.6), (1.2, 1, -1.3), (1.5, -0.66, -1.6), (-1.5, -0.66, -1.6) ])
        cmds.select(str(ctrl) +'.cv[0:16]')
        cmds.scale(1.2, 1, 1, r=True)
        return ctrl
    
    def circle_ctrl(self, args):
        # Circle CTRL
        ctrl = cmds.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=1.5, d=3, ut=0, tol=0.01, s=8, ch=1)
        return ctrl[0]
    
    def middle_circle_ctrl(self, args):
        # Circle CTRL
        ctrl = cmds.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=0.75, d=3, ut=0, tol=0.01, s=8, ch=1)
        return ctrl[0]
    
    def small_circle_ctrl(self, args):
        # Circle CTRL
        ctrl = cmds.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=0.25, d=3, ut=0, tol=0.01, s=8, ch=1)
        return ctrl[0]
        
    def curved_circle_ctrl(self, args):
        # Shoulder CTRL
        ctrl = cmds.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=0.6, d=3, ut=0, tol=0.01, s=8, ch=1)[0]
        cmds.softSelect(sse=1)
        cmds.select(str(ctrl) + '.cv[3]')
        cmds.select(str(ctrl) + '.cv[7]', add=True)
        cmds.move(0, 2, 0, r=True)
        cmds.select(str(ctrl) + '.cv[0]')
        cmds.select(str(ctrl) + '.cv[4]', add=True)
        cmds.move(0, -1, 0, r=True)
        cmds.select(clear=True)
        return ctrl
    
    def square_ctrl(self, args):
        # Square CTRL
        ctrl = cmds.curve(d=1, p=[(-0.6, 0, -0.6), (0.6, 0, -0.6), (0.6, 0, 0.6), (-0.6, 0, 0.6), (-0.6, 0, -0.6)])
        return ctrl
    
    def cube_ctrl(self, args):
        # Square CTRL
        ctrl = cmds.curve(d=1, p=[0.5, 0.5, -0.5], k=0)
        cmds.curve(ctrl, a=True, d=1, p=[ (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5) ])
        return ctrl
    
    def pelvis_ctrl(self, args):
        # Pelvis L CTRL
        ctrl = cmds.curve(n='a', d=3,p=[ (17.843656, 20.178663, 17.843148), (12.080365, 22.618025, 18.512651), (7.86362, 39.020472, 7.619858), (-1.752994, 41.604984, 0.00413769), (-1.60196, 26.960052, -14.072872), (12.008345, 20.679325, -19.572681), (24.09459, 30.523275, -11.78492), (24.289722, 30.876347, 11.763753), (17.843656, 20.178663, 17.843148)])
        cmds.scale(0.05, 0.05, 0.05, ctrl)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.closeCurve(ctrl, ch=True, ps=True, rpo=True)
        constraint = cmds.parentConstraint('pelvis_lf_001_jnt', ctrl, w=1, mo=False)
        cmds.delete(constraint)
        cmds.move(1.1, 1.1, 0, ctrl+'.cv[0:8]', r=True)
        return ctrl
    
    def arrow_ctrl(self, args):
        # Arrow CTRL
        ctrl = cmds.curve(d=1, p=[ (0, 0, 0.5), (-0.4, 0, -0.5), (0.4, 0, -0.5), (0, 0, 0.5), (0, 0.4, -0.5), (0, -0.4, -0.5), (0, 0, 0.5) ])
        cmds.select(ctrl+'.cv[0:6]')
        cmds.move(0, 0, -2.5, r=True)
        cmds.select(cl=True)
        return ctrl
    
    def arrow2_ctrl(self, args):
        # Arrow CTRL
        ctrl = cmds.curve(d=1, p=[(0,0,0), (0,0,-5), (-1,0,-3), (1,0,-3), (0,0,-5), (0,1,-3), (0,-1,-3), (0,0,-5)])
        return ctrl
    
    def sphere_ctrl(self, args):
        ctrl = cmds.curve(d=1, p=[ (0, 0.5052389, 0), (0.1307653, 0.4880228, 0), (0.2526193, 0.4375493, 0), (0.3572577, 0.3572577, 0), (0.4375493, 0.2526193, 0), (0.4880228, 0.1307653, 0), (0.5052389, 0, 0), (0.4880228, -0.1307653, 0), (0.4375493, -0.2526193, 0), (0.3572577, -0.3572577, 0), (0.2526193, -0.4375493, 0), (0.1307653, -0.4880228, 0), (0, -0.5052389, 0), (-0.1307653, -0.4880228, 0), (-0.2526193, -0.4375493, 0), (-0.3572577, -0.3572577, 0), (-0.4375493, -0.2526193, 0), (-0.4880228, -0.1307653, 0), (-0.5052389, 0, 0), (-0.4880228, 0.1307653, 0), (-0.4375493, 0.2526193, 0), (-0.3572577, 0.3572577, 0), (-0.2526193, 0.4375493, 0), (-0.1307653, 0.4880228, 0), (0, 0.5052389, 0), (0, 0.4880228, 0.1307653), (0, 0.4375493, 0.2526193), (0, 0.3572577, 0.3572577), (0, 0.2526193, 0.4375493), (0, 0.1307653, 0.4880228), (0, 0, 0.5052389), (0, -0.1307653, 0.4880228), (0, -0.2526193, 0.4375493), (0, -0.3572577, 0.3572577), (0, -0.4375493, 0.2526193), (0, -0.4880228, 0.1307653), (0, -0.5052389, 0), (0, -0.4880228, -0.1307653), (0, -0.4375493, -0.2526193), (0, -0.3572577, -0.3572577), (0, -0.2526193, -0.4375493), (0, -0.1307653, -0.4880228), (0, 0, -0.5052389), (-0.1307653, 0, -0.4880228), (-0.2526193, 0, -0.4375493), (-0.3572577, 0, -0.3572577), (-0.4375493, 0, -0.2526193), (-0.4880228, 0, -0.1307653), (-0.5052389, 0, 0), (-0.4880228, 0, 0.1307653), (-0.4375493, 0, 0.2526193), (-0.3572577, 0, 0.3572577), (-0.2526193, 0, 0.4375493), (-0.1307653, 0, 0.4880228), (0, 0, 0.5052389), (0.1307653, 0, 0.4880228), (0.2526193, 0, 0.4375493), (0.3572577, 0, 0.3572577), (0.4375493, 0, 0.2526193), (0.4880228, 0, 0.1307653), (0.5052389, 0, 0), (0.4880228, 0, -0.1307653), (0.4375493, 0, -0.2526193), (0.3572577, 0, -0.3572577), (0.2526193, 0, -0.4375493), (0.1307653, 0, -0.4880228), (0, 0, -0.5052389), (0, 0.1307653, -0.4880228), (0, 0.2526193, -0.4375493), (0, 0.3572577, -0.3572577), (0, 0.4375493, -0.2526193), (0, 0.4880228, -0.1307653), (0, 0.5052389, 0) ] )
        return ctrl
    
    def foot_lf_ctrl(self, args):
        ctrl = cmds.curve(d=1, p=[0, 0, -2.120128], k=0) 
        cmds.curve(ctrl, a=True, d=1, p=[ (0, 0, -2.120128), (0, 0, -2.120128), (0.127027, 0, -2.098891), (0.266394, 0, -2.035954), (0.392426, 0, -1.923814), (0.51076, 0, -1.7556), (0.570988, 0, -1.45298), (0.547002, 0, -1.124658), (0.546137, 0, -0.739398), (0.596986, 0, -0.424671), (0.749207, 0, 0.167214), (0.821629, 0, 0.540794), (0.845588, 0, 0.814546), (0.819474, 0, 1.166447), (0.740338, 0, 1.442584), (0.639319, 0, 1.672901), (0.518089, 0, 1.859678), (0.395504, 0, 1.9981), (0.267004, 0, 2.095142), (0.134293, 0, 2.163449), (0.00467529, 0, 2.182247), (-0.129434, 0, 2.164107), (-0.263571, 0, 2.097171), (-0.394311, 0, 1.99895), (-0.519026, 0, 1.858581), (-0.639218, 0, 1.673153), (-0.741687, 0, 1.437876), (-0.814669, 0, 1.183211), (-0.845483, 0, 0.813956), (-0.823555, 0, 0.546201), (-0.787024, 0, 0.199789), (-0.740926, 0, -0.141818), (-0.709665, 0, -0.449727), (-0.673223, 0, -0.84127), (-0.647076, 0, -1.105326), (-0.607085, 0, -1.441585), (-0.515494, 0, -1.742999), (-0.403107, 0, -1.909041), (-0.26381, 0, -2.03716), (-0.134123, 0, -2.097657), (0.00016811, 0, -2.1201) ])
        cmds.scale(-0.8, 0.8, 0.8, r=True)
        cmds.move(0.967, 0, 0.3, rpr=True)
        cmds.move(0.967, 0.785, -0.193, ".scalePivot", ".rotatePivot", a=True)
        cmds.select(cl=True)
        return ctrl
    
    def foot_rt_ctrl(self, args):
        ctrl = cmds.curve(d=1, p=[0, 0, -2.120128], k=0) 
        cmds.curve(ctrl, a=True, d=1, p=[ (0, 0, -2.120128), (0, 0, -2.120128), (0.127027, 0, -2.098891), (0.266394, 0, -2.035954), (0.392426, 0, -1.923814), (0.51076, 0, -1.7556), (0.570988, 0, -1.45298), (0.547002, 0, -1.124658), (0.546137, 0, -0.739398), (0.596986, 0, -0.424671), (0.749207, 0, 0.167214), (0.821629, 0, 0.540794), (0.845588, 0, 0.814546), (0.819474, 0, 1.166447), (0.740338, 0, 1.442584), (0.639319, 0, 1.672901), (0.518089, 0, 1.859678), (0.395504, 0, 1.9981), (0.267004, 0, 2.095142), (0.134293, 0, 2.163449), (0.00467529, 0, 2.182247), (-0.129434, 0, 2.164107), (-0.263571, 0, 2.097171), (-0.394311, 0, 1.99895), (-0.519026, 0, 1.858581), (-0.639218, 0, 1.673153), (-0.741687, 0, 1.437876), (-0.814669, 0, 1.183211), (-0.845483, 0, 0.813956), (-0.823555, 0, 0.546201), (-0.787024, 0, 0.199789), (-0.740926, 0, -0.141818), (-0.709665, 0, -0.449727), (-0.673223, 0, -0.84127), (-0.647076, 0, -1.105326), (-0.607085, 0, -1.441585), (-0.515494, 0, -1.742999), (-0.403107, 0, -1.909041), (-0.26381, 0, -2.03716), (-0.134123, 0, -2.097657), (0.00016811, 0, -2.1201) ])
        cmds.scale(0.8, 0.8, 0.8, r=True)
        cmds.move(-0.967, 0, 0.3, rpr=True)
        cmds.move(-0.967, 0.785, -0.193, ".scalePivot", ".rotatePivot", a=True)
        '''
        t = cmds.xform('leg_rt_bind_ball_jnt', a=True, q=True, t=True)
        cmds.move(t[0], t[1], t[2], ctrl)
        t = cmds.xform('leg_rt_bind_ankle_jnt', a=True, q=True, t=True)
        cmds.move(t[0], t[1], t[2], ".scalePivot", ".rotatePivot", a=True)
        '''
        cmds.select(cl=True)
        return ctrl
    
    def root_ctrl(self, args):
        ctrl = cmds.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=5, d=3, ut=0, tol=0.01, s=8, ch=1)[0]
        cmds.rename(ctrl, 'root_ctrl')
        return ctrl
    
    # Coloring CTRL
    def coloring_ctrl(self, args):
        
        sel = cmds.ls(sl=True)
        
        for s in sel:
            cmds.setAttr(str(s) + '.overrideEnabled', 1)
            
            if(self.color == 'BLACK'):
                cmds.setAttr(str(s) + '.overrideColor', 1)
            elif(self.color == 'DARK_GREY'):
                cmds.setAttr(str(s) + '.overrideColor', 2)
            elif(self.color == 'LIGHT_GREY'):
                cmds.setAttr(str(s) + '.overrideColor', 3)
            elif(self.color == 'RED'):
                cmds.setAttr(str(s) + '.overrideColor', 4)
            elif(self.color == 'DEFAULT'):
                cmds.setAttr(str(s) + '.overrideColor', 5) 
            elif(self.color == 'BLUE'):
                cmds.setAttr(str(s) + '.overrideColor', 6)
            elif(self.color == 'DARK_GREEN'):
                cmds.setAttr(str(s) + '.overrideColor', 7)
            elif(self.color == 'PINK'):
                cmds.setAttr(str(s) + '.overrideColor', 9)
            elif(self.color == 'YELLOW'):
                cmds.setAttr(str(s) + '.overrideColor', 13)
            elif(self.color == 'WHITE'):
                cmds.setAttr(str(s) + '.overrideColor', 16)
            elif(self.color == 'LIGHT_GREEN'):
                cmds.setAttr(str(s) + '.overrideColor', 17)
            elif(self.color == 'SKYBLUE'):
                cmds.setAttr(str(s) + '.overrideColor', 18)
            elif(self.color == 'MINT'):
                cmds.setAttr(str(s) + '.overrideColor', 19)
            elif(self.color == 'APRICOT'):    # 살구색
                cmds.setAttr(str(s) + '.overrideColor', 20)
            elif(self.color == 'PURPLE'):
                cmds.setAttr(str(s) + '.overrideColor', 31)
        
        cmds.select(cl=True)
    
    
    def fix_ctrl(self, args):
        '''
            STEP 4: Fix the CTRLs (Build)
        '''
        
        # Head
        cmds.parentConstraint('head_001_jnt_ctrl', 'head_001_jnt', w=1, mo=True)
        
        # Jaw
        cmds.parentConstraint('jaw_001_jnt_ctrl', 'jaw_001_jnt', w=1, mo=True)
        
        # Neck
        cmds.parentConstraint('neck_001_jnt_ctrl', 'neck_001_jnt', w=1, mo=True)
        cmds.parentConstraint('neck_002_jnt_ctrl', 'neck_002_jnt', w=1, mo=True)
        
        # Shoulder
        ## Shoulder CTRL
        cmds.parentConstraint('shoulder_lf_001_jnt_ctrl', 'shoulder_lf_001_jnt', w=1, mo=True)
        cmds.parentConstraint('shoulder_rt_001_jnt_ctrl', 'shoulder_rt_001_jnt', w=1, mo=True)
        
        cmds.pointConstraint('shoulder_lf_002_jnt', 'arm_lf_jnt_grp', w=1, mo=True)
        cmds.pointConstraint('shoulder_rt_002_jnt', 'arm_rt_jnt_grp', w=1, mo=True)
        cmds.pointConstraint('shoulder_lf_002_jnt', 'arm_lf_fk_shoulder_jnt_ctrl_grp', w=1, mo=True)
        cmds.pointConstraint('shoulder_rt_002_jnt', 'arm_rt_fk_shoulder_jnt_ctrl_grp', w=1, mo=True)
        
        ## Add Shoulder Atribute
        
        
        # Arm
        ## Set Arm CTRL
        cmds.parentConstraint('arm_lf_fk_shoulder_jnt_ctrl', 'arm_lf_fk_shoulder_jnt', w=1, mo=True)
        cmds.parentConstraint('arm_lf_fk_elbow_jnt_ctrl', 'arm_lf_fk_elbow_jnt', w=1, mo=True)
        cmds.parentConstraint('arm_lf_fk_wrist_jnt_ctrl', 'arm_lf_fk_wrist_jnt', w=1, mo=True)
        
        cmds.parentConstraint('arm_rt_fk_shoulder_jnt_ctrl', 'arm_rt_fk_shoulder_jnt', w=1, mo=True)
        cmds.parentConstraint('arm_rt_fk_elbow_jnt_ctrl', 'arm_rt_fk_elbow_jnt', w=1, mo=True)
        cmds.parentConstraint('arm_rt_fk_wrist_jnt_ctrl', 'arm_rt_fk_wrist_jnt', w=1, mo=True)
        
        ## Create Arm IK Handles
        ik_handle = cmds.ikHandle(sj='arm_lf_ik_shoulder_jnt', ee='arm_lf_ik_wrist_jnt', sol='ikRPsolver', p=2, w=1)[0]
        cmds.rename(ik_handle, 'lf_wrist_ikHandle')
        ik_handle = cmds.ikHandle(sj='arm_lf_ik_wrist_jnt', ee='arm_lf_ik_hand_jnt', sol='ikSCsolver', p=2, w=1)[0]
        cmds.rename(ik_handle, 'lf_hand_ikHandle')
        #, aim=(0.0, -1.0, 0.0), wut='object', wuo='arm_lf_ik_elbow_jnt'
        #cmds.aimConstraint()
        cmds.poleVectorConstraint('arm_lf_pv_ctrl', 'lf_wrist_ikHandle', w=1)
        cmds.parent('lf_hand_ikHandle', 'lf_wrist_ikHandle')
        cmds.parent('lf_wrist_ikHandle', 'arm_lf_ik_wrist_jnt_ctrl')
        
        ik_handle = cmds.ikHandle(sj='arm_rt_ik_shoulder_jnt', ee='arm_rt_ik_wrist_jnt', sol='ikRPsolver', p=2, w=1)[0]
        cmds.rename(ik_handle, 'rt_wrist_ikHandle')
        ik_handle = cmds.ikHandle(sj='arm_rt_ik_wrist_jnt', ee='arm_rt_ik_hand_jnt', sol='ikSCsolver', p=2, w=1)[0]
        cmds.rename(ik_handle, 'rt_hand_ikHandle')
        cmds.poleVectorConstraint('arm_rt_pv_ctrl', 'rt_wrist_ikHandle', w=1)
        cmds.parent('rt_hand_ikHandle', 'rt_wrist_ikHandle')
        cmds.parent('rt_wrist_ikHandle', 'arm_rt_ik_wrist_jnt_ctrl')
        
        cmds.setAttr('arm_lf_ik_wrist_jnt_ctrl.sx', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_ik_wrist_jnt_ctrl.sy', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_ik_wrist_jnt_ctrl.sz', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_ik_wrist_jnt_ctrl.v', l=True, k=False, cb=False)
        
        cmds.setAttr('arm_lf_pv_ctrl.sx', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_pv_ctrl.sy', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_pv_ctrl.sz', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_pv_ctrl.rx', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_pv_ctrl.ry', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_pv_ctrl.rz', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_pv_ctrl.v', l=True, k=False, cb=False)
        
        cmds.setAttr('arm_rt_ik_wrist_jnt_ctrl.sx', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_ik_wrist_jnt_ctrl.sy', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_ik_wrist_jnt_ctrl.sz', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_ik_wrist_jnt_ctrl.v', l=True, k=False, cb=False)
        
        cmds.setAttr('arm_rt_pv_ctrl.sx', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_pv_ctrl.sy', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_pv_ctrl.sz', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_pv_ctrl.rx', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_pv_ctrl.ry', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_pv_ctrl.rz', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_pv_ctrl.v', l=True, k=False, cb=False)
        
        # Hand
        cmds.parentConstraint('arm_lf_bind_wrist_jnt', 'hand_lf_ctrl_grp', w=1, mo=True)
        cmds.parentConstraint('arm_rt_bind_wrist_jnt', 'hand_rt_ctrl_grp', w=1, mo=True)
        
        ## Set Left Hand CTRL
        cmds.parentConstraint('thumb_lf_001_jnt_ctrl', 'thumb_lf_001_jnt', w=1, mo=True)
        cmds.parentConstraint('thumb_lf_002_jnt_ctrl', 'thumb_lf_002_jnt', w=1, mo=True)
        cmds.parentConstraint('thumb_lf_003_jnt_ctrl', 'thumb_lf_003_jnt', w=1, mo=True)
        
        cmds.parentConstraint('index_lf_001_jnt_ctrl', 'index_lf_001_jnt', w=1, mo=True)
        cmds.parentConstraint('index_lf_002_jnt_ctrl', 'index_lf_002_jnt', w=1, mo=True)
        cmds.parentConstraint('index_lf_003_jnt_ctrl', 'index_lf_003_jnt', w=1, mo=True)
        
        cmds.parentConstraint('middle_lf_001_jnt_ctrl', 'middle_lf_001_jnt', w=1, mo=True)
        cmds.parentConstraint('middle_lf_002_jnt_ctrl', 'middle_lf_002_jnt', w=1, mo=True)
        cmds.parentConstraint('middle_lf_003_jnt_ctrl', 'middle_lf_003_jnt', w=1, mo=True)
        
        cmds.parentConstraint('ring_lf_001_jnt_ctrl', 'ring_lf_001_jnt', w=1, mo=True)
        cmds.parentConstraint('ring_lf_002_jnt_ctrl', 'ring_lf_002_jnt', w=1, mo=True)
        cmds.parentConstraint('ring_lf_003_jnt_ctrl', 'ring_lf_003_jnt', w=1, mo=True)
        
        cmds.parentConstraint('pinky_lf_001_jnt_ctrl', 'pinky_lf_001_jnt', w=1, mo=True)
        cmds.parentConstraint('pinky_lf_002_jnt_ctrl', 'pinky_lf_002_jnt', w=1, mo=True)
        cmds.parentConstraint('pinky_lf_003_jnt_ctrl', 'pinky_lf_003_jnt', w=1, mo=True)
        
        ## Set Right Hand CTRL
        cmds.parentConstraint('thumb_rt_001_jnt_ctrl', 'thumb_rt_001_jnt', w=1, mo=True)
        cmds.parentConstraint('thumb_rt_002_jnt_ctrl', 'thumb_rt_002_jnt', w=1, mo=True)
        cmds.parentConstraint('thumb_rt_003_jnt_ctrl', 'thumb_rt_003_jnt', w=1, mo=True)
        
        cmds.parentConstraint('index_rt_001_jnt_ctrl', 'index_rt_001_jnt', w=1, mo=True)
        cmds.parentConstraint('index_rt_002_jnt_ctrl', 'index_rt_002_jnt', w=1, mo=True)
        cmds.parentConstraint('index_rt_003_jnt_ctrl', 'index_rt_003_jnt', w=1, mo=True)
        
        cmds.parentConstraint('middle_rt_001_jnt_ctrl', 'middle_rt_001_jnt', w=1, mo=True)
        cmds.parentConstraint('middle_rt_002_jnt_ctrl', 'middle_rt_002_jnt', w=1, mo=True)
        cmds.parentConstraint('middle_rt_003_jnt_ctrl', 'middle_rt_003_jnt', w=1, mo=True)
        
        cmds.parentConstraint('ring_rt_001_jnt_ctrl', 'ring_rt_001_jnt', w=1, mo=True)
        cmds.parentConstraint('ring_rt_002_jnt_ctrl', 'ring_rt_002_jnt', w=1, mo=True)
        cmds.parentConstraint('ring_rt_003_jnt_ctrl', 'ring_rt_003_jnt', w=1, mo=True)
        
        cmds.parentConstraint('pinky_rt_001_jnt_ctrl', 'pinky_rt_001_jnt', w=1, mo=True)
        cmds.parentConstraint('pinky_rt_002_jnt_ctrl', 'pinky_rt_002_jnt', w=1, mo=True)
        cmds.parentConstraint('pinky_rt_003_jnt_ctrl', 'pinky_rt_003_jnt', w=1, mo=True)
        
        
        # Spine
        ## Set Spine CTRL
        cmds.parentConstraint('spine_fk_001_jnt', 'lower_body_ctrl_grp', w=1, mo=True)
        cmds.parentConstraint('spine_fk_009_jnt', 'upper_body_ctrl_grp', w=1, mo=True)
        
        cmds.parentConstraint('spine_fk_001_jnt_ctrl', 'spine_fk_001_jnt', w=1, mo=True)
        cmds.parentConstraint('spine_fk_002_jnt_ctrl', 'spine_fk_002_jnt', w=1, mo=True)
        cmds.parentConstraint('spine_fk_006_jnt_ctrl', 'spine_fk_006_jnt', w=1, mo=True)
        
        ## Create Spine IK Handles 
        ik_handle = cmds.ikHandle(sj='spine_ik_bind_001_jnt', ee='spine_ik_bind_009_jnt', sol='ikSplineSolver', ns=4)[0]
        cmds.parent(ik_handle, 'spine_jnt_grp')
        cmds.rename(ik_handle, 'spine_ik_bind_001_ikHandle')
        cmds.rename('curve1', 'spine_ik_bind_001_crv')
        cmds.parentConstraint('spine_fk_001_jnt_ctrl', 'spine_fk_001_jnt', w=1, mo=True)
        cmds.parentConstraint('spine_fk_002_jnt_ctrl', 'spine_fk_002_jnt', w=1, mo=True)
        cmds.parentConstraint('spine_fk_006_jnt_ctrl', 'spine_fk_006_jnt', w=1, mo=True)
        cmds.skinCluster('lower_body_jnt', 'upper_body_jnt', 'spine_ik_bind_001_crv', dr=4.5)    # bindSkin() ERR
        cmds.parentConstraint('spine_fk_001_jnt', 'lower_body_ctrl_grp', w=1, mo=True)
        cmds.parentConstraint('spine_fk_009_jnt', 'upper_body_ctrl_grp', w=1, mo=True)
        
        # Pelvis
        ## Set Pelvis CTRL
        cmds.parentConstraint('pelvis_lf_001_jnt_ctrl', 'pelvis_lf_001_jnt', w=1, mo=True)
        cmds.parentConstraint('pelvis_rt_001_jnt_ctrl', 'pelvis_rt_001_jnt', w=1, mo=True)
        
        ## Set Pelvis Follow Leg Joint
        cmds.pointConstraint('pelvis_lf_002_jnt', 'leg_lf_jnt_grp', w=1, mo=True)
        cmds.pointConstraint('pelvis_rt_002_jnt', 'leg_rt_jnt_grp', w=1, mo=True)
        cmds.pointConstraint('pelvis_lf_002_jnt', 'leg_lf_fk_tight_jnt_ctrl_grp', w=1, mo=True)
        cmds.pointConstraint('pelvis_rt_002_jnt', 'leg_rt_fk_tight_jnt_ctrl_grp', w=1, mo=True)
        
        
        # Leg
        ## Create Leg IK Hadles
        ik_handle = cmds.ikHandle(sj='leg_lf_ik_tight_jnt', ee='leg_lf_ik_ankle_jnt', sol='ikRPsolver', p=2, w=1)[0]
        cmds.rename(ik_handle, 'lf_ankle_ikHandle')
        ik_handle = cmds.ikHandle(sj='leg_lf_ik_ankle_jnt', ee='leg_lf_ik_ball_jnt', sol='ikSCsolver', p=2, w=1)[0]
        cmds.rename(ik_handle, 'lf_ankleToBall_ikHandle')
        ik_handle = cmds.ikHandle(sj='leg_lf_ik_ball_jnt', ee='leg_lf_ik_toe_jnt', sol='ikSCsolver', p=2, w=1)[0]
        cmds.rename(ik_handle, 'lf_ballToToe_ikHandle')
        cmds.poleVectorConstraint('leg_lf_pv_ctrl', 'lf_ankle_ikHandle', w=1)
        
        ik_handle = cmds.ikHandle(sj='leg_rt_ik_tight_jnt', ee='leg_rt_ik_ankle_jnt', sol='ikRPsolver', p=2, w=1)[0]
        cmds.rename(ik_handle, 'rt_ankle_ikHandle')
        ik_handle = cmds.ikHandle(sj='leg_rt_ik_ankle_jnt', ee='leg_rt_ik_ball_jnt', sol='ikSCsolver', p=2, w=1)[0]
        cmds.rename(ik_handle, 'rt_ankleToBall_ikHandle')
        ik_handle = cmds.ikHandle(sj='leg_rt_ik_ball_jnt', ee='leg_rt_ik_toe_jnt', sol='ikSCsolver', p=2, w=1)[0]
        cmds.rename(ik_handle, 'rt_ballToToe_ikHandle')
        cmds.poleVectorConstraint('leg_rt_pv_ctrl', 'rt_ankle_ikHandle', w=1)
        
        ## Create Leg CTRL
        cmds.parentConstraint('leg_lf_fk_tight_jnt_ctrl', 'leg_lf_fk_tight_jnt', w=1, mo=True)
        cmds.parentConstraint('leg_lf_fk_shin_jnt_ctrl', 'leg_lf_fk_shin_jnt', w=1, mo=True)
        cmds.parentConstraint('leg_lf_fk_ankle_jnt_ctrl', 'leg_lf_fk_ankle_jnt', w=1, mo=True)
        cmds.parentConstraint('leg_lf_fk_ball_jnt_ctrl', 'leg_lf_fk_ball_jnt', w=1, mo=True)
        
        cmds.parentConstraint('leg_rt_fk_tight_jnt_ctrl', 'leg_rt_fk_tight_jnt', w=1, mo=True)
        cmds.parentConstraint('leg_rt_fk_shin_jnt_ctrl', 'leg_rt_fk_shin_jnt', w=1, mo=True)
        cmds.parentConstraint('leg_rt_fk_ankle_jnt_ctrl', 'leg_rt_fk_ankle_jnt', w=1, mo=True)
        cmds.parentConstraint('leg_rt_fk_ball_jnt_ctrl', 'leg_rt_fk_ball_jnt', w=1, mo=True)
        
        
        # Foot
        ## Add Foot Atribute
        foot_ik_lf_bank_grp = cmds.group(empty=True, n="foot_ik_lf_bank_grp")
        cmds.move(0.967, 0.186, 0.733, foot_ik_lf_bank_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.joint(a=True, p=[0.967, 0.186, -0.632], rad=0.1, n='heel_ik_lf_ctrl_jnt')
        cmds.joint(a=True, p=[0.967, 0.186, 0.733], rad=0.1, n='ball_twist_ik_lf_ctrl_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0.967, 0.186, 1.418], rad=0.1, n='toe_ik_lf_ctrl_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0.967, 0.186, 0.733], rad=0.1, n='ball_lift_ik_lf_ctrl_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0.967, 0.785, -0.193], rad=0.1, n='ankle_ik_lf_ctrl_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('heel_ik_lf_ctrl_jnt', hi=True)
        cmds.joint(e=True, oj='yzx', sao='zup', ch=True, zso=True)
        cmds.select(clear=True)
        
        cmds.spaceLocator(a=True, p=[1.475, 0.181, 0.769], n='lf_L_bank_loc')
        cmds.xform(r=True, cp=True)
        cmds.spaceLocator(a=True, p=[0.736, 0.181, 0.769], n='lf_R_bank_loc')
        cmds.xform(r=True, cp=True)
        cmds.spaceLocator(a=True, p=[0.967, 0.181, 1.418], n='lf_F_bank_loc')
        cmds.xform(r=True, cp=True)
        
        cmds.parent('foot_ik_lf_bank_grp', 'foot_lf_ik_ctrl')
        cmds.parent('lf_L_bank_loc', 'foot_lf_ik_ctrl')
        cmds.parent('lf_R_bank_loc', 'foot_lf_ik_ctrl')
        cmds.parent('lf_F_bank_loc', 'foot_lf_ik_ctrl')
        #
        foot_ik_rt_bank_grp = cmds.group(empty=True, n="foot_ik_rt_bank_grp")
        cmds.move(-0.967, 0.186, 0.733, foot_ik_rt_bank_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.joint(a=True, p=[-0.967, 0.186, -0.632], rad=0.1, n='heel_ik_rt_ctrl_jnt')
        cmds.joint(a=True, p=[-0.967, 0.186, 0.733], rad=0.1, n='ball_twist_ik_rt_ctrl_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[-0.967, 0.186, 1.418], rad=0.1, n='toe_ik_rt_ctrl_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[-0.967, 0.186, 0.733], rad=0.1, n='ball_lift_ik_rt_ctrl_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[-0.967, 0.785, -0.193], rad=0.1, n='ankle_ik_rt_ctrl_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('heel_ik_rt_ctrl_jnt', hi=True)
        cmds.joint(e=True, oj='yzx', sao='zup', ch=True, zso=True)
        cmds.select(clear=True)
        
        cmds.parent('lf_ankle_ikHandle', 'ankle_ik_lf_ctrl_jnt')
        cmds.parent('lf_ankleToBall_ikHandle', 'ball_lift_ik_lf_ctrl_jnt')
        cmds.parent('lf_ballToToe_ikHandle', 'toe_ik_lf_ctrl_jnt')
        
        cmds.parent('rt_ankle_ikHandle', 'ankle_ik_rt_ctrl_jnt')
        cmds.parent('rt_ankleToBall_ikHandle', 'ball_lift_ik_rt_ctrl_jnt')
        cmds.parent('rt_ballToToe_ikHandle', 'toe_ik_rt_ctrl_jnt')
        
        cmds.spaceLocator(r=True, p=[-1.475, 0.181, 0.769], n='rt_L_bank_loc')
        cmds.xform(r=True, cp=True)
        cmds.spaceLocator(r=True, p=[-0.736, 0.181, 0.769], n='rt_R_bank_loc')
        cmds.xform(r=True, cp=True)
        cmds.spaceLocator(a=True, p=[-0.967, 0.181, 1.418], n='rt_F_bank_loc')
        cmds.xform(r=True, cp=True)
        
        cmds.parent('foot_ik_rt_bank_grp', 'foot_rt_ik_ctrl')
        cmds.parent('rt_L_bank_loc', 'foot_rt_ik_ctrl')
        cmds.parent('rt_R_bank_loc', 'foot_rt_ik_ctrl')
        cmds.parent('rt_F_bank_loc', 'foot_rt_ik_ctrl')
        
        cmds.parentConstraint('lf_L_bank_loc', 'foot_ik_lf_bank_grp', w=1, mo=True)
        cmds.parentConstraint('lf_R_bank_loc', 'foot_ik_lf_bank_grp', w=1, mo=True)
        cmds.parentConstraint('lf_F_bank_loc', 'foot_ik_lf_bank_grp', w=1, mo=True)
        cmds.parentConstraint('rt_L_bank_loc', 'foot_ik_rt_bank_grp', w=1, mo=True)
        cmds.parentConstraint('rt_R_bank_loc', 'foot_ik_rt_bank_grp', w=1, mo=True)
        cmds.parentConstraint('rt_F_bank_loc', 'foot_ik_rt_bank_grp', w=1, mo=True)
        
        cmds.setAttr('heel_ik_lf_ctrl_jnt.visibility', 0)
        cmds.setAttr('lf_L_bank_loc.visibility', 0)
        cmds.setAttr('lf_R_bank_loc.visibility', 0)
        cmds.setAttr('lf_F_bank_loc.visibility', 0)
        cmds.setAttr('heel_ik_rt_ctrl_jnt.visibility', 0)
        cmds.setAttr('rt_L_bank_loc.visibility', 0)
        cmds.setAttr('rt_R_bank_loc.visibility', 0)
        cmds.setAttr('rt_F_bank_loc.visibility', 0)
        #
        
        # Attach Switch to IK CTRL
        cmds.parentConstraint('arm_lf_bind_wrist_jnt', 'arm_lf_switch', w=1, mo=True)
        cmds.parentConstraint('arm_rt_bind_wrist_jnt', 'arm_rt_switch', w=1, mo=True)
        
        cmds.parentConstraint('leg_lf_bind_ankle_jnt', 'leg_lf_switch', w=1, mo=True)
        cmds.parentConstraint('leg_rt_bind_ankle_jnt', 'leg_rt_switch', w=1, mo=True)
        
        # Hide ikHandles
        cmds.select('*_ikHandle')
        sel = cmds.ls(sl=True)
        for s in sel:
            cmds.setAttr(s+'.visibility', 0)
        
        cmds.select(clear=True)
        
        # Set Driven Key
        ## FK CTRLs
        cmds.select('*_fk_*_jnt_ctrl', '*_00*_jnt_ctrl')
        cmds.select('spine_*', d=True)
        fk = cmds.ls(sl=True)
        
        for f in fk:
            cmds.setAttr(f+'.tx', l=True, k=False, cb=False)
            cmds.setAttr(f+'.ty', l=True, k=False, cb=False)
            cmds.setAttr(f+'.tz', l=True, k=False, cb=False)
            cmds.setAttr(f+'.sx', l=True, k=False, cb=False)
            cmds.setAttr(f+'.sy', l=True, k=False, cb=False)
            cmds.setAttr(f+'.sz', l=True, k=False, cb=False)
            cmds.setAttr(f+'.v', l=True, k=False, cb=False)
        
        cmds.select('spine_fk_00*_jnt_ctrl')
        spinefk = cmds.ls(sl=True)
        
        for sf in spinefk:
            cmds.setAttr(sf+'.sx', l=True, k=False, cb=False)
            cmds.setAttr(sf+'.sy', l=True, k=False, cb=False)
            cmds.setAttr(sf+'.sz', l=True, k=False, cb=False)
            cmds.setAttr(sf+'.v', l=True, k=False, cb=False)
        
        cmds.select(clear=True)
        
        ## IK_FK Switch
        ### Left Arm Switch
        cmds.setAttr('arm_lf_switch.tx', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_switch.ty', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_switch.tz', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_switch.rx', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_switch.ry', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_switch.rz', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_switch.sx', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_switch.sy', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_switch.sz', l=True, k=False, cb=False)
        cmds.setAttr('arm_lf_switch.v', l=True, k=False, cb=False)
        
        cmds.select('arm_lf_switch')
        cmds.addAttr(ln='IK_FK', at='double', min=0, max=10, dv=0)
        cmds.setAttr('arm_lf_switch.IK_FK', 0, k=True)
        cmds.addAttr(ln='Thumb_Curl', at='double', min=-10, max=10, dv=0)
        cmds.setAttr('arm_lf_switch.Thumb_Curl', 0, k=True)
        cmds.addAttr(ln='Index_Curl', at='double', min=-10, max=10, dv=0)
        cmds.setAttr('arm_lf_switch.Index_Curl', 0, k=True)
        cmds.addAttr(ln='Middle_Curl', at='double', min=-10, max=10, dv=0)
        cmds.setAttr('arm_lf_switch.Middle_Curl', 0, k=True)
        cmds.addAttr(ln='Ring_Curl', at='double', min=-10, max=10, dv=0)
        cmds.setAttr('arm_lf_switch.Ring_Curl', 0, k=True)
        cmds.addAttr(ln='Pinky_Curl', at='double', min=-10, max=10, dv=0)
        cmds.setAttr('arm_lf_switch.Pinky_Curl', 0, k=True)
        cmds.addAttr(ln='Spread', at='double', min=-10, max=10, dv=0)
        cmds.setAttr('arm_lf_switch.Spread', 0, k=True)
        
        cmds.setAttr('arm_lf_switch.IK_FK', 0)
        cmds.setAttr('arm_lf_fk_shoulder_jnt_ctrl_grp.visibility', 0)
        cmds.setAttr('arm_lf_ik_wrist_jnt_ctrl_grp.visibility', 1)
        cmds.setAttr('arm_lf_pv_ctrl_grp.visibility', 1)
        cmds.setDrivenKeyframe('arm_lf_pv_ctrl_grp.visibility', cd='arm_lf_switch.IK_FK')
        cmds.setDrivenKeyframe('arm_lf_ik_wrist_jnt_ctrl_grp.visibility', cd='arm_lf_switch.IK_FK')
        cmds.setDrivenKeyframe('arm_lf_fk_shoulder_jnt_ctrl_grp.visibility', cd='arm_lf_switch.IK_FK')
        cmds.setAttr('arm_lf_switch.IK_FK', 10)
        cmds.setAttr('arm_lf_fk_shoulder_jnt_ctrl_grp.visibility', 1)
        cmds.setAttr('arm_lf_ik_wrist_jnt_ctrl_grp.visibility', 0)
        cmds.setAttr('arm_lf_pv_ctrl_grp.visibility', 0)
        cmds.setDrivenKeyframe('arm_lf_pv_ctrl_grp.visibility', cd='arm_lf_switch.IK_FK')
        cmds.setDrivenKeyframe('arm_lf_ik_wrist_jnt_ctrl_grp.visibility', cd='arm_lf_switch.IK_FK')
        cmds.setDrivenKeyframe('arm_lf_fk_shoulder_jnt_ctrl_grp.visibility', cd='arm_lf_switch.IK_FK')
        
        cmds.setAttr('arm_lf_switch.IK_FK', 0)
        
        ### Left Hand Attributes
        #### Create Groups for Curl Attributes
        cmds.select('thumb_lf_001_jnt_ctrl', hi=True)
        cmds.select('index_lf_001_jnt_ctrl', hi=True, add=True)
        cmds.select('middle_lf_001_jnt_ctrl', hi=True, add=True)
        cmds.select('ring_lf_001_jnt_ctrl', hi=True, add=True)
        cmds.select('pinky_lf_001_jnt_ctrl', hi=True, add=True)
        
        selectedObjs = cmds.ls(sl=True)
        ctrl_list = []
        
        for sel in selectedObjs:
            shapeNode = cmds.listRelatives(sel, shapes=True)
            nodeType = cmds.nodeType(shapeNode)
                
            if(nodeType=='nurbsCurve'):
                ctrl_list.append(sel)
                print sel
        
        for cl in ctrl_list:
            name = cl +'_curl_grp'
            cl_grp = cmds.group(cl, n=name)
            
            jnt = cl.replace('_ctrl_curl_grp', '')
            jnt_pos = cmds.xform(jnt, q=True, ws=True, rp=True)
            
            cmds.select(cl_grp)
            cmds.move(jnt_pos[0], jnt_pos[1], jnt_pos[2], ".scalePivot", ".rotatePivot", a=True)
        
        #### Create Groups for Spread Attributes
        cmds.select('thumb_lf_001_jnt_ctrl_curl_grp')
        cmds.select('index_lf_001_jnt_ctrl_curl_grp', add=True)
        cmds.select('middle_lf_001_jnt_ctrl_curl_grp', add=True)
        cmds.select('ring_lf_001_jnt_ctrl_curl_grp', add=True)
        cmds.select('pinky_lf_001_jnt_ctrl_curl_grp', add=True)
        
        selectedObjs = cmds.ls(sl=True)
        ctrl_list = []
        
        for sel in selectedObjs:
            name = sel.replace('curl', 'spread')
            sel_grp = cmds.group(sel, n=name)
            
            jnt = sel.replace('_ctrl_curl_grp', '')
            jnt_pos = cmds.xform(jnt, q=True, ws=True, rp=True)
            
            cmds.select(sel_grp)
            cmds.move(jnt_pos[0], jnt_pos[1], jnt_pos[2], ".scalePivot", ".rotatePivot", a=True)
        
        #### Set Finger Curl Attributes
        cmds.setAttr('arm_lf_switch.Thumb_Curl', 0)
        cmds.setAttr('thumb_lf_001_jnt_ctrl_curl_grp.rx', 0)
        cmds.setAttr('thumb_lf_002_jnt_ctrl_curl_grp.rx', 0)
        cmds.setAttr('thumb_lf_003_jnt_ctrl_curl_grp.rx', 0)
        cmds.setDrivenKeyframe('thumb_lf_001_jnt_ctrl_curl_grp.rx', cd='arm_lf_switch.Thumb_Curl')
        cmds.setDrivenKeyframe('thumb_lf_002_jnt_ctrl_curl_grp.rx', cd='arm_lf_switch.Thumb_Curl')
        cmds.setDrivenKeyframe('thumb_lf_003_jnt_ctrl_curl_grp.rx', cd='arm_lf_switch.Thumb_Curl')
        cmds.setAttr('arm_lf_switch.Thumb_Curl', 10)
        cmds.setAttr('thumb_lf_001_jnt_ctrl_curl_grp.rx', -40)
        cmds.setAttr('thumb_lf_002_jnt_ctrl_curl_grp.rx', -40)
        cmds.setAttr('thumb_lf_003_jnt_ctrl_curl_grp.rx', -40)
        cmds.setDrivenKeyframe('thumb_lf_001_jnt_ctrl_curl_grp.rx', cd='arm_lf_switch.Thumb_Curl')
        cmds.setDrivenKeyframe('thumb_lf_002_jnt_ctrl_curl_grp.rx', cd='arm_lf_switch.Thumb_Curl')
        cmds.setDrivenKeyframe('thumb_lf_003_jnt_ctrl_curl_grp.rx', cd='arm_lf_switch.Thumb_Curl')
        cmds.setAttr('arm_lf_switch.Thumb_Curl', -10)
        cmds.setAttr('thumb_lf_001_jnt_ctrl_curl_grp.rx', 40)
        cmds.setAttr('thumb_lf_002_jnt_ctrl_curl_grp.rx', 40)
        cmds.setAttr('thumb_lf_003_jnt_ctrl_curl_grp.rx', 40)
        cmds.setDrivenKeyframe('thumb_lf_001_jnt_ctrl_curl_grp.rx', cd='arm_lf_switch.Thumb_Curl')
        cmds.setDrivenKeyframe('thumb_lf_002_jnt_ctrl_curl_grp.rx', cd='arm_lf_switch.Thumb_Curl')
        cmds.setDrivenKeyframe('thumb_lf_003_jnt_ctrl_curl_grp.rx', cd='arm_lf_switch.Thumb_Curl')
        cmds.setAttr('arm_lf_switch.Thumb_Curl', 0)
        
        cmds.setAttr('arm_lf_switch.Index_Curl', 0)
        cmds.setAttr('index_lf_001_jnt_ctrl_curl_grp.rz', 0)
        cmds.setAttr('index_lf_002_jnt_ctrl_curl_grp.rz', 0)
        cmds.setAttr('index_lf_003_jnt_ctrl_curl_grp.rz', 0)
        cmds.setDrivenKeyframe('index_lf_001_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Index_Curl')
        cmds.setDrivenKeyframe('index_lf_002_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Index_Curl')
        cmds.setDrivenKeyframe('index_lf_003_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Index_Curl')
        cmds.setAttr('arm_lf_switch.Index_Curl', 10)
        cmds.setAttr('index_lf_001_jnt_ctrl_curl_grp.rz', -40)
        cmds.setAttr('index_lf_002_jnt_ctrl_curl_grp.rz', -40)
        cmds.setAttr('index_lf_003_jnt_ctrl_curl_grp.rz', -40)
        cmds.setDrivenKeyframe('index_lf_001_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Index_Curl')
        cmds.setDrivenKeyframe('index_lf_002_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Index_Curl')
        cmds.setDrivenKeyframe('index_lf_003_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Index_Curl')
        cmds.setAttr('arm_lf_switch.Index_Curl', -10)
        cmds.setAttr('index_lf_001_jnt_ctrl_curl_grp.rz', 40)
        cmds.setAttr('index_lf_002_jnt_ctrl_curl_grp.rz', 40)
        cmds.setAttr('index_lf_003_jnt_ctrl_curl_grp.rz', 40)
        cmds.setDrivenKeyframe('index_lf_001_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Index_Curl')
        cmds.setDrivenKeyframe('index_lf_002_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Index_Curl')
        cmds.setDrivenKeyframe('index_lf_003_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Index_Curl')
        cmds.setAttr('arm_lf_switch.Index_Curl', 0)
        
        cmds.setAttr('arm_lf_switch.Middle_Curl', 0)
        cmds.setAttr('middle_lf_001_jnt_ctrl_curl_grp.rz', 0)
        cmds.setAttr('middle_lf_002_jnt_ctrl_curl_grp.rz', 0)
        cmds.setAttr('middle_lf_003_jnt_ctrl_curl_grp.rz', 0)
        cmds.setDrivenKeyframe('middle_lf_001_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Middle_Curl')
        cmds.setDrivenKeyframe('middle_lf_002_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Middle_Curl')
        cmds.setDrivenKeyframe('middle_lf_003_jnt_ctrl_grp.rz', cd='arm_lf_switch.Middle_Curl')
        cmds.setAttr('arm_lf_switch.Middle_Curl', 10)
        cmds.setAttr('middle_lf_001_jnt_ctrl_curl_grp.rz', -40)
        cmds.setAttr('middle_lf_002_jnt_ctrl_curl_grp.rz', -40)
        cmds.setAttr('middle_lf_003_jnt_ctrl_curl_grp.rz', -40)
        cmds.setDrivenKeyframe('middle_lf_001_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Middle_Curl')
        cmds.setDrivenKeyframe('middle_lf_002_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Middle_Curl')
        cmds.setDrivenKeyframe('middle_lf_003_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Middle_Curl')
        cmds.setAttr('arm_lf_switch.Middle_Curl', -10)
        cmds.setAttr('middle_lf_001_jnt_ctrl_curl_grp.rz', 40)
        cmds.setAttr('middle_lf_002_jnt_ctrl_curl_grp.rz', 40)
        cmds.setAttr('middle_lf_003_jnt_ctrl_curl_grp.rz', 40)
        cmds.setDrivenKeyframe('middle_lf_001_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Middle_Curl')
        cmds.setDrivenKeyframe('middle_lf_002_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Middle_Curl')
        cmds.setDrivenKeyframe('middle_lf_003_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Middle_Curl')
        cmds.setAttr('arm_lf_switch.Middle_Curl', 0)
        
        cmds.setAttr('arm_lf_switch.Ring_Curl', 0)
        cmds.setAttr('ring_lf_001_jnt_ctrl_curl_grp.rz', 0)
        cmds.setAttr('ring_lf_002_jnt_ctrl_curl_grp.rz', 0)
        cmds.setAttr('ring_lf_003_jnt_ctrl_curl_grp.rz', 0)
        cmds.setDrivenKeyframe('ring_lf_001_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Ring_Curl')
        cmds.setDrivenKeyframe('ring_lf_002_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Ring_Curl')
        cmds.setDrivenKeyframe('ring_lf_003_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Ring_Curl')
        cmds.setAttr('arm_lf_switch.Ring_Curl', 10)
        cmds.setAttr('ring_lf_001_jnt_ctrl_curl_grp.rz', -40)
        cmds.setAttr('ring_lf_002_jnt_ctrl_curl_grp.rz', -40)
        cmds.setAttr('ring_lf_003_jnt_ctrl_curl_grp.rz', -40)
        cmds.setDrivenKeyframe('ring_lf_001_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Ring_Curl')
        cmds.setDrivenKeyframe('ring_lf_002_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Ring_Curl')
        cmds.setDrivenKeyframe('ring_lf_003_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Ring_Curl')
        cmds.setAttr('arm_lf_switch.Ring_Curl', -10)
        cmds.setAttr('ring_lf_001_jnt_ctrl_curl_grp.rz', 40)
        cmds.setAttr('ring_lf_002_jnt_ctrl_curl_grp.rz', 40)
        cmds.setAttr('ring_lf_003_jnt_ctrl_curl_grp.rz', 40)
        cmds.setDrivenKeyframe('ring_lf_001_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Ring_Curl')
        cmds.setDrivenKeyframe('ring_lf_002_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Ring_Curl')
        cmds.setDrivenKeyframe('ring_lf_003_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Ring_Curl')
        cmds.setAttr('arm_lf_switch.Ring_Curl', 0)
        
        cmds.setAttr('arm_lf_switch.Pinky_Curl', 0)
        cmds.setAttr('pinky_lf_001_jnt_ctrl_curl_grp.rz', 0)
        cmds.setAttr('pinky_lf_002_jnt_ctrl_curl_grp.rz', 0)
        cmds.setAttr('pinky_lf_003_jnt_ctrl_curl_grp.rz', 0)
        cmds.setDrivenKeyframe('pinky_lf_001_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Pinky_Curl')
        cmds.setDrivenKeyframe('pinky_lf_002_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Pinky_Curl')
        cmds.setDrivenKeyframe('pinky_lf_003_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Pinky_Curl')
        cmds.setAttr('arm_lf_switch.Pinky_Curl', 10)
        cmds.setAttr('pinky_lf_001_jnt_ctrl_curl_grp.rz', -40)
        cmds.setAttr('pinky_lf_002_jnt_ctrl_curl_grp.rz', -40)
        cmds.setAttr('pinky_lf_003_jnt_ctrl_curl_grp.rz', -40)
        cmds.setDrivenKeyframe('pinky_lf_001_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Pinky_Curl')
        cmds.setDrivenKeyframe('pinky_lf_002_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Pinky_Curl')
        cmds.setDrivenKeyframe('pinky_lf_003_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Pinky_Curl')
        cmds.setAttr('arm_lf_switch.Pinky_Curl', -10)
        cmds.setAttr('pinky_lf_001_jnt_ctrl_curl_grp.rz', 40)
        cmds.setAttr('pinky_lf_002_jnt_ctrl_curl_grp.rz', 40)
        cmds.setAttr('pinky_lf_003_jnt_ctrl_curl_grp.rz', 40)
        cmds.setDrivenKeyframe('pinky_lf_001_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Pinky_Curl')
        cmds.setDrivenKeyframe('pinky_lf_002_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Pinky_Curl')
        cmds.setDrivenKeyframe('pinky_lf_003_jnt_ctrl_curl_grp.rz', cd='arm_lf_switch.Pinky_Curl')
        cmds.setAttr('arm_lf_switch.Pinky_Curl', 0)
        
        #### Set Finger Spread Attributes
        cmds.setAttr('arm_lf_switch.Spread', 0)
        cmds.setAttr('thumb_lf_001_jnt_ctrl_spread_grp.rz', 0)
        cmds.setAttr('index_lf_001_jnt_ctrl_spread_grp.rx', 0)
        cmds.setAttr('middle_lf_001_jnt_ctrl_spread_grp.rx', 0)
        cmds.setAttr('ring_lf_001_jnt_ctrl_spread_grp.rx', 0)
        cmds.setAttr('pinky_lf_001_jnt_ctrl_spread_grp.rx', 0)
        cmds.setDrivenKeyframe('thumb_lf_001_jnt_ctrl_spread_grp.rz', cd='arm_lf_switch.Spread')
        cmds.setDrivenKeyframe('index_lf_001_jnt_ctrl_spread_grp.rx', cd='arm_lf_switch.Spread')
        cmds.setDrivenKeyframe('middle_lf_001_jnt_ctrl_spread_grp.rx', cd='arm_lf_switch.Spread')
        cmds.setDrivenKeyframe('ring_lf_001_jnt_ctrl_spread_grp.rx', cd='arm_lf_switch.Spread')
        cmds.setDrivenKeyframe('pinky_lf_001_jnt_ctrl_spread_grp.rx', cd='arm_lf_switch.Spread')
        cmds.setAttr('arm_lf_switch.Spread', 10)
        cmds.setAttr('thumb_lf_001_jnt_ctrl_spread_grp.rz', -60)
        cmds.setAttr('index_lf_001_jnt_ctrl_spread_grp.rx', 25)
        cmds.setAttr('middle_lf_001_jnt_ctrl_spread_grp.rx', 0)
        cmds.setAttr('ring_lf_001_jnt_ctrl_spread_grp.rx', -25)
        cmds.setAttr('pinky_lf_001_jnt_ctrl_spread_grp.rx', -40)
        cmds.setDrivenKeyframe('thumb_lf_001_jnt_ctrl_spread_grp.rz', cd='arm_lf_switch.Spread')
        cmds.setDrivenKeyframe('index_lf_001_jnt_ctrl_spread_grp.rx', cd='arm_lf_switch.Spread')
        cmds.setDrivenKeyframe('middle_lf_001_jnt_ctrl_spread_grp.rx', cd='arm_lf_switch.Spread')
        cmds.setDrivenKeyframe('ring_lf_001_jnt_ctrl_spread_grp.rx', cd='arm_lf_switch.Spread')
        cmds.setDrivenKeyframe('pinky_lf_001_jnt_ctrl_spread_grp.rx', cd='arm_lf_switch.Spread')
        cmds.setAttr('arm_lf_switch.Spread', -10)
        cmds.setAttr('thumb_lf_001_jnt_ctrl_spread_grp.rz', 35)
        cmds.setAttr('index_lf_001_jnt_ctrl_spread_grp.rx', -25)
        cmds.setAttr('middle_lf_001_jnt_ctrl_spread_grp.rx', 0)
        cmds.setAttr('ring_lf_001_jnt_ctrl_spread_grp.rx', 25)
        cmds.setAttr('pinky_lf_001_jnt_ctrl_spread_grp.rx', 40)
        cmds.setDrivenKeyframe('thumb_lf_001_jnt_ctrl_spread_grp.rz', cd='arm_lf_switch.Spread')
        cmds.setDrivenKeyframe('index_lf_001_jnt_ctrl_spread_grp.rx', cd='arm_lf_switch.Spread')
        cmds.setDrivenKeyframe('middle_lf_001_jnt_ctrl_spread_grp.rx', cd='arm_lf_switch.Spread')
        cmds.setDrivenKeyframe('ring_lf_001_jnt_ctrl_spread_grp.rx', cd='arm_lf_switch.Spread')
        cmds.setDrivenKeyframe('pinky_lf_001_jnt_ctrl_spread_grp.rx', cd='arm_lf_switch.Spread')
        cmds.setAttr('arm_lf_switch.Spread', 0)
        
        ### Right Arm Switch
        cmds.setAttr('arm_rt_switch.tx', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_switch.ty', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_switch.tz', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_switch.rx', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_switch.ry', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_switch.rz', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_switch.sx', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_switch.sy', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_switch.sz', l=True, k=False, cb=False)
        cmds.setAttr('arm_rt_switch.v', l=True, k=False, cb=False)
        
        cmds.select('arm_rt_switch')
        cmds.addAttr(ln='IK_FK', at='double', min=0, max=10, dv=0)
        cmds.setAttr('arm_rt_switch.IK_FK', 0, k=True)
        cmds.addAttr(ln='Thumb_Curl', at='double', min=-10, max=10, dv=0)
        cmds.setAttr('arm_rt_switch.Thumb_Curl', 0, k=True)
        cmds.addAttr(ln='Index_Curl', at='double', min=-10, max=10, dv=0)
        cmds.setAttr('arm_rt_switch.Index_Curl', 0, k=True)
        cmds.addAttr(ln='Middle_Curl', at='double', min=-10, max=10, dv=0)
        cmds.setAttr('arm_rt_switch.Middle_Curl', 0, k=True)
        cmds.addAttr(ln='Ring_Curl', at='double', min=-10, max=10, dv=0)
        cmds.setAttr('arm_rt_switch.Ring_Curl', 0, k=True)
        cmds.addAttr(ln='Pinky_Curl', at='double', min=-10, max=10, dv=0)
        cmds.setAttr('arm_rt_switch.Pinky_Curl', 0, k=True)
        cmds.addAttr(ln='Spread', at='double', min=-10, max=10, dv=0)
        cmds.setAttr('arm_rt_switch.Spread', 0, k=True)
        
        cmds.setAttr('arm_rt_switch.IK_FK', 0)
        cmds.setAttr('arm_rt_fk_shoulder_jnt_ctrl_grp.visibility', 0)
        cmds.setAttr('arm_rt_ik_wrist_jnt_ctrl_grp.visibility', 1)
        cmds.setAttr('arm_rt_pv_ctrl_grp.visibility', 1)
        cmds.setDrivenKeyframe('arm_rt_pv_ctrl_grp.visibility', cd='arm_rt_switch.IK_FK')
        cmds.setDrivenKeyframe('arm_rt_ik_wrist_jnt_ctrl_grp.visibility', cd='arm_rt_switch.IK_FK')
        cmds.setDrivenKeyframe('arm_rt_fk_shoulder_jnt_ctrl_grp.visibility', cd='arm_rt_switch.IK_FK')
        cmds.setAttr('arm_rt_switch.IK_FK', 10)
        cmds.setAttr('arm_rt_fk_shoulder_jnt_ctrl_grp.visibility', 1)
        cmds.setAttr('arm_rt_ik_wrist_jnt_ctrl_grp.visibility', 0)
        cmds.setAttr('arm_rt_pv_ctrl_grp.visibility', 0)
        cmds.setDrivenKeyframe('arm_rt_pv_ctrl_grp.visibility', cd='arm_rt_switch.IK_FK')
        cmds.setDrivenKeyframe('arm_rt_ik_wrist_jnt_ctrl_grp.visibility', cd='arm_rt_switch.IK_FK')
        cmds.setDrivenKeyframe('arm_rt_fk_shoulder_jnt_ctrl_grp.visibility', cd='arm_rt_switch.IK_FK')
        
        cmds.setAttr('arm_rt_switch.IK_FK', 0)
        
        ### Right Hand Attributes
        #### Create Groups for Curl Attributes
        cmds.select('thumb_rt_001_jnt_ctrl', hi=True)
        cmds.select('index_rt_001_jnt_ctrl', hi=True, add=True)
        cmds.select('middle_rt_001_jnt_ctrl', hi=True, add=True)
        cmds.select('ring_rt_001_jnt_ctrl', hi=True, add=True)
        cmds.select('pinky_rt_001_jnt_ctrl', hi=True, add=True)
        
        selectedObjs = cmds.ls(sl=True)
        ctrl_list = []
        
        for sel in selectedObjs:
            shapeNode = cmds.listRelatives(sel, shapes=True)
            nodeType = cmds.nodeType(shapeNode)
                
            if(nodeType=='nurbsCurve'):
                ctrl_list.append(sel)
                print sel
        
        for cl in ctrl_list:
            name = cl +'_curl_grp'
            cl_grp = cmds.group(cl, n=name)
            
            jnt = cl.replace('_ctrl_curl_grp', '')
            jnt_pos = cmds.xform(jnt, q=True, ws=True, rp=True)
            
            cmds.select(cl_grp)
            cmds.move(jnt_pos[0], jnt_pos[1], jnt_pos[2], ".scalePivot", ".rotatePivot", a=True)
        
        #### Create Groups for Spread Attributes
        cmds.select('thumb_rt_001_jnt_ctrl_curl_grp')
        cmds.select('index_rt_001_jnt_ctrl_curl_grp', add=True)
        cmds.select('middle_rt_001_jnt_ctrl_curl_grp', add=True)
        cmds.select('ring_rt_001_jnt_ctrl_curl_grp', add=True)
        cmds.select('pinky_rt_001_jnt_ctrl_curl_grp', add=True)
        
        selectedObjs = cmds.ls(sl=True)
        ctrl_list = []
        
        for sel in selectedObjs:
            name = sel.replace('curl', 'spread')
            sel_grp = cmds.group(sel, n=name)
            
            jnt = sel.replace('_ctrl_curl_grp', '')
            jnt_pos = cmds.xform(jnt, q=True, ws=True, rp=True)
            
            cmds.select(sel_grp)
            cmds.move(jnt_pos[0], jnt_pos[1], jnt_pos[2], ".scalePivot", ".rotatePivot", a=True)
        
        #### Set Finger Curl Attributes
        cmds.setAttr('arm_rt_switch.Thumb_Curl', 0)
        cmds.setAttr('thumb_rt_001_jnt_ctrl_curl_grp.rx', 0)
        cmds.setAttr('thumb_rt_002_jnt_ctrl_curl_grp.rx', 0)
        cmds.setAttr('thumb_rt_003_jnt_ctrl_curl_grp.rx', 0)
        cmds.setDrivenKeyframe('thumb_rt_001_jnt_ctrl_curl_grp.rx', cd='arm_rt_switch.Thumb_Curl')
        cmds.setDrivenKeyframe('thumb_rt_002_jnt_ctrl_curl_grp.rx', cd='arm_rt_switch.Thumb_Curl')
        cmds.setDrivenKeyframe('thumb_rt_003_jnt_ctrl_curl_grp.rx', cd='arm_rt_switch.Thumb_Curl')
        cmds.setAttr('arm_rt_switch.Thumb_Curl', 10)
        cmds.setAttr('thumb_rt_001_jnt_ctrl_curl_grp.rx', 40)
        cmds.setAttr('thumb_rt_002_jnt_ctrl_curl_grp.rx', 40)
        cmds.setAttr('thumb_rt_003_jnt_ctrl_curl_grp.rx', 40)
        cmds.setDrivenKeyframe('thumb_rt_001_jnt_ctrl_curl_grp.rx', cd='arm_rt_switch.Thumb_Curl')
        cmds.setDrivenKeyframe('thumb_rt_002_jnt_ctrl_curl_grp.rx', cd='arm_rt_switch.Thumb_Curl')
        cmds.setDrivenKeyframe('thumb_rt_003_jnt_ctrl_curl_grp.rx', cd='arm_rt_switch.Thumb_Curl')
        cmds.setAttr('arm_rt_switch.Thumb_Curl', -10)
        cmds.setAttr('thumb_rt_001_jnt_ctrl_curl_grp.rx', -40)
        cmds.setAttr('thumb_rt_002_jnt_ctrl_curl_grp.rx', -40)
        cmds.setAttr('thumb_rt_003_jnt_ctrl_curl_grp.rx', -40)
        cmds.setDrivenKeyframe('thumb_rt_001_jnt_ctrl_curl_grp.rx', cd='arm_rt_switch.Thumb_Curl')
        cmds.setDrivenKeyframe('thumb_rt_002_jnt_ctrl_curl_grp.rx', cd='arm_rt_switch.Thumb_Curl')
        cmds.setDrivenKeyframe('thumb_rt_003_jnt_ctrl_curl_grp.rx', cd='arm_rt_switch.Thumb_Curl')
        cmds.setAttr('arm_rt_switch.Thumb_Curl', 0)
        
        cmds.setAttr('arm_rt_switch.Index_Curl', 0)
        cmds.setAttr('index_rt_001_jnt_ctrl_curl_grp.rz', 0)
        cmds.setAttr('index_rt_002_jnt_ctrl_curl_grp.rz', 0)
        cmds.setAttr('index_rt_003_jnt_ctrl_curl_grp.rz', 0)
        cmds.setDrivenKeyframe('index_rt_001_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Index_Curl')
        cmds.setDrivenKeyframe('index_rt_002_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Index_Curl')
        cmds.setDrivenKeyframe('index_rt_003_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Index_Curl')
        cmds.setAttr('arm_rt_switch.Index_Curl', 10)
        cmds.setAttr('index_rt_001_jnt_ctrl_curl_grp.rz', -40)
        cmds.setAttr('index_rt_002_jnt_ctrl_curl_grp.rz', -40)
        cmds.setAttr('index_rt_003_jnt_ctrl_curl_grp.rz', -40)
        cmds.setDrivenKeyframe('index_rt_001_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Index_Curl')
        cmds.setDrivenKeyframe('index_rt_002_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Index_Curl')
        cmds.setDrivenKeyframe('index_rt_003_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Index_Curl')
        cmds.setAttr('arm_rt_switch.Index_Curl', -10)
        cmds.setAttr('index_rt_001_jnt_ctrl_curl_grp.rz', 40)
        cmds.setAttr('index_rt_002_jnt_ctrl_curl_grp.rz', 40)
        cmds.setAttr('index_rt_003_jnt_ctrl_curl_grp.rz', 40)
        cmds.setDrivenKeyframe('index_rt_001_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Index_Curl')
        cmds.setDrivenKeyframe('index_rt_002_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Index_Curl')
        cmds.setDrivenKeyframe('index_rt_003_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Index_Curl')
        cmds.setAttr('arm_rt_switch.Index_Curl', 0)
        
        cmds.setAttr('arm_rt_switch.Middle_Curl', 0)
        cmds.setAttr('middle_rt_001_jnt_ctrl_curl_grp.rz', 0)
        cmds.setAttr('middle_rt_002_jnt_ctrl_curl_grp.rz', 0)
        cmds.setAttr('middle_rt_003_jnt_ctrl_curl_grp.rz', 0)
        cmds.setDrivenKeyframe('middle_rt_001_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Middle_Curl')
        cmds.setDrivenKeyframe('middle_rt_002_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Middle_Curl')
        cmds.setDrivenKeyframe('middle_rt_003_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Middle_Curl')
        cmds.setAttr('arm_rt_switch.Middle_Curl', 10)
        cmds.setAttr('middle_rt_001_jnt_ctrl_curl_grp.rz', -40)
        cmds.setAttr('middle_rt_002_jnt_ctrl_curl_grp.rz', -40)
        cmds.setAttr('middle_rt_003_jnt_ctrl_curl_grp.rz', -40)
        cmds.setDrivenKeyframe('middle_rt_001_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Middle_Curl')
        cmds.setDrivenKeyframe('middle_rt_002_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Middle_Curl')
        cmds.setDrivenKeyframe('middle_rt_003_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Middle_Curl')
        cmds.setAttr('arm_rt_switch.Middle_Curl', -10)
        cmds.setAttr('middle_rt_001_jnt_ctrl_curl_grp.rz', 40)
        cmds.setAttr('middle_rt_002_jnt_ctrl_curl_grp.rz', 40)
        cmds.setAttr('middle_rt_003_jnt_ctrl_curl_grp.rz', 40)
        cmds.setDrivenKeyframe('middle_rt_001_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Middle_Curl')
        cmds.setDrivenKeyframe('middle_rt_002_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Middle_Curl')
        cmds.setDrivenKeyframe('middle_rt_003_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Middle_Curl')
        cmds.setAttr('arm_rt_switch.Middle_Curl', 0)
        
        cmds.setAttr('arm_rt_switch.Ring_Curl', 0)
        cmds.setAttr('ring_rt_001_jnt_ctrl_curl_grp.rz', 0)
        cmds.setAttr('ring_rt_002_jnt_ctrl_curl_grp.rz', 0)
        cmds.setAttr('ring_rt_003_jnt_ctrl_curl_grp.rz', 0)
        cmds.setDrivenKeyframe('ring_rt_001_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Ring_Curl')
        cmds.setDrivenKeyframe('ring_rt_002_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Ring_Curl')
        cmds.setDrivenKeyframe('ring_rt_003_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Ring_Curl')
        cmds.setAttr('arm_rt_switch.Ring_Curl', 10)
        cmds.setAttr('ring_rt_001_jnt_ctrl_curl_grp.rz', -40)
        cmds.setAttr('ring_rt_002_jnt_ctrl_curl_grp.rz', -40)
        cmds.setAttr('ring_rt_003_jnt_ctrl_curl_grp.rz', -40)
        cmds.setDrivenKeyframe('ring_rt_001_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Ring_Curl')
        cmds.setDrivenKeyframe('ring_rt_002_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Ring_Curl')
        cmds.setDrivenKeyframe('ring_rt_003_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Ring_Curl')
        cmds.setAttr('arm_rt_switch.Ring_Curl', -10)
        cmds.setAttr('ring_rt_001_jnt_ctrl_curl_grp.rz', 40)
        cmds.setAttr('ring_rt_002_jnt_ctrl_curl_grp.rz', 40)
        cmds.setAttr('ring_rt_003_jnt_ctrl_curl_grp.rz', 40)
        cmds.setDrivenKeyframe('ring_rt_001_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Ring_Curl')
        cmds.setDrivenKeyframe('ring_rt_002_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Ring_Curl')
        cmds.setDrivenKeyframe('ring_rt_003_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Ring_Curl')
        cmds.setAttr('arm_rt_switch.Ring_Curl', 0)
        
        cmds.setAttr('arm_rt_switch.Pinky_Curl', 0)
        cmds.setAttr('pinky_rt_001_jnt_ctrl_curl_grp.rz', 0)
        cmds.setAttr('pinky_rt_002_jnt_ctrl_curl_grp.rz', 0)
        cmds.setAttr('pinky_rt_003_jnt_ctrl_curl_grp.rz', 0)
        cmds.setDrivenKeyframe('pinky_rt_001_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Pinky_Curl')
        cmds.setDrivenKeyframe('pinky_rt_002_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Pinky_Curl')
        cmds.setDrivenKeyframe('pinky_rt_003_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Pinky_Curl')
        cmds.setAttr('arm_rt_switch.Pinky_Curl', 10)
        cmds.setAttr('pinky_rt_001_jnt_ctrl_curl_grp.rz', -40)
        cmds.setAttr('pinky_rt_002_jnt_ctrl_curl_grp.rz', -40)
        cmds.setAttr('pinky_rt_003_jnt_ctrl_curl_grp.rz', -40)
        cmds.setDrivenKeyframe('pinky_rt_001_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Pinky_Curl')
        cmds.setDrivenKeyframe('pinky_rt_002_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Pinky_Curl')
        cmds.setDrivenKeyframe('pinky_rt_003_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Pinky_Curl')
        cmds.setAttr('arm_rt_switch.Pinky_Curl', -10)
        cmds.setAttr('pinky_rt_001_jnt_ctrl_curl_grp.rz', 40)
        cmds.setAttr('pinky_rt_002_jnt_ctrl_curl_grp.rz', 40)
        cmds.setAttr('pinky_rt_003_jnt_ctrl_curl_grp.rz', 40)
        cmds.setDrivenKeyframe('pinky_rt_001_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Pinky_Curl')
        cmds.setDrivenKeyframe('pinky_rt_002_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Pinky_Curl')
        cmds.setDrivenKeyframe('pinky_rt_003_jnt_ctrl_curl_grp.rz', cd='arm_rt_switch.Pinky_Curl')
        cmds.setAttr('arm_rt_switch.Pinky_Curl', 0)
        
        #### Set Finger Spread Attributes
        cmds.setAttr('arm_rt_switch.Spread', 0)
        cmds.setAttr('thumb_rt_001_jnt_ctrl_spread_grp.rz', 0)
        cmds.setAttr('index_rt_001_jnt_ctrl_spread_grp.rx', 0)
        cmds.setAttr('middle_rt_001_jnt_ctrl_spread_grp.rx', 0)
        cmds.setAttr('ring_rt_001_jnt_ctrl_spread_grp.rx', 0)
        cmds.setAttr('pinky_rt_001_jnt_ctrl_spread_grp.rx', 0)
        cmds.setDrivenKeyframe('thumb_rt_001_jnt_ctrl_spread_grp.rz', cd='arm_rt_switch.Spread')
        cmds.setDrivenKeyframe('index_rt_001_jnt_ctrl_spread_grp.rx', cd='arm_rt_switch.Spread')
        cmds.setDrivenKeyframe('middle_rt_001_jnt_ctrl_spread_grp.rx', cd='arm_rt_switch.Spread')
        cmds.setDrivenKeyframe('ring_rt_001_jnt_ctrl_spread_grp.rx', cd='arm_rt_switch.Spread')
        cmds.setDrivenKeyframe('pinky_rt_001_jnt_ctrl_spread_grp.rx', cd='arm_rt_switch.Spread')
        cmds.setAttr('arm_rt_switch.Spread', 10)
        cmds.setAttr('thumb_rt_001_jnt_ctrl_spread_grp.rz', 60)
        cmds.setAttr('index_rt_001_jnt_ctrl_spread_grp.rx', 25)
        cmds.setAttr('middle_rt_001_jnt_ctrl_spread_grp.rx', 0)
        cmds.setAttr('ring_rt_001_jnt_ctrl_spread_grp.rx', -25)
        cmds.setAttr('pinky_rt_001_jnt_ctrl_spread_grp.rx', -40)
        cmds.setDrivenKeyframe('thumb_rt_001_jnt_ctrl_spread_grp.rz', cd='arm_rt_switch.Spread')
        cmds.setDrivenKeyframe('index_rt_001_jnt_ctrl_spread_grp.rx', cd='arm_rt_switch.Spread')
        cmds.setDrivenKeyframe('middle_rt_001_jnt_ctrl_spread_grp.rx', cd='arm_rt_switch.Spread')
        cmds.setDrivenKeyframe('ring_rt_001_jnt_ctrl_spread_grp.rx', cd='arm_rt_switch.Spread')
        cmds.setDrivenKeyframe('pinky_rt_001_jnt_ctrl_spread_grp.rx', cd='arm_rt_switch.Spread')
        cmds.setAttr('arm_rt_switch.Spread', -10)
        cmds.setAttr('thumb_rt_001_jnt_ctrl_spread_grp.rz', -35)
        cmds.setAttr('index_rt_001_jnt_ctrl_spread_grp.rx', -25)
        cmds.setAttr('middle_rt_001_jnt_ctrl_spread_grp.rx', 0)
        cmds.setAttr('ring_rt_001_jnt_ctrl_spread_grp.rx', 25)
        cmds.setAttr('pinky_rt_001_jnt_ctrl_spread_grp.rx', 40)
        cmds.setDrivenKeyframe('thumb_rt_001_jnt_ctrl_spread_grp.rz', cd='arm_rt_switch.Spread')
        cmds.setDrivenKeyframe('index_rt_001_jnt_ctrl_spread_grp.rx', cd='arm_rt_switch.Spread')
        cmds.setDrivenKeyframe('middle_rt_001_jnt_ctrl_spread_grp.rx', cd='arm_rt_switch.Spread')
        cmds.setDrivenKeyframe('ring_rt_001_jnt_ctrl_spread_grp.rx', cd='arm_rt_switch.Spread')
        cmds.setDrivenKeyframe('pinky_rt_001_jnt_ctrl_spread_grp.rx', cd='arm_rt_switch.Spread')
        cmds.setAttr('arm_rt_switch.Spread', 0)
        
        ### Left Leg Switch 
        cmds.setAttr('leg_lf_switch.tx', l=True, k=False, cb=False)
        cmds.setAttr('leg_lf_switch.ty', l=True, k=False, cb=False)
        cmds.setAttr('leg_lf_switch.tz', l=True, k=False, cb=False)
        cmds.setAttr('leg_lf_switch.rx', l=True, k=False, cb=False)
        cmds.setAttr('leg_lf_switch.ry', l=True, k=False, cb=False)
        cmds.setAttr('leg_lf_switch.rz', l=True, k=False, cb=False)
        cmds.setAttr('leg_lf_switch.sx', l=True, k=False, cb=False)
        cmds.setAttr('leg_lf_switch.sy', l=True, k=False, cb=False)
        cmds.setAttr('leg_lf_switch.sz', l=True, k=False, cb=False)
        cmds.setAttr('leg_lf_switch.v', l=True, k=False, cb=False)
        
        cmds.select('leg_lf_switch')
        cmds.addAttr(ln='IK_FK', at='double', min=0, max=10, dv=0)
        cmds.setAttr('leg_lf_switch.IK_FK', 0, k=True)
        
        cmds.setAttr('foot_lf_ik_ctrl.sx', l=True, k=False, cb=False)
        cmds.setAttr('foot_lf_ik_ctrl.sy', l=True, k=False, cb=False)
        cmds.setAttr('foot_lf_ik_ctrl.sz', l=True, k=False, cb=False)
        cmds.setAttr('foot_lf_ik_ctrl.v', l=True, k=False, cb=False)
        
        cmds.select('foot_lf_ik_ctrl')
        cmds.addAttr(ln='Heel_Twist', at='double', dv=0)
        cmds.setAttr('foot_lf_ik_ctrl.Heel_Twist', 0, k=True)
        cmds.addAttr(ln='Heel_Lift', at='double', dv=0)
        cmds.setAttr('foot_lf_ik_ctrl.Heel_Lift', 0, k=True)
        cmds.addAttr(ln='Ball_Twist', at='double', dv=0)
        cmds.setAttr('foot_lf_ik_ctrl.Ball_Twist', 0, k=True)
        cmds.addAttr(ln='Ball_Lift', at='double', dv=0)
        cmds.setAttr('foot_lf_ik_ctrl.Ball_Lift', 0, k=True)
        cmds.addAttr(ln='Toe_Twist', at='double', dv=0)
        cmds.setAttr('foot_lf_ik_ctrl.Toe_Twist', 0, k=True)
        cmds.addAttr(ln='Toe_Lift', at='double', min=-10, max=10, dv=0)
        cmds.setAttr('foot_lf_ik_ctrl.Toe_Lift', 0, k=True)
        cmds.addAttr(ln='Bank', at='double', min=-10, max=10, dv=0)
        cmds.setAttr('foot_lf_ik_ctrl.Bank', 0, k=True)
        cmds.addAttr(ln='Tip_Toe', at='double', dv=0)
        cmds.setAttr('foot_lf_ik_ctrl.Tip_Toe', 0, k=True)
        
        cmds.setAttr('leg_lf_switch.IK_FK', 0)
        cmds.setAttr('leg_lf_fk_tight_jnt_ctrl_grp.visibility', 0)
        cmds.setAttr('foot_lf_ik_ctrl_grp.visibility', 1)
        cmds.setAttr('leg_lf_pv_ctrl_grp.visibility', 1)
        cmds.setDrivenKeyframe('leg_lf_pv_ctrl_grp.visibility', cd='leg_lf_switch.IK_FK')
        cmds.setDrivenKeyframe('foot_lf_ik_ctrl_grp.visibility', cd='leg_lf_switch.IK_FK')
        cmds.setDrivenKeyframe('leg_lf_fk_tight_jnt_ctrl_grp.visibility', cd='leg_lf_switch.IK_FK')
        cmds.setAttr('leg_lf_switch.IK_FK', 10)
        cmds.setAttr('leg_lf_fk_tight_jnt_ctrl_grp.visibility', 1)
        cmds.setAttr('foot_lf_ik_ctrl_grp.visibility', 0)
        cmds.setAttr('leg_lf_pv_ctrl_grp.visibility', 0)
        cmds.setDrivenKeyframe('leg_lf_pv_ctrl_grp.visibility', cd='leg_lf_switch.IK_FK')
        cmds.setDrivenKeyframe('foot_lf_ik_ctrl_grp.visibility', cd='leg_lf_switch.IK_FK')
        cmds.setDrivenKeyframe('leg_lf_fk_tight_jnt_ctrl_grp.visibility', cd='leg_lf_switch.IK_FK')
        
        cmds.setAttr('leg_lf_switch.IK_FK', 0)
        
        ### Right Leg Switch 
        cmds.setAttr('leg_rt_switch.tx', l=True, k=False, cb=False)
        cmds.setAttr('leg_rt_switch.ty', l=True, k=False, cb=False)
        cmds.setAttr('leg_rt_switch.tz', l=True, k=False, cb=False)
        cmds.setAttr('leg_rt_switch.rx', l=True, k=False, cb=False)
        cmds.setAttr('leg_rt_switch.ry', l=True, k=False, cb=False)
        cmds.setAttr('leg_rt_switch.rz', l=True, k=False, cb=False)
        cmds.setAttr('leg_rt_switch.sx', l=True, k=False, cb=False)
        cmds.setAttr('leg_rt_switch.sy', l=True, k=False, cb=False)
        cmds.setAttr('leg_rt_switch.sz', l=True, k=False, cb=False)
        cmds.setAttr('leg_rt_switch.v', l=True, k=False, cb=False)
        
        cmds.select('leg_rt_switch')
        cmds.addAttr(ln='IK_FK', at='double', min=0, max=10, dv=0)
        cmds.setAttr('leg_rt_switch.IK_FK', 0, k=True)
        
        cmds.setAttr('foot_rt_ik_ctrl.sx', l=True, k=False, cb=False)
        cmds.setAttr('foot_rt_ik_ctrl.sy', l=True, k=False, cb=False)
        cmds.setAttr('foot_rt_ik_ctrl.sz', l=True, k=False, cb=False)
        cmds.setAttr('foot_rt_ik_ctrl.v', l=True, k=False, cb=False)
        
        cmds.select('foot_rt_ik_ctrl')
        cmds.addAttr(ln='Heel_Twist', at='double', dv=0)
        cmds.setAttr('foot_rt_ik_ctrl.Heel_Twist', 0, k=True)
        cmds.addAttr(ln='Heel_Lift', at='double', dv=0)
        cmds.setAttr('foot_rt_ik_ctrl.Heel_Lift', 0, k=True)
        cmds.addAttr(ln='Ball_Twist', at='double', dv=0)
        cmds.setAttr('foot_rt_ik_ctrl.Ball_Twist', 0, k=True)
        cmds.addAttr(ln='Ball_Lift', at='double', dv=0)
        cmds.setAttr('foot_rt_ik_ctrl.Ball_Lift', 0, k=True)
        cmds.addAttr(ln='Toe_Twist', at='double', dv=0)
        cmds.setAttr('foot_rt_ik_ctrl.Toe_Twist', 0, k=True)
        cmds.addAttr(ln='Toe_Lift', at='double', min=-10, max=10, dv=0)
        cmds.setAttr('foot_rt_ik_ctrl.Toe_Lift', 0, k=True)
        cmds.addAttr(ln='Bank', at='double', min=-10, max=10, dv=0)
        cmds.setAttr('foot_rt_ik_ctrl.Bank', 0, k=True)
        cmds.addAttr(ln='Tip_Toe', at='double', dv=0)
        cmds.setAttr('foot_rt_ik_ctrl.Tip_Toe', 0, k=True)
        
        cmds.setAttr('leg_rt_switch.IK_FK', 0)
        cmds.setAttr('leg_rt_fk_tight_jnt_ctrl_grp.visibility', 0)
        cmds.setAttr('foot_rt_ik_ctrl_grp.visibility', 1)
        cmds.setAttr('leg_rt_pv_ctrl_grp.visibility', 1)
        cmds.setDrivenKeyframe('leg_rt_pv_ctrl_grp.visibility', cd='leg_rt_switch.IK_FK')
        cmds.setDrivenKeyframe('foot_rt_ik_ctrl_grp.visibility', cd='leg_rt_switch.IK_FK')
        cmds.setDrivenKeyframe('leg_rt_fk_tight_jnt_ctrl_grp.visibility', cd='leg_rt_switch.IK_FK')
        cmds.setAttr('leg_rt_switch.IK_FK', 10)
        cmds.setAttr('leg_rt_fk_tight_jnt_ctrl_grp.visibility', 1)
        cmds.setAttr('foot_rt_ik_ctrl_grp.visibility', 0)
        cmds.setAttr('leg_rt_pv_ctrl_grp.visibility', 0)
        cmds.setDrivenKeyframe('leg_rt_pv_ctrl_grp.visibility', cd='leg_rt_switch.IK_FK')
        cmds.setDrivenKeyframe('foot_rt_ik_ctrl_grp.visibility', cd='leg_rt_switch.IK_FK')
        cmds.setDrivenKeyframe('leg_rt_fk_tight_jnt_ctrl_grp.visibility', cd='leg_rt_switch.IK_FK')
        
        cmds.setAttr('leg_rt_switch.IK_FK', 0)
        
        ## Foot Attribute
        ### Left Foot Attribute
        cmds.select('foot_lf_ik_ctrl')
        cmds.connectAttr('foot_lf_ik_ctrl.Heel_Twist', 'heel_ik_lf_ctrl_jnt.rotateZ')
        cmds.connectAttr('foot_lf_ik_ctrl.Heel_Lift', 'heel_ik_lf_ctrl_jnt.rotateX')
        cmds.connectAttr('foot_lf_ik_ctrl.Ball_Twist', 'ball_twist_ik_lf_ctrl_jnt.rotateZ')
        cmds.connectAttr('foot_lf_ik_ctrl.Ball_Lift', 'ball_lift_ik_lf_ctrl_jnt.rotateX')
        cmds.connectAttr('foot_lf_ik_ctrl.Toe_Twist', 'toe_ik_lf_ctrl_jnt.rotateZ')
        cmds.connectAttr('foot_lf_ik_ctrl.Toe_Lift', 'lf_ballToToe_ikHandle.translateZ')
        cmds.connectAttr('foot_lf_ik_ctrl.Tip_Toe', 'lf_F_bank_loc.rotateX')
        ###
        cmds.setAttr('foot_lf_ik_ctrl.Bank', 0)
        cmds.setAttr('lf_L_bank_loc.rotateZ', 0)
        cmds.setAttr('lf_R_bank_loc.rotateZ', 0)
        cmds.setAttr('foot_ik_lf_bank_grp_parentConstraint1.lf_L_bank_locW0', 0)
        cmds.setAttr('foot_ik_lf_bank_grp_parentConstraint1.lf_R_bank_locW1', 0)
        cmds.setDrivenKeyframe('lf_L_bank_loc.rotateZ', cd='foot_lf_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('lf_R_bank_loc.rotateZ', cd='foot_lf_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('foot_ik_lf_bank_grp_parentConstraint1.lf_L_bank_locW0', cd='foot_lf_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('foot_ik_lf_bank_grp_parentConstraint1.lf_R_bank_locW1', cd='foot_lf_ik_ctrl.Bank')
        
        cmds.setAttr('foot_lf_ik_ctrl.Bank', 10)
        cmds.setAttr('lf_L_bank_loc.rotateZ', -90)
        cmds.setAttr('lf_R_bank_loc.rotateZ', 0)
        cmds.setAttr('foot_ik_lf_bank_grp_parentConstraint1.lf_L_bank_locW0', 1)
        cmds.setAttr('foot_ik_lf_bank_grp_parentConstraint1.lf_R_bank_locW1', 0)
        cmds.setDrivenKeyframe('lf_L_bank_loc.rotateZ', cd='foot_lf_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('lf_R_bank_loc.rotateZ', cd='foot_lf_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('foot_ik_lf_bank_grp_parentConstraint1.lf_L_bank_locW0', cd='foot_lf_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('foot_ik_lf_bank_grp_parentConstraint1.lf_R_bank_locW1', cd='foot_lf_ik_ctrl.Bank')
        
        cmds.setAttr('foot_lf_ik_ctrl.Bank', -10)
        cmds.setAttr('lf_L_bank_loc.rotateZ', 0)
        cmds.setAttr('lf_R_bank_loc.rotateZ', 90)
        cmds.setAttr('foot_ik_lf_bank_grp_parentConstraint1.lf_L_bank_locW0', 0)
        cmds.setAttr('foot_ik_lf_bank_grp_parentConstraint1.lf_R_bank_locW1', 1)
        cmds.setDrivenKeyframe('lf_L_bank_loc.rotateZ', cd='foot_lf_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('lf_R_bank_loc.rotateZ', cd='foot_lf_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('foot_ik_lf_bank_grp_parentConstraint1.lf_L_bank_locW0', cd='foot_lf_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('foot_ik_lf_bank_grp_parentConstraint1.lf_R_bank_locW1', cd='foot_lf_ik_ctrl.Bank')
        
        cmds.setAttr('foot_lf_ik_ctrl.Bank', 0)
        
        ## Foot Attribute
        ### Right Foot Attribute
        cmds.select('foot_rt_ik_ctrl')
        cmds.connectAttr('foot_rt_ik_ctrl.Heel_Twist', 'heel_ik_rt_ctrl_jnt.rotateZ')
        cmds.connectAttr('foot_rt_ik_ctrl.Heel_Lift', 'heel_ik_rt_ctrl_jnt.rotateX')
        cmds.connectAttr('foot_rt_ik_ctrl.Ball_Twist', 'ball_twist_ik_rt_ctrl_jnt.rotateZ')
        cmds.connectAttr('foot_rt_ik_ctrl.Ball_Lift', 'ball_lift_ik_rt_ctrl_jnt.rotateX')
        cmds.connectAttr('foot_rt_ik_ctrl.Toe_Twist', 'toe_ik_rt_ctrl_jnt.rotateZ')
        cmds.connectAttr('foot_rt_ik_ctrl.Toe_Lift', 'rt_ballToToe_ikHandle.translateZ')
        cmds.connectAttr('foot_rt_ik_ctrl.Tip_Toe', 'rt_F_bank_loc.rotateX')
        ###
        cmds.setAttr('foot_rt_ik_ctrl.Bank', 0)
        cmds.setAttr('rt_L_bank_loc.rotateZ', 0)
        cmds.setAttr('rt_R_bank_loc.rotateZ', 0)
        cmds.setAttr('foot_ik_rt_bank_grp_parentConstraint1.rt_L_bank_locW0', 0)
        cmds.setAttr('foot_ik_rt_bank_grp_parentConstraint1.rt_R_bank_locW1', 0)
        cmds.setDrivenKeyframe('rt_L_bank_loc.rotateZ', cd='foot_rt_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('rt_R_bank_loc.rotateZ', cd='foot_rt_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('foot_ik_rt_bank_grp_parentConstraint1.rt_L_bank_locW0', cd='foot_rt_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('foot_ik_rt_bank_grp_parentConstraint1.rt_R_bank_locW1', cd='foot_rt_ik_ctrl.Bank')
        
        cmds.setAttr('foot_rt_ik_ctrl.Bank', 10)
        cmds.setAttr('rt_L_bank_loc.rotateZ', 90)
        cmds.setAttr('rt_R_bank_loc.rotateZ', 0)
        cmds.setAttr('foot_ik_rt_bank_grp_parentConstraint1.rt_L_bank_locW0', 1)
        cmds.setAttr('foot_ik_rt_bank_grp_parentConstraint1.rt_R_bank_locW1', 0)
        cmds.setDrivenKeyframe('rt_L_bank_loc.rotateZ', cd='foot_rt_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('rt_R_bank_loc.rotateZ', cd='foot_rt_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('foot_ik_rt_bank_grp_parentConstraint1.rt_L_bank_locW0', cd='foot_rt_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('foot_ik_rt_bank_grp_parentConstraint1.rt_R_bank_locW1', cd='foot_rt_ik_ctrl.Bank')
        
        cmds.setAttr('foot_rt_ik_ctrl.Bank', -10)
        cmds.setAttr('rt_L_bank_loc.rotateZ', 0)
        cmds.setAttr('rt_R_bank_loc.rotateZ', -90)
        cmds.setAttr('foot_ik_rt_bank_grp_parentConstraint1.rt_L_bank_locW0', 0)
        cmds.setAttr('foot_ik_rt_bank_grp_parentConstraint1.rt_R_bank_locW1', 1)
        cmds.setDrivenKeyframe('rt_L_bank_loc.rotateZ', cd='foot_rt_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('rt_R_bank_loc.rotateZ', cd='foot_rt_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('foot_ik_rt_bank_grp_parentConstraint1.rt_L_bank_locW0', cd='foot_rt_ik_ctrl.Bank')
        cmds.setDrivenKeyframe('foot_ik_rt_bank_grp_parentConstraint1.rt_R_bank_locW1', cd='foot_rt_ik_ctrl.Bank')
        
        cmds.setAttr('foot_rt_ik_ctrl.Bank', 0)
        
        # Root X, Y, Z
        cmds.parentConstraint('root_x_ctrl', 'ctrl_grp', w=1, mo=True)
        cmds.scaleConstraint('root_x_ctrl', 'ctrl_grp', w=1, mo=True)
        cmds.parentConstraint('root_x_ctrl', 'jnt_grp', w=1, mo=True)
        cmds.scaleConstraint('root_x_ctrl', 'jnt_grp', w=1, mo=True)
        
        cmds.select(clear=True)
    
    
    def bind(self, args):
        '''
            STEP 5: Bind skin
        '''
        pass
    
    
    def import_weight(self, args):
        '''
            STEP 6: Import Weight
        '''
        pass
        cmds.fileBrowserDialog(mode=0, fileCommand=self.apply_weight, fileType='directory', an='Import weight', operationMode='Import')
    
    
    def apply_weight(self, fileName, fileType):
        pass
    
    
    def showHelp(self, args):
        cmds.showHelp("https://github.com/JaewanKim/maya-plugin", absolute=True)


BipedAutoRig()