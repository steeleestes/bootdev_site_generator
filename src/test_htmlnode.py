import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode

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


    def test_tohtml_one_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
                parent_node.to_html(), 
                "<div><span>child</span></div>"
        )

    def test_tohtml_grandchild(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
                parent_node.to_html(), 
                "<div><span><b>grandchild</b></span></div>"
        )

    def test_tohtml_many_children(self):
        child1 = LeafNode("p", "child1")
        child2 = LeafNode("span", "child2 span")
        child3 = LeafNode(None, "no tag text")
        parent = ParentNode("div", [child1, child2, child3])
        self.assertEqual(
                parent.to_html(),
                "<div><p>child1</p><span>child2 span</span>no tag text</div>"
        )

if __name__ == "__main__":
    unittest.main()
