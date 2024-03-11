import unittest
from markdown_blocks import block_to_block_type, markdown_to_blocks


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "This is a sample\n\nmarkdown\n\nwith multiple blocks"
        expected_blocks = ["This is a sample", "markdown", "with multiple blocks"]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_to_blocks_empty(self):
        markdown = ""
        expected_blocks = []
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_to_blocks_single_block(self):
        markdown = "This is a single block"
        expected_blocks = ["This is a single block"]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_to_blocks_multiple_empty_blocks(self):
        markdown = "\n\n\n"
        expected_blocks = [""]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_to_blocks_with_multiple_text_types(self):
        markdown = "# This is a sample\n\n**markdown**\n\nwith multiple blocks"
        expected_blocks = ["# This is a sample", "**markdown**", "with multiple blocks"]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_to_blocks_with_all_text_types(self):
        markdown = "# Heading 1\n\nThis is a paragraph with **bold** and *italic* text.\n\n## Heading 2\n\nHere is an unordered list:\n- Item 1\n- Item 2\n- Item 3\n\n### Heading 3\n\nThis is a code block:\n\n```code = True```"
        expected_blocks = [
            "# Heading 1",
            "This is a paragraph with **bold** and *italic* text.",
            "## Heading 2",
            "Here is an unordered list:\n- Item 1\n- Item 2\n- Item 3",
            "### Heading 3",
            "This is a code block:",
            "```code = True```",
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_block_to_block_type_ordered_list(self):
        block = "1. This is an ordered list item"
        expected_block_type = "ordered_list"
        self.assertEqual(block_to_block_type(block), expected_block_type)

    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        expected_block_type = "heading1"
        self.assertEqual(block_to_block_type(block), expected_block_type)

    def test_block_to_block_type_paragraph(self):
        block = "This is a paragraph"
        expected_block_type = "paragraph"
        self.assertEqual(block_to_block_type(block), expected_block_type)

    def test_block_to_block_type_code_block(self):
        block = "```python\nprint('Hello, World!')\n```"
        expected_block_type = "code"
        self.assertEqual(block_to_block_type(block), expected_block_type)

    def test_block_to_block_type_quote(self):
        block = "> This is a quote"
        expected_block_type = "quote"
        self.assertEqual(block_to_block_type(block), expected_block_type)


if __name__ == "__main__":
    unittest.main()
