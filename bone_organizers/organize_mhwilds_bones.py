import bpy
from bpy.props import BoolProperty

class OBJECT_OT_organize_mhwilds_bones(bpy.types.Operator):
    bl_idname = "object.organize_mhwilds_bones"
    bl_label = "Organize MH Wilds Bones"
    bl_description = "Organizes MH Wilds armature bones based on Blender version (Layers for 3.x, Collections for 4.x)"
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
            "Head", "Neck_1", "Neck_0", "Spine_2", "Spine_1", "Spine_0", "Hip",
            "L_Thigh", "L_Shin", "L_Foot", "L_Toe",
            "L_Shoulder", "L_UpperArm", "L_Forearm", "L_Hand",
            "R_Thigh", "R_Shin", "R_Foot", "R_Toe",
            "R_Shoulder", "R_UpperArm", "R_Forearm", "R_Hand"
        ]

        finger_bones = [
            "L_Thumb1", "L_Thumb2", "L_Thumb3",
            "L_IndexF1", "L_IndexF2", "L_IndexF3",
            "L_MiddleF1", "L_MiddleF2", "L_MiddleF3",
            "L_RingF1", "L_RingF2", "L_RingF3",
            "L_PinkyF1", "L_PinkyF2", "L_PinkyF3",
            "R_Thumb1", "R_Thumb2", "R_Thumb3",
            "R_IndexF1", "R_IndexF2", "R_IndexF3",
            "R_MiddleF1", "R_MiddleF2", "R_MiddleF3",
            "R_RingF1", "R_RingF2", "R_RingF3",
            "R_PinkyF1", "R_PinkyF2", "R_PinkyF3"
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