import maya.cmds as cmds

class JWAutoRig():
    '''
        Description : AutoRig.py made by JW
            STEP 1. Create Joints
            STEP 2. Check Joint Orientation
            STEP 3. Create Controllers
            STEP 4. Build
            STEP 5. Import Weight
        
        Things to do :
            - Create Joint Controllers
            - Build
            - Import Weight (fileDialog2/fileBrowseDialog)
            - Layout
            - Refactoring
    '''
    
    def __init__(self):
        
        # Window
        if (cmds.window("JWAutoRig", exists=True)):
            cmds.deleteUI("JWAutoRig", window=True)
        
        self.win = cmds.window("JWAutoRig", title="JWAutoRig", sizeable=True, resizeToFitChildren=True, menuBar=True)
        
        # Menu Bar
        fileMenu = cmds.menu(label="Edit")
        saveOption = cmds.menuItem(label="Save Settings", enable=False)
        resetOption = cmds.menuItem(label="Reset Settings", enable=False)
        
        helpMenu = cmds.menu(label="Help")
        helpOption = cmds.menuItem(label="Help on JWAutoRig.py", command=self.showHelp)
        cmds.setParent("..")
        
        # Button Group
        cmds.columnLayout()
        cmds.separator(h=5, style='single', hr=True)
        
        cmds.button(label="Create Joint", command=self.create_jnt)
        cmds.button(label="Confirm Joint Orient", command=self.confirm_orient_joint)
        cmds.button(label="Control Generate", command=self.create_ctrl)
        cmds.button(label="Build", command=self.build)
        cmds.button(label="Import Weight", command=self.import_weight)
        
        cmds.separator(h=5, style='single', hr=True)
        cmds.setParent("..")
        
        cmds.showWindow(self.win)
    
    
    def create_jnt(self, args):
        '''
            STEP 1: Create Joint
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
        cmds.joint(e=True, oj='xyz', sao='yup', ch=True, zso=True)
        cmds.select(clear=True)
        
        
        # Jaw Joint
        jaw_jnt_grp = cmds.group(empty=True, n="jaw_jnt_grp")
        cmds.move(0, 14.447, -0.066, jaw_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        
        cmds.joint(a=True, p=[0, 14.447, -0.066], rad=0.6, n='jaw_001_jnt')
        cmds.joint(a=True, p=[0, 14.094, 0.707], rad=0.6, n='jaw_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('jaw_001_jnt', hi=True)
        cmds.joint(e=True, oj='xzy', sao='zup', ch=True, zso=True)
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
        cmds.joint(e=True, oj='xzy', sao='zup', ch=True, zso=True)
        cmds.select(clear=True)
        
        
        # Left Shoulder Joint
        shoulder_jnt_grp = cmds.group(empty=True, n="shoulder_jnt_grp")
        cmds.move(0, 12.965, -0.251, shoulder_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        
        cmds.joint(a=True, p=[0.232, 12.965, -0.251], rad=0.6, n='shoulder_lf_001_jnt')
        cmds.joint(a=True, p=[1.135, 13.093, -0.504], rad=0.6, n='shoulder_lf_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('shoulder_lf_001_jnt', hi=True)
        cmds.joint(e=True, oj='xyz', sao='yup', ch=True, zso=True)
        cmds.select(clear=True)
        
        
        # Left Arm Joint
        arm_jnt_grp = cmds.group(empty=True, n="arm_jnt_grp")
        cmds.move(0, 13.093, -0.504, arm_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        
        cmds.joint(a=True, p=[1.135, 13.093, -0.504], rad=0.6, n='arm_lf_ik_shoulder_jntt')
        cmds.joint(a=True, p=[2.992, 11.146, -0.809], rad=0.6, n='arm_lf_ik_elbow_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[4.556, 9.612, -0.458], rad=0.6, n='arm_lf_ik_wrist_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.824, 8.343, -0.32], rad=0.6, n='arm_lf_ik_hand_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('arm_lf_ik_shoulder_jntt', hi=True)
        cmds.joint(e=True, oj='xyz', sao='yup', ch=True, zso=True)
        cmds.select(clear=True)
        
        
        # Left Hand Joint
        # Thumb
        hand_jnt_grp = cmds.group(empty=True, n="hand_jnt_grp")
        cmds.move(0, 9.612, -0.458, hand_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        
        cmds.joint(a=True, p=[4.691, 9.483, -0.228], rad=0.1, n='thumb_lf_001_jntt')
        cmds.joint(a=True, p=[4.851, 9.195, 0.036], rad=0.1, n='thumb_lf_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.024, 8.925, 0.138], rad=0.1, n='thumb_lf_003_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.186, 8.694, 0.144], rad=0.1, n='thumb_lf_004_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('thumb_lf_001_jntt', hi=True)
        cmds.joint(e=True, oj='xyz', sao='zup', ch=True, zso=True)
        cmds.select(clear=True)
        
        # Index
        cmds.select(hand_jnt_grp, replace=True)
        cmds.joint(a=True, p=[5.272, 9.168, -0.203], rad=0.1, n='index_lf_001_jntt')
        cmds.joint(a=True, p=[5.548, 8.913, -0.07], rad=0.1, n='index_lf_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.61, 8.694, -0.004], rad=0.1, n='index_lf_003_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.63, 8.49, 0.046], rad=0.1, n='index_lf_004_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('index_lf_001_jntt', hi=True)
        cmds.joint(e=True, oj='xyz', sao='yup', ch=True, zso=True)
        cmds.select(clear=True)
        
        # Middle
        cmds.select(hand_jnt_grp, replace=True)
        cmds.joint(a=True, p=[5.286, 9.176, -0.423], rad=0.1, n='middle_lf_001_jntt')
        cmds.joint(a=True, p=[5.605, 8.834, -0.376], rad=0.1, n='middle_lf_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.678, 8.604, -0.354], rad=0.1, n='middle_lf_003_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.702, 8.373, -0.336], rad=0.1, n='middle_lf_004_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('middle_lf_001_jntt', hi=True)
        cmds.joint(e=True, oj='xyz', sao='yup', ch=True, zso=True)
        cmds.select(clear=True)
        
        # Ring
        cmds.select(hand_jnt_grp, replace=True)
        cmds.joint(a=True, p=[5.206, 9.126, -0.574], rad=0.1, n='ring_lf_001_jntt')
        cmds.joint(a=True, p=[5.501, 8.846, -0.639], rad=0.1, n='ring_lf_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.508, 8.61, -0.619], rad=0.1, n='ring_lf_003_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.477, 8.378, -0.586], rad=0.1, n='ring_lf_004_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('ring_lf_001_jntt', hi=True)
        cmds.joint(e=True, oj='xyz', sao='yup', ch=True, zso=True)
        cmds.select(clear=True)
        
        # Pinky
        cmds.select(hand_jnt_grp, replace=True)
        cmds.joint(a=True, p=[5.069, 9.116, -0.734], rad=0.1, n='pinky_lf_001_jntt')
        cmds.joint(a=True, p=[5.209, 8.834, -0.826], rad=0.1, n='pinky_lf_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.233, 8.673, -0.842], rad=0.1, n='pinky_lf_003_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[5.236, 8.465, -0.843], rad=0.1, n='pinky_lf_004_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('pinky_lf_001_jntt', hi=True)
        cmds.joint(e=True, oj='xyz', sao='yup', ch=True, zso=True)
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
        cmds.joint(e=True, oj='xyz', sao='zup', ch=True, zso=True)
        cmds.select(clear=True)
        
        
        # Left Pelvis Joint
        pelvis_jnt_grp = cmds.group(empty=True, n="pelvis_jnt_grp")
        cmds.move(0, 8.85, 0.266, pelvis_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        
        cmds.joint(a=True, p=[0.181, 8.85, 0.266], rad=0.6, n='pelvis_lf_001_jnt')
        cmds.joint(a=True, p=[0.967, 8.495, 0.266], rad=0.6, n='pelvis_lf_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('pelvis_lf_001_jnt', hi=True)
        cmds.joint(e=True, oj='xyz', sao='yup', ch=True, zso=True)
        cmds.select(clear=True)
        
        
        # Left Leg Joint
        leg_jnt_grp = cmds.group(empty=True, n="leg_jnt_grp")
        cmds.move(0, 8.495, 0.266, leg_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        
        cmds.joint(a=True, p=[0.967, 8.495, 0.266], rad=0.6, n='leg_lf_ik_tight_jntt')
        cmds.joint(a=True, p=[0.967, 5.156, 0.344], rad=0.6, n='leg_lf_ik_shin_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0.967, 0.785, -0.193], rad=0.6, n='leg_lf_ik_ankle_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0.967, 0.186, 0.733], rad=0.6, n='leg_lf_ik_ball_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0.967, 0.186, 1.418], rad=0.6, n='leg_lf_ik_toe_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('leg_lf_ik_tight_jntt', hi=True)
        cmds.joint(e=True, oj='xyz', sao='zup', ch=True, zso=True)    # Orient Joint Options
        cmds.select(clear=True)
        
        ### Left Foot Joint    # When create controllers
        
        # Mirror Joint
        cmds.mirrorJoint('shoulder_lf_001_jnt', myz=True, mb=True, sr=('lf', 'rt'))
        cmds.mirrorJoint('arm_lf_ik_shoulder_jntt', myz=True, mb=True, sr=('lf', 'rt'))
        cmds.mirrorJoint('pelvis_lf_001_jnt', myz=True, mb=False, sr=('lf', 'rt'))
        cmds.mirrorJoint('leg_lf_ik_tight_jntt', myz=True, mb=True, sr=('lf', 'rt'))
        cmds.mirrorJoint('thumb_lf_001_jntt', myz=True, mb=True, sr=('lf', 'rt'))
        cmds.mirrorJoint('index_lf_001_jntt', myz=True, mb=True, sr=('lf', 'rt'))
        cmds.mirrorJoint('middle_lf_001_jntt', myz=True, mb=True, sr=('lf', 'rt'))
        cmds.mirrorJoint('ring_lf_001_jntt', myz=True, mb=True, sr=('lf', 'rt'))
        cmds.mirrorJoint('pinky_lf_001_jntt', myz=True, mb=True, sr=('lf', 'rt'))
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
        cmds.parent('arm_lf_ik_shoulder_jntt', arm_lf_jnt_grp)
        
        arm_rt_jnt_grp = cmds.group(empty=True, parent='arm_jnt_grp', n="arm_rt_jnt_grp")
        cmds.move(-1.135, 13.093, -0.504, arm_rt_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('arm_rt_ik_shoulder_jntt', arm_rt_jnt_grp)
        
        hand_lf_jnt_grp = cmds.group(empty=True, parent='hand_jnt_grp', n="hand_lf_jnt_grp")
        cmds.move(4.556, 9.612, -0.458, hand_lf_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('thumb_lf_001_jntt', hand_lf_jnt_grp)
        cmds.parent('index_lf_001_jntt', hand_lf_jnt_grp)
        cmds.parent('middle_lf_001_jntt', hand_lf_jnt_grp)
        cmds.parent('ring_lf_001_jntt', hand_lf_jnt_grp)
        cmds.parent('pinky_lf_001_jntt', hand_lf_jnt_grp)
        
        hand_rt_jnt_grp = cmds.group(empty=True, parent='hand_jnt_grp', n="hand_rt_jnt_grp")
        cmds.move(-4.556, 9.612, -0.458, hand_rt_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('thumb_rt_001_jntt', hand_rt_jnt_grp)
        cmds.parent('index_rt_001_jntt', hand_rt_jnt_grp)
        cmds.parent('middle_rt_001_jntt', hand_rt_jnt_grp)
        cmds.parent('ring_rt_001_jntt', hand_rt_jnt_grp)
        cmds.parent('pinky_rt_001_jntt', hand_rt_jnt_grp)
        
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
        cmds.parent('leg_lf_ik_tight_jntt', leg_lf_jnt_grp)
        
        leg_rt_jnt_grp = cmds.group(empty=True, parent='leg_jnt_grp', n="leg_rt_jnt_grp")
        cmds.move(-0.967, 8.495, 0.266, leg_rt_jnt_grp)
        cmds.makeIdentity(apply=True, t=True, r=True, s=True)
        cmds.parent('leg_rt_ik_tight_jntt', leg_rt_jnt_grp)
        
        cmds.select(clear=True)
        
        
        # Duplicate IK Joints for FK,BIND
        # Left Arm
        cmds.duplicate('arm_lf_ik_shoulder_jntt', rc=True)
        
        cmds.select('arm_lf_ik_shoulder_jntt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_bind = [0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_bind[i] = tmp_ik[i].replace('ik', 'fk')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_bind[i].split("|")[-1])
        
        cmds.select('arm_lf_fk_shoulder_jntt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_fk[i] = tmp_ik[i].replace('t1', 't')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_fk[i].split("|")[-1])
        #
        cmds.duplicate('arm_lf_ik_shoulder_jntt', rc=True)
        
        cmds.select('arm_lf_ik_shoulder_jntt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_bind = [0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_bind[i] = tmp_ik[i].replace('ik', 'bind')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_bind[i].split("|")[-1])
        
        cmds.select('arm_lf_bind_shoulder_jntt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_fk[i] = tmp_ik[i].replace('t1', 't')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_fk[i].split("|")[-1])
        #
        # Right Arm
        cmds.duplicate('arm_rt_ik_shoulder_jntt', rc=True)
        
        cmds.select('arm_rt_ik_shoulder_jntt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_bind = [0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_bind[i] = tmp_ik[i].replace('ik', 'fk')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_bind[i].split("|")[-1])
        
        cmds.select('arm_rt_fk_shoulder_jntt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_fk[i] = tmp_ik[i].replace('t1', 't')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_fk[i].split("|")[-1])
        #
        cmds.duplicate('arm_rt_ik_shoulder_jntt', rc=True)
        
        cmds.select('arm_rt_ik_shoulder_jntt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_bind = [0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_bind[i] = tmp_ik[i].replace('ik', 'bind')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_bind[i].split("|")[-1])
        
        cmds.select('arm_rt_bind_shoulder_jntt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_fk[i] = tmp_ik[i].replace('t1', 't')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_fk[i].split("|")[-1])
        #
        
        # Spine
        cmds.select(spine_jnt_grp)
        cmds.joint(a=True, p=[0, 8.869, 0.316], rad=0.6, n='spine_fk_001_jnt')
        cmds.joint(a=True, p=[0, 9.742, 0.404], rad=0.6, n='spine_fk_002_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0, 10.862, 0.379], rad=0.6, n='spine_fk_006_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        cmds.joint(a=True, p=[0, 11.847, 0.188], rad=0.6, n='spine_fk_009_jnt')
        cmds.joint(e=True, zso=True, oj='xyz', sao='yup')
        
        cmds.select('spine_fk_001_jnt', hi=True)
        cmds.joint(e=True, oj='xyz', sao='zup', ch=True, zso=True)
        
        # Left Leg
        cmds.duplicate('leg_lf_ik_tight_jntt', rc=True)
        
        cmds.select('leg_lf_ik_tight_jntt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_bind = [0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_bind[i] = tmp_ik[i].replace('ik', 'fk')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_bind[i].split("|")[-1])
        
        cmds.select('leg_lf_fk_tight_jntt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_fk[i] = tmp_ik[i].replace('t1', 't')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_fk[i].split("|")[-1])
        #
        cmds.duplicate('leg_lf_ik_tight_jntt', rc=True)
        
        cmds.select('leg_lf_ik_tight_jntt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_bind = [0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_bind[i] = tmp_ik[i].replace('ik', 'bind')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_bind[i].split("|")[-1])
        
        cmds.select('leg_lf_bind_tight_jntt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_fk[i] = tmp_ik[i].replace('t1', 't')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_fk[i].split("|")[-1])
        #
        # Right Leg
        cmds.duplicate('leg_rt_ik_tight_jntt', rc=True)
        
        cmds.select('leg_rt_ik_tight_jntt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_bind = [0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_bind[i] = tmp_ik[i].replace('ik', 'fk')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_bind[i].split("|")[-1])
        
        cmds.select('leg_rt_fk_tight_jntt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_fk[i] = tmp_ik[i].replace('t1', 't')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_fk[i].split("|")[-1])
        #
        cmds.duplicate('leg_rt_ik_tight_jntt', rc=True)
        
        cmds.select('leg_rt_ik_tight_jntt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_bind = [0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_bind[i] = tmp_ik[i].replace('ik', 'bind')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_bind[i].split("|")[-1])
        
        cmds.select('leg_rt_bind_tight_jntt1', hi=True)
        tmp_ik = cmds.ls(sl=True)
        tmp_fk = [0, 0, 0, 0, 0]
        for i in range(0, len(tmp_ik)):
            tmp_fk[i] = tmp_ik[i].replace('t1', 't')
            cmds.rename(tmp_ik[i].split("|")[-1], tmp_fk[i].split("|")[-1])
        #
        
        cmds.select(clear=True)
        
        
    def confirm_orient_joint(self, args):
        '''
            STEP 2: Check Joint Orientation
        '''
        
        cmds.select(all=True, hi=True)
        selectedObjs = cmds.ls(sl=True)
        
        for obj in selectedObjs:
            if (cmds.objectType(obj) == 'joint'):
                cmds.toggle(obj, localAxis=True)
        
        cmds.select(clear=True)
        
        
    def create_ctrl(self, args):
        '''
            STEP 3: Create Controllers
        '''
        pass
    

    def build(self, args):
        '''
            STEP 4: Build
        '''
        pass
    

    def import_weight(self, args):
        '''
            STEP 5: Import Weight
        '''
        pass
        cmds.fileBrowserDialog(mode=0, fileCommand=self.apply_weight, fileType='directory', an='Import weight', operationMode='Import')
        

    def apply_weight(self, fileName, fileType):
        pass
    
    
    def showHelp(self, args):
        cmds.showHelp("https://github.com/JaewanKim/maya-plugin", absolute=True)


JWAutoRig()