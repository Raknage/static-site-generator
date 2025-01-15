import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
