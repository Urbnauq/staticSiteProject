import unittest

from textnode import (
    TextNode,
)

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
    def test_text_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
    def test_text_neq(self):
        node = TextNode("This is a text ", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
        
    def test_text_type_neq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)
        
    def test_url_is_not_none(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev/")
        self.assertIsNotNone(node.url)
        
if __name__ == "__main__":
    unittest.main()
