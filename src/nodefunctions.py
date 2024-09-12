from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return sum(list(map(
        lambda x: split_node_by_delimiter(x, delimiter, text_type), old_nodes)),[])

def split_node_by_delimiter(single_node, delimiter, text_type):
    return list(map(
        lambda x, y: TextNode(x, y)
        , single_node.text.split(delimiter,2)
        , [single_node.text_type, text_type, single_node.text_type]))

