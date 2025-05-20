import bpy

class OBJECT_OT_rename_mmd_bones_to_dmc5(bpy.types.Operator):
    bl_idname = "object.rename_mmd_bones_to_dmc5"
    bl_label = "Rename Bones (MMD to DMC5)"
    bl_description = "Renames commonly used MMD bones to DMC5's naming conventions"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Correct dictionary definition
        bone_rename_dict = {
            'ひじ.L': 'L_Forearm',
            '親指０.L': 'L_Thumb1',
            '親指１.L': 'L_Thumb2',
            '親指２.L': 'L_Thumb3',
            '人指１.L': 'L_IndexF1',
            '人指２.L': 'L_IndexF2',
            '人指３.L': 'L_IndexF3',
            '中指１.L': 'L_MiddleF1',
            '中指２.L': 'L_MiddleF2',
            '中指３.L': 'L_MiddleF3',
            '薬指１.L': 'L_RingF1',
            '薬指２.L': 'L_RingF2',
            '薬指３.L': 'L_RingF3',
            '小指１.L': 'L_PinkyF1',
            '小指２.L': 'L_PinkyF2',
            '小指３.L': 'L_PinkyF3',
            '肩.L': 'L_Shoulder',
            '腕.L': 'L_UpperArm',
            '手首.L': 'L_Hand',
            'ひじ.R': 'R_Forearm',
            '親指０.R': 'R_Thumb1',
            '親指１.R': 'R_Thumb2',
            '親指２.R': 'R_Thumb3',
            '人指１.R': 'R_IndexF1',
            '人指２.R': 'R_IndexF2',
            '人指３.R': 'R_IndexF3',
            '中指１.R': 'R_MiddleF1',
            '中指２.R': 'R_MiddleF2',
            '中指３.R': 'R_MiddleF3',
            '薬指１.R': 'R_RingF1',
            '薬指２.R': 'R_RingF2',
            '薬指３.R': 'R_RingF3',
            '小指１.R': 'R_PinkyF1',
            '小指２.R': 'R_PinkyF2',
            '小指３.R': 'R_PinkyF3',
            '肩.R': 'R_Shoulder',
            '腕.R': 'R_UpperArm',
            '手首.R': 'R_Hand',
            '首': 'Neck',
            '頭': 'Head',
            '足首.L': 'L_Foot',
            'ひざ.L': 'L_Shin',
            '足.L': 'L_Thigh',
            'つま先.L': 'L_Toe',
            '足首.R': 'R_Foot',
            'ひざ.R': 'R_Shin',
            '足.R': 'R_Thigh',
            'つま先.R': 'R_Toe',
            '下半身': 'Hip',
            '上半身': 'Waist',
            '上半身１': 'Stomach',
            '上半身2': 'Chest',

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