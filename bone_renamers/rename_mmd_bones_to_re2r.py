import bpy

class OBJECT_OT_rename_mmd_bones_to_re2r(bpy.types.Operator):
    bl_idname = "object.rename_mmd_bones_to_re2r"
    bl_label = "Rename Bones (MMD to RE2R)"
    bl_description = "Renames commonly used MMD bones to RE2R's naming conventions"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Correct dictionary definition
        bone_rename_dict = {
            'ひじ.L': 'l_arm_radius',
            '親指０.L': 'l_hand_thumb_0',
            '親指１.L': 'l_hand_thumb_1',
            '親指２.L': 'l_hand_thumb_2',
            '人指１.L': 'l_hand_index_0',
            '人指２.L': 'l_hand_index_1',
            '人指３.L': 'l_hand_index_2',
            '中指１.L': 'l_hand_middle_0',
            '中指２.L': 'l_hand_middle_1',
            '中指３.L': 'l_hand_middle_2',
            '薬指１.L': 'l_hand_ring_1',
            '薬指２.L': 'l_hand_ring_2',
            '薬指３.L': 'l_hand_ring_3',
            '小指１.L': 'l_hand_little_1',
            '小指２.L': 'l_hand_little_2',
            '小指３.L': 'l_hand_little_3',
            '肩.L': 'l_arm_clavicle',
            '腕.L': 'l_arm_humerus',
            '手首.L': 'l_arm_wrist',
            'ひじ.R': 'r_arm_radius',
            '親指０.R': 'r_hand_thumb_0',
            '親指１.R': 'r_hand_thumb_1',
            '親指２.R': 'r_hand_thumb_2',
            '人指１.R': 'r_hand_index_0',
            '人指２.R': 'r_hand_index_1',
            '人指３.R': 'r_hand_index_2',
            '中指１.R': 'r_hand_middle_0',
            '中指２.R': 'r_hand_middle_1',
            '中指３.R': 'r_hand_middle_2',
            '薬指１.R': 'r_hand_ring_1',
            '薬指２.R': 'r_hand_ring_2',
            '薬指３.R': 'r_hand_ring_3',
            '小指１.R': 'r_hand_little_1',
            '小指２.R': 'r_hand_little_2',
            '小指３.R': 'r_hand_little_3',
            '肩.R': 'r_arm_clavicle',
            '腕.R': 'r_arm_humerus',
            '手首.R': 'r_arm_wrist',
            '首': 'neck_0',
            '頭': 'head',
            '足首.L': 'l_leg_ankle',
            'ひざ.L': 'l_leg_tibia',
            '足.L': 'l_leg_femur',
            'つま先.L': 'l_leg_ball',
            '足首.R': 'r_leg_ankle',
            'ひざ.R': 'r_leg_tibia',
            '足.R': 'r_leg_femur',
            'つま先.R': 'r_leg_ball',
            '下半身': 'hips',
            '上半身': 'spine_0',
            '上半身１': 'spine_1',
            '上半身2': 'spine_2',
            
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