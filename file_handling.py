import os
import sys 
from  fileinput import FileInput
# file_in = input("enter file name:")
file_in = "data.txt"
if os.path.isfile(file_in):
    with FileInput(file_in,inplace=True,backup ='.bak') as f:
        print("file opened")
        lcount=wcount=ccount=0
        for line in f:
            if ";" in line:
                print(line.replace(";",""), end="")
        #     lcount += 1
        #     wcount+= len(line.split())
        #     ccount += len(line)
        # print("lcount:", lcount, "wcount:", wcount, "ccount:", ccount)
else:
    print("file not exists")
    sys.exit(0)

