# -*- coding: utf-8 -*-
# occiput 
# Stefano Pedemonte 
# Harvard University, Martinos Center for Biomedical Imaging 
# Aalto University
from . import Core
from .Core import Transform_Affine, Transform_Identity, Transform_6DOF, Transform_Scale, Transform_Translation, Transform_Rotation, Grid3D, Image3D, GridND, ImageND
from .Core import grid_from_box_and_affine
from .Core import nifti_to_occiput, nipy_to_occiput, occiput_from_array

from . import transformations
from . import NiftyPy_wrap
from . import Conversion
from . import Errors
from . import Print
# from occiput.Core import Core
# from occiput.Core.Core import Transform_Affine, Transform_Identity, Transform_6DOF, Transform_Scale, Transform_Translation, Transform_Rotation, Grid3D, Image3D, GridND, ImageND
# from occiput.Core.Core import grid_from_box_and_affine
# from occiput.Core.Core import nipy_to_occiput, nifti_to_occiput, occiput_from_array
#
# from occiput.Core import transformations
# from occiput.Core import NiftyPy_wrap
# from occiput.Core import Conversion
# from occiput.Core import Errors
# from occiput.Core import Print