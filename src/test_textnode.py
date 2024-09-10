import unittest

from textnode import TextNode


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

if __name__ == "__main__":
    unittest.main()
