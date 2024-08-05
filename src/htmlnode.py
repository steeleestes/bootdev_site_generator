
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        return f"HTMLNode: TAG={self.tag}, VALUE={self.value}, CHILDREN={self.children}, PROPS={self.props}"
    
    def to_html(self):
        raise NotImpementedError()

    def props_to_html(self):
        if self.props == None:
            return ""
        out_str = ""
        for prop in self.props:
            out_str += f" {prop}=\"{self.props[prop]}\""
        return out_str
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"ParentNode: TAG={self.tag}, CHILDREN={self.children}, PROPS={self.props}"

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node must include a tag.")
        if self.children == None:
            raise ValueError("Parent node must have children.")
        out_s = ""
        for c in self.children:
            out_s += c.to_html()
        return f"<{self.tag}{self.props_to_html()}>{out_s}</{self.tag}>"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode: TAG={self.tag}, VALUE={self.value}, PROPS={self.props}"

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf nodes require a value.")
        if self.tag == None:
            return self.value
        #if self.props == None:
        #    return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

       
