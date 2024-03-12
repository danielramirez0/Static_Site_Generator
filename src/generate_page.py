from extract_title import extract_title
from markdown_blocks import markdown_to_html_node as md_to_html

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} using {template_path} to {dest_path}")
    with open(from_path, "r") as f:
        content = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    node = md_to_html(content)
    print(node)
    # html = node.to_html()
    title = extract_title(content)
    print(title)
    # print(template.replace("{{Content}}", html).replace("{{Title}}", title))
    # with open(dest_path, "w") as f:
    #     f.write(template.replace("{{Content}}", html).replace("{{Title}}", title))

    