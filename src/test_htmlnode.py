import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(
            node2.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        self.assertEqual(
            ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            ).to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

        self.assertEqual(
            ParentNode(
                "p",
                [LeafNode("b", "Bold text")],
                {"style": "color"},
            ).to_html(),
            '<p style="color"><b>Bold text</b></p>',
        )

        with self.assertRaises(ValueError):
            ParentNode("div", [ParentNode("b", [], None)]).to_html()

        with self.assertRaises(ValueError):
            ParentNode("div", [], None).to_html()


if __name__ == "__main__":
    unittest.main()
