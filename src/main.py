import os
import shutil
from copy_static import copy_dir_to_dest
from textnode import TextNode


def main():
    SRC_DIR = "static"
    DST_DIR = "public"
    if os.path.exists(DST_DIR):
        shutil.rmtree(DST_DIR)
        print(f"Deleted {DST_DIR}")
    copy_dir_to_dest(SRC_DIR, DST_DIR)


if __name__ == "__main__":
    main()
