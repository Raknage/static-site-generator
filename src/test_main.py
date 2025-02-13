import unittest

from main import extract_title


class Test_extract_title(unittest.TestCase):
    def test_extract_title(self):
        markdown = """#   This is a heading  

This is a paragraph of text. It has some **bold** and *italic* words inside of it.         

## this is heading too

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        self.assertEqual(extract_title(markdown), "This is a heading")
        with self.assertRaises(
            ValueError,
        ):
            extract_title("## this is not an h1 heading\n # h1 not at the start")


if __name__ == "__main__":
    unittest.main()
