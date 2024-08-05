from htmlnode import LeafNode
from enum import Enum

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_img = "img"

NodeType = Enum(
        'NodeType',
        [
            text_type_text, 
            text_type_bold,
            text_type_italic,
            text_type_code,
            text_type_link,
            text_type_img
        ]
    )

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text and self.text_type == other.text_type and self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case NodeType.text.name:
            return LeafNode(None, text_node.text)
        case NodeType.bold.name:
            return LeafNode("b", text_node.text)
        case NodeType.italic.name:
            return LeafNode("i", text_node.text)
        case NodeType.code.name:
            return LeafNode("code", text_node.text)
        case NodeType.link.name:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case NodeType.img.name:
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("bad type / type mismatch in func: text_node_to_html_node")

