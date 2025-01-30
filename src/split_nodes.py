from textnode import TextNode, TextType
import re


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


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        new_nodes = recursive_image_nodes(node.text, images, new_nodes)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        new_nodes = recursive_link_nodes(node.text, links, new_nodes)
    return new_nodes


def recursive_link_nodes(text, links, new_nodes, n=0):
    if not text:
        return new_nodes
    txt_nodes = text.split(f"[{links[n][0]}]({links[n][1]})", 1)
    new_nodes.append(TextNode(txt_nodes[0], TextType.NORMAL))
    new_nodes.append(TextNode(links[n][0], TextType.LINK, links[n][1]))
    new_nodes = recursive_link_nodes(txt_nodes[1], links, new_nodes, n + 1)
    return new_nodes


def recursive_image_nodes(text, images, new_nodes, n=0):
    if not text:
        return new_nodes
    txt_nodes = text.split(f"![{images[n][0]}]({images[n][1]})", 1)
    new_nodes.append(TextNode(txt_nodes[0], TextType.NORMAL))
    new_nodes.append(TextNode(images[n][0], TextType.IMAGE, images[n][1]))
    new_nodes = recursive_image_nodes(txt_nodes[1], images, new_nodes, n + 1)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
