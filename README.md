# XML Image File Reader
## The purpose of this script is to automate the task of renaming and moving all XML Image files to their respective directories within the BJC repository.
---
### This script will read in a .txt file that you will fill out appropriately as shown below in the template.
---
## Template:
### Lines 1 through N will for English images.
### Lines N + 1 through 2N will be for Spanish images.
### N = number of images
### Beyond that, it will be the respective file path of where the image should go.
---
#### For a concrete example, see sample.txt
\
1st line: New file name of img. 1\
2nd line: New file name of img. 2\
3rd line: New file name of img. 3\
.\
.\
.\
Nth line: New file name of img. N\
(N + 1)th line: New file name of img. 1 .es\
(N + 2)th line: New file name of img. 2 .es\
(N + 3)th line: New file name of img. 3 .es\
(N + 4)th line: New file name of img. 4 .es\
.\
.\
.\
2Nth line: New file name of img. N .es\
**space**\
File path for where img. 1 should be\
File path for where img. 2 should be\
File path for where img. 3 should be\
File path for where img. 4 should be\
.\
.\
.\
File path for where img. N should be\
File path for where img. 1 .es should be\
File path for where img. 2 .es should be\
File path for where img. 3 .es should be\
File path for where img. 4 .es should be\
.\
.\
.\
File path for where img. N .es should be\
**end**

