from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return self.text == other.text and self.text_type == other.text_type and self.url == other.url
        else:
            return False
    
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type},{self.url})"

#function to convert from textnode to html(leaf)node 
def text_node_to_html_node(text_node):
    valid_types = [text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image]
    if text_node.text_type not in valid_types:
        raise ValueError("text_type of the text node must be one of: text, bold, italic, code, link, image"
    )
    match text_node.text_type:
        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case "code":
            return LeafNode("code", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "text":
            return LeafNode(None, text_node.text)
