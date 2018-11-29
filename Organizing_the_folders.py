# -*- coding: utf-8 -*-
import os
import re
import shutil
from zipfile import ZipFile
import subprocess
import hashlib
path = 'C:\\Users\\libsys\\Desktop\\success'
target = 'C:\\Users\\libsys\\Desktop\\test'
#path = input("Enter the collection path:")
#target = input("Enter the target path:")
collections = []
old_file_paths = []
new_file_paths = []
working_dir = os.listdir(path)
for folder in working_dir:
    issues_folder = os.path.join(path,folder)
    sub_folder = os.listdir(issues_folder)
    for issue in sub_folder:
        folder_path = os.path.join(issues_folder,issue)
        files = os.listdir(folder_path)
        plain = re.sub('[^A-Za-z]+', '', issue)
        new_path = os.path.join(target,plain)
        if not os.path.exists(new_path):
            os.mkdir(new_path)
            collections.append(plain)
        sub_folder_new = os.path.join(new_path,issue)
        if not os.path.exists(sub_folder_new):
            os.mkdir(sub_folder_new)
        for file in files:
            file_path = os.path.join(folder_path,file)
            if file.endswith('.pdf'):
                pdf_path = os.path.join(sub_folder_new,'PDF.pdf')
                shutil.copy(file_path,pdf_path)
                old_file_paths.append(file_path)
                new_file_paths.append(pdf_path)
            if file.endswith('.xml'):
                if file.find("METS"):
                    xml_path = os.path.join(sub_folder_new,'MODS.xml')
                    shutil.copy(file_path,xml_path)
                    xml_new_path = xml_path #os.path.join(folder_path,file)
                    saxon_source_option = "-s:%s" % xml_new_path
                    saxon_output_option = "-o:%s" % xml_path
                    saxon_xsl = 'C:\\Users\\libsys\\.spyder-py3\\work\\mods_from_mets.xsl'
                    subprocess.call(["saxon", saxon_output_option, saxon_source_option, saxon_xsl], shell=True)
            if file.endswith('.jp2'):
                jp = re.search('\d+(?=\.\w+$)', file)
                issue_number_folder = os.path.join(sub_folder_new,jp.group(0))
                if not os.path.exists(issue_number_folder):
                    os.mkdir(issue_number_folder) 
                jp_path = os.path.join(issue_number_folder,'OBJ.jp2')
                shutil.copy(file_path,jp_path)
                old_file_paths.append(file_path)
                new_file_paths.append(jp_path)
            if file.endswith('.txt'):
                txt = re.search('\d+(?=\.\w+$)', file)
                issue_number_folder = os.path.join(sub_folder_new,txt.group(0))
                if not os.path.exists(issue_number_folder):
                    os.mkdir(issue_number_folder)
                txt_path = os.path.join(issue_number_folder,'OCR.txt')
                shutil.copy(file_path,txt_path)
                old_file_paths.append(file_path)
                new_file_paths.append(txt_path)
#checksum
md5_returned_old = []
for file in old_file_paths:
    with open(file,"rb") as file_to_check:
        hash1 = hashlib.md5()
        data = file_to_check.read()        
        hash1.update(data.strip())
        md5_return = hash1.hexdigest()
        md5_returned_old.append(md5_return)
md5_returned_new = []
for file in new_file_paths:
    with open(file,"rb") as file_to_check:
        hash1 = hashlib.md5()
        data = file_to_check.read()        
        hash1.update(data.strip())
        md5_return = hash1.hexdigest()
        md5_returned_new.append(md5_return)
if (md5_returned_new == md5_returned_old) == True:
    print("Checksum verified. Continuing to compress the new folder")
    os.chdir(target)
    for collection in collections:
        zp = collection + '.zip'
        zipf = ZipFile(zp , mode='w')
        lenDirPath = len(new_path)
        for root, _ , files in os.walk(new_path):
            for file in files:
                filePath = os.path.join(root, file)
                zipf.write(filePath , filePath[lenDirPath :] )
        zipf.close()
else:
    print("Checksum not verified. Stopped compressing the new folder")