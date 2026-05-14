import os
f = os.listdir('.')
 
for stuff in f:
    if stuff:
         print(stuff,"is a directory")
    else:
        print(stuff,"is a file")