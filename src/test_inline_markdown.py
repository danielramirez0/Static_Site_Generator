import unittest
from inline_markdown import split_nodes_delimiter, TextNode, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link

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
        expected_images = [("test", "test.png")]
        self.assertEqual(extract_markdown_images(text), expected_images)

        multiple_images_text = "This is a ![test](test.png) with an image and another ![image](image.png)"
        expected_images = [("test", "test.png"), ("image", "image.png")]
        self.assertEqual(extract_markdown_images(multiple_images_text), expected_images)
    
    def test_extract_markdown_links(self):
        text = "This is a [test](https://test.com) with a link"
        expected_links = [("test", "https://test.com")]
        self.assertEqual(extract_markdown_links(text), expected_links)

        multiple_links_text = "This is a [test](https://test.com) with a link and another [link](https://link.com)"
        expected_links = [("test", "https://test.com"), ("link", "https://link.com")]
        self.assertEqual(extract_markdown_links(multiple_links_text), expected_links)

    def test_split_nodes_image(self):
        old_nodes = [
            TextNode("This is a ![test](test.png) with an image", "text"),
            TextNode("This is another ![image](image.png)", "text"),
        ]
        expected_nodes = [
            TextNode("This is a ", "text"),
            TextNode("test", "image", "test.png"),
            TextNode(" with an image", "text"),
            TextNode("This is another ", "text"),
            TextNode("image", "image", "image.png"),
        ]
        self.assertEqual(split_nodes_image(old_nodes), expected_nodes)

        single_node = [
            TextNode("This is a ![test](test.png) with an image", "text"),
        ]
        expected_nodes = [
            TextNode("This is a ", "text"),
            TextNode("test", "image", "test.png"),
            TextNode(" with an image", "text"),
        ]
        self.assertEqual(split_nodes_image(single_node), expected_nodes)

        multiple_images_node = [
            TextNode("This is a ![test](test.png) with an image and another ![image](image.png)", "text"),
        ]
        expected_nodes = [
            TextNode("This is a ", "text"),
            TextNode("test", "image", "test.png"),
            TextNode(" with an image and another ", "text"),
            TextNode("image", "image", "image.png"),
        ]
        self.assertEqual(split_nodes_image(multiple_images_node), expected_nodes)

        no_image_node = [
            TextNode("This is a text without an image", "text"),
        ]
        expected_nodes = [
            TextNode("This is a text without an image", "text"),
        ]
        self.assertEqual(split_nodes_image(no_image_node), expected_nodes)

    def test_split_nodes_link(self):
        old_nodes = [
            TextNode("This is a [test](https://test.com) with a link", "text"),
            TextNode("This is another [link](https://link.com)", "text"),
        ]
        expected_nodes = [
            TextNode("This is a ", "text"),
            TextNode("test", "link", "https://test.com"),
            TextNode(" with a link", "text"),
            TextNode("This is another ", "text"),
            TextNode("link", "link", "https://link.com"),
        ]
        self.assertEqual(split_nodes_link(old_nodes), expected_nodes)

        single_node = [
            TextNode("This is a [test](https://test.com) with a link", "text"),
        ]
        expected_nodes = [
            TextNode("This is a ", "text"),
            TextNode("test", "link", "https://test.com"),
            TextNode(" with a link", "text"),
        ]
        self.assertEqual(split_nodes_link(single_node), expected_nodes)

        multiple_links_node = [
            TextNode("This is a [test](https://test.com) with a link and another [link](https://link.com)", "text"),
        ]
        expected_nodes = [
            TextNode("This is a ", "text"),
            TextNode("test", "link", "https://test.com"),
            TextNode(" with a link and another ", "text"),
            TextNode("link", "link", "https://link.com"),
        ]
        self.assertEqual(split_nodes_link(multiple_links_node), expected_nodes)

        no_link_node = [
            TextNode("This is a text without a link", "text"),
        ]
        expected_nodes = [
            TextNode("This is a text without a link", "text"),
        ]
        self.assertEqual(split_nodes_link(no_link_node), expected_nodes)


if __name__ == "__main__":
    unittest.main()