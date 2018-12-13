#!/usr/bin/python3
# -*- coding: utf-8 -*-
import glob
import os
import shutil
import subprocess
path = '/home/wconli1/Desktop/Reveille_playground/reveillecentennial'
target = '/home/wconli1/Desktop/Reveille_jpg'
working_dir = os.listdir(path)
for issue in working_dir:
    issue_folder = os.path.join(path, issue)
    page_folders = os.listdir(issue_folder)
    for page in page_folders:
        if os.path.isdir(os.path.join(issue_folder, page)):
            page_path = os.path.join(issue_folder, page)
            new_path = os.path.join(target, issue)
            if not os.path.exists(new_path):
                os.mkdir(new_path)
            jp2s = glob.glob('%s/*.jp2' % page_path)
            for jp2 in jp2s:
                jp2_path = os.path.join(page_path, jp2)
                rename = '%s-%s.jp2' % (issue, page)
                newname = '%s-%s.jpg' % (issue, page)
                dest_path = os.path.join(new_path, rename)
                shutil.copy(jp2_path, dest_path)
                subprocess.call('convert %s %s' % (dest_path, os.path.join(new_path, newname)), shell=True)
                os.remove(dest_path)
            ocrs = glob.glob('%s/*.txt' % page_path)
            for ocr in ocrs:
                ocr_path = os.path.join(page_path, ocr)
                rename = '%s-%s-OCR.txt' % (issue, page)
                dest_path = os.path.join(new_path, rename)
                shutil.copy(ocr_path, dest_path)
    print(issue, 'is finished')
