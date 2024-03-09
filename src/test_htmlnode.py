import unittest
from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_to_html(self):
        # Test case 1: Empty HtmlNode
        node = HtmlNode()
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        # Test case 1: Empty props
        node = HtmlNode()
        self.assertEqual(node.props_to_html(), None)

        # Test case 2: HtmlNode with props
        node = HtmlNode(tag="div", props={"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), 'class=container id=main')

    def test_repr(self):
        # Test case 1: Empty HtmlNode
        node = HtmlNode()
        self.assertEqual(repr(node), "HtmlNode(None, None, None, None)")

        # Test case 2: HtmlNode with tag, value, children, and props
        child = HtmlNode(tag="p", value="This is a paragraph.")
        node = HtmlNode(tag="div", value="Hello, world!", children=[child], props={"class": "container"})
        self.assertEqual(repr(node), "HtmlNode(div, Hello, world!, [HtmlNode(p, This is a paragraph., None, None)], {'class': 'container'})")

if __name__ == '__main__':
    unittest.main()