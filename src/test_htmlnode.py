import unittest

from htmlnode import HTMLNode

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
                "HTMLNode, TAG=div, VALUE=this is a value, CHILDREN=None, PROPS=None"
        )
        
if __name__ == "__main__":
    unittest.main()
