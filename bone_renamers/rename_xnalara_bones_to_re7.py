import bpy

class OBJECT_OT_rename_xnalara_bones_to_re7(bpy.types.Operator):
    bl_idname = "object.rename_xnalara_bones_to_re7"
    bl_label = "Rename Bones (Xnalara to RE7)"
    bl_description = "Renames commonly used Xnalara bones to RE7's naming conventions"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Correct dictionary definition
        bone_rename_dict = {
            'arm left elbow': 'L_Forearm',
            'arm left finger 1a': 'L_Thumb1',
            'arm left finger 1b': 'L_Thumb2',
            'arm left finger 1c': 'L_Thumb3',
            'arm left finger 2a': 'L_IndexF1',
            'arm left finger 2b': 'L_IndexF2',
            'arm left finger 2c': 'L_IndexF3',
            'arm left finger 3a': 'L_MiddleF1',
            'arm left finger 3b': 'L_MiddleF2',
            'arm left finger 3c': 'L_MiddleF3',
            'arm left finger 4a': 'L_RingF1',
            'arm left finger 4b': 'L_RingF2',
            'arm left finger 4c': 'L_RingF3',
            'arm left finger 5a': 'L_PinkyF1',
            'arm left finger 5b': 'L_PinkyF2',
            'arm left finger 5c': 'L_PinkyF3',
            'arm left shoulder 1': 'L_Shoulder',
            'arm left shoulder 2': 'L_UpperArm',
            'arm left shoulder ctrl 1': 'L_UpperArm',
            'arm left shoulder ctrl 2': 'L_UpperArm',
            'arm left wrist': 'L_Hand',
            'arm left wrist ctrl 1': 'L_Hand',
            'arm left wrist ctrl 2': 'L_Hand',
            'arm right elbow': 'R_Forearm',
            'arm right elbow ctrl': 'R_Forearm',
            'arm right finger 1a': 'R_Thumb1',
            'arm right finger 1b': 'R_Thumb2',
            'arm right finger 1c': 'R_Thumb3',
            'arm right finger 2a': 'R_IndexF1',
            'arm right finger 2b': 'R_IndexF2',
            'arm right finger 2c': 'R_IndexF3',
            'arm right finger 3a': 'R_MiddleF1',
            'arm right finger 3b': 'R_MiddleF2',
            'arm right finger 3c': 'R_MiddleF3',
            'arm right finger 4a': 'R_RingF1',
            'arm right finger 4b': 'R_RingF2',
            'arm right finger 4c': 'R_RingF3',
            'arm right finger 5a': 'R_PinkyF1',
            'arm right finger 5b': 'R_PinkyF2',
            'arm right finger 5c': 'R_PinkyF3',
            'arm right shoulder 1': 'R_Shoulder',
            'arm right shoulder 2': 'R_UpperArm',
            'arm right shoulder ctrl 1': 'R_Shoulder',
            'arm right shoulder ctrl 2': 'R_Shoulder',
            'arm right wrist': 'R_Hand',
            'arm right wrist ctrl 1': 'R_Hand',
            'arm right wrist ctrl 2': 'R_Hand',
            'head neck lower': 'Neck',
            'head neck upper': 'Head',
            'leg left ankle': 'L_Foot',
            'leg left knee': 'L_Shin',
            'leg left knee ctrl': 'L_Shin',
            'leg left thigh': 'L_Thigh',
            'leg left thigh ctrl 1': 'L_Thigh',
            'leg left thigh ctrl 2': 'L_Thigh',
            'leg left thigh ctrl 3': 'L_Thigh',
            'leg left toes': 'L_Toe',
            'leg right ankle': 'R_Foot',
            'leg right knee': 'R_Shin',
            'leg right knee ctrl': 'R_Shin',
            'leg right thigh': 'R_Thigh',
            'leg right thigh ctrl 1': 'R_Thigh',
            'leg right thigh ctrl 2': 'R_Thigh',
            'leg right thigh ctrl 3': 'R_Thigh',
            'leg right toes': 'R_Toe',
            'pelvis': 'Hip',
            'spine lower': 'Waist',
            'spine middle': 'Stomach',
            'spine upper': 'Chest',
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