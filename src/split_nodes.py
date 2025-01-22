from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        nodes = node.text.split(delimiter)
        if node.text.count(delimiter) % 2 != 0:
            raise ValueError("Not valid markdown syntax")

        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        elif len(nodes) == 3:
            new_nodes.append(TextNode(nodes[0], TextType.NORMAL))
            new_nodes.append(TextNode(nodes[1], text_type))
            new_nodes.append(TextNode(nodes[2], TextType.NORMAL))
        elif node.text_type == TextType.NORMAL:
            new_nodes.append(node)

    return new_nodes
