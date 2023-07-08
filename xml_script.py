import os
import shutil

# TODO: Get rid of writing .es.png or .png in .txt file
# TODO: Redundant to rewrite file paths for .es images as their the same as their english counter part.

fd = open('script.txt', 'r')
# You'd put the directory of where the images are downwloaded:
img_dir = '../'
# You'd put the path from where the image is to atleast the img folder for bjc:
default_path = '../../personal/work/bjc-r/img/'

old_img_names = [f for f in os.listdir(img_dir) if 'png' in f.lower()]
# Sort the list with respect to the time it was downloaded to make sure the image is renamed correctly:
old_img_names.sort(key=lambda file: os.path.getmtime(img_dir + file))

# Rename all img files
for img in old_img_names:
    new_name = img_dir + fd.readline().rstrip()
    prev_name = img_dir + img
    os.rename(prev_name, new_name)

new_img_names = [f for f in os.listdir(img_dir) if 'png' in f.lower()]
# Sort the list with respect to the time it was modified (renamed) to ensure it will be sent to the correct directory.
new_img_names.sort(key=lambda file: os.path.getmtime(img_dir + file))

fd.readline()  # Skip line

# Move all img files to their respective directories.
for img in new_img_names:
    new_path = default_path + fd.readline().rstrip() + img
    old_path = img_dir + img
    shutil.move(old_path, new_path)

fd.close()
