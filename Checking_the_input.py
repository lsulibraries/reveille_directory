import os
import glob
path = '/media/wconli1/HDD-118/LSU_18-040'
years_folder = os.listdir(path)
for year in years_folder:
    year_path = os.path.join(path, year)
    issues = os.listdir(year_path)
    for issue in issues:
        issue_path = os.path.join(year_path, issue)
        tif_count = len (glob.glob("%s/*.tif" % issue_path))
        jp2_count = len (glob.glob("%s/*.jp2" % issue_path))
        ocr_count = len (glob.glob("%s/*.txt" % issue_path))
        if tif_count != jp2_count:
            print(issue_path, "tif and jp2 count are off")
        if jp2_count != ocr_count:
            print(issue_path, "ocr and jp2 count are off")
print('complete')
