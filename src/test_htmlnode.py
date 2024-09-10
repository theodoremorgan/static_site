import unittest

from htmlnode import HTMLNode

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
