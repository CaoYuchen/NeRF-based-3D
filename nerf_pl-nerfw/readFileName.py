import os

a = open("output.txt", "w")
i = 0
for path, subdirs, files in os.walk(r'./data/MMCH/images'):
   for filename in files:
        i+=1
        f = filename + " " + str(i) + " train MMCH"
        a.write(str(f) + os.linesep)