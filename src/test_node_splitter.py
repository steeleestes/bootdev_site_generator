import unittest

from node_splitter import (
        split_nodes_delimiter, 
        split_nodes_link,
        split_nodes_image
    )

from textnode import (
        TextNode, 
        text_type_text, 
        text_type_code, 
        text_type_bold, 
        text_type_italic,
        text_type_img,
        text_type_link
    )

class TestNodeSplitter(unittest.TestCase):
    def test_single_code_block(self):
        base_node = TextNode("this is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([base_node], "`", text_type_code)
        self.assertEqual(
            new_nodes[0].text,
            "this is text with a "
        )
        self.assertEqual(
            new_nodes[1].text_type,
            text_type_code
        )


    def test_bold_md(self):
        node = TextNode(
                "This is text with a **bolded** word and **another**",
                text_type_text
            )
        test_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
                [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("bolded", text_type_bold),
                    TextNode(" word and ", text_type_text),
                    TextNode("another", text_type_bold),
                ],
                test_nodes
            )

    def test_italic_md(self):
        node = TextNode("This is text with an *italic* word.", text_type_text)
        test_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual([
                    TextNode("This is text with an ", text_type_text),
                    TextNode("italic", text_type_italic),
                    TextNode(" word.", text_type_text)
                ],
                test_nodes         
            )

    
    def test_multi_word_multi_marker(self):
        node = TextNode("**bold words** and *italic words.*", text_type_text)
        test_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        test_nodes = split_nodes_delimiter(test_nodes, "*", text_type_italic)
        self.assertListEqual(
                [
                    TextNode("bold words", text_type_bold),
                    TextNode(" and ", text_type_text),
                    TextNode("italic words.", text_type_italic)
                ],
                test_nodes
            )



    def test_split_nodes_link(self):
        node = TextNode(
                "This is a node with a [link](https://boot.dev)",
                text_type_text
            )
        test_nodes = split_nodes_link([node])
        self.assertListEqual(
                [
                    TextNode(
                        "This is a node with a ",
                        text_type_text
                    ),
                    TextNode(
                        "link",
                        text_type_link,
                        "https://boot.dev"
                    ),
                ],
                test_nodes
            )
                

    def test_split_nodes_links(self):
        node = TextNode(
                "these are [links](https://boot.dev) on [more links](https://youtube.com)",
                text_type_text
            )
        test_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(
                    "these are ",
                    text_type_text
                ),
                TextNode(
                    "links",
                    text_type_link,
                    "https://boot.dev"
                ),
                TextNode(
                    " on ",
                    text_type_text
                ),
                TextNode(
                    "more links",
                    text_type_link,
                    "https://youtube.com"
                )
            ],
            test_nodes
        )

    def test_split_nodes_link_only(self):
        node = TextNode(
            "[link only](https://boot.dev)",
            text_type_text
        )
        test_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(
                    "link only",
                    text_type_link,
                    "https://boot.dev"
                )
            ],
            test_nodes
        )

    def test_split_nodes_image(self):
        node = TextNode(
                "This is a node with an ![image](https://i.imgur.com/zjjcJKZ.png)",
                text_type_text
            )
        test_nodes = split_nodes_image([node])
        self.assertListEqual(
                [
                    TextNode(
                        "This is a node with an ", 
                        text_type_text
                    ),
                    TextNode(
                        "image", 
                        text_type_img, 
                        "https://i.imgur.com/zjjcJKZ.png"
                    )
                ],
                test_nodes
            )






















