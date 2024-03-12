import os
import shutil
from copy_static import copy_dir_to_dest
from generate_page import generate_page
from textnode import TextNode


def main():
    try:
        SRC_DIR = "static"
        DST_DIR = "public"
        if os.path.exists(DST_DIR):
            shutil.rmtree(DST_DIR)
            print(f"Deleted {DST_DIR}")
        copy_dir_to_dest(SRC_DIR, DST_DIR)

        generate_page("content/index.md", "template.html", "public/index.html")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
