block_types = {
    "heading1": {"name": "heading1", "prefix": "# "},
    "heading2": {"name": "heading2", "prefix": "## "},
    "heading3": {"name": "heading3", "prefix": "### "},
    "heading4": {"name": "heading4", "prefix": "#### "},
    "heading5": {"name": "heading5", "prefix": "##### "},
    "heading6": {"name": "heading6", "prefix": "###### "},
    "unordered_list": {"name": "unordered_list", "prefix": "- "},
    "ordered_list": {"name": "ordered_list", "prefix": "1. "},
    "code": {"name": "code", "prefix": "```"},
    "quote": {"name": "quote", "prefix": "> "},
    "paragraph": {"name": "paragraph", "prefix": ""},
}


def markdown_to_blocks(markdown):
    return [block.strip() for block in markdown.split("\n\n") if block]


def block_to_block_type(block):
    if block[0].isdigit() and block[1] == ".":
        return "ordered_list"
    for block_type in block_types.values():
        if block.startswith(block_type["prefix"]):
            return block_type["name"]
