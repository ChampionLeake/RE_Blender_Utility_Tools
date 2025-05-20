import bpy
from bpy.props import BoolProperty

class OBJECT_OT_organize_drdr_bones(bpy.types.Operator):
    bl_idname = "object.organize_drdr_bones"
    bl_label = "Organize DRDR Bones"
    bl_description = "Organizes DRDR armature bones based on Blender version (Layers for 3.x, Collections for 4.x)"
    bl_options = {'REGISTER', 'UNDO'}

    delete_existing: BoolProperty(
        name="Delete Existing Organization",
        description="Reset bone layers (3.x) or delete existing bone collections (4.x) before organizing?",
        default=False
    )

    def execute(self, context):
        obj = context.object
        if obj is None or obj.type != 'ARMATURE':
            self.report({'ERROR'}, "Please select an armature object.")
            return {'CANCELLED'}

        arm = obj.data
        bones = arm.bones
        blender_version = bpy.app.version

        primary_bones = [
            "C_Head", "C_Neck", "C_Spine_02", "C_Spine_01", "C_Spine_00", "COG",
            "L_UpperLeg", "L_Foreleg", "L_Foot", "L_Toe",
            "L_Shoulder", "L_UpperArm", "L_Forearm", "L_Hand",
            "R_UpperLeg", "R_Foreleg", "R_Foot", "R_Toe",
            "R_Shoulder", "R_UpperArm", "R_Forearm", "R_Hand"
        ]

        finger_bones = [
            "L_Thumb_01", "L_Thumb_02", "L_Thumb_03",
            "L_Index_01", "L_Index_02", "L_Index_03",
            "L_Middle_01", "L_Middle_02", "L_Middle_03",
            "L_Ring_01", "L_Ring_02", "L_Ring_03",
            "L_Pinky_01", "L_Pinky_02", "L_Pinky_03",
            "R_Thumb_01", "R_Thumb_02", "R_Thumb_03",
            "R_Index_01", "R_Index_02", "R_Index_03",
            "R_Middle_01", "R_Middle_02", "R_Middle_03",
            "R_Ring_01", "R_Ring_02", "R_Ring_03",
            "R_Pinky_01", "R_Pinky_02", "R_Pinky_03"
        ]

        if blender_version[0] == 4:  # Blender 4.x - Use Collections
            # Remove existing collections if requested
            if self.delete_existing:
                for coll in list(arm.collections):
                    arm.collections.remove(coll)

            # Create new collections
            primary_coll = arm.collections.new(name="Primary")
            fingers_coll = arm.collections.new(name="Fingers")

            for bone_name in primary_bones:
                if bone_name in bones:
                    primary_coll.assign(bones[bone_name])
            for bone_name in finger_bones:
                if bone_name in bones:
                    fingers_coll.assign(bones[bone_name])

            # Hide both "Primary" and "Fingers" collections
            primary_coll.is_visible = False
            fingers_coll.is_visible = False

            # Create and assign new "Main Body" collection
            main_coll = arm.collections.new(name="Main Body")
            for bone in bones:
                main_coll.assign(bone)

        elif blender_version[0] == 3:  # Blender 3.x - Use Layers
            def set_bone_layer(bone_name, layer):
                if bone_name in bones:
                    for i in range(32):
                        bones[bone_name].layers[i] = False
                    bones[bone_name].layers[layer] = True

            if self.delete_existing:
                for bone in bones:
                    for i in range(32):
                        bone.layers[i] = (i == 0)  # Reset to layer 1

            for bone_name in primary_bones:
                set_bone_layer(bone_name, 16)
            for bone_name in finger_bones:
                set_bone_layer(bone_name, 17)

        else:
            self.report({'WARNING'}, "Blender version not fully supported. Using layers.")
            # Fallback to layers logic (Blender 3.x logic here)
            # --- (Layers logic from above, inside the 'else' block) ---
            def set_bone_layer(bone_name, layer):
                if bone_name in bones:
                    for i in range(32):
                        bones[bone_name].layers[i] = False
                    bones[bone_name].layers[layer] = True

            if self.delete_existing:
                for bone in bones:
                    for i in range(32):
                        bone.layers[i] = (i == 0)  # Reset to layer 1

            for bone_name in primary_bones:
                set_bone_layer(bone_name, 16)
            for bone_name in finger_bones:
                set_bone_layer(bone_name, 17)

        bpy.ops.object.mode_set(mode='POSE')
        bpy.ops.pose.select_all(action='SELECT')

        self.report({'INFO'}, "RE4R Bones organized successfully!")
        return {'FINISHED'}

    def invoke(self, context, event):
        arm = context.object.data
        if bpy.app.version[0] == 4 and len(arm.collections) > 0:
            return context.window_manager.invoke_props_dialog(self)
        elif bpy.app.version[0] == 3 and any(not bone.layers[0] for bone in arm.bones):
            return context.window_manager.invoke_props_dialog(self)
        else:
            return self.execute(context)

    def draw(self, context):
        layout = self.layout
        if bpy.app.version[0] == 4:
            layout.label(text="Existing bone collections detected.")
        elif bpy.app.version[0] == 3:
            layout.label(text="Some bones are not on the first layer.")
        layout.prop(self, "delete_existing")