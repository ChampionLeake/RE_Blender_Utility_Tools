import bpy

class OBJECT_OT_rename_mixamo_bones_to_sf6(bpy.types.Operator):
    bl_idname = "object.rename_mixamo_bones_to_sf6"
    bl_label = "Rename Bones (Mixamo to SF6)"
    bl_description = "Renames commonly used Mixamo bones to SF6's naming conventions"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Correct dictionary definition
        bone_rename_dict = {
            'mixamorig:LeftForeArm': 'L_ForeArm',
            'mixamorig:LeftHandThumb1': 'L_Thumb1',
            'mixamorig:LeftHandThumb2': 'L_Thumb2',
            'mixamorig:LeftHandThumb3': 'L_Thumb3',
            'mixamorig:LeftHandIndex1': 'L_Index1',
            'mixamorig:LeftHandIndex2': 'L_Index2',
            'mixamorig:LeftHandIndex3': 'L_Index3',
            'mixamorig:LeftHandMiddle1': 'L_Middle1',
            'mixamorig:LeftHandMiddle2': 'L_Middle2',
            'mixamorig:LeftHandMiddle3': 'L_Middle3',
            'mixamorig:LeftHandRing1': 'L_Ring2',
            'mixamorig:LeftHandRing2': 'L_Ring3',
            'mixamorig:LeftHandRing3': 'L_Ring4',
            'mixamorig:LeftHandPinky1': 'L_Pinky2',
            'mixamorig:LeftHandPinky2': 'L_Pinky3',
            'mixamorig:LeftHandPinky3': 'L_Pinky4',
            'mixamorig:LeftShoulder': 'L_Shoulder',
            'mixamorig:LeftArm': 'L_UpperArm',
            'mixamorig:LeftHand': 'L_Hand',
            'mixamorig:RightShoulder': 'R_Shoulder',
            'mixamorig:RightForeArm': 'R_ForeArm',
            'mixamorig:RightHandThumb1': 'R_Thumb1',
            'mixamorig:RightHandThumb2': 'R_Thumb2',
            'mixamorig:RightHandThumb3': 'R_Thumb3',
            'mixamorig:RightHandIndex1': 'R_Index1',
            'mixamorig:RightHandIndex2': 'R_Index2',
            'mixamorig:RightHandIndex3': 'R_Index3',
            'mixamorig:RightHandMiddle1': 'R_Middle1',
            'mixamorig:RightHandMiddle2': 'R_Middle2',
            'mixamorig:RightHandMiddle3': 'R_Middle3',
            'mixamorig:RightHandRing1': 'R_Ring2',
            'mixamorig:RightHandRing2': 'R_Ring3',
            'mixamorig:RightHandRing3': 'R_Ring4',
            'mixamorig:RightHandPinky1': 'R_Pinky2',
            'mixamorig:RightHandPinky2': 'R_Pinky3',
            'mixamorig:RightHandPinky3': 'R_Pinky4',
            'mixamorig:RightArm': 'R_UpperArm',
            'mixamorig:RightHand': 'R_Hand',
            'mixamorig:Neck': 'C_Neck1',
            'mixamorig:Head': 'C_Head',
            'mixamorig:LeftFoot': 'L_Foot',
            'mixamorig:LeftLeg': 'L_Knee',
            'mixamorig:LeftUpLeg': 'L_Thigh',
            'mixamorig:LeftToeBase': 'L_Toe',
            'mixamorig:RightFoot': 'R_Foot',
            'mixamorig:RightLeg': 'R_Knee',
            'mixamorig:RightUpLeg': 'R_Thigh',
            'mixamorig:RightToeBase': 'R_Toe',
            'mixamorig:Hips': 'C_Hip',
            'mixamorig:Spine': 'C_Spine1',
            'mixamorig:Spine1': 'C_Spine2',
            'mixamorig:Spine2': 'C_Chest',

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