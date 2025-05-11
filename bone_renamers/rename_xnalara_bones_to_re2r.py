import bpy

class OBJECT_OT_rename_xnalara_bones_to_re2r(bpy.types.Operator):
    bl_idname = "object.rename_xnalara_bones_to_re2r"
    bl_label = "Rename Bones (Xnalara to RE2R)"
    bl_description = "Renames commonly used Xnalara bones to RE2R's naming conventions"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Correct dictionary definition
        bone_rename_dict = {
            'arm left elbow': 'l_arm_radius',
            'arm left finger 1a': 'l_hand_thumb_0',
            'arm left finger 1b': 'l_hand_thumb_1',
            'arm left finger 1c': 'l_hand_thumb_2',
            'arm left finger 2a': 'l_hand_index_0',
            'arm left finger 2b': 'l_hand_index_1',
            'arm left finger 2c': 'l_hand_index_2',
            'arm left finger 3a': 'l_hand_middle_0',
            'arm left finger 3b': 'l_hand_middle_1',
            'arm left finger 3c': 'l_hand_middle_2',
            'arm left finger 4a': 'l_hand_ring_1',
            'arm left finger 4b': 'l_hand_ring_2',
            'arm left finger 4c': 'l_hand_ring_3',
            'arm left finger 5a': 'l_hand_little_1',
            'arm left finger 5b': 'l_hand_little_2',
            'arm left finger 5c': 'l_hand_little_3',
            'arm left shoulder 1': 'l_arm_clavicle',
            'arm left shoulder 2': 'l_arm_humerus',
            'arm left shoulder ctrl 1': 'l_arm_humerus',
            'arm left shoulder ctrl 2': 'l_arm_humerus',
            'arm left wrist': 'l_arm_wrist',
            'arm left wrist ctrl 1': 'l_arm_wrist',
            'arm left wrist ctrl 2': 'l_arm_wrist',
            'arm right elbow': 'r_arm_radius',
            'arm right elbow ctrl': 'r_arm_radius',
            'arm right finger 1a': 'r_hand_thumb_0',
            'arm right finger 1b': 'r_hand_thumb_1',
            'arm right finger 1c': 'r_hand_thumb_2',
            'arm right finger 2a': 'r_hand_index_0',
            'arm right finger 2b': 'r_hand_index_1',
            'arm right finger 2c': 'r_hand_index_2',
            'arm right finger 3a': 'r_hand_middle_0',
            'arm right finger 3b': 'r_hand_middle_1',
            'arm right finger 3c': 'r_hand_middle_2',
            'arm right finger 4a': 'r_hand_ring_1',
            'arm right finger 4b': 'r_hand_ring_2',
            'arm right finger 4c': 'r_hand_ring_3',
            'arm right finger 5a': 'r_hand_little_1',
            'arm right finger 5b': 'r_hand_little_2',
            'arm right finger 5c': 'r_hand_little_3',
            'arm right shoulder 1': 'r_arm_clavicle',
            'arm right shoulder 2': 'r_arm_humerus',
            'arm right shoulder ctrl 1': 'r_arm_clavicle',
            'arm right shoulder ctrl 2': 'r_arm_clavicle',
            'arm right wrist': 'r_arm_wrist',
            'arm right wrist ctrl 1': 'r_arm_wrist',
            'arm right wrist ctrl 2': 'r_arm_wrist',
            'head neck lower': 'neck_0',
            'head neck upper': 'head',
            'leg left ankle': 'l_leg_ankle',
            'leg left knee': 'l_leg_tibia',
            'leg left knee ctrl': 'l_leg_tibia',
            'leg left thigh': 'l_leg_femur',
            'leg left thigh ctrl 1': 'l_leg_femur',
            'leg left thigh ctrl 2': 'l_leg_femur',
            'leg left thigh ctrl 3': 'l_leg_femur',
            'leg left toes': 'l_leg_ball',
            'leg right ankle': 'r_leg_ankle',
            'leg right knee': 'r_leg_tibia',
            'leg right knee ctrl': 'r_leg_tibia',
            'leg right thigh': 'r_leg_femur',
            'leg right thigh ctrl 1': 'r_leg_femur',
            'leg right thigh ctrl 2': 'r_leg_femur',
            'leg right thigh ctrl 3': 'r_leg_femur',
            'leg right toes': 'r_leg_ball',
            'pelvis': 'hips',
            'spine lower': 'spine_0',
            'spine middle': 'spine_1',
            'spine upper': 'spine_2',
        }

        try:
            arm = context.object.data
            for bone in arm.bones:
                if bone.name.lower() in bone_rename_dict:  # Check if bone name exists in the dictionary keys
                    bone.name = bone_rename_dict[bone.name.lower()]  # Rename using dictionary value
            self.report({'INFO'}, "Bones renamed successfully!")
            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}