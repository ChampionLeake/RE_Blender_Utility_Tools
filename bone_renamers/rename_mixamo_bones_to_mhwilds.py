import bpy

class OBJECT_OT_rename_mixamo_bones_to_mhwilds(bpy.types.Operator):
    bl_idname = "object.rename_mixamo_bones_to_mhwilds"
    bl_label = "Rename Bones (Mixamo to MH Wilds)"
    bl_description = "Renames commonly used Mixamo bones to MH Wilds's naming conventions"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Correct dictionary definition
        bone_rename_dict = {
            'mixamorig:LeftForeArm': 'L_Forearm',
            'mixamorig:LeftHandThumb1': 'L_Thumb1',
            'mixamorig:LeftHandThumb2': 'L_Thumb2',
            'mixamorig:LeftHandThumb3': 'L_Thumb3',
            'mixamorig:LeftHandIndex1': 'L_IndexF1',
            'mixamorig:LeftHandIndex2': 'L_IndexF2',
            'mixamorig:LeftHandIndex3': 'L_IndexF3',
            'mixamorig:LeftHandMiddle1': 'L_MiddleF1',
            'mixamorig:LeftHandMiddle2': 'L_MiddleF2',
            'mixamorig:LeftHandMiddle3': 'L_MiddleF3',
            'mixamorig:LeftHandRing1': 'L_RingF1',
            'mixamorig:LeftHandRing2': 'L_RingF2',
            'mixamorig:LeftHandRing3': 'L_RingF3',
            'mixamorig:LeftHandPinky1': 'L_PinkyF1',
            'mixamorig:LeftHandPinky2': 'L_PinkyF2',
            'mixamorig:LeftHandPinky3': 'L_PinkyF3',
            'mixamorig:LeftShoulder': 'L_Shoulder',
            'mixamorig:LeftArm': 'L_UpperArm',
            'mixamorig:LeftHand': 'L_Hand',
            'mixamorig:RightShoulder': 'R_Shoulder',
            'mixamorig:RightForeArm': 'R_Forearm',
            'mixamorig:RightHandThumb1': 'R_Thumb1',
            'mixamorig:RightHandThumb2': 'R_Thumb2',
            'mixamorig:RightHandThumb3': 'R_Thumb3',
            'mixamorig:RightHandIndex1': 'R_IndexF1',
            'mixamorig:RightHandIndex2': 'R_IndexF2',
            'mixamorig:RightHandIndex3': 'R_IndexF3',
            'mixamorig:RightHandMiddle1': 'R_MiddleF1',
            'mixamorig:RightHandMiddle2': 'R_MiddleF2',
            'mixamorig:RightHandMiddle3': 'R_MiddleF3',
            'mixamorig:RightHandRing1': 'R_RingF1',
            'mixamorig:RightHandRing2': 'R_RingF2',
            'mixamorig:RightHandRing3': 'R_RingF3',
            'mixamorig:RightHandPinky1': 'R_PinkyF1',
            'mixamorig:RightHandPinky2': 'R_PinkyF2',
            'mixamorig:RightHandPinky3': 'R_PinkyF3',
            'mixamorig:RightArm': 'R_UpperArm',
            'mixamorig:RightHand': 'R_Hand',
            'mixamorig:Neck': 'Neck_0',
            'mixamorig:Head': 'Head',
            'mixamorig:LeftFoot': 'L_Foot',
            'mixamorig:LeftLeg': 'L_Shin',
            'mixamorig:LeftUpLeg': 'L_Thigh',
            'mixamorig:LeftToeBase': 'L_Toe',
            'mixamorig:RightFoot': 'R_Foot',
            'mixamorig:RightLeg': 'R_Shin',
            'mixamorig:RightUpLeg': 'R_Thigh',
            'mixamorig:RightToeBase': 'R_Toe',
            'mixamorig:Hips': 'Hip',
            'mixamorig:Spine': 'Spine_0',
            'mixamorig:Spine1': 'Spine_1',
            'mixamorig:Spine2': 'Spine_2',

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