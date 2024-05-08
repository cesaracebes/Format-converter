# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 08:50:46 2023

@author: cacebes
"""

"""
Spyder Editor

This is a temporary script file.
"""

import os
import glob
import nrrd#pip install pynrrd, if pynrrd is not already installed
import nibabel as nib #pip install nibabel, if nibabel is not already installed
import numpy as np


  
  
# Get a list of .nrrd files in a directory
nrrd_files = glob.glob('U:/Dlab_docent/Estudiantes_curso_23_24/BElEmrani_est_UPF_23-24/ASOCA_full/Normal/Annotations/*.nrrd')
#nrrd_files = glob.glob('U:/Dlab_projectes/AI_Cesar/DB ASOCA/Train_Masks/*.nrrd')

# Loop through each .nrrd file
for nrrd_file in nrrd_files:
    # Read the .nrrd file
    data, header = nrrd.read(nrrd_file)
    
    # Create a NIfTI1Image object
    nifti_img = nib.Nifti1Image(data, affine=None)
    
    # Update the NIfTI header with necessary information
    nifti_img.header.set_data_dtype(data.dtype)
    nifti_img.header.set_zooms([header['space directions'][0, 0],
                            header['space directions'][1, 1],
                            header['space directions'][2, 2]])
        
    # Generate the output .nii file path by replacing the extension
    nii_file = nrrd_file.replace('.nrrd', '.nii.gz')
    
    # Save the NIfTI1Image object as .nii file
    nib.save(nifti_img, nii_file)