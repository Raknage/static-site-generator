from split_blocks import markdown_to_blocks, block_to_blocktype
from split_nodes import text_to_textnodes

from htmlnode import LeafNode, ParentNode


def markdown_to_html_node(markdown):
    parent_html_node = ParentNode("div", [])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_blocktype(block)
        match block_type:
            case "heading":
                parent_html_node.children.append(block_to_heading(block))
            case "code":
                parent_html_node.children.append(block_to_code(block))
            case "quote":
                parent_html_node.children.append(block_to_quote(block))
            case "unordered_list":
                parent_html_node.children.append(block_to_unordered_list(block))
            case "ordered_list":
                parent_html_node.children.append(block_to_ordered_list(block))
            case "paragraph":
                parent_html_node.children.append(block_to_paragraph(block))
            case _:
                raise ValueError("Invalid blocktype")
    return parent_html_node


def block_to_paragraph(block):
    children = text_to_children(block.strip())
    return ParentNode("p", children)


def block_to_ordered_list(block):
    list_items = [
        ParentNode("li", text_to_children(line.lstrip("1234567890").lstrip(". ")))
        for line in block.split("\n")
    ]
    return ParentNode("ol", list_items)


def block_to_unordered_list(block):
    list_items = [
        ParentNode("li", text_to_children(line.lstrip("* ")))
        for line in block.split("\n")
    ]
    return ParentNode("ul", list_items)


def block_to_quote(block):
    combined_lines = "\n".join(line.strip("> ") for line in block.split("\n"))
    quotes = text_to_children(combined_lines)
    return ParentNode("blockquote", quotes)


def block_to_code(block):
    return ParentNode("pre", [LeafNode("code", block.strip("` \n"))])


def block_to_heading(block):
    count = block.count("#", 0, 6)
    return LeafNode(f"h{count}", block.strip("# "))


def text_to_children(text):
    textnodes = text_to_textnodes(text)
    leafnodes = [node.textnode_to_htmlnode() for node in textnodes]
    return leafnodes
