import unittest
from nodefunctions import split_nodes_delimiter
from textnode import TextNode

class TestNodeFunctions(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", "text")
        actual_nodes = split_nodes_delimiter([node], "`", "code")
        expected_nodes = [
                TextNode("This is text with a ", "text"),
                TextNode("code block", "code"),
                TextNode(" word", "text"),
                ]
        self.assertEqual(actual_nodes, expected_nodes)

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bold block** word", "text")
        actual_nodes = split_nodes_delimiter([node], "**", "bold")
        expected_nodes = [
                TextNode("This is text with a ", "text"),
                TextNode("bold block", "bold"),
                TextNode(" word", "text"),
                ]
        self.assertEqual(actual_nodes, expected_nodes)
    
    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is text with a *italic block* word", "text")
        actual_nodes = split_nodes_delimiter([node], "*", "italic")
        expected_nodes = [
                TextNode("This is text with a ", "text"),
                TextNode("italic block", "italic"),
                TextNode(" word", "text"),
                ]
        self.assertEqual(actual_nodes, expected_nodes)

#not totally sure of the expected behaviour here; if italics can keep urls etc.
    def test_split_nodes_delimiter_with_url(self):
        node = TextNode("This is text with *italic* words", "text", "https://www.boot.dev")
        actual_nodes = split_nodes_delimiter([node], "*", "italic")
        expected_nodes = [
                TextNode("This is text with ", "text"),
                TextNode("italic", "italic"),
                TextNode(" words", "text"),
                ]
        self.assertEqual(actual_nodes, expected_nodes)

    def test_split_multiple_nodes(self):
        nodes = [
                TextNode("This is text with a **1st bold block** word", "text"),
                TextNode("This is text with a **2nd bold block** word", "text"),
                TextNode("This is text with a **3rd bold block** word", "text"),
                ]
        actual_nodes = split_nodes_delimiter(nodes, "**", "bold")
        expected_nodes =[
                TextNode("This is text with a ", "text"),
                TextNode("1st bold block", "bold"),
                TextNode(" word", "text"),
                TextNode("This is text with a ", "text"),
                TextNode("2nd bold block", "bold"),
                TextNode(" word", "text"),
                TextNode("This is text with a ", "text"),
                TextNode("3rd bold block", "bold"),
                TextNode(" word", "text"),
                ]
        self.assertEqual(actual_nodes, expected_nodes)

if __name__ == "__main__":
    unittest.main()
