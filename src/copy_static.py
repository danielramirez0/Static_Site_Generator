import os
import shutil


def copy_dir_to_dest(src, dest):
    print(f" * {src} -> {dest}")
    if not os.path.exists(dest):
        os.makedirs(dest)
    for item in os.listdir(src):
        if os.path.isfile(os.path.join(src, item)):
            shutil.copy(os.path.join(src, item), os.path.join(dest, item))
        else:
            copy_dir_to_dest(os.path.join(src, item), os.path.join(dest, item))