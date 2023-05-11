import os
import shutil
from pathlib import Path
or_path = input("Enter the Destination path ex ; D: or E: ; or any absulute path like ex ; d:\paper "
                "remember to put colen after any single drive mention if any\n"
                "now Enter the Value ;:  ")
dis_path = input("Enter the Destination path Where you want to copy the file : " )
fol_name = input("Enter the Destination folder name Where you want to copy the file : " )
os.chdir(or_path)
with open('path.txt', 'w+') as f:
    count = 0;
    for dirpath, dirname, filename in os.walk(or_path):
        if len(dirpath) > 240:
            f.write(dirpath+'\n')
        if len(dirpath) > 255:
            p = Path(dirpath)
            new_p = Path(*p.parts[20:])
            print(new_p)
            try:
                os.mkdir(dis_path +'/'+ fol_name)
            except:
                print("folder done")
            os.chdir(dis_path +'/'+ fol_name)
            os.makedirs(new_p)
            for dir in dirname:
                try:
                    os.chdir(dis_path + '/' + fol_name + '/' +new_p)
                    print(os.getcwd())
                    os.mkdir(dir)
                    print(dir)
                except :
                    print("folder exists")

            for nam in filename:
                 # os.chdir(dirpath)
                 # print(os.listdir(os.getcwd()))
                 # shutil.copyfile(str(nam),dis_path + '/' + fol_name + '/' + str(new_p))
                 os.chdir(dis_path + '/' + fol_name + '/' + str(new_p))
                 soouce = dirpath + '/'+nam
                 des = os.getcwd()
                 try:

                    os.chdir(dis_path + '/' + fol_name + '/' +new_p)
                    print(os.getcwd())
                    os.system("copy " + soouce + " " + des)
                 except:
                    print(os.getcwd())
                    print("file exists or file is opened")

        if len(dirpath) <= 255:
            drive, path = os.path.splitdrive(dirpath)
            for dir in dirname:
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






































# os.chdir(or_path)

# with open('path.txt', 'r') as f, open ('fianl.txt', 'w+') as g:
#         # for line in f :
#         #     if not line in g.read():
#         #         g.write(line)
#         #     else:
#         #         print("hello")
#         for line in f:
#             print(line)
#             try:
#                 os.mkdir(dis_path+ '/' + fol_name)
#
#                 # shutil.copy(line, dis_path + '/'+fol_name)
#             except:
#                 print("there is some issue files are not copided")
#             drr, dirr = os.path.splitdrive(line)
#             final = os.path.join(or_path , dirr)
#             print(final)
#             shutil.copytree(final, dis_path + '/'+fol_name)
#





