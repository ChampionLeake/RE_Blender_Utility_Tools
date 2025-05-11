import bpy

class OBJECT_OT_rename_mmd_bones_to_re3r(bpy.types.Operator):
    bl_idname = "object.rename_mmd_bones_to_re3r"
    bl_label = "Rename Bones (MMD to RE3R)"
    bl_description = "Renames commonly used MMD bones to RE3R's naming conventions"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Correct dictionary definition
        bone_rename_dict = {
            'ひじ.L': 'l arm radius',
            '親指０.L': 'l hand thumb 0',
            '親指１.L': 'l hand thumb 1',
            '親指２.L': 'l hand thumb 2',
            '人指１.L': 'l hand index 0',
            '人指２.L': 'l hand index 1',
            '人指３.L': 'l hand index 2',
            '中指１.L': 'l hand middle 0',
            '中指２.L': 'l hand middle 1',
            '中指３.L': 'l hand middle 2',
            '薬指１.L': 'l hand ring 1',
            '薬指２.L': 'l hand ring 2',
            '薬指３.L': 'l hand ring 3',
            '小指１.L': 'l hand little 1',
            '小指２.L': 'l hand little 2',
            '小指３.L': 'l hand little 3',
            '肩.L': 'l arm clavicle',
            '腕.L': 'l arm humerus',
            '手首.L': 'l arm wrist',
            'ひじ.R': 'r arm radius',
            '親指０.R': 'r hand thumb 0',
            '親指１.R': 'r hand thumb 1',
            '親指２.R': 'r hand thumb 2',
            '人指１.R': 'r hand index 0',
            '人指２.R': 'r hand index 1',
            '人指３.R': 'r hand index 2',
            '中指１.R': 'r hand middle 0',
            '中指２.R': 'r hand middle 1',
            '中指３.R': 'r hand middle 2',
            '薬指１.R': 'r hand ring 1',
            '薬指２.R': 'r hand ring 2',
            '薬指３.R': 'r hand ring 3',
            '小指１.R': 'r hand little 1',
            '小指２.R': 'r hand little 2',
            '小指３.R': 'r hand little 3',
            '肩.R': 'r arm clavicle',
            '腕.R': 'r arm humerus',
            '手首.R': 'r arm wrist',
            '首': 'neck 0',
            '頭': 'head',
            '足首.L': 'l leg ankle',
            'ひざ.L': 'l leg tibia',
            '足.L': 'l leg femur',
            'つま先.L': 'l leg ball',
            '足首.R': 'r leg ankle',
            'ひざ.R': 'r leg tibia',
            '足.R': 'r leg femur',
            'つま先.R': 'r leg ball',
            '下半身': 'hips',
            '上半身': 'spine 0',
            '上半身１': 'spine 1',
            '上半身2': 'spine 2',

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