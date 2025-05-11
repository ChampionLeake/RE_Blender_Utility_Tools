import bpy
from bpy.props import BoolProperty

class OBJECT_OT_organize_re2r_bones(bpy.types.Operator):
    bl_idname = "object.organize_re2r_bones"
    bl_label = "Organize RE2R Bones"
    bl_description = "Organizes RE2R armature bones based on Blender version (Layers for 3.x, Collections for 4.x)"
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
            "head", "neck_1", "neck_0", "spine_2", "spine_1", "spine_0", "hips",
            "l_leg_femur", "l_leg_tibia", "l_leg_ankle", "l_leg_ball",
            "l_arm_clavicle", "l_arm_humerus", "l_arm_radius", "l_arm_wrist",
            "r_leg_femur", "r_leg_tibia", "r_leg_ankle", "r_leg_ball",
            "r_arm_clavicle", "r_arm_humerus", "r_arm_radius", "r_arm_wrist"
        ]

        finger_bones = [
            "l_hand_thumb_0", "l_hand_thumb_1", "l_hand_thumb_2",
            "l_hand_index_0", "l_hand_index_1", "l_hand_index_2",
            "l_hand_middle_0", "l_hand_middle_1", "l_hand_middle_2",
            "l_hand_ring_1", "l_hand_ring_2", "l_hand_ring_3",
            "l_hand_little_1", "l_hand_little_2", "l_hand_little_3",
            "r_hand_thumb_0", "r_hand_thumb_1", "r_hand_thumb_2",
            "r_hand_index_0", "r_hand_index_1", "r_hand_index_2",
            "r_hand_middle_0", "r_hand_middle_1", "r_hand_middle_2",
            "r_hand_ring_1", "r_hand_ring_2", "r_hand_ring_3",
            "r_hand_little_1", "r_hand_little_2", "r_hand_little_3"
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

        self.report({'INFO'}, "RE2R Bones organized successfully!")
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