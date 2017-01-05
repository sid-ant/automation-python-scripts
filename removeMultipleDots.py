import os

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

def GetFiles(dirs):
    for file in dirs:
        count=0
        for k in file:
            if k==".":
                count+=1
        if count>1:
            index=file.find(".")
            keep=file[:index]
            exti=file.rfind(".")
            ext=file[exti:]
            name=keep+ext
            os.rename(file,name)

main()
