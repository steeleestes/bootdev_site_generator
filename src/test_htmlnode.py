import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(
            "div", #tag
            "some text here", #value
            None, #children
            {"class": "greeting", "href": "https://something.place"} #props
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://something.place"',
            )
        

    def test_values(self):
        node = HTMLNode(
            "div", #tag
            "some text here", #value
            None, #chilren
            {"class": "greeting", "href": "https://something.place"} #props
        )
        self.assertEqual(
            node.tag,
            "div"
        )
        self.assertEqual(
            node.value,
            "some text here"
        )
        self.assertEqual(
            node.children,
            None
        )
        self.assertEqual(
            node.props,
            {"class": "greeting", "href": "https://something.place"}
        )
    def test_repr(self):
        node = HTMLNode(
                "div",
                "this is a value",
                None,
                None
        )
        self.assertEqual(
                node.__repr__(),
                "HTMLNode: TAG=div, VALUE=this is a value, CHILDREN=None, PROPS=None"
        )

    def test_leaf_no_children(self):
        node = LeafNode(
            "p", #tag
            "this is a paragraph", #value
        )
        self.assertEqual(
            node.to_html(),
            "<p>this is a paragraph</p>"
        )
        
    def test_leaf_no_tag(self):
        node = LeafNode(
            None,
            "no tag, still text"
        )
        self.assertEqual(
            node.to_html(),
            "no tag, still text"
        )

    def test_leaf_repr(self):
        node = LeafNode(
            "p", #tag
            "test with text", #value
        )
        self.assertEqual(
                node.__repr__(), 
                "LeafNode: TAG=p, VALUE=test with text, PROPS=None"
        )


    def test_parent_single_child(self):
        pass

if __name__ == "__main__":
    unittest.main()
