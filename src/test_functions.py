import unittest
from functions import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link

from textnode import (
    TextNode, 
    text_type_text, 
    text_type_bold,
    text_type_image,
)

class TestFunctions(unittest.TestCase):

    def test_split_nodes_delimiter(self):
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
        
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        match = extract_markdown_images(text)
        self.assertEqual(match, [('image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'), ('another', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png')])
        
    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        match = extract_markdown_links(text)
        self.assertEqual(match, [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])
        
    def test_split_nodes_image(self):
        node = TextNode(
        "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", text_type_text)
        match = split_nodes_image([node])
        self.assertEqual(match, 
            [  TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), 
                TextNode("second image" , text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"), 
                TextNode("This is text with an ", text_type_text, None), 
                TextNode(" and another ", text_type_text, None),]
            )
        
    def test_split_nodes_image(self):
        node = TextNode("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)", text_type_text)
        match = split_nodes_link([node])
        print(match)
        
if __name__ == "__main__":
    unittest.main()
