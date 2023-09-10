import os
import shutil
from pathlib import Path
or_path = input("Enter the Source path ex ; D: or E: ; or any absulute path like ex ; d:\paper "
                "remember to put colen after any single drive mention if any\n"
                "now Enter the Value ;:  ")
dis_path = input("Enter the Destination path Where you want to copy the file : " )
fol_name = input("Enter the Destination folder name Where you want to copy the file : " )
os.chdir(or_path)
with open('path.txt', 'a') as f:
    count = 0;
    for dirpath, dirname, filename in os.walk(or_path):
        print(len(dirpath))
        if len(dirpath) > 250 :
            f.write(dirpath + '\n')
            p = Path(dirpath)
            new_p = Path(*p.parts[6:])

            try:
                os.mkdir(dis_path +'/'+ fol_name)
            except:
                print("folder done")
            try:
                os.chdir(dis_path + '/' + fol_name)
                os.makedirs(new_p)
            except:
                print("makedirs will not worked")
                # os.chdir(dis_path + '/' + fol_name)
                # os.mkdir(new_p)

            for dir in dirname:
                try:
                    os.chdir(dis_path + '/' + fol_name)
                    os.chdir(new_p)
                    print(os.getcwd())
                    os.mkdir(dir)
                    print(dir)
                except :
                    print("folder exists")

            for nam in filename:
                 # os.chdir(dirpath)
                 # print(os.listdir(os.getcwd()))
                 # shutil.copyfile(str(nam),dis_path + '/' + fol_name + '/' + str(new_p))
                 # os.chdir(dis_path + '/' + fol_name + '/' + str(new_p))
                 # soouce = dirpath + '/'+nam
                 # des = os.getcwd()
                 try:

                    os.chdir(dis_path + '/' + fol_name)
                    os.chdir(new_p)
                    print(os.getcwd())
                    shutil.copy(dirpath + '/' + nam, os.getcwd())
                 except:
                    print(os.getcwd())
                    print("file exists or file is opened")

        if len(dirpath) <= 250:
            drive, path = os.path.splitdrive(dirpath)
            for dir in dirname:
                try:
                    os.makedirs(dis_path + '/' + path)
                except:
                    print("folder is already created")
                try:
                    os.chdir(dis_path + '/' + path)
                    print(os.getcwd())
                    os.mkdir(dir)
                    print(dir)
                except :
                    print("folder exists")

            for nam in filename:
                try:
                    os.chdir(dis_path + '/' + path)
                    shutil.copy(dirpath +'/' + nam, os.getcwd())

                except:
                    print("file exists file is opened")
