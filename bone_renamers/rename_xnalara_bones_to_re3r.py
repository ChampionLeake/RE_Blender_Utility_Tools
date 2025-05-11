import bpy

class OBJECT_OT_rename_xnalara_bones_to_re3r(bpy.types.Operator):
    bl_idname = "object.rename_xnalara_bones_to_re3r"
    bl_label = "Rename Bones (Xnalara to RE3R)"
    bl_description = "Renames commonly used Xnalara bones to RE3R's naming conventions"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Correct dictionary definition
        bone_rename_dict = {
            'arm left elbow': 'l arm radius',
            'arm left finger 1a': 'l hand thumb 0',
            'arm left finger 1b': 'l hand thumb 1',
            'arm left finger 1c': 'l hand thumb 2',
            'arm left finger 2a': 'l hand index 0',
            'arm left finger 2b': 'l hand index 1',
            'arm left finger 2c': 'l hand index 2',
            'arm left finger 3a': 'l hand middle 0',
            'arm left finger 3b': 'l hand middle 1',
            'arm left finger 3c': 'l hand middle 2',
            'arm left finger 4a': 'l hand ring 1',
            'arm left finger 4b': 'l hand ring 2',
            'arm left finger 4c': 'l hand ring 3',
            'arm left finger 5a': 'l hand little 1',
            'arm left finger 5b': 'l hand little 2',
            'arm left finger 5c': 'l hand little 3',
            'arm left shoulder 1': 'l arm clavicle',
            'arm left shoulder 2': 'l arm humerus',
            'arm left shoulder ctrl 1': 'l arm humerus',
            'arm left shoulder ctrl 2': 'l arm humerus',
            'arm left wrist': 'l arm wrist',
            'arm left wrist ctrl 1': 'l arm wrist',
            'arm left wrist ctrl 2': 'l arm wrist',
            'arm right elbow': 'r arm radius',
            'arm right elbow ctrl': 'r arm radius',
            'arm right finger 1a': 'r hand thumb 0',
            'arm right finger 1b': 'r hand thumb 1',
            'arm right finger 1c': 'r hand thumb 2',
            'arm right finger 2a': 'r hand index 0',
            'arm right finger 2b': 'r hand index 1',
            'arm right finger 2c': 'r hand index 2',
            'arm right finger 3a': 'r hand middle 0',
            'arm right finger 3b': 'r hand middle 1',
            'arm right finger 3c': 'r hand middle 2',
            'arm right finger 4a': 'r hand ring 1',
            'arm right finger 4b': 'r hand ring 2',
            'arm right finger 4c': 'r hand ring 3',
            'arm right finger 5a': 'r hand little 1',
            'arm right finger 5b': 'r hand little 2',
            'arm right finger 5c': 'r hand little 3',
            'arm right shoulder 1': 'r arm clavicle',
            'arm right shoulder 2': 'r arm humerus',
            'arm right shoulder ctrl 1': 'r arm clavicle',
            'arm right shoulder ctrl 2': 'r arm clavicle',
            'arm right wrist': 'r arm wrist',
            'arm right wrist ctrl 1': 'r arm wrist',
            'arm right wrist ctrl 2': 'r arm wrist',
            'head neck lower': 'neck 0',
            'head neck upper': 'head',
            'leg left ankle': 'l leg ankle',
            'leg left knee': 'l leg tibia',
            'leg left knee ctrl': 'l leg tibia',
            'leg left thigh': 'l leg femur',
            'leg left thigh ctrl 1': 'l leg femur',
            'leg left thigh ctrl 2': 'l leg femur',
            'leg left thigh ctrl 3': 'l leg femur',
            'leg left toes': 'l leg ball',
            'leg right ankle': 'r leg ankle',
            'leg right knee': 'r leg tibia',
            'leg right knee ctrl': 'r leg tibia',
            'leg right thigh': 'r leg femur',
            'leg right thigh ctrl 1': 'r leg femur',
            'leg right thigh ctrl 2': 'r leg femur',
            'leg right thigh ctrl 3': 'r leg femur',
            'leg right toes': 'r leg ball',
            'pelvis': 'hips',
            'spine lower': 'spine 0',
            'spine middle': 'spine 1',
            'spine upper': 'spine 2',
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