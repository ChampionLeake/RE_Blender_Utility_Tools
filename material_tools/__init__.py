import bpy

from .set_blend_opaque import OBJECT_OT_set_blend_opaque
from .set_blend_alpha import OBJECT_OT_set_blend_alpha
from .set_blend_clip import OBJECT_OT_set_blend_clip
from .set_blend_hashed import OBJECT_OT_set_blend_hashed

classes = [
    OBJECT_OT_set_blend_opaque,
    OBJECT_OT_set_blend_alpha,
    OBJECT_OT_set_blend_clip,
    OBJECT_OT_set_blend_hashed,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)