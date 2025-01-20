import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.LINK, "www.url.com")
        node2 = TextNode("This is a text node", TextType.LINK, "www.url.com")
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("", TextType.CODE)
        node2 = TextNode("", TextType.CODE)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("gg", TextType.LINK, "www.test.com")
        node2 = TextNode("gg", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_not_eq3(self):
        node = TextNode("This is a text", TextType.CODE)
        node2 = TextNode("This is a different text", TextType.CODE)
        self.assertNotEqual(node, node2)


class Test_textnode_to_htmlnode(unittest.TestCase):
    def test_textnode_to_htmlnode(self):
        text = "This is some text!"
        self.assertEqual(
            TextNode(text, TextType.NORMAL).textnode_to_htmlnode().to_html(),
            LeafNode(None, text).to_html(),
        )
        self.assertEqual(
            TextNode(text, TextType.BOLD).textnode_to_htmlnode().to_html(),
            LeafNode("b", text).to_html(),
        )
        self.assertEqual(
            TextNode(text, TextType.ITALIC).textnode_to_htmlnode().to_html(),
            LeafNode("i", text).to_html(),
        )
        self.assertEqual(
            TextNode(text, TextType.CODE).textnode_to_htmlnode().to_html(),
            LeafNode("code", text).to_html(),
        )
        self.assertEqual(
            TextNode(text, TextType.LINK, "http://www.raknage.com")
            .textnode_to_htmlnode()
            .to_html(),
            LeafNode("a", text, {"href": "http://www.raknage.com"}).to_html(),
        )
        self.assertEqual(
            TextNode(text, TextType.IMAGE, "http://www.raknage.com")
            .textnode_to_htmlnode()
            .to_html(),
            LeafNode(
                "img", "", {"src": "http://www.raknage.com", "alt": text}
            ).to_html(),
        )


if __name__ == "__main__":
    unittest.main()
