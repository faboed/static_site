import unittest

from htmlnode import HTMLnode

class TestHTMLnode(unittest.TestCase):
    def test_eq(self):
        node = HTMLnode(tag="p", value="This is a paragraph", props={"class": "text"})
        node2 = HTMLnode(tag="p", value="This is a paragraph", props={"class": "text"})
        self.assertEqual(node, node2)

    def test_not_equal_different_value(self):
        node1 = HTMLnode(tag="p", value="Hello", props={"class": "text"})
        node2 = HTMLnode(tag="p", value="Hi", props={"class": "text"})
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_tag(self):
        node1 = HTMLnode(tag="p", value="Hello", props={"class": "text"})
        node2 = HTMLnode(tag="div", value="Hello", props={"class": "text"})
        self.assertNotEqual(node1, node2)

    def test_not_equal_props_none_vs_value(self):
        node1 = HTMLnode(tag="a", value="Link", props=None)
        node2 = HTMLnode(tag="a", value="Link", props={"href": "https://example.com"})
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()