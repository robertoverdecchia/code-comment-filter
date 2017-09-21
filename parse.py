import os
import csv
import fnmatch
import shutil
from comment_parser import comment_parser
import git
from git import Repo
        
git_repository_url = "https://github.com/r0ket/r0ket.git" # URL of git repository
MIME = "text/x-c" # MIME type

L = list()                  
C = list()
i = 0

print "Cloning repository..."
Repo.clone_from(git_repository_url, "repository_root")   
print "Repository cloning ended"

print "Comment parsing started..."
for root, dirs, files in os.walk("repository_root"): # recursively find files starting from root folder
    for filename in files:
        if filename.lower().endswith((".c", ".h")): # filter for given file extention
            L.append(os.path.join(root, filename))              
            c = (comment_parser.extract_comments(L[i], MIME))  # parse comments according to 
                                                                     # hardcoded MIME and store them 
                                                                     # in list
            C.append(c)
            i += 1
            #print C[i]
print "Comment parsing ended"


with open("patterns.txt") as f:           # patterns to be matched
    keywords = [line.strip() for line in f]

print "Pattern matching started..."
with open('output_parsing.tsv', 'w') as csvfile:
    writer=csv.writer(csvfile, delimiter='\t')
    writer.writerow(["File name", "Keyword",  "Comment"]) # write header

    for x in range(len(L)):               # for each file
        for y in range(len(C[x])):        # for each comment
            for z in range (len(keywords)):
                s = str(C[x][y])  
                if keywords[z].lower() in s.lower(): # match lower case for case insensivity
                    writer.writerow([L[x], keywords[z],  str(C[x][y])]) # store file name, keyword and comment
print "Pattern matching ended"

shutil.rmtree("repository_root") # remove local copy of cloned repository