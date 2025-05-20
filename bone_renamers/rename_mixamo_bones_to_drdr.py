import bpy

class OBJECT_OT_rename_mixamo_bones_to_drdr(bpy.types.Operator):
    bl_idname = "object.rename_mixamo_bones_to_drdr"
    bl_label = "Rename Bones (Mixamo to DRDR)"
    bl_description = "Renames commonly used Mixamo bones to DRDR's naming conventions"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Correct dictionary definition
        bone_rename_dict = {
            'mixamorig:LeftForeArm': 'L_Forearm',
            'mixamorig:LeftHandThumb1': 'L_Thumb_01',
            'mixamorig:LeftHandThumb2': 'L_Thumb_02',
            'mixamorig:LeftHandThumb3': 'L_Thumb_03',
            'mixamorig:LeftHandIndex1': 'L_Index_01',
            'mixamorig:LeftHandIndex2': 'L_Index_02',
            'mixamorig:LeftHandIndex3': 'L_Index_03',
            'mixamorig:LeftHandMiddle1': 'L_Middle_01',
            'mixamorig:LeftHandMiddle2': 'L_Middle_02',
            'mixamorig:LeftHandMiddle3': 'L_Middle_03',
            'mixamorig:LeftHandRing1': 'L_Ring_01',
            'mixamorig:LeftHandRing2': 'L_Ring_02',
            'mixamorig:LeftHandRing3': 'L_Ring_03',
            'mixamorig:LeftHandPinky1': 'L_Pinky_01',
            'mixamorig:LeftHandPinky2': 'L_Pinky_02',
            'mixamorig:LeftHandPinky3': 'L_Pinky_03',
            'mixamorig:LeftShoulder': 'L_Shoulder',
            'mixamorig:LeftArm': 'L_UpperArm',
            'mixamorig:LeftHand': 'L_Hand',
            'mixamorig:RightShoulder': 'R_Shoulder',
            'mixamorig:RightForeArm': 'R_Forearm',
            'mixamorig:RightHandThumb1': 'R_Thumb_01',
            'mixamorig:RightHandThumb2': 'R_Thumb_02',
            'mixamorig:RightHandThumb3': 'R_Thumb_03',
            'mixamorig:RightHandIndex1': 'R_Index_01',
            'mixamorig:RightHandIndex2': 'R_Index_02',
            'mixamorig:RightHandIndex3': 'R_Index_03',
            'mixamorig:RightHandMiddle1': 'R_Middle_01',
            'mixamorig:RightHandMiddle2': 'R_Middle_02',
            'mixamorig:RightHandMiddle3': 'R_Middle_03',
            'mixamorig:RightHandRing1': 'R_Ring_01',
            'mixamorig:RightHandRing2': 'R_Ring_02',
            'mixamorig:RightHandRing3': 'R_Ring_03',
            'mixamorig:RightHandPinky1': 'R_Pinky_01',
            'mixamorig:RightHandPinky2': 'R_Pinky_02',
            'mixamorig:RightHandPinky3': 'R_Pinky_03',
            'mixamorig:RightArm': 'R_UpperArm',
            'mixamorig:RightHand': 'R_Hand',
            'mixamorig:Neck': 'C_Neck',
            'mixamorig:Head': 'C_Head',
            'mixamorig:LeftFoot': 'L_Foot',
            'mixamorig:LeftLeg': 'L_Foreleg',
            'mixamorig:LeftUpLeg': 'L_UpperLeg',
            'mixamorig:LeftToeBase': 'L_Toe',
            'mixamorig:RightFoot': 'R_Foot',
            'mixamorig:RightLeg': 'R_Foreleg',
            'mixamorig:RightUpLeg': 'R_UpperLeg',
            'mixamorig:RightToeBase': 'R_Toe',
            'mixamorig:Hips': 'COG',
            'mixamorig:Spine': 'C_Spine_00',
            'mixamorig:Spine1': 'C_Spine_01',
            'mixamorig:Spine2': 'C_Spine_02',

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