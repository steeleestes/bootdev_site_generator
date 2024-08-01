import unittest

from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code,
        text_type_image,
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


if __name__ == "__main__":
    unittest.main()
