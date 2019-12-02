# -*- coding: utf-8 -*-
# occiput  
# Harvard University, Martinos Center for Biomedical Imaging 
# Aalto University, Department of Computer Science


from .Volume import import_nifti

def import_kspace(filename): 
    return import_nifti(filename) 

