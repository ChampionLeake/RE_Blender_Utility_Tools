import bpy

from .apply_rest_pose import OBJECT_OT_apply_rest_pose

classes = [
    OBJECT_OT_apply_rest_pose,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)