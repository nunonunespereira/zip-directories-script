import zipfile
import os

# get directory from input
dir_path = input("Enter the path of the directory to compress: ")

# create ZIP file inside directory 
zip_file_path = os.path.join(dir_path, os.path.basename(dir_path) + ".zip")

with zipfile.ZipFile(zip_file_path, "w", compression=zipfile.ZIP_DEFLATED) as zip:
    # add files
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            zip.write(os.path.join(root, file))

print(f"Directory compressed, ZIP created at: {zip_file_path}")
