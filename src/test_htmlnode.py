import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = repr(HTMLNode("h1", "Text", [], {"href": "www.raknage.com"}))
        node2 = 'HTMLNode(h1, Text, [],  href="www.raknage.com")'
        self.assertEqual(node, node2)

    def test_values(self):
        node = HTMLNode("div", "This is a value")

        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "This is a value")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        node = HTMLNode(
            None,
            None,
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        node2 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), node2)


if __name__ == "__main__":
    unittest.main()
