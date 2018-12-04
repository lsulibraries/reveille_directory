import os
import glob
path_to_check = '/home/wconli1/Desktop/Reveille_playground/reveillecentennial'
top_directory = os.listdir(path_to_check)
for folder in top_directory:
    abs_path = os.path.join(path_to_check, folder)
    members = os.listdir(abs_path)
    for member in members:
#        print(member)
        abs_member_path = os.path.join(abs_path, member)
#        print(abs_member_path)
        if os.path.isdir(abs_member_path):
            #check for a single OBJ.jp2
#            print(len(glob.glob("%s/*.jp2" % abs_member_path)))
            if len(glob.glob("%s/*.jp2" % abs_member_path)) < 1:

                print(abs_member_path, 'is missing a jp2')
            #check for a single OCR.txt
#            print(len(glob.glob("%s/*.jp2" % abs_member_path)))
            if len(glob.glob("%s/*.txt" % abs_member_path)) < 1:
                print(abs_member_path, 'is missing a ocr')
#        else if not member.endswith('.xml'):
#            print(abs_path, 'is missing the metadata for the issue.')
print('complete')
