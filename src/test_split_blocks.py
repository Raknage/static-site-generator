import unittest

from split_blocks import markdown_to_blocks, block_to_blocktype


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

    def test_block_to_blocktype(self):
        header = "###### this is a header"
        code = """```this is\ncode```"""
        quote = """> this\n> is\n> a\n> quote"""
        u_list = """* list item 1\n* list item 2\n- list item 3"""
        o_list = """1. list item 1\n1. list item 2\n3. list item 3"""
        paragraph = "this is just a\nnormal paragraph"

        self.assertEqual(block_to_blocktype(header), "heading")
        self.assertEqual(block_to_blocktype(code), "code")
        self.assertEqual(block_to_blocktype(quote), "quote")
        self.assertEqual(block_to_blocktype(u_list), "unordered_list")
        self.assertEqual(block_to_blocktype(o_list), "ordered_list")
        self.assertEqual(block_to_blocktype(paragraph), "paragraph")
