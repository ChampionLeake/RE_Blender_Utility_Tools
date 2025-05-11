import bpy

def register():
    bpy.types.Scene.show_mmd_renamer_tools = bpy.props.BoolProperty(
        name="MMD to RE Engine",
        description="Show or hide the MMD to RE renamer tools",
        default=False
    )
    bpy.types.Scene.show_xps_renamer_tools = bpy.props.BoolProperty(
        name="XPS to RE Engine",
        description="Show or hide the XPS to RE renamer tools",
        default=False
    )
    bpy.types.Scene.show_mixamo_renamer_tools = bpy.props.BoolProperty(
        name="Mixamo to RE Engine",
        description="Show or hide the Mixamo to RE renamer tools",
        default=False
    )

def unregister():
    del bpy.types.Scene.show_mmd_renamer_tools
    del bpy.types.Scene.show_xps_renamer_tools
    del bpy.types.Scene.show_mixamo_renamer_tools