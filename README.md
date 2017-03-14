# Search_File_reg_expression
This project use os and re to search keyword in a directory

This script should recursively walk the “root_dir” and detect all the files under that dir contains “keywords” and 
count the number of files for that sub dir. All results should be saved in a key:value array with key being 
subdir string, and value being counts of file contains the key line 

I created a small data set to test the code.
1. test whether it can go through all subdirectories. It works for this test set.
2. test some regular expression. For example, use (.*)!(.*) checks how many countries for each subdir.
If we want to open specific file format such as '.dat', we need to add one line code: if fname.endswith('.dat').


Thanks the link from https://github.com/jem20th/File-Search, I get good idears. I also add some new featrues so we can search
regular expression and I use seaborn to make the figure better.
