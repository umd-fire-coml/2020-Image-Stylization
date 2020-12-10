import os
import sys
import pickle
#modes for checking file or directory
mode = "" #both file and directories are checked
#mode = "d" #only directories are checked
#d contains directories f contains the files
d = set()
f = set()
#looks at data directory 
cur_directory = "../data"
#if there is argument, it's the directory name assumed
if (len(sys.argv) > 1):
    cur_directory = sys.argv[1]
for root, dirs, files in os.walk(cur_directory, topdown=False):
    for name in files:
        f.add(os.path.join(root, name))
    for name in dirs:
        d.add(os.path.join(root, name))
original = pickle.load( open( "save.p", "rb" ))
#this is the files and directory in where you want to match
f_o = original[0]
d_o = original[1]
#store the things that are in local but not in correct one
file_only_here = set()
directory_only_here = set()
#check the differences
for file_here in f:
    if file_here not in f_o:
        file_only_here.add(file_here)
    else:
        f_o.remove(file_here)
for directory_here in d:
    if directory_here not in d_o:
        directory_only_here.add(directory_here)
    else:
        d_o.remove(directory_here)
result = True
if mode != "d":
    if (len(f_o) > 0):
        result = False
        print("here are the files not found")
        for x in f_o:
            print(x)
if (len(d_o) > 0):
    result = False
    print("here are the directories not found")
    for x in d_o:
        print(x)
if mode != "d":
    if (len(file_only_here) > 0):
        result = False
        print("here are files only in local")
        for x in file_only_here:
            print(x)
if (len(directory_only_here) > 0):
    result = False
    print("here are directories only in local")
    for x in directory_only_here:
        print(x)
if result:
    print("everything is exactly the same :)")