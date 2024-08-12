import unittest

from extractors import extract_markdown_images, extract_markdown_links

class ExtractorTests(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
                "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
            )
        self.assertListEqual(
                [("rick roll", "https://i.imgur.com/aKaOqIh.gif")],
                matches
            )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://youtube.com)"
            )
        self.assertListEqual(
                [
                    ("to boot dev", "https://www.boot.dev"),
                    ("to youtube", "https://youtube.com")
                ],
                matches
            )


if __name__ == "__main__":
    unittest.main()        
