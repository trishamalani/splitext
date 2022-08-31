import os
import shutil

source="C:/Users/trish/OneDrive/Desktop/python/class 110"
destination=""
listoffiles=os.listdir(source)
print(listoffiles)

for i in listoffiles:
    root,ext=os.path.splitext(i)
    print(root)
    print(ext)