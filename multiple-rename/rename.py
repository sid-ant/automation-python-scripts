import os,sys
import random

names=[]
namefile=open("correct.txt")
for line in namefile:
    names.append(line)

def main():
    path=raw_input("enter path to the directory \n")
    try:
        dirs = os.listdir(path)
        os.chdir(path)
    except:
        print "error incorrect path name! enter again"
        main()
    else:
        GetFiles(dirs)
    print "Finished"

def GetFiles(dirs):
    for file in dirs:
        index=file.rfind(".")
        if index == -1:
            RenameFile(file)
            continue
        extension=file[index:]
        RenameFile(file,extension)

def RenameFile(file,ext=""):
    global names
    randomName=random.choice(names)
    newName=str(randomName[:-1])+ext
    try:
        os.rename(file,newName)
    except OSError:
        randomName=random.choice(names)
        newName=str(randomName)+ext
        try:
            os.rename(file,newName)
        except:
            print "Unkown error occurred changing name of file:",file," to:",newName,"\n"
    except:
        print "Unkown error occurred changing name of file:",file," to:",newName,"\n"
    else:
        try:
            i=names.index(randomName)
        except:
            print "\n couldn't get index of the random file name! duh what? "
        else:
            del names[i]

main()
