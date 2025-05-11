import bpy

class OBJECT_OT_rename_mixamo_bones_to_re3r(bpy.types.Operator):
    bl_idname = "object.rename_mixamo_bones_to_re3r"
    bl_label = "Rename Bones (Mixamo to RE3R)"
    bl_description = "Renames commonly used Mixamo bones to RE3R's naming conventions"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Correct dictionary definition
        bone_rename_dict = {
            'mixamorig:LeftForeArm': 'l arm radius',
            'mixamorig:LeftHandThumb1': 'l hand thumb 0',
            'mixamorig:LeftHandThumb2': 'l hand thumb 1',
            'mixamorig:LeftHandThumb3': 'l hand thumb 2',
            'mixamorig:LeftHandIndex1': 'l hand index 0',
            'mixamorig:LeftHandIndex2': 'l hand index 1',
            'mixamorig:LeftHandIndex3': 'l hand index 2',
            'mixamorig:LeftHandMiddle1': 'l hand middle 0',
            'mixamorig:LeftHandMiddle2': 'l hand middle 1',
            'mixamorig:LeftHandMiddle3': 'l hand middle 2',
            'mixamorig:LeftHandRing1': 'l hand ring 1',
            'mixamorig:LeftHandRing2': 'l hand ring 2',
            'mixamorig:LeftHandRing3': 'l hand ring 3',
            'mixamorig:LeftHandPinky1': 'l hand little 1',
            'mixamorig:LeftHandPinky2': 'l hand little 2',
            'mixamorig:LeftHandPinky3': 'l hand little 3',
            'mixamorig:LeftShoulder': 'l arm clavicle',
            'mixamorig:LeftArm': 'l arm humerus',
            'mixamorig:LeftHand': 'l arm wrist',
            'mixamorig:RightShoulder': 'r arm clavicle',
            'mixamorig:RightForeArm': 'r arm radius',
            'mixamorig:RightHandThumb1': 'r hand thumb 0',
            'mixamorig:RightHandThumb2': 'r hand thumb 1',
            'mixamorig:RightHandThumb3': 'r hand thumb 2',
            'mixamorig:RightHandIndex1': 'r hand index 0',
            'mixamorig:RightHandIndex2': 'r hand index 1',
            'mixamorig:RightHandIndex3': 'r hand index 2',
            'mixamorig:RightHandMiddle1': 'r hand middle 0',
            'mixamorig:RightHandMiddle2': 'r hand middle 1',
            'mixamorig:RightHandMiddle3': 'r hand middle 2',
            'mixamorig:RightHandRing1': 'r hand ring 1',
            'mixamorig:RightHandRing2': 'r hand ring 2',
            'mixamorig:RightHandRing3': 'r hand ring 3',
            'mixamorig:RightHandPinky1': 'r hand little 1',
            'mixamorig:RightHandPinky2': 'r hand little 2',
            'mixamorig:RightHandPinky3': 'r hand little 3',
            'mixamorig:RightArm': 'r arm humerus',
            'mixamorig:RightHand': 'r arm wrist',
            'mixamorig:Neck': 'neck 0',
            'mixamorig:Head': 'head',
            'mixamorig:LeftFoot': 'l leg ankle',
            'mixamorig:LeftLeg': 'l leg tibia',
            'mixamorig:LeftUpLeg': 'l leg femur',
            'mixamorig:LeftToeBase': 'l leg ball',
            'mixamorig:RightFoot': 'r leg ankle',
            'mixamorig:RightLeg': 'r leg tibia',
            'mixamorig:RightUpLeg': 'r leg femur',
            'mixamorig:RightToeBase': 'r leg ball',
            'mixamorig:Hips': 'hips',
            'mixamorig:Spine': 'spine 0',
            'mixamorig:Spine1': 'spine 1',
            'mixamorig:Spine2': 'spine 2',

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