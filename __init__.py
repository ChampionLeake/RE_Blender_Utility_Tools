bl_info = {
    "name": "RE_Blender_Utility_Tools",
    "author": "LeakeGG",
    "version": (0, 1, 7),
    "blender": (4, 0, 0),
    "location": "View3D > Tool Shelf > RE Engine Utility Tool",
    "description": "Tools to simply your RE Engine modding workflow",
    "category": "Development",
}

import bpy
from . import properties
from . import addon_updater_ops
# from .bone_organizers import *
from .bone_renamers import *
from .material_tools import *
from .skeleton_tools import *

# === Update Preferences ===
class UpdaterPreferences(bpy.types.AddonPreferences):
    """Updater Class."""

    bl_idname = __package__

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
        max=23
    )
    updater_interval_minutes: bpy.props.IntProperty(
        name='Minutes',
        description="Number of minutes between checking for updates",
        default=0,
        min=0,
        max=59
    )


# === Organizer Dropdown ===
class OBJECT_OT_organize_re_bones(bpy.types.Operator):
    bl_idname = "object.organize_re_bones"
    bl_label = "Organize Bones"
    bl_description = "Organizes bones for the selected RE Engine game"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        game = scene.re_engine_game

        if game == 're2r':
            bpy.ops.object.organize_re2r_bones('INVOKE_DEFAULT')
        elif game == 're3r':
            bpy.ops.object.organize_re3r_bones('INVOKE_DEFAULT')
        elif game == 're4r':
            bpy.ops.object.organize_re4r_bones('INVOKE_DEFAULT')
        elif game == 're7':
            bpy.ops.object.organize_re7_bones('INVOKE_DEFAULT')
        elif game == 're8':
            bpy.ops.object.organize_re8_bones('INVOKE_DEFAULT')
        elif game == 'sf6':
            bpy.ops.object.organize_sf6_bones('INVOKE_DEFAULT')
        elif game == 'dmc5':
            bpy.ops.object.organize_dmc5_bones('INVOKE_DEFAULT')
        elif game == 'mhwilds':    
            bpy.ops.object.organize_mhwilds_bones('INVOKE_DEFAULT')
        elif game == 'drdr':    
            bpy.ops.object.organize_drdr_bones('INVOKE_DEFAULT')
        else:
            self.report({'ERROR'}, f"Unsupported game selected: {game}")
            return {'CANCELLED'}
        return {'FINISHED'}


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

        row = box.row()
        row.prop(scene, "re_engine_game", text="Target Game")
        box.operator("object.organize_re_bones", text="Organize Bones")

        box2 = layout.box()
        box2.label(text="Bone Renamer Tools", icon='BONE_DATA')

        row = box2.row(align=True)
        row.prop(scene, "show_xps_renamer_tools", text="",
                 icon="TRIA_DOWN" if scene.show_xps_renamer_tools else "TRIA_RIGHT", emboss=False)
        row.label(text="XPS --> RE Engine")
        if scene.show_xps_renamer_tools:
            box2.operator("object.rename_xnalara_bones_to_re2r", text="XPS to RE2R")
            box2.operator("object.rename_xnalara_bones_to_re3r", text="XPS to RE3R")
            box2.operator("object.rename_xnalara_bones_to_re4r", text="XPS to RE4R")
            box2.operator("object.rename_xnalara_bones_to_re7", text="XPS to RE7")
            box2.operator("object.rename_xnalara_bones_to_re8", text="XPS to RE8")
            box2.operator("object.rename_xnalara_bones_to_sf6", text="XPS to SF6")
            box2.operator("object.rename_xnalara_bones_to_dmc5", text="XPS to DMC5")
            box2.operator("object.rename_xnalara_bones_to_mhwilds", text="XPS to MHWilds")
            box2.operator("object.rename_xnalara_bones_to_drdr", text="XPS to DRDR")

        row = box2.row(align=True)
        row.prop(scene, "show_mmd_renamer_tools", text="",
                 icon="TRIA_DOWN" if scene.show_mmd_renamer_tools else "TRIA_RIGHT", emboss=False)
        row.label(text="MMD --> RE Engine")
        if scene.show_mmd_renamer_tools:
            box2.operator("object.rename_mmd_bones_to_re2r", text="MMD to RE2R")
            box2.operator("object.rename_mmd_bones_to_re3r", text="MMD to RE3R")
            box2.operator("object.rename_mmd_bones_to_re4r", text="MMD to RE4R")
            box2.operator("object.rename_mmd_bones_to_re7", text="MMD to RE7")
            box2.operator("object.rename_mmd_bones_to_re8", text="MMD to RE8")
            box2.operator("object.rename_mmd_bones_to_sf6", text="MMD to SF6")
            box2.operator("object.rename_mmd_bones_to_dmc5", text="MMD to DMC5")
            box2.operator("object.rename_mmd_bones_to_mhwilds", text="MMD to MHWilds")
            box2.operator("object.rename_mmd_bones_to_drdr", text="MMD to DRDR")

        row = box2.row(align=True)
        row.prop(scene, "show_mixamo_renamer_tools", text="",
                 icon="TRIA_DOWN" if scene.show_mixamo_renamer_tools else "TRIA_RIGHT", emboss=False)
        row.label(text="Mixamo --> RE Engine")
        if scene.show_mixamo_renamer_tools:
            box2.operator("object.rename_mixamo_bones_to_re2r", text="Mixamo to RE2R")
            box2.operator("object.rename_mixamo_bones_to_re3r", text="Mixamo to RE3R")
            box2.operator("object.rename_mixamo_bones_to_re4r", text="Mixamo to RE4R")
            box2.operator("object.rename_mixamo_bones_to_re7", text="Mixamo to RE7")
            box2.operator("object.rename_mixamo_bones_to_re8", text="Mixamo to RE8")
            box2.operator("object.rename_mixamo_bones_to_sf6", text="Mixamo to SF6")
            box2.operator("object.rename_mixamo_bones_to_dmc5", text="Mixamo to DMC5")
            box2.operator("object.rename_mixamo_bones_to_mhwilds", text="Mixamo to MHWilds")
            box2.operator("object.rename_mixamo_bones_to_drdr", text="Mixamo to DRDR")

        col = layout.column(align=True)
        col.label(text="Set Material Blend Mode:")
        col.operator("object.set_blend_opaque", icon='SHADING_SOLID')
        col.operator("object.set_blend_alpha", icon='SHADING_TEXTURE')
        col.operator("object.set_blend_clip", icon='SHADING_BBOX')
        col.operator("object.set_blend_hashed", icon='SHADING_RENDERED')

        layout.label(text="Skeleton Tools:")
        layout.operator("object.apply_rest_pose", icon='ARMATURE_DATA')
        layout.label(text="Updating the Add-On:")
        addon_updater_ops.update_settings_ui(self, context)


