import os
import glob
import sys
os.chdir(sys.path[0])

keepasking = True
while(keepasking):
    yesORno = str(input("Should I also delete the video? (y / n)"))
    if yesORno == "y":
        delVid = True
        keepasking = False
    elif yesORno == "n":
        delVid = False
        keepasking = False
    else:
        print("either y or n")

if delVid == True:
    files = glob.glob('./video/*')
    for f in files:
        os.remove(f)


files = glob.glob('./frames/*')
for f in files:
        os.remove(f)

files = glob.glob('./render/*')
for f in files:
        os.remove(f)
    

files = glob.glob('./styleOriginal/*')
for f in files:
        os.remove(f)

files = glob.glob('./styleCorrect/*')
for f in files:
        os.remove(f)