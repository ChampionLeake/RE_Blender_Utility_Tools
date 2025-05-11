bl_info = {
    "name": "RE_Blender_Utility_Tools",
    "author": "LeakeGG",
    "version": (0, 1, 0),
    "blender": (3, 6, 5),
    "location": "View3D > Tool Shelf > RE Engine Utility Tool",
    "description": "Tools to simply your RE Engine modding workflow",
    "category": "Development",
}

import bpy
from . import properties
from . import addon_updater_ops
from .bone_organizers import *
from .bone_renamers import *
from .material_tools import *
from .skeleton_tools import *

class UpdaterPreferences(bpy.types.AddonPreferences):
    """Updater Class."""

    bl_idname = __package__

    # addon updater preferences from `__init__`, be sure to copy all of them
    auto_check_update: bpy.props.BoolProperty(
        name="Auto-check for Update",
        description="If enabled, auto-check for updates using an interval",
        default=False,
    )
    updater_interval_months: bpy.props.IntProperty(
        name='Months',
        description="Number of months between checking for updates",
        default=0,
        min=0
    )
    updater_interval_days: bpy.props.IntProperty(
        name='Days',
        description="Number of days between checking for updates",
        default=7,
        min=0,
    )
    updater_interval_hours: bpy.props.IntProperty(
        name='Hours',
        description="Number of hours between checking for updates",
        default=0,
        min=0,
        max=23
    )
    updater_interval_minutes: bpy.props.IntProperty(
        name='Minutes',
        description="Number of minutes between checking for updates",
        default=0,
        min=0,
        max=59
    )

# === UI Panel ===
class VIEW3D_PT_re_engine_panel(bpy.types.Panel):    
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "RE Engine Utility Panel"
    bl_label = "RE Engine Utility Panel"    
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        box = layout.box()
        box.label(text="Bone Layer Tools", icon='ARMATURE_DATA')
        box.operator("object.organize_re2r_bones", text="Organize RE2R Bones")
        box.operator("object.organize_re3r_bones", text="Organize RE3R Bones")
        box.operator("object.organize_re4r_bones", text="Organize RE4R Bones")

        box2 = layout.box()
        box2.label(text="Bone Renamer Tools", icon='BONE_DATA')

        row = box2.row(align=True)
        row.prop(scene, "show_xps_renamer_tools", text="", icon="TRIA_DOWN" if scene.show_xps_renamer_tools else "TRIA_RIGHT", emboss=False)
        row.label(text="XPS --> RE Engine")
        if scene.show_xps_renamer_tools:
            box2.operator("object.rename_xnalara_bones_to_re2r", text="XPS to RE2R")
            box2.operator("object.rename_xnalara_bones_to_re3r", text="XPS to RE3R")
            box2.operator("object.rename_xnalara_bones_to_re4r", text="XPS to RE4R")

        row = box2.row(align=True)
        row.prop(scene, "show_mmd_renamer_tools", text="", icon="TRIA_DOWN" if scene.show_mmd_renamer_tools else "TRIA_RIGHT", emboss=False)
        row.label(text="MMD --> RE Engine")
        if scene.show_mmd_renamer_tools:
            box2.operator("object.rename_mmd_bones_to_re2r", text="MMD to RE2R")
            box2.operator("object.rename_mmd_bones_to_re3r", text="MMD to RE3R")
            box2.operator("object.rename_mmd_bones_to_re4r", text="MMD to RE4R")
            
        row = box2.row(align=True)
        row.prop(scene, "show_mixamo_renamer_tools", text="", icon="TRIA_DOWN" if scene.show_mixamo_renamer_tools else "TRIA_RIGHT", emboss=False)
        row.label(text="Mixamo --> RE Engine")
        if scene.show_mixamo_renamer_tools:
            box2.operator("object.rename_mixamo_bones_to_re2r", text="Mixamo to RE2R")
            box2.operator("object.rename_mixamo_bones_to_re3r", text="Mixamo to RE3R")
            box2.operator("object.rename_mixamo_bones_to_re4r", text="Mixamo to RE4R")           
            
        col = layout.column(align=True)
        col.label(text="Set Material Blend Mode:")
        col.operator("object.set_blend_opaque", icon='SHADING_SOLID')
        col.operator("object.set_blend_alpha", icon='SHADING_TEXTURE')
        col.operator("object.set_blend_clip", icon='SHADING_BBOX')
        col.operator("object.set_blend_hashed", icon='SHADING_RENDERED')
        
        layout.label(text="Skeleton Tools:")
        layout.operator("object.apply_rest_pose", icon='ARMATURE_DATA')
        
        layout.label(text="Updating the Add-On:")
        addon_updater_ops.update_settings_ui(self,context)

classes = [
    UpdaterPreferences,
    VIEW3D_PT_re_engine_panel,
]

def register():
    addon_updater_ops.register(bl_info)
    for cls in classes:
        bpy.utils.register_class(cls)
    properties.register()
    bone_organizers.register()
    bone_renamers.register()
    material_tools.register()
    skeleton_tools.register()

def unregister():
    addon_updater_ops.unregister()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    properties.unregister()
    bone_organizers.unregister()
    bone_renamers.unregister()
    material_tools.unregister()
    skeleton_tools.unregister()

if __name__ == "__main__":
    register()