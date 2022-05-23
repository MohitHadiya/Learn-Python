import os

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


def file_read(tmp, internal_file, fro):
    file_path = tmp + "/" + internal_file
    f = open(file_path, "r")
    if fro == 'base':
        print(PIPE + internal_file)
    else:
        print(PIPE + SPACE_PREFIX + ELBOW + internal_file)
    line = f.readline()
    while line:
        if "class " in line or "def " in line:
            print(PIPE + SPACE_PREFIX + ELBOW + line)
        line = f.readline()
    f.close()


def folder_read(path, file, fo):
    if not file == "__pycache__":
        if fo == 'base':
            print(PIPE + file)
        else:
            print(PIPE + SPACE_PREFIX + ELBOW + file)
        os.chdir(path+"/"+file)
        tmp = path+"/"+file
        sorted_files = os.listdir()
        sorted_files.sort()
        for internal_file in sorted_files:
            if os.path.isfile(tmp + "/" + internal_file):
                if internal_file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                    print(PIPE + SPACE_PREFIX + PIPE + SPACE_PREFIX + ELBOW + internal_file)
                else:
                    fro = 'abc'
                    file_read(tmp, internal_file, fro)
            else:
                fo = 'xyz'
                folder_read(tmp, internal_file, fo)


path = "/home/fims12/workspace/odoo_11/custom_addons/fims_login_background_and_styles"
os.chdir(path)
sorted_lst = os.listdir()
sorted_lst.sort()
for file in sorted_lst:
    if os.path.isfile(path+"/"+file):
        fro = 'base'
        file_read(path, file, fro)
    else:
        if not file == "__pycache__":
            fo = 'base'
            folder_read(path, file, fo)
