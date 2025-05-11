import bpy

class SetMaterialBlendBase(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}

    blend_mode = 'BLEND'  # Override this in subclasses

    def execute(self, context):
        selected_objects = [obj for obj in context.selected_objects if obj.type == 'MESH']
        if not selected_objects:
            self.report({'ERROR'}, "No mesh objects selected.")
            return {'CANCELLED'}

        for obj in selected_objects:
            for slot in obj.material_slots:
                mat = slot.material
                if mat:
                    mat.blend_method = self.blend_mode

        self.report({'INFO'}, f"Set materials on {len(selected_objects)} object(s) to {self.blend_mode}.")
        return {'FINISHED'}

class OBJECT_OT_set_blend_alpha(SetMaterialBlendBase):
    bl_idname = "object.set_blend_alpha"
    bl_label = "Set Alpha Blend"
    blend_mode = 'BLEND'