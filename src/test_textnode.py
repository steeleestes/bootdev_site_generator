
import unittest

from textnode import (
        TextNode,
        text_node_to_html_node,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code,
        text_type_img,
        text_type_link
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a text node", "bold")
        node2 = TextNode("this is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        # testing input text type mismatch
        node = TextNode("this is a text node", text_type_bold)
        node2 = TextNode("this is a text node", text_type_italic)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        # testing input text mismatch
        node = TextNode("this is a text node", "bold")
        node2 = TextNode("this is text node", "bold")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        #testing url matching
        node = TextNode("this is a text node", "bold", "url7")
        node2 = TextNode("this is a text node", "bold", "url7")
        self.assertEqual(node, node2)

    def testing_eq_url_false(self):
        # url mismatch
        node = TextNode("this is a text node", "bold", "url7")
        node2 = TextNode("this is a text node", "bold", "url8")
        self.assertNotEqual(node, node2)

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_node(self):
        node = TextNode("this is some text", text_type_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "this is some text")

    def test_image_node(self):
        node = TextNode("this is img alt", text_type_img, "img.url.place")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(
                html_node.props,
                {"src":"img.url.place", "alt":"this is img alt"}
        )

    def test_emph_node(self):
        node = TextNode("this is important", text_type_italic)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "this is important")


if __name__ == "__main__":
    unittest.main()









