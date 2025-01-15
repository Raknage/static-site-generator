from textnode import TextNode
from textnode import TextType


def main():
    txtnode = TextNode("This is a textnode", TextType.BOLD, "www.raknage.com")
    print(txtnode)


main()
