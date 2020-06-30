import os
import setting
from pathlib import Path
import shutil

def organize(project, scanPath):
    for dir in range(len(setting.SUB_FOLDER)):
        if setting.SUB_FOLDER[dir] == "":
            dirStructure(setting.PATH, setting.ROOT_FOLDER, project, setting.FOLDER[dir])
        else:
            for sdir in range(len(setting.SUB_FOLDER[dir])):
                dirStructure(setting.PATH, setting.ROOT_FOLDER, project, setting.FOLDER[dir], setting.SUB_FOLDER[dir][sdir])

    organizeFile(scanPath, project)

def dirStructure(*args):
    FPATH = str(args[0]) + "/" + str(args[1])
    createDirectory(FPATH)
    FPATH = str(FPATH) + "/" + str(args[2])
    createDirectory(FPATH)
    FPATH = str(FPATH) + "/" + str(args[3])
    createDirectory(FPATH)

    if len(args) > 4:
        FPATH = str(FPATH) + "/" + str(args[4])
        createDirectory(FPATH)

def createDirectory(dirPath):
    if not os.path.exists(dirPath):
        os.makedirs(dirPath, exist_ok=True)

def organizeFile(scanPath, project):
    if os.path.exists(scanPath):
        FILE_FORMATS = {fformat: directory 
                        for directory, file_formats in setting.DIRECTORIES.items() 
                        for fformat in file_formats}

        FPATH = setting.PATH + "/" + setting.ROOT_FOLDER + "/" + project + "/Assets"

        for content in os.scandir(scanPath):
            if content.is_file():
                file_path = Path(content)
                file_format = file_path.suffix.lower()
                if file_format in FILE_FORMATS:
                    directory = Path(FPATH + "/" + FILE_FORMATS[file_format] + "/")
                    directory.mkdir(exist_ok=True)
                    shutil.copy(file_path, directory)

def createFolder(filepath):
    if os.path.exists(filepath):
        os.makedirs(filepath)

if __name__ == "__main__":
    organize("BOT", "SCAN_ME/")