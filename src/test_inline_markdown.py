import unittest
from inline_markdown import (
        split_nodes_delimiter, 
        extract_markdown_images,
        extract_markdown_links, 
        split_nodes_image, 
        split_nodes_link, 
        text_to_textnodes,
        )
from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code,
        text_type_link,
        text_type_image,
        )

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        actual_nodes = split_nodes_delimiter([node], "`", text_type_code)
        expected_nodes = [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
                ]
        self.assertEqual(actual_nodes, expected_nodes)

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bold block** word", text_type_text)
        actual_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected_nodes = [
                TextNode("This is text with a ", text_type_text),
                TextNode("bold block", text_type_bold),
                TextNode(" word", text_type_text),
                ]
        self.assertEqual(actual_nodes, expected_nodes)
    
    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is text with a *italic block* word", text_type_text)
        actual_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        expected_nodes = [
                TextNode("This is text with a ", text_type_text),
                TextNode("italic block", text_type_italic),
                TextNode(" word", text_type_text),
                ]
        self.assertEqual(actual_nodes, expected_nodes)
    '''
    def test_split_nodes_delimiter_italic_ignore_bold(self):
        node = TextNode("This is text with an *italic block* and a **bold block**", text_type_text)
        actual_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        expected_nodes = [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic block", text_type_italic),
                TextNode(" and a **bold block**", text_type_text),
                ]
        self.assertEqual(actual_nodes, expected_nodes)
    '''
    '''def test_split_nodes_delimiter_italic_ignore_bold_before(self):
        node = TextNode("This is text with a **bold block** then an *italic block*.", text_type_text)
        actual_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        expected_nodes = [
                TextNode("This is text with a **bold block** then an ", text_type_text),
                TextNode("italic block", text_type_italic),
                TextNode(".", text_type_text),
                ]
        self.assertEqual(actual_nodes, expected_nodes)
    '''

    #not totally sure of the expected behaviour here; if italics can keep urls etc.
    def test_split_nodes_delimiter_with_url(self):
        node = TextNode("This is text with *italic* words", text_type_text, "https://www.boot.dev")
        actual_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        expected_nodes = [
                TextNode("This is text with ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" words", text_type_text),
                ]
        self.assertEqual(actual_nodes, expected_nodes)

    def test_split_multiple_nodes(self):
        nodes = [
                TextNode("This is text with a **1st bold block** word", text_type_text),
                TextNode("This is text with a **2nd bold block** word", text_type_text),
                TextNode("This is text with a **3rd bold block** word", text_type_text),
                ]
        actual_nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
        expected_nodes =[
                TextNode("This is text with a ", text_type_text),
                TextNode("1st bold block", text_type_bold),
                TextNode(" word", text_type_text),
                TextNode("This is text with a ", text_type_text),
                TextNode("2nd bold block", text_type_bold),
                TextNode(" word", text_type_text),
                TextNode("This is text with a ", text_type_text),
                TextNode("3rd bold block", text_type_bold),
                TextNode(" word", text_type_text),
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

        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and a red herring ![rick roll](https://i.imgur.com/aKa0qIh.gif)", "text",)
        actual_new_nodes = split_nodes_link([node])
        expected_new_nodes = [
                TextNode("This is text with a link ", "text"),
                TextNode("to boot dev", "link", "https://www.boot.dev"),
                TextNode(" and ", "text"),
                TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev"),
                TextNode(" and a red herring ![rick roll](https://i.imgur.com/aKa0qIh.gif)", "text",),
                ]
        self.assertEqual(actual_new_nodes, expected_new_nodes)

    def test_split_nodes_image(self): 
        node = TextNode("This is text with a image ![rick roll](https://i.imgur.com/aKa0qIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and a red herring [to boot dev](https://www.boot.dev)", text_type_text,)
        actual_new_nodes = split_nodes_image([node])
        expected_new_nodes = [
                TextNode("This is text with a image ", text_type_text,),
                TextNode("rick roll", text_type_image, "https://i.imgur.com/aKa0qIh.gif"),
                TextNode(" and ", text_type_text),
                TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a red herring [to boot dev](https://www.boot.dev)", text_type_text,),
                ]
        self.assertEqual(actual_new_nodes, expected_new_nodes)

    def test_split_image(self):
        node = TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
                text_type_text,
                )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
                [
                    TextNode("This is text with an ", text_type_text),
                    TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                ],
                new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
                "![image](https://www.example.com/image.png)",
                text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", text_type_image, "https://www.example.com/image.png"),
            ],
            new_nodes,
        )
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode("another link", text_type_link, "https://blog.boot.dev"),
                TextNode(" with text that follows", text_type_text),
            ],
            new_nodes,
            )

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        actual_textnodes = text_to_textnodes(text)
        expected_textnodes = [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
                ]
        self.assertEqual(actual_textnodes, expected_textnodes)

if __name__ == "__main__":
    unittest.main()
