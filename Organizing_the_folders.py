# -*- coding: utf-8 -*-
import os
import re
import shutil
from zipfile import ZipFile
path = 'C:\\Users\\libsys\\Desktop\\success'
target = 'C:\\Users\\libsys\\Desktop\\test'
#shutil.copytree(path,target)
collections = []
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
            collections.append(plain)
        sub_fol_new = os.path.join(new_path,single)
        if not os.path.exists(sub_fol_new):
            os.mkdir(sub_fol_new)
        for file in files:
            file_path = os.path.join(folder_path,file)
            if file.endswith('.pdf'):
                pdf_path = os.path.join(sub_fol_new,'PDF.pdf')
                shutil.copy(file_path,pdf_path)
            if file.endswith('.xml'):
                if file.find("METS"):
                    xml_path = os.path.join(sub_fol_new,'MODS.xml')
                    shutil.copy(file_path,xml_path)
                    #add xslt stuff eventually...
            if file.endswith('.jp2'):
                jp = re.search('\d+(?=\.\w+$)', file)
                new_fol = os.path.join(sub_fol_new,jp.group(0))
                if not os.path.exists(new_fol):
                    os.mkdir(new_fol) 
                jp_path = os.path.join(new_fol,'OBJ.jp2')
                shutil.copy(file_path,jp_path)
            if file.endswith('.txt'):
                txt = re.search('\d+(?=\.\w+$)', file)
                new_fol = os.path.join(sub_fol_new,txt.group(0))
                if not os.path.exists(new_fol):
                    os.mkdir(new_fol)
                txt_path = os.path.join(new_fol,'OCR.txt')
                shutil.copy(file_path,txt_path)
#    shutil.rmtree(main_fol)
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
