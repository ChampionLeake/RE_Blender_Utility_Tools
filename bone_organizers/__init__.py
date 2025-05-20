import bpy

from .organize_re2r_bones import OBJECT_OT_organize_re2r_bones
from .organize_re3r_bones import OBJECT_OT_organize_re3r_bones
from .organize_re4r_bones import OBJECT_OT_organize_re4r_bones
from .organize_re7_bones import OBJECT_OT_organize_re7_bones
from .organize_re8_bones import OBJECT_OT_organize_re8_bones
from .organize_sf6_bones import OBJECT_OT_organize_sf6_bones
from .organize_dmc5_bones import OBJECT_OT_organize_dmc5_bones
from .organize_mhwilds_bones import OBJECT_OT_organize_mhwilds_bones
from .organize_drdr_bones import OBJECT_OT_organize_drdr_bones

classes = [
    OBJECT_OT_organize_re2r_bones,
    OBJECT_OT_organize_re3r_bones,
    OBJECT_OT_organize_re4r_bones,
    OBJECT_OT_organize_re7_bones,
    OBJECT_OT_organize_re8_bones,
    OBJECT_OT_organize_sf6_bones,
    OBJECT_OT_organize_dmc5_bones,
    OBJECT_OT_organize_mhwilds_bones,
    OBJECT_OT_organize_drdr_bones,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()