import os
import shutil
from copy_static import copy_dir_to_dest
from generators import generate_pages_recursive
from textnode import TextNode


def main():
    CONTENT_DIR = "content"
    TEMPLATE_PATH = "template.html"

    try:
        SRC_DIR = "static"
        DST_DIR = "public"
        if os.path.exists(DST_DIR):
            shutil.rmtree(DST_DIR)
            print(f"Deleted {DST_DIR}")

        copy_dir_to_dest(SRC_DIR, DST_DIR)
        generate_pages_recursive(CONTENT_DIR, TEMPLATE_PATH, DST_DIR)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
