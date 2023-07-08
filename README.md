# XML Image File Reader
## The purpose of this script is to automate the task of renaming and moving all XML Image files to their respective directories within the BJC repository.
---
### This script will read in a .txt file that you will fill out appropriately as shown below in the template.
---
## Template:
### Lines 1 through N will for English images.
### Lines N + 1 through 2N will be for Spanish images.
### N = number of images
---
#### For a concrete example, see sample.txt
\
Line 1: new_file_name_of_img_1,file_path_for_img_1\
Line 2: new_file_name_of_img_2,file_path_for_img_2\
Line 3: new_file_name_of_img_3,file_path_for_img_3\
Line 4: new_file_name_of_img_4,file_path_for_img_4\
.\
.\
.\
Line N: new_file_name_of_img_N,file_path_for_img_N\
Line N + 1: new_file_name_of_img.es_1,file_path_for_img.es_1\
Line N + 2: new_file_name_of_img.es_1,file_path_for_img.es_2\
Line N + 3: new_file_name_of_img.es_1,file_path_for_img.es_3\
Line N + 4: new_file_name_of_img.es_1,file_path_for_img.es_4\
.\
.\
.\
Line 2N: new_file_name_of_img.es_N,file_path_for_img.es_N\
\
**Sample.txt**

        
        map-list-figures.png,3-lists/
        keep-list-figures.png,3-lists/
        combine-list-figures.png,3-lists/
        map-example-1.png,3-lists/
        keep-items-(last-letter-h)-reporting.png,3-lists/
        combine-simple-example.png,3-lists/
        map-list-figures.es.png,3-lists/
        keep-list-figures.es.png,3-lists/
        combine-list-figures.es.png,3-lists/
        map-example-1.es.png,3-lists/
        keep-items-(last-letter-h)-reporting.es.png,3-lists/
        combine-simple-example.es.png,3-lists/    
        