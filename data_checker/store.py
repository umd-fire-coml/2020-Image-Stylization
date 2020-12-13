import os
import sys
import pickle
#d contains directories f contains the files
d = set()
f = set()
#by default it looks at the current directory 
cur_directory = "../data"
#if there is argument, it's the directory name assumed
if (len(sys.argv) > 1):
    cur_directory = sys.argv[1]
for root, dirs, files in os.walk(cur_directory, topdown=False):
    for name in files:
        f.add(os.path.join(root, name))
    for name in dirs:
        d.add(os.path.join(root, name))
pickle.dump((f, d), open( "save.p", "wb" ) )
print(f, d)