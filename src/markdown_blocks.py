from htmlnode import ParentNode
from inline_markdown import text_to_textnodes

block_types = {
    "heading": {"name": "heading", "prefix": "# ", "html_tag": "h"},
    "unordered_list": {"name": "unordered_list", "prefix": "- ", "html_tag": "ul"},
    "ordered_list": {"name": "ordered_list", "prefix": "1. ", "html_tag": "ol"},
    "code": {"name": "code", "prefix": "```", "html_tag": "code"},
    "quote": {"name": "quote", "prefix": "> ", "html_tag": "blockquote"},
    "paragraph": {"name": "paragraph", "prefix": "", "html_tag": "p"},
}


def markdown_to_blocks(markdown):
    return [block.strip() for block in markdown.split("\n\n") if block]


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = [block_to_html_node(block) for block in blocks]
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type["name"] == "heading":
        return heading_to_html_node(block)
    if block_type["name"] == "paragraph":
        return paragraph_to_html_node(block)
    if block_type["name"] == "code":
        return code_to_html_node(block)
    if block_type["name"] == "ordered_list":
        return olist_to_html_node(block)
    if block_type["name"] == "unordered_list":
        return ulist_to_html_node(block)
    if block_type["name"] == "quote":
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")


def block_to_block_type(block):
    lines = block.split("\n")
    if (
        lines[0].startswith("# ")
        or lines[0].startswith("## ")
        or lines[0].startswith("### ")
        or lines[0].startswith("#### ")
        or lines[0].startswith("##### ")
        or lines[0].startswith("###### ")
    ):
        return block_types["heading"]
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_types["code"]
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_types["paragraph"]["name"]
        return block_types["quote"]
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_types["paragraph"]["name"]
        return block_types["unordered_list"]
    if block[0].isdigit() and block[1] == ".":
        for line in lines:
            if not line[0].isdigit() and line[1] == ".":
                return block_types["paragraph"]
        return block_types["ordered_list"]
    return block_types["paragraph"]


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node.text_node_to_html_node() for text_node in text_nodes]


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 > len(block):
        raise ValueError("Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    code = ParentNode("code", text_to_children(block[4:-3]))
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    html_items = [ParentNode("li", text_to_children(item[3:])) for item in block.split("\n")]
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    html_items = [ParentNode("li", text_to_children(item[2:])) for item in block.split("\n")]
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = [ParentNode("p", text_to_children(line[2:]), None) for line in block.split("\n")]
    return ParentNode("blockquote", lines)
