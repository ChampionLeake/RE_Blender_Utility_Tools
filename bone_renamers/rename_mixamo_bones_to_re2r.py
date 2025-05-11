import bpy

class OBJECT_OT_rename_mixamo_bones_to_re2r(bpy.types.Operator):
    bl_idname = "object.rename_mixamo_bones_to_re2r"
    bl_label = "Rename Bones (Mixamo to RE2R)"
    bl_description = "Renames commonly used Mixamo bones to RE2R's naming conventions"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Correct dictionary definition
        bone_rename_dict = {
            'mixamorig:LeftForeArm': 'l_arm_radius',
            'mixamorig:LeftHandThumb1': 'l_hand_thumb_0',
            'mixamorig:LeftHandThumb2': 'l_hand_thumb_1',
            'mixamorig:LeftHandThumb3': 'l_hand_thumb_2',
            'mixamorig:LeftHandIndex1': 'l_hand_index_0',
            'mixamorig:LeftHandIndex2': 'l_hand_index_1',
            'mixamorig:LeftHandIndex3': 'l_hand_index_2',
            'mixamorig:LeftHandMiddle1': 'l_hand_middle_0',
            'mixamorig:LeftHandMiddle2': 'l_hand_middle_1',
            'mixamorig:LeftHandMiddle3': 'l_hand_middle_2',
            'mixamorig:LeftHandRing1': 'l_hand_ring_1',
            'mixamorig:LeftHandRing2': 'l_hand_ring_2',
            'mixamorig:LeftHandRing3': 'l_hand_ring_3',
            'mixamorig:LeftHandPinky1': 'l_hand_little_1',
            'mixamorig:LeftHandPinky2': 'l_hand_little_2',
            'mixamorig:LeftHandPinky3': 'l_hand_little_3',
            'mixamorig:LeftShoulder': 'l_arm_clavicle',
            'mixamorig:LeftArm': 'l_arm_humerus',
            'mixamorig:LeftHand': 'l_arm_wrist',
            'mixamorig:RightShoulder': 'r_arm_clavicle',
            'mixamorig:RightForeArm': 'r_arm_radius',
            'mixamorig:RightHandThumb1': 'r_hand_thumb_0',
            'mixamorig:RightHandThumb2': 'r_hand_thumb_1',
            'mixamorig:RightHandThumb3': 'r_hand_thumb_2',
            'mixamorig:RightHandIndex1': 'r_hand_index_0',
            'mixamorig:RightHandIndex2': 'r_hand_index_1',
            'mixamorig:RightHandIndex3': 'r_hand_index_2',
            'mixamorig:RightHandMiddle1': 'r_hand_middle_0',
            'mixamorig:RightHandMiddle2': 'r_hand_middle_1',
            'mixamorig:RightHandMiddle3': 'r_hand_middle_2',
            'mixamorig:RightHandRing1': 'r_hand_ring_1',
            'mixamorig:RightHandRing2': 'r_hand_ring_2',
            'mixamorig:RightHandRing3': 'r_hand_ring_3',
            'mixamorig:RightHandPinky1': 'r_hand_little_1',
            'mixamorig:RightHandPinky2': 'r_hand_little_2',
            'mixamorig:RightHandPinky3': 'r_hand_little_3',
            'mixamorig:RightArm': 'r_arm_humerus',
            'mixamorig:RightHand': 'r_arm_wrist',
            'mixamorig:Neck': 'neck_0',
            'mixamorig:Head': 'head',
            'mixamorig:LeftFoot': 'l_leg_ankle',
            'mixamorig:LeftLeg': 'l_leg_tibia',
            'mixamorig:LeftUpLeg': 'l_leg_femur',
            'mixamorig:LeftToeBase': 'l_leg_ball',
            'mixamorig:RightFoot': 'r_leg_ankle',
            'mixamorig:RightLeg': 'r_leg_tibia',
            'mixamorig:RightUpLeg': 'r_leg_femur',
            'mixamorig:RightToeBase': 'r_leg_ball',
            'mixamorig:Hips': 'hips',
            'mixamorig:Spine': 'spine_0',
            'mixamorig:Spine1': 'spine_1',
            'mixamorig:Spine2': 'spine_2',

        }

        try:
            arm = context.object.data
            for bone in arm.bones:
                if bone.name in bone_rename_dict:  # Check if bone name exists in the dictionary keys
                    bone.name = bone_rename_dict[bone.name]  # Rename using dictionary value
            self.report({'INFO'}, "Bones renamed successfully!")
            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}