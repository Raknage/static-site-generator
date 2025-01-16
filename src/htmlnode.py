class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props:
            new_props = ""
            for i in self.props:
                new_props += f' {i}="{self.props[i]}"'
            return new_props
        return ""

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode needs a tag")
        if not self.children:
            raise ValueError("ParentNode needs children")

        # TODO: This should be recursive method:
        child_nodes_str = ""
        for node in self.children:
            child_nodes_str += node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{child_nodes_str}</{self.tag}>"
