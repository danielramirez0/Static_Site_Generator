import unittest
from inline_markdown import split_nodes_delimiter, TextNode, extract_markdown_images, extract_markdown_links

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
    
    def test_extract_markdown_images(self):
        text = "This is a ![test](test.png) with an image"
        expected_images = [TextNode("test", "image", "test.png")]
        self.assertEqual(extract_markdown_images(text), expected_images)

        multiple_images_text = "This is a ![test](test.png) with an image and another ![image](image.png)"
        expected_images = [TextNode("test", "image", "test.png"), TextNode("image", "image", "image.png")]
        self.assertEqual(extract_markdown_images(multiple_images_text), expected_images)
    
    def test_extract_markdown_links(self):
        text = "This is a [test](https://test.com) with a link"
        expected_links = [TextNode("test", "link", "https://test.com")]
        self.assertEqual(extract_markdown_links(text), expected_links)

        multiple_links_text = "This is a [test](https://test.com) with a link and another [link](https://link.com)"
        expected_links = [TextNode("test", "link", "https://test.com"), TextNode("link", "link", "https://link.com")]
        self.assertEqual(extract_markdown_links(multiple_links_text), expected_links)

if __name__ == "__main__":
    unittest.main()