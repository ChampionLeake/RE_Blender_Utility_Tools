import bpy

from .organize_re2r_bones import OBJECT_OT_organize_re2r_bones
from .organize_re3r_bones import OBJECT_OT_organize_re3r_bones
from .organize_re4r_bones import OBJECT_OT_organize_re4r_bones

classes = [
    OBJECT_OT_organize_re2r_bones,
    OBJECT_OT_organize_re3r_bones,
    OBJECT_OT_organize_re4r_bones,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()