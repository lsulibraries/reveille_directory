import os
import glob
path_to_check = '/home/wconli1/Desktop/Reveille_playground/reveillecentennial'
top_directory = os.listdir(path_to_check)
replace = input("would you like to replace any empty OCR? cannot be undone, y/n")
for folder in top_directory:
    abs_path = os.path.join(path_to_check, folder)
    members = os.listdir(abs_path)
    for member in members:
        abs_member_path = os.path.join(abs_path, member)
        if os.path.isdir(abs_member_path):
            #check for a single OBJ.jp2
            if len(glob.glob("%s/*.jp2" % abs_member_path)) < 1:

                print(abs_member_path, 'is missing a jp2')
            #check for a single OCR.txt
            if len(glob.glob("%s/*.txt" % abs_member_path)) < 1:
                print(abs_member_path, 'is missing a ocr')
            if os.stat("%s/OCR.txt" % abs_member_path).st_size < 1:
                print(abs_member_path, 'OCR file is empty')
                if replace == 'y':
                    os.unlink("%s/OCR.txt" % abs_member_path)
                    os.rmdir(abs_member_path)
print('complete')
