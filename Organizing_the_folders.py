#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import re
import shutil
from zipfile import ZipFile
import subprocess
import hashlib
target = '/home/wconli1/Desktop/Reveille_playground/'
path = '/home/wconli1/Desktop/Reveille_test-two/'
#path = input("Enter the collection path:")
#target = input("Enter the target path:")
collections = []
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
            if file.endswith('.xml'):
                if file.find("METS") != -1:
                    print(file)
                    xml_path = os.path.join(sub_folder_new,'MODS.xml')
                    shutil.copy(file_path,xml_path)
                    xml_new_path = xml_path #os.path.join(folder_path,file)
                    saxon_args = "-s:%s" % xml_new_path
                    saxon_args += " -o:%s" % xml_path
                    saxon_args += ' /home/wconli1/Clones/reveille_directory/mods_from_mets.xsl'
                    saxon_call = "java -jar /usr/share/java/saxon9he.jar %s" % saxon_args
                    subprocess.call([saxon_call ], shell=True)
            if file.endswith('.jp2'):
                jp = re.search('\d+(?=\.\w+$)', file)
                issue_number_folder = os.path.join(sub_folder_new,jp.group(0))
                if not os.path.exists(issue_number_folder):
                    os.mkdir(issue_number_folder) 
                jp_path = os.path.join(issue_number_folder,'OBJ.jp2')
                shutil.copy(file_path,jp_path)
            if file.endswith('.txt'):
                txt = re.search('\d+(?=\.\w+$)', file)
                issue_number_folder = os.path.join(sub_folder_new,txt.group(0))
                if not os.path.exists(issue_number_folder):
                    os.mkdir(issue_number_folder)
                txt_path = os.path.join(issue_number_folder,'OCR.txt')
                shutil.copy(file_path,txt_path)
#checksum
#with open(path,"r+") as f:
#    for chunk in iter(lambda: f.read(4096), b""):
#        hashlib.md5.update(chunk)
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
