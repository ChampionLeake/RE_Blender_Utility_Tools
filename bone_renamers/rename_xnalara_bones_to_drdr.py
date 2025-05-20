import bpy

class OBJECT_OT_rename_xnalara_bones_to_drdr(bpy.types.Operator):
    bl_idname = "object.rename_xnalara_bones_to_drdr"
    bl_label = "Rename Bones (Xnalara to DRDR)"
    bl_description = "Renames commonly used Xnalara bones to DRDR's naming conventions"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Correct dictionary definition
        bone_rename_dict = {
            'arm left elbow': 'L_Forearm',
            'arm left finger 1a': 'L_Thumb_01',
            'arm left finger 1b': 'L_Thumb_02',
            'arm left finger 1c': 'L_Thumb_03',
            'arm left finger 2a': 'L_Index_01',
            'arm left finger 2b': 'L_Index_02',
            'arm left finger 2c': 'L_Index_03',
            'arm left finger 3a': 'L_Middle_01',
            'arm left finger 3b': 'L_Middle_02',
            'arm left finger 3c': 'L_Middle_03',
            'arm left finger 4a': 'L_Ring_01',
            'arm left finger 4b': 'L_Ring_02',
            'arm left finger 4c': 'L_Ring_03',
            'arm left finger 5a': 'L_Pinky_01',
            'arm left finger 5b': 'L_Pinky_02',
            'arm left finger 5c': 'L_Pinky_03',
            'arm left shoulder 1': 'L_Shoulder',
            'arm left shoulder 2': 'L_UpperArm',
            'arm left shoulder ctrl 1': 'L_UpperArm',
            'arm left shoulder ctrl 2': 'L_UpperArm',
            'arm left wrist': 'L_Hand',
            'arm left wrist ctrl 1': 'L_Hand',
            'arm left wrist ctrl 2': 'L_Hand',
            'arm right elbow': 'R_Forearm',
            'arm right elbow ctrl': 'R_Forearm',
            'arm right finger 1a': 'R_Thumb_01',
            'arm right finger 1b': 'R_Thumb_02',
            'arm right finger 1c': 'R_Thumb_03',
            'arm right finger 2a': 'R_Index_01',
            'arm right finger 2b': 'R_Index_02',
            'arm right finger 2c': 'R_Index_03',
            'arm right finger 3a': 'R_Middle_01',
            'arm right finger 3b': 'R_Middle_02',
            'arm right finger 3c': 'R_Middle_03',
            'arm right finger 4a': 'R_Ring_01',
            'arm right finger 4b': 'R_Ring_02',
            'arm right finger 4c': 'R_Ring_03',
            'arm right finger 5a': 'R_Pinky_01',
            'arm right finger 5b': 'R_Pinky_02',
            'arm right finger 5c': 'R_Pinky_03',
            'arm right shoulder 1': 'R_Shoulder',
            'arm right shoulder 2': 'R_UpperArm',
            'arm right shoulder ctrl 1': 'R_Shoulder',
            'arm right shoulder ctrl 2': 'R_Shoulder',
            'arm right wrist': 'R_Hand',
            'arm right wrist ctrl 1': 'R_Hand',
            'arm right wrist ctrl 2': 'R_Hand',
            'head neck lower': 'C_Neck',
            'head neck upper': 'C_Head',
            'leg left ankle': 'L_Foot',
            'leg left knee': 'L_Foreleg',
            'leg left knee ctrl': 'L_Foreleg',
            'leg left thigh': 'L_UpperLeg',
            'leg left thigh ctrl 1': 'L_UpperLeg',
            'leg left thigh ctrl 2': 'L_UpperLeg',
            'leg left thigh ctrl 3': 'L_UpperLeg',
            'leg left toes': 'L_Toe',
            'leg right ankle': 'R_Foot',
            'leg right knee': 'R_Foreleg',
            'leg right knee ctrl': 'R_Foreleg',
            'leg right thigh': 'R_UpperLeg',
            'leg right thigh ctrl 1': 'R_UpperLeg',
            'leg right thigh ctrl 2': 'R_UpperLeg',
            'leg right thigh ctrl 3': 'R_UpperLeg',
            'leg right toes': 'R_Toe',
            'pelvis': 'COG',
            'spine lower': 'C_Spine_00',
            'spine middle': 'C_Spine_01',
            'spine upper': 'C_Spine_02',
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