import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("div", "Hello, world!", None, {"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(node.props_to_html(),' class="greeting" href="https://boot.dev"')
        
    def test_leaf(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(),'<p>This is a paragraph of text.</p>')
        
    def test_tag_none(self):
        node = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(node.to_html(),'This is a paragraph of text.')
        
    def test_leaf_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Click me!</a>')

    def test_parent_one_children(self):
        node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b></p>")
        
    def test_parent_many_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Hello World! "),
                LeafNode(None, "Hello World!"),
                LeafNode("i", "italic text"),
                
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div><b>Bold text</b>Hello World! Hello World!<i>italic text</i></div>"
        )
        

if __name__ == "__main__":
    unittest.main()
