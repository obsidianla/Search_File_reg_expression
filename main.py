'''
Created on Mar 13, 2017

@author: bowenzhi
'''

import os, re
import matplotlib.pyplot as plt
import seaborn as sns

#user prompt input
root_dir = raw_input('Please enter the full path of root directory: ')
keyword = raw_input('Please enter keyword to search: ')


#search through all files in given directory
def SearchFile(tmp_dir, exp):
    #initialize count
    count = 0
    #search through all files 
    for filename in os.listdir(tmp_dir):
        #check to make sure it is a file
        fname = os.path.join(tmp_dir, filename)
        if os.path.isfile(fname):
            if fname.endswith('.txt'):
            #open file, check for matches
                with open(fname) as f:
                    for line in f:
                        searchObj = re.search(exp, line, re.M|re.I)
                        #if find a match
                        if searchObj:
                            count += 1

    return count
    
#initialize key:value array
output = {}
#recursively walk through all directories and call SearchFile for each subdir
for root, dirs, files in os.walk(root_dir):
    output[root] = SearchFile(root, keyword)
#output array of all the data
print output


#output bar graph using seaborn
sns.set_style("whitegrid")
plt.figure(figsize=(12,6))
ax = sns.barplot(x=output.keys(), y=output.values())
plt.title('Distribution of keyword')
plt.xlabel('Subdirectory Names')
plt.ylabel('Number of Count')
plt.show()

