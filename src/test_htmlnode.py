import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class HTMLNodeUnitTest(unittest.TestCase):

    def test_init_defaults(self):
        empty = HTMLNode()
        self.assertEqual(empty.tag, None)
        self.assertEqual(empty.value, None)
        self.assertEqual(empty.children, None)
        self.assertEqual(empty.props, None)

    def test_init_child_link(self):
        child_link_props = {"href": "https://www.google.com"}
        child_link = HTMLNode("a", "This is a child link in the paragraph", None, child_link_props)
        testnode = HTMLNode("p", "This is a paragraph", [child_link])
        self.assertEqual(testnode.tag, "p")
        self.assertEqual(testnode.value, "This is a paragraph")
        self.assertEqual(testnode.children, [HTMLNode("a", "This is a child link in the paragraph", None, {"href": "https://www.google.com"})])
        self.assertEqual(testnode.props, None)

    def test_props_to_html(self):
        child_link_props = {"href": "https://www.google.com",
                "target": "_blank",}
        testnode = HTMLNode("a", "This is a link node", None, child_link_props)
        expectedstring = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(testnode.props_to_html(),expectedstring)

    def test_leafnode_to_html(self):
        leaf1 = LeafNode("p", "This is a paragraph of text.")
        leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        html1 = leaf1.to_html()
        html2 = leaf2.to_html()

        self.assertEqual(html1, "<p>This is a paragraph of text.</p>")
        self.assertEqual(html2, "<a href=\"https://www.google.com\">Click me!</a>")

    def test_leafnode_to_html_no_tag(self):
        leaf1 = LeafNode("", "This is a paragraph of text.")
        leaf2 = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual("This is a paragraph of text.", leaf1.to_html())
        self.assertEqual("This is a paragraph of text.", leaf2.to_html())

    def test_parentnode_to_html(self):
        parent1 = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
        )
        parent2 = ParentNode(
                "p",
                [
                    ParentNode("p",
                        [
                            LeafNode("b", "Bold text"),
                            LeafNode(None, "Normal text"),
                            LeafNode("i", "italic text"),
                            LeafNode(None, "Normal text"),
                            ]
                        ),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                    ]
                )
        self.assertEqual(parent1.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        self.assertEqual(parent2.to_html(), "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>Normal text<i>italic text</i>Normal text</p>")
    def test_parentnode_to_html_enforce_children(self):
        with self.assertRaises(ValueError):
            parent = ParentNode("p", [], {})

if __name__ == "__main__":
    unittest.main()
