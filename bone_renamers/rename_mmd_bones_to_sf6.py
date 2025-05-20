import bpy

class OBJECT_OT_rename_mmd_bones_to_sf6(bpy.types.Operator):
    bl_idname = "object.rename_mmd_bones_to_sf6"
    bl_label = "Rename Bones (MMD to SF6)"
    bl_description = "Renames commonly used MMD bones to SF6's naming conventions"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Correct dictionary definition
        bone_rename_dict = {
            'ひじ.L': 'L_ForeArm',
            '親指０.L': 'L_Thumb1',
            '親指１.L': 'L_Thumb2',
            '親指２.L': 'L_Thumb3',
            '人指１.L': 'L_Index1',
            '人指２.L': 'L_Index2',
            '人指３.L': 'L_Index3',
            '中指１.L': 'L_Middle1',
            '中指２.L': 'L_Middle2',
            '中指３.L': 'L_Middle3',
            '薬指１.L': 'L_Ring2',
            '薬指２.L': 'L_Ring3',
            '薬指３.L': 'L_Ring4',
            '小指１.L': 'L_Pinky2',
            '小指２.L': 'L_Pinky3',
            '小指３.L': 'L_Pinky4',
            '肩.L': 'L_Shoulder',
            '腕.L': 'L_UpperArm',
            '手首.L': 'L_Hand',
            'ひじ.R': 'R_ForeArm',
            '親指０.R': 'R_Thumb1',
            '親指１.R': 'R_Thumb2',
            '親指２.R': 'R_Thumb3',
            '人指１.R': 'R_Index1',
            '人指２.R': 'R_Index2',
            '人指３.R': 'R_Index3',
            '中指１.R': 'R_Middle1',
            '中指２.R': 'R_Middle2',
            '中指３.R': 'R_Middle3',
            '薬指１.R': 'R_Ring2',
            '薬指２.R': 'R_Ring3',
            '薬指３.R': 'R_Ring4',
            '小指１.R': 'R_Pinky2',
            '小指２.R': 'R_Pinky3',
            '小指３.R': 'R_Pinky4',
            '肩.R': 'R_Shoulder',
            '腕.R': 'R_UpperArm',
            '手首.R': 'R_Hand',
            '首': 'C_Neck1',
            '頭': 'C_Head',
            '足首.L': 'L_Foot',
            'ひざ.L': 'L_Knee',
            '足.L': 'L_Thigh',
            'つま先.L': 'L_Toe',
            '足首.R': 'R_Foot',
            'ひざ.R': 'R_Knee',
            '足.R': 'R_Thigh',
            'つま先.R': 'R_Toe',
            '下半身': 'C_Hip',
            '上半身': 'C_Spine1',
            '上半身１': 'C_Spine2',
            '上半身2': 'C_Chest',

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