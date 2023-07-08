import os
import shutil

# TODO: Get rid of writing .es.png or .png in .txt file
# TODO: Redundant to rewrite file paths for .es images as their the same as their english counter part.

fd = open('sample.txt', 'r')
# You'd put the directory of where the images are downwloaded:
img_dir = '../../../Downloads/'
# You'd put the path from where the image is to atleast the img folder for bjc:
default_path = '../bjc-r/img/'

old_img_names = [f for f in os.listdir(img_dir) if 'png' in f.lower()]
# Sort the list with respect to the time it was downloaded to make sure the image is renamed correctly:
old_img_names.sort(key=lambda file: os.path.getmtime(img_dir + file))

# Rename and move each img file to its respective directory within the BJC repository.
for old_img_name in old_img_names:
    img = fd.readline().rstrip().split(',')
    new_name = img_dir + img[0]
    prev_name = img_dir + old_img_name
    os.rename(prev_name, new_name)
    new_path = default_path + img[1] + '/' + img[0]
    old_path = img_dir + img[0]
    shutil.move(old_path, new_path)

fd.close()
