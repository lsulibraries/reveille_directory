# -*- coding: utf-8 -*-
import os
import re
import shutil
from zipfile import ZipFile
path = 'C:\\Users\\libsys\\Desktop\\success'
target = 'C:\\Users\\libsys\\Desktop\\success'
main1 = os.listdir(path)
for each in main1:
    main_fol = os.path.join(path,each)
    sub_fol = os.listdir(main_fol)
    for single in sub_fol:
        folder_path = os.path.join(main_fol,single)
        files = os.listdir(folder_path)
        plain = re.sub('[^A-Za-z]+', '', single)
        new_path = os.path.join(target,plain)
        if not os.path.exists(new_path):
            os.mkdir(new_path)
        sub_fol_new = os.path.join(new_path,single)
        if not os.path.exists(sub_fol_new):
            os.mkdir(sub_fol_new)
        for file in files:
            file_path = os.path.join(folder_path,file)
            if file.endswith('.pdf'):
                pdf_path = os.path.join(sub_fol_new,'PDF.pdf')
                shutil.copy(file_path,pdf_path)
            if file.endswith('.xml'):
                n = len(file)
                xml = file[n-7:n-4]
                if xml == "ETS":
                    xml_path = os.path.join(sub_fol_new,'MODS.xml')
                    shutil.copy(file_path,xml_path)
            if file.endswith('.jp2'):
                l = len(file)
                jp = file[l-7:l-4]
                new_fol = os.path.join(sub_fol_new,jp)
                if not os.path.exists(new_fol):
                    os.mkdir(new_fol)
                jp_path = os.path.join(new_fol,'OBJ.jp2')
                shutil.copy(file_path,jp_path)
            if file.endswith('.txt'):
                m = len(file)
                txt = file[m-7:m-4]
                new_fol = os.path.join(sub_fol_new,txt)
                if not os.path.exists(new_fol):
                    os.mkdir(new_fol)
                txt_path = os.path.join(new_fol,'OCR.txt')
                shutil.copy(file_path,txt_path)
    shutil.rmtree(main_fol)
file_paths = []
zp = os.path.join(plain,'.zip')
for folder, subfolders, files_1 in os.walk(new_path): 
        for eachfilename in files_1: 
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(folder, eachfilename) 
            file_paths.append(filepath) 
for file_name in file_paths: 
        print(file_name) 
    # writing files to a zipfile 
with ZipFile(zp,'w') as zip: 
        # writing each file one by one 
        for file in file_paths: 
            zip.write(file) 