def re_engine_game_items(self, context):
    """Items for the game selection dropdown."""
    items = [
        ('re2r', "Resident Evil 2 Remake", "Organize bones for Resident Evil 2 Remake"),
        ('re3r', "Resident Evil 3 Remake", "Organize bones for Resident Evil 3 Remake"),
        ('re4r', "Resident Evil 4 Remake", "Organize bones for Resident Evil 4 Remake"),
        ('re7', "Resident Evil 7", "Organize bones for Resident Evil 7"),
        ('re8', "Resident Evil Village", "Organize bones for Resident Evil Village"),
        ('sf6', "Street Fighter 6", "Organize bones for Street Fighter 6"),
        ('dmc5', "Devil May Cry 5", "Organize bones for Devil May Cry 5"),
        ('mhwilds', "Monster Hunter Wilds", "Organize bones for Monster Hunter Wilds"),
        ('drdr', "Dead Rising Deluxe Remaster", "Organize bones for Dead Rising Deluxe Remaster"),
    ]
    return items


classes = [
    UpdaterPreferences,
    VIEW3D_PT_re_engine_panel,
    OBJECT_OT_organize_re_bones,
]


def register():
    addon_updater_ops.register(bl_info)
    for cls in classes:
        bpy.utils.register_class(cls)
    properties.register()
    from . import bone_organizers
    bone_organizers.register()
    bone_renamers.register()
    material_tools.register()
    skeleton_tools.register()
    bpy.types.Scene.re_engine_game = bpy.props.EnumProperty(items=re_engine_game_items)


def unregister():
    addon_updater_ops.unregister()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    properties.unregister()
    from . import bone_organizers
    bone_organizers.unregister()
    bone_renamers.unregister()
    material_tools.unregister()
    skeleton_tools.unregister()
    del bpy.types.Scene.re_engine_game


if __name__ == "__main__":
    register()