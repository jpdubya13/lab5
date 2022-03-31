import os
import hashlib
import datetime
import time
import sys

protectedDirs = ['dev','proc','run','sys','tmp','var/lib','var/run']

def printAllFiles():
    for root, dirs, files in os.walk("/"):
        for file in files:
            if (root.split('/')[1] or '/'.join(root.split('/')[1:2])) not in protectedDirs:
                print(root+'/'+file)

def hashFiles():
    hashfile = "PWD_Hashlog "+str(datetime.datetime.now())+".log"
    f = open(hashfile,'a')
    for root, dirs, files in os.walk("/home/sy402/Desktop/lab5"):
        for file in files:
            if (root.split('/')[1] or '/'.join(root.split('/')[1:2])) not in protectedDirs:
                pathname = root+'/'+file
                h = hashlib.sha256(open(pathname,'rb').read()).hexdigest()
                f.write(h+":::"+pathname+":::"+str(time.time())+'\n')
    f.close()
    print("Files hashed.\nLog File:",hashfile)

def hashList(hf):
    hashlist = []
    pathlist = []
    for line in open(hf).readlines():
        hashlist.append(line.split(':::')[0])
        pathlist.append(line.split(':::')[1])
    return hashlist,pathlist

def compareState(hf):
    hashlist,pathlist = hashList(hf)
    for root, dirs, files in os.walk("/home/sy402/Desktop/lab5"):
        for file in files:
            if (root.split('/')[1] or '/'.join(root.split('/')[1:2])) not in protectedDirs:
                pathname = root+'/'+file
                h = hashlib.sha256(open(pathname,'rb').read()).hexdigest()
                if h not in hashlist:
                    if pathname in pathlist:
                        print("FILE MODIFIED:",pathname)
                    else:
                        print("NEW FILE: ", pathname)
                
if __name__ == "__main__":
    if sys.argv[1] == '-compare':
        f = sys.argv[2]
        compareState(f)
    if sys.argv[1] == '-hash':
        hashFiles()
