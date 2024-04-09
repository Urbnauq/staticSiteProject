import unittest

from textnode import (
    TextNode, 
    split_nodes_delimiter,
    text_type_text,
    text_type_bold
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
    
    def test_url_is_not_none(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )
        
if __name__ == "__main__":
    unittest.main()
