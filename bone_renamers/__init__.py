import bpy

from .rename_xnalara_bones_to_re2r import OBJECT_OT_rename_xnalara_bones_to_re2r
from .rename_xnalara_bones_to_re3r import OBJECT_OT_rename_xnalara_bones_to_re3r
from .rename_xnalara_bones_to_re4r import OBJECT_OT_rename_xnalara_bones_to_re4r
from .rename_mmd_bones_to_re2r import OBJECT_OT_rename_mmd_bones_to_re2r
from .rename_mmd_bones_to_re3r import OBJECT_OT_rename_mmd_bones_to_re3r
from .rename_mmd_bones_to_re4r import OBJECT_OT_rename_mmd_bones_to_re4r
from .rename_mixamo_bones_to_re2r import OBJECT_OT_rename_mixamo_bones_to_re2r
from .rename_mixamo_bones_to_re3r import OBJECT_OT_rename_mixamo_bones_to_re3r
from .rename_mixamo_bones_to_re4r import OBJECT_OT_rename_mixamo_bones_to_re4r

classes = [
    OBJECT_OT_rename_xnalara_bones_to_re2r,
    OBJECT_OT_rename_xnalara_bones_to_re3r,
    OBJECT_OT_rename_xnalara_bones_to_re4r,
    OBJECT_OT_rename_mmd_bones_to_re2r,
    OBJECT_OT_rename_mmd_bones_to_re3r,
    OBJECT_OT_rename_mmd_bones_to_re4r,
    OBJECT_OT_rename_mixamo_bones_to_re2r,
    OBJECT_OT_rename_mixamo_bones_to_re3r,
    OBJECT_OT_rename_mixamo_bones_to_re4r,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)