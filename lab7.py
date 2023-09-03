import os
import zipfile
def backup_folder_to_zip(source_folder,zip_filename):
    #check if the source folder exists
    if not os.path.exists(source_folder):
        print(f"Error:source folder'{source_folder}' does not exist.")
        return
    #create zipfile in the cwd
    zipf=zipfile.Zipfile(zip_filename,'w')
    #walkthrough the source folder and add its contents to the zipfile
    for foldername,subfolders,filenames in os.walk(source_folder):
        for filename in filename:
            file_path=os.path.join(foldername,filename)
            zipf.write(file_path,os.path.relpath(file_path,source_folder))
            print(f"Zipping:{file_path}")
    #close the zip file
    zipf.close()
    print(f"backup succesfull:'{source_folder}' has been backed up to '{zip_filename}'")
folder_to_backup=input("Enter the name of the folder to backup(into the current working directory)")
zip_filename=f"{folder_to_backup}.zip"
backup_folder_to_zip(folder_to_backup,zip_filename)