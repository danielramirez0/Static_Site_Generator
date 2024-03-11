import unittest
from htmlnode import HtmlNode, LeafNode, ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_to_html(self):
        # Test case 1: Empty HtmlNode
        node = HtmlNode()
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        # Test case 1: Empty props
        node = HtmlNode()
        self.assertEqual(node.props_to_html(), "")

        # Test case 2: HtmlNode with props
        node = HtmlNode(tag="div", props={"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), "class=container id=main")

    def test_repr(self):
        # Test case 1: Empty HtmlNode
        node = HtmlNode()
        self.assertEqual(repr(node), "HtmlNode(None, None, None, None)")

        # Test case 2: HtmlNode with tag, value, children, and props
        child = HtmlNode(tag="p", value="This is a paragraph.")
        node = HtmlNode(
            tag="div",
            value="Hello, world!",
            children=[child],
            props={"class": "container"},
        )
        self.assertEqual(
            repr(node),
            "HtmlNode(div, Hello, world!, [HtmlNode(p, This is a paragraph., None, None)], {'class': 'container'})",
        )


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        # Test case 1: Empty LeafNode
        node = LeafNode(None, None)
        self.assertRaises(ValueError, node.to_html)

        # Test case 2: LeafNode with value only
        node = LeafNode(None, value="Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

        # Test case 3: LeafNode with tag and value
        node = LeafNode(tag="p", value="This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")

        # Test case 4: LeafNode with tag, value, and props
        node = LeafNode(
            tag="div", value="Hello, world!", props={"class": "container", "id": "main"}
        )
        self.assertEqual(
            node.to_html(), "<div class=container id=main>Hello, world!</div>"
        )


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        # Test case 1: Empty ParentNode
        node = ParentNode(None, [])
        self.assertRaises(ValueError, node.to_html)

        # Test case 2: ParentNode with tag and empty children
        node = ParentNode("div", [])
        self.assertRaises(ValueError, node.to_html)

        # Test case 3: ParentNode with tag and children
        child1 = LeafNode("p", "This is paragraph 1.")
        child2 = LeafNode("p", "This is paragraph 2.")
        node = ParentNode("div", [child1, child2])
        self.assertEqual(
            node.to_html(),
            "<div><p>This is paragraph 1.</p><p>This is paragraph 2.</p></div>",
        )

        # Test case 4: ParentNode with tag, children, and props
        child = LeafNode("p", "This is a paragraph.")
        node = ParentNode("div", [child], {"class": "container", "id": "main"})
        self.assertEqual(
            node.to_html(),
            "<div class=container id=main><p>This is a paragraph.</p></div>",
        )

        # Test case 5: ParentNode with nested ParentNode as a child
        child1 = LeafNode("p", "This is paragraph 1.")
        child2 = LeafNode("p", "This is paragraph 2.")
        nested_node = ParentNode("div", [child1, child2])
        main_node = ParentNode("div", [nested_node])
        self.assertEqual(
            main_node.to_html(),
            "<div><div><p>This is paragraph 1.</p><p>This is paragraph 2.</p></div></div>",
        )


if __name__ == "__main__":
    unittest.main()
