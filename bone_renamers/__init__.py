import bpy

from .rename_xnalara_bones_to_re2r import OBJECT_OT_rename_xnalara_bones_to_re2r
from .rename_xnalara_bones_to_re3r import OBJECT_OT_rename_xnalara_bones_to_re3r
from .rename_xnalara_bones_to_re4r import OBJECT_OT_rename_xnalara_bones_to_re4r
from .rename_xnalara_bones_to_re7 import OBJECT_OT_rename_xnalara_bones_to_re7
from .rename_xnalara_bones_to_re8 import OBJECT_OT_rename_xnalara_bones_to_re8
from .rename_xnalara_bones_to_sf6 import OBJECT_OT_rename_xnalara_bones_to_sf6
from .rename_xnalara_bones_to_dmc5 import OBJECT_OT_rename_xnalara_bones_to_dmc5
from .rename_xnalara_bones_to_mhwilds import OBJECT_OT_rename_xnalara_bones_to_mhwilds
from .rename_xnalara_bones_to_drdr import OBJECT_OT_rename_xnalara_bones_to_drdr
from .rename_mmd_bones_to_re2r import OBJECT_OT_rename_mmd_bones_to_re2r
from .rename_mmd_bones_to_re3r import OBJECT_OT_rename_mmd_bones_to_re3r
from .rename_mmd_bones_to_re4r import OBJECT_OT_rename_mmd_bones_to_re4r
from .rename_mmd_bones_to_re7 import OBJECT_OT_rename_mmd_bones_to_re7
from .rename_mmd_bones_to_re8 import OBJECT_OT_rename_mmd_bones_to_re8
from .rename_mmd_bones_to_sf6 import OBJECT_OT_rename_mmd_bones_to_sf6
from .rename_mmd_bones_to_dmc5 import OBJECT_OT_rename_mmd_bones_to_dmc5
from .rename_mmd_bones_to_mhwilds import OBJECT_OT_rename_mmd_bones_to_mhwilds
from .rename_mmd_bones_to_drdr import OBJECT_OT_rename_mmd_bones_to_drdr
from .rename_mixamo_bones_to_re2r import OBJECT_OT_rename_mixamo_bones_to_re2r
from .rename_mixamo_bones_to_re3r import OBJECT_OT_rename_mixamo_bones_to_re3r
from .rename_mixamo_bones_to_re4r import OBJECT_OT_rename_mixamo_bones_to_re4r
from .rename_mixamo_bones_to_re7 import OBJECT_OT_rename_mixamo_bones_to_re7
from .rename_mixamo_bones_to_re8 import OBJECT_OT_rename_mixamo_bones_to_re8
from .rename_mixamo_bones_to_sf6 import OBJECT_OT_rename_mixamo_bones_to_sf6
from .rename_mixamo_bones_to_dmc5 import OBJECT_OT_rename_mixamo_bones_to_dmc5
from .rename_mixamo_bones_to_mhwilds import OBJECT_OT_rename_mixamo_bones_to_mhwilds
from .rename_mixamo_bones_to_drdr import OBJECT_OT_rename_mixamo_bones_to_drdr

classes = [
    OBJECT_OT_rename_xnalara_bones_to_re2r,
    OBJECT_OT_rename_xnalara_bones_to_re3r,
    OBJECT_OT_rename_xnalara_bones_to_re4r,
    OBJECT_OT_rename_xnalara_bones_to_re7,
    OBJECT_OT_rename_xnalara_bones_to_re8,
    OBJECT_OT_rename_xnalara_bones_to_sf6,
    OBJECT_OT_rename_xnalara_bones_to_dmc5,
    OBJECT_OT_rename_xnalara_bones_to_mhwilds,
    OBJECT_OT_rename_xnalara_bones_to_drdr,
    OBJECT_OT_rename_mmd_bones_to_re2r,
    OBJECT_OT_rename_mmd_bones_to_re3r,
    OBJECT_OT_rename_mmd_bones_to_re4r,
    OBJECT_OT_rename_mmd_bones_to_re7,
    OBJECT_OT_rename_mmd_bones_to_re8,
    OBJECT_OT_rename_mmd_bones_to_sf6,
    OBJECT_OT_rename_mmd_bones_to_dmc5,
    OBJECT_OT_rename_mmd_bones_to_mhwilds,
    OBJECT_OT_rename_mmd_bones_to_drdr,
    OBJECT_OT_rename_mixamo_bones_to_re2r,
    OBJECT_OT_rename_mixamo_bones_to_re3r,
    OBJECT_OT_rename_mixamo_bones_to_re4r,
    OBJECT_OT_rename_mixamo_bones_to_re7,
    OBJECT_OT_rename_mixamo_bones_to_re8,
    OBJECT_OT_rename_mixamo_bones_to_sf6,
    OBJECT_OT_rename_mixamo_bones_to_dmc5,
    OBJECT_OT_rename_mixamo_bones_to_mhwilds,
    OBJECT_OT_rename_mixamo_bones_to_drdr,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)