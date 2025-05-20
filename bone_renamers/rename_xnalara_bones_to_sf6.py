import bpy

class OBJECT_OT_rename_xnalara_bones_to_sf6(bpy.types.Operator):
    bl_idname = "object.rename_xnalara_bones_to_sf6"
    bl_label = "Rename Bones (Xnalara to SF6)"
    bl_description = "Renames commonly used Xnalara bones to SF6's naming conventions"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Correct dictionary definition
        bone_rename_dict = {
            'arm left elbow': 'L_ForeArm',
            'arm left finger 1a': 'L_Thumb1',
            'arm left finger 1b': 'L_Thumb2',
            'arm left finger 1c': 'L_Thumb3',
            'arm left finger 2a': 'L_Index1',
            'arm left finger 2b': 'L_Index2',
            'arm left finger 2c': 'L_Index3',
            'arm left finger 3a': 'L_Middle1',
            'arm left finger 3b': 'L_Middle2',
            'arm left finger 3c': 'L_Middle3',
            'arm left finger 4a': 'L_Ring2',
            'arm left finger 4b': 'L_Ring3',
            'arm left finger 4c': 'L_Ring4',
            'arm left finger 5a': 'L_Pinky2',
            'arm left finger 5b': 'L_Pinky3',
            'arm left finger 5c': 'L_Pinky4',
            'arm left shoulder 1': 'L_Shoulder',
            'arm left shoulder 2': 'L_UpperArm',
            'arm left shoulder ctrl 1': 'L_UpperArm',
            'arm left shoulder ctrl 2': 'L_UpperArm',
            'arm left wrist': 'L_Hand',
            'arm left wrist ctrl 1': 'L_Hand',
            'arm left wrist ctrl 2': 'L_Hand',
            'arm right elbow': 'R_ForeArm',
            'arm right elbow ctrl': 'R_ForeArm',
            'arm right finger 1a': 'R_Thumb1',
            'arm right finger 1b': 'R_Thumb2',
            'arm right finger 1c': 'R_Thumb3',
            'arm right finger 2a': 'R_Index1',
            'arm right finger 2b': 'R_Index2',
            'arm right finger 2c': 'R_Index3',
            'arm right finger 3a': 'R_Middle1',
            'arm right finger 3b': 'R_Middle2',
            'arm right finger 3c': 'R_Middle3',
            'arm right finger 4a': 'R_Ring2',
            'arm right finger 4b': 'R_Ring3',
            'arm right finger 4c': 'R_Ring4',
            'arm right finger 5a': 'R_Pinky2',
            'arm right finger 5b': 'R_Pinky3',
            'arm right finger 5c': 'R_Pinky4',
            'arm right shoulder 1': 'R_Shoulder',
            'arm right shoulder 2': 'R_UpperArm',
            'arm right shoulder ctrl 1': 'R_Shoulder',
            'arm right shoulder ctrl 2': 'R_Shoulder',
            'arm right wrist': 'R_Hand',
            'arm right wrist ctrl 1': 'R_Hand',
            'arm right wrist ctrl 2': 'R_Hand',
            'head neck lower': 'C_Neck1',
            'head neck upper': 'C_Head',
            'leg left ankle': 'L_Foot',
            'leg left knee': 'L_Knee',
            'leg left knee ctrl': 'L_Knee',
            'leg left thigh': 'L_Thigh',
            'leg left thigh ctrl 1': 'L_Thigh',
            'leg left thigh ctrl 2': 'L_Thigh',
            'leg left thigh ctrl 3': 'L_Thigh',
            'leg left toes': 'L_Toe',
            'leg right ankle': 'R_Foot',
            'leg right knee': 'R_Knee',
            'leg right knee ctrl': 'R_Knee',
            'leg right thigh': 'R_Thigh',
            'leg right thigh ctrl 1': 'R_Thigh',
            'leg right thigh ctrl 2': 'R_Thigh',
            'leg right thigh ctrl 3': 'R_Thigh',
            'leg right toes': 'R_Toe',
            'pelvis': 'C_Hip',
            'spine lower': 'C_Spine1',
            'spine middle': 'C_Spine2',
            'spine upper': 'C_Chest',
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