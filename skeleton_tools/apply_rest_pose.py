import bpy

class OBJECT_OT_apply_rest_pose(bpy.types.Operator):
    bl_idname = "object.apply_rest_pose"
    bl_label = "Apply Current Rest Pose"
    bl_description = "Applies the rest pose of the active armature to the selected mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        mesh = context.object

        if mesh.type != 'MESH':
            self.report({'ERROR'}, "Active object must be a mesh.")
            return {'CANCELLED'}

        # Find the first Armature modifier
        arm_mod = None
        for mod in mesh.modifiers:
            if mod.type == 'ARMATURE':
                arm_mod = mod
                break

        if not arm_mod:
            self.report({'ERROR'}, "No Armature modifier found on the mesh.")
            return {'CANCELLED'}

        # Duplicate the modifier
        mod_copy = mesh.modifiers.new(name=arm_mod.name + "_COPY", type='ARMATURE')
        mod_copy.object = arm_mod.object

        # Apply the first armature modifier
        context.view_layer.objects.active = mesh
        bpy.ops.object.modifier_apply(modifier=arm_mod.name)

        # Switch to pose mode
        arm_obj = mod_copy.object
        context.view_layer.objects.active = arm_obj
        bpy.ops.object.mode_set(mode='POSE')

        # Select all bones
        bpy.ops.pose.select_all(action='SELECT')

        # Apply Pose as Rest Pose
        bpy.ops.pose.armature_apply(selected=True)

        # Return to object mode
        bpy.ops.object.mode_set(mode='OBJECT')

        self.report({'INFO'}, "Rest pose applied successfully.")
        return {'FINISHED'}