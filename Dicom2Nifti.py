import dicom2nifti


initial_file=1
last_file=10

for iteration in range (initial_file,last_file):#from the initial to the last+1
    try:
        input_dir='/Users/cesaracebes/Desktop/OneDrive/AI coronary/Patients/Case '+str(iteration)+'/DICOM'
        output_dir='/Users/cesaracebes/Desktop/OneDrive/AI coronary/Patients/Case '+str(iteration)+'/NIfTI/COROS_00'+str(iteration)+'_0000.nii.gz'
        dicom2nifti.dicom_series_to_nifti(input_dir,output_dir,reorient_nifti=True)
        print('case '+str(iteration)+' correctly changed in format')
    except:
        print('case '+str(iteration)+' INCORRECT')
    #case 1 does not work well