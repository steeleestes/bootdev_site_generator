
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        return f"HTMLNode, TAG={self.tag}, VALUE={self.value}, CHILDREN={self.children}, PROPS={self.props}"
    
    def to_html(self):
        raise NotImpementedError()

    def props_to_html(self):
        out_str = ""
        for prop in self.props:
            out_str += f" {prop}=\"{self.props[prop]}\""
        return out_str

    
