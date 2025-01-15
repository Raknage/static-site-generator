from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode


def main():
    txtnode = TextNode("This is a textnode", TextType.BOLD, "www.raknage.com")
    html_node = HTMLNode("h1", "Text", [], {"href": "www.raknage.com"})
    print(txtnode)
    print(html_node)


main()
