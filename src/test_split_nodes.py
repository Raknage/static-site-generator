import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode
from split_nodes import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)


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

    def test_delimiter_code_times_two(self):
        node = TextNode(
            "An elaborate pantheon of deities (the `Valar` and `Maiar`)",
            TextType.NORMAL,
            None,
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            new_nodes,
            [
                TextNode("An elaborate pantheon of deities (the ", TextType.NORMAL),
                TextNode("Valar", TextType.CODE),
                TextNode(" and ", TextType.NORMAL),
                TextNode("Maiar", TextType.CODE),
                TextNode(")", TextType.NORMAL),
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


class Test_Extract_Markdown(unittest.TestCase):
    def test_extract_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_images(text),
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )

    def test_extract_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(
            extract_markdown_links(text),
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
        )


class Test_Split_Images_And_Links(unittest.TestCase):
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with ![an image](https://www.link.to/image.png) and ![another image](https://www.link.to/anotherimage.jpg) also text in the end",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.NORMAL),
                TextNode("an image", TextType.IMAGE, "https://www.link.to/image.png"),
                TextNode(" and ", TextType.NORMAL),
                TextNode(
                    "another image",
                    TextType.IMAGE,
                    "https://www.link.to/anotherimage.jpg",
                ),
                TextNode(" also text in the end", TextType.NORMAL),
            ],
        )
        self.assertEqual(
            split_nodes_image(
                [
                    TextNode(
                        "This is **text** with ![an image](https://www.link.to/image.png)",
                        TextType.NORMAL,
                    )
                ]
            ),
            [
                TextNode("This is **text** with ", TextType.NORMAL),
                TextNode("an image", TextType.IMAGE, "https://www.link.to/image.png"),
            ],
        )

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a link ", TextType.NORMAL),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.NORMAL),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
        )

    def test_text_to_textnodes(self):

        self.assertEqual(
            text_to_textnodes(
                "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
            ),
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.NORMAL),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
