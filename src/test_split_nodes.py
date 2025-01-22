import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode
from split_nodes import split_nodes_delimiter


class Test_split_nodes(unittest.TestCase):
    def test_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.NORMAL),
            ],
        )

    def test_delimiter_bold_and_italic(self):
        node = TextNode(
            "This is text with a **bolded** and *italic* words", TextType.NORMAL
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded", TextType.BOLD),
                TextNode(" and *italic* words", TextType.NORMAL),
            ],
        )
        self.assertEqual(
            split_nodes_delimiter(new_nodes, "*", TextType.ITALIC),
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded", TextType.BOLD),
                TextNode(" and ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" words", TextType.NORMAL),
            ],
        )

    def test_delimiter_italic(self):
        node = TextNode("This is text with a *italic* word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.NORMAL),
            ],
        )

        with self.assertRaises(ValueError):
            node = TextNode("This is text with a *italic word", TextType.NORMAL)
            new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)


if __name__ == "__main__":
    unittest.main()
