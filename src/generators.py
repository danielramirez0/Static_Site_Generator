import os
from extract_title import extract_title
from markdown_blocks import markdown_to_html_node as md_to_html

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    root = dir_path_content
    items = os.listdir(root)
    for item in items:
        if os.path.isfile(os.path.join(root, item)) and item.endswith(".md"):
            from_path = os.path.join(root, item)
            dest_path = os.path.join(dest_dir_path, f"{os.path.splitext(item)[0]}.html")
            generate_page(from_path, template_path, dest_path)
            continue
        next_dest_dir_path = os.path.join(dest_dir_path, item)
        os.mkdir(next_dest_dir_path)
        generate_pages_recursive(os.path.join(root, item), template_path, dest_dir_path + "/" + item)



    # for root, dirs, files in os.walk(dir_path_content):
    #     print(f"root: {root}, dirs: {dirs}, files: {files}")
    #     for file in files:
    #         print(os.path.isfile(file) and file.endswith(".md"))
    #         if os.path.isfile(file) and file.endswith(".md"):
    #             from_path = os.path.join(root, file)
    #             dest_path = os.path.join(dest_dir_path, root, file)
    #             print(f"Generating page from {from_path} using {template_path} to {dest_path}")
    #     for directory in dirs:
    #         generate_pages_recursive(os.path.join(root, directory), template_path, dest_dir_path)



    # for root, dirs, files in os.walk(dir_path_content):
    #     for file in files:
    #         if file.endswith(".md"):
    #             from_path = os.path.join(root, file)
    #             rel_path = os.path.relpath(from_path, dir_path_content)
    #             rel_path = os.path.splitext(rel_path)[0]
    #             rel_path = rel_path.replace("\\", "/")
    #             rel_path = rel_path + ".html"
    #             dest_path = os.path.join(dest_dir_path, rel_path)
    #             generate_page(from_path, template_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} using {template_path} to {dest_path}")
    with open(from_path, "r") as f:
        content = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    node = md_to_html(content)
    html = node.to_html()
    title = extract_title(content)
    with open(dest_path, "w") as f:
        f.write(template.replace("{{ Content }}", html).replace("{{ Title }}", title))