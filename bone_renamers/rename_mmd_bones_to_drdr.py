import bpy

class OBJECT_OT_rename_mmd_bones_to_drdr(bpy.types.Operator):
    bl_idname = "object.rename_mmd_bones_to_drdr"
    bl_label = "Rename Bones (MMD to DRDR)"
    bl_description = "Renames commonly used MMD bones to DRDR's naming conventions"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Correct dictionary definition
        bone_rename_dict = {
            'ひじ.L': 'L_Forearm',
            '親指０.L': 'L_Thumb_01',
            '親指１.L': 'L_Thumb_02',
            '親指２.L': 'L_Thumb_03',
            '人指１.L': 'L_Index_01',
            '人指２.L': 'L_Index_02',
            '人指３.L': 'L_Index_03',
            '中指１.L': 'L_Middle_01',
            '中指２.L': 'L_Middle_02',
            '中指３.L': 'L_Middle_03',
            '薬指１.L': 'L_Ring_01',
            '薬指２.L': 'L_Ring_02',
            '薬指３.L': 'L_Ring_03',
            '小指１.L': 'L_Pinky_01',
            '小指２.L': 'L_Pinky_02',
            '小指３.L': 'L_Pinky_03',
            '肩.L': 'L_Shoulder',
            '腕.L': 'L_UpperArm',
            '手首.L': 'L_Hand',
            'ひじ.R': 'R_Forearm',
            '親指０.R': 'R_Thumb_01',
            '親指１.R': 'R_Thumb_02',
            '親指２.R': 'R_Thumb_03',
            '人指１.R': 'R_Index_01',
            '人指２.R': 'R_Index_02',
            '人指３.R': 'R_Index_03',
            '中指１.R': 'R_Middle_01',
            '中指２.R': 'R_Middle_02',
            '中指３.R': 'R_Middle_03',
            '薬指１.R': 'R_Ring_01',
            '薬指２.R': 'R_Ring_02',
            '薬指３.R': 'R_Ring_03',
            '小指１.R': 'R_Pinky_01',
            '小指２.R': 'R_Pinky_02',
            '小指３.R': 'R_Pinky_03',
            '肩.R': 'R_Shoulder',
            '腕.R': 'R_UpperArm',
            '手首.R': 'R_Hand',
            '首': 'C_Neck',
            '頭': 'C_Head',
            '足首.L': 'L_Foot',
            'ひざ.L': 'L_Foreleg',
            '足.L': 'L_UpperLeg',
            'つま先.L': 'L_Toe',
            '足首.R': 'R_Foot',
            'ひざ.R': 'R_Foreleg',
            '足.R': 'R_UpperLeg',
            'つま先.R': 'R_Toe',
            '下半身': 'COG',
            '上半身': 'C_Spine_00',
            '上半身１': 'C_Spine_01',
            '上半身2': 'C_Spine_02',

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