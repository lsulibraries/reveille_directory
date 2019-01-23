#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
time_start = time.time()
import glob
import os
path = '/home/wconli1/Desktop/Reveille_jpg'
target = '/home/wconli1/Desktop/Reveille_OCR'

ocrs = []

working_dir = os.listdir(path)
with open('%s/reveille_ocr_master.txt' % target, 'wb') as result:
    for folder in working_dir:
        issues_folder = os.path.join(path, folder)
        files =  glob.glob('%s/*OCR.txt' % issues_folder)
        for file in files:
            ocrs.append(file)
    ocrs = sorted(ocrs)
    for ocr in ocrs:
        with open(ocr, 'rb') as text:
            result.write(text.read())
print(time.time() - time_start)
