import os
import shutil
import piexif
from datetime import datetime

file_list = os.listdir('unsorted')
for file in file_list:
    file_path = os.path.join('unsorted', file)
    date_string = piexif.load(file_path)['Exif'][36867].decode()
    date = datetime.strptime(date_string, '%Y:%m:%d %H:%M:%S')
    month_folder = date.strftime('%Y_%m')
    day_folder = date.strftime('%Y_%m_%d')
    print(month_folder, '->', day_folder)
    if not os.path.exists(month_folder):
        os.mkdir(month_folder)
    full_path = os.path.join(month_folder, day_folder)
    if not os.path.exists(full_path):
        os.mkdir(full_path)
    shutil.move(file_path, os.path.join(full_path, file))