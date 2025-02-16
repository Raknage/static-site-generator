import unittest

from markdown_to_htmlnode import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_markdown_to_html_node(self):
        markdown = """# Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

> All that is *gold* does **not** glitter

## Reasons I like Tolkien

* You can spend years studying the legendarium and still not understand its depths
* It can be enjoyed by children and adults alike
* Disney *didn't ruin it*
* It created an entirely new genre of fantasy

## My favorite characters (in order)

1. Gandalf
2. Bilbo
3. Sam
4. Glorfindel
5. Galadriel
6. Elrond
7. Thorin
8. Sauron
9. Aragorn

Here's what `elflang` looks like (the perfect coding language):

```
func main(){
    fmt.Println("Hello, World!")
}
```"""
        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            '<div><h1>Tolkien Fan Club</h1><p><b>I like Tolkien</b>. Read my <a href="/majesty">first post here</a> (sorry the link doesn\'t work yet)</p><blockquote>All that is <i>gold</i> does <b>not</b> glitter</blockquote><h2>Reasons I like Tolkien</h2><ul><li>You can spend years studying the legendarium and still not understand its depths</li><li>It can be enjoyed by children and adults alike</li><li>Disney <i>didn\'t ruin it</i></li><li>It created an entirely new genre of fantasy</li></ul><h2>My favorite characters (in order)</h2><ol><li>Gandalf</li><li>Bilbo</li><li>Sam</li><li>Glorfindel</li><li>Galadriel</li><li>Elrond</li><li>Thorin</li><li>Sauron</li><li>Aragorn</li></ol><p>Here\'s what <code>elflang</code> looks like (the perfect coding language):</p><pre><code>func main(){\n    fmt.Println("Hello, World!")\n}</code></pre></div>',
        )

    def test_block_to_paragraph(self):
        markdown_p = "**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)"
        self.assertEqual(
            markdown_to_html_node(markdown_p).to_html(),
            '<div><p><b>I like Tolkien</b>. Read my <a href="/majesty">first post here</a> (sorry the link doesn\'t work yet)</p></div>',
        )

    def test_block_to_ordered_list(self):
        markdown_ol = "1. Gandalf\n2. Bilbo\n3. Sam\n4. Glorfindel\n5. Galadriel\n6. Elrond\n7. Thorin\n8. Sauron\n9. Aragorn\n"
        self.assertEqual(
            markdown_to_html_node(markdown_ol).to_html(),
            "<div><ol><li>Gandalf</li><li>Bilbo</li><li>Sam</li><li>Glorfindel</li><li>Galadriel</li><li>Elrond</li><li>Thorin</li><li>Sauron</li><li>Aragorn</li></ol></div>",
        )

    def test_block_to_unordered_list(self):
        markdown_ul = "* You can spend years studying the legendarium and still not understand its depths\n* It can be enjoyed by children and adults alike\n* Disney *didn't ruin it*\n* It created an entirely new genre of fantasy"
        self.assertEqual(
            markdown_to_html_node(markdown_ul).to_html(),
            "<div><ul><li>You can spend years studying the legendarium and still not understand its depths</li><li>It can be enjoyed by children and adults alike</li><li>Disney <i>didn't ruin it</i></li><li>It created an entirely new genre of fantasy</li></ul></div>",
        )

    def test_block_to_quote(self):
        markdown_quote = (
            "> All that is *gold* does **not** glitter\n> All That Glitters Is Not Gold"
        )

        self.assertEqual(
            markdown_to_html_node(markdown_quote).to_html(),
            "<div><blockquote>All that is <i>gold</i> does <b>not</b> glitter\nAll That Glitters Is Not Gold</blockquote></div>",
        )

    def test_block_to_heading(self):
        markdown_h = "# Tolkien **Fan** Club"
        self.assertEqual(
            markdown_to_html_node(markdown_h).to_html(),
            "<div><h1>Tolkien <b>Fan</b> Club</h1></div>",
        )

    def test_block_to_code(self):
        markdown = """```\nfunc main(){\n    fmt.Println("Hello, World!")\n}\n```"""
        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            '<div><pre><code>func main(){\n    fmt.Println("Hello, World!")\n}</code></pre></div>',
        )


if __name__ == "__main__":
    unittest.main()
