import re
from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        if node.text_type != text_type:
            nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid Markdown, {delimiter} delimiter is not balanced")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], "text"))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        nodes.extend(split_nodes)
    return nodes

def extract_markdown_images(text):
    images = []
    for match in re.finditer(r"!\[(.*?)\]\((.*?)\)", text):
        images.append(TextNode(match.group(1), "image", match.group(2)))
    return images

def extract_markdown_links(text):
    links = []
    for match in re.finditer(r"\[(.*?)\]\((.*?)\)", text):
        links.append(TextNode(match.group(1), "link", match.group(2)))
    return links
