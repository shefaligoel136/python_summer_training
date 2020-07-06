# copying data of the file from one to another

f = open("fh.txt","r")
f1 = open("fh1.txt","a")

for i in f:
 f1.write(i)