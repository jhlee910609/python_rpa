from os import listdir, makedirs
from os.path import isdir
import shutil
import os


originDir = "/Volumes/samsung_ssd/img_files/"
outDir = "/Volumes/samsung_ssd/img_files/"
fileList = listdir(originDir)


def getTargetDir(outDir, name_splited):
    if (name_splited[0] != ""):
        return outDir + name_splited[0] + "/"
    else:
        return outDir + name_splited[1] + "/"


def getDir(targetDir):
    if not isdir(targetDir):
        makedirs(targetDir)


for f_name in fileList:
    origin_name = f_name
    name_splited = origin_name.split("_")

    if (len(name_splited) > 1):

        if (name_splited[0] != "."):
            target_dir = getTargetDir(outDir, name_splited)
            getDir(target_dir)
            shutil.copyfile(originDir + f_name, target_dir + f_name)
            os.remove(originDir + f_name)

print("========[ arrangement is completed! ]========")
