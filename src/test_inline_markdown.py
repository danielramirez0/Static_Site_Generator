import unittest
from inline_markdown import split_nodes_delimiter, TextNode

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_bold_delimiter(self):
        old_nodes = [
            TextNode("This is a **bolded** test", "bold"),
            TextNode("This is another **bold** test", "bold"),
        ]
        delimiter = "**"
        text_type = "bold"
        expected_nodes = [
            TextNode("This is a ", "text"),
            TextNode("bolded", "bold"),
            TextNode(" test", "text"),
            TextNode("This is another ", "text"),
            TextNode("bold", "bold"),
            TextNode(" test", "text")
        ]
        self.assertEqual(split_nodes_delimiter(old_nodes, delimiter, text_type), expected_nodes)

    def test_split_nodes_italic_delimiter(self):
        old_nodes = [
            TextNode("This is *italic* text", "italic"),
            TextNode("This is *another* test with *italic* text", "italic"),
        ]
        delimiter = "*"
        text_type = "italic"
        expected_nodes = [
            TextNode("This is ", "text"),
            TextNode("italic", "italic"),
            TextNode(" text", "text"),
            TextNode("This is ", "text"),
            TextNode("another", "italic"),
            TextNode(" test with ", "text"),
            TextNode("italic", "italic"),
            TextNode(" text", "text")
        ]
        self.assertEqual(split_nodes_delimiter(old_nodes, delimiter, text_type), expected_nodes)

    def test_split_nodes_delimiter_with_unbalanced_delimiter(self):
        old_nodes = [
            TextNode("Bold test with unbalanced** delimiter", "bold"),
        ]
        delimiter = "**"
        text_type = "bold"
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, delimiter, text_type)

if __name__ == "__main__":
    unittest.main()