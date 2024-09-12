import unittest

from textnode import TextNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_eq_fail_on_text(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is also a text node", "bold", "https://www.boot.dev")
        self.assertEqual(False, node == node2)
     
    def test_eq_fail_on_text_type(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "italic", "https://www.boot.dev")
        self.assertEqual(False, node == node2)

    def test_eq_fail_on_url(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.boot2.dev")
        self.assertEqual(False, node == node2)

    def text_url_optional(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, "bold")
        self.assertEqual(node.url, None)

from htmlnode import LeafNode

class TestTextNodeToLeafNode(unittest.TestCase):
    def test_text_to_html(self):
        text1 = TextNode("This is some text", "text")
        text2 = TextNode("This is some text", "bold")
        text3 = TextNode("This is some text", "italic")
        text4 = TextNode("This is some text", "code")
        text5 = TextNode("This is some text", "link", "https://www.boot.dev")
        text6 = TextNode("This is some alt text", "image", "https://www.boot.dev/nicepicture")

        self.assertEqual(text_node_to_html_node(text1), LeafNode(None, "This is some text"))
        self.assertEqual(text_node_to_html_node(text2), LeafNode("b", "This is some text"))
        self.assertEqual(text_node_to_html_node(text3), LeafNode("i", "This is some text"))
        self.assertEqual(text_node_to_html_node(text4), LeafNode("code", "This is some text"))
        self.assertEqual(text_node_to_html_node(text5), LeafNode("a", "This is some text", {"href": "https://www.boot.dev"}))
        self.assertEqual(text_node_to_html_node(text6), LeafNode("img", "", {"src": "https://www.boot.dev/nicepicture", "alt": "This is some alt text"}))

    def test_text_to_html_invalid_text_type(self):
        with self.assertRaises(ValueError):
            text = TextNode("This is some text", "this is an invalid type")
            text_node_to_html_node(text)

if __name__ == "__main__":
    unittest.main()
