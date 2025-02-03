import unittest

from split_blocks import markdown_to_blocks


class Test_(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """      # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.         





* This is the first list item in a list block
* This is a list item
* This is another list item"""
        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
            ],
        )
