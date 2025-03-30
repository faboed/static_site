import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_different_text(self):
        node1 = TextNode("Hello", TextType.BOLD)
        node2 = TextNode("Hi", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_type(self):
        node1 = TextNode("Hello", TextType.BOLD)
        node2 = TextNode("Hello", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_equal_url_none_vs_value(self):
        node1 = TextNode("Hello", TextType.LINK, url=None)
        node2 = TextNode("Hello", TextType.LINK, url="https://example.com")
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()