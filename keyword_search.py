import re
import os

# Get working dir
rootdir = os.getcwd()

#Hardcoded, maybe argument later on?
with open('keyword_list.txt') as f:
    keywords = f.read().splitlines()

# For each dir in fold and it's childern
for subdir, dirs, files in os.walk(rootdir):
    for dir in dirs:
        #For each file in each dir 
        for filename in os.listdir(dir):
            f = os.path.join(dir, filename)
            #read the file
            with open(f, "r") as curr_file:
                #Find keyword by iterating over everything
                for word in curr_file:
                    for keyword in keywords:
                        if re.search(keyword, word):
                            print(word)
                            print('\x1b[6;30;42m' + f + '\x1b[0m')