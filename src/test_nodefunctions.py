import unittest
from nodefunctions import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
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

    def test_extract_markdown_images(self):
        text = "This is text with a image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and a red herring [to boot dev](https://www.boot.dev)"
        expected_images = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        actual_images = extract_markdown_images(text)
        self.assertEqual(actual_images, expected_images)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and a red herring ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        expected_links = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]   
        actual_links = extract_markdown_links(text)
        self.assertEqual(actual_links, expected_links)

    def test_split_nodes_link(self):

        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and a red herring ![rick roll](https://i.imgur.com/aKaOqIh.gif)", "text",)
        actual_new_nodes = split_nodes_link([node])
        expected_new_nodes = [
                TextNode("This is text with a link ", "text"),
                TextNode("to boot dev", "link", "https://www.boot.dev"),
                TextNode(" and ", "text"),
                TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev"),
                TextNode(" and a red herring ![rick roll](https://i.imagur.com/aKa0qIh.gif)", "text",),
                ]
        self.assertEqual(actual_new_nodes, expected_new_nodes)

    def test_split_nodes_image(self): 
        node = TextNode("This is text with a image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and a red herring [to boot dev](https://www.boot.dev)", "text",)
        actual_new_nodes = split_nodes_image([node])
        expected_new_nodes = [
                TextNode("This is text with a image ", "text",),
                TextNode("rick roll", "link", "https://i.imgur.com/aKa0qIh.gif"),
                TextNode(" and ", "text"),
                TextNode("obi wan", "link", "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode("and a red herring [to boot dev](https://www.boot.dev)", "text",),
                ]
        self.assertEqual(actual_new_nodes, expected_new_nodes)


if __name__ == "__main__":
    unittest.main()
