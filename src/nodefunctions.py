import re
from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code,
        text_type_link,
        text_type_image,
        )

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue                
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

'''def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return sum(list(map(
        lambda x: split_node_by_delimiter(x, delimiter, text_type), old_nodes)),[])

def split_node_by_delimiter(single_node, delimiter, text_type):
    return list(map(
        lambda x, y: TextNode(x, y)
        , single_node.text.split(delimiter,2)
        , [single_node.text_type, text_type, single_node.text_type]))
'''

def extract_markdown_images(text):
    return re.findall( r"!\[(.*?)\]\((.*?)\)" , text)
    
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

'''def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

def split_nodes_image(old_nodes):
    return flatten(list(map(split_single_node_image, old_nodes)))

def split_nodes_link(old_nodes):
    return flatten(list(map(split_single_node_link, old_nodes)))

def split_single_node_image(node):
    images_extract = extract_markdown_images(node.text)
    if images_extract:
        alt, link = zip(*images_extract)
        image_textnode = TextNode(alt[0], text_type_image, link[0])
        text_split = node.text.split(f"![{alt[0]}]({link[0]})", 1)
        text_textnodes = list(map(lambda x: TextNode(x, text_type_text) , text_split)) 
        
        node_chained_list = [
                text_textnodes[0],
                image_textnode,
                flatten(split_single_node_image(text_textnodes[1])),
                ]

        return flatten(node_chained_list)
    else:
        return [node]

def split_single_node_link(node):
    link_extract = extract_markdown_links(node.text)
    if link_extract:
        alt, link = zip(*link_extract)
        link_textnode = TextNode(alt[0], text_type_link, link[0])
        text_split = node.text.split(f"[{alt[0]}]({link[0]})", 1)
        text_textnodes = list(map(lambda x: TextNode(x, text_type_text) , text_split)) 
        
        node_chained_list = [
                text_textnodes[0],
                link_textnode,
                flatten(split_single_node_link(text_textnodes[1])),
                ]

        return flatten(node_chained_list)
    else:
        return [node]'''

def text_to_textnodes(text):
    nodes = [TextNode(text, "text")]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    return nodes
    
