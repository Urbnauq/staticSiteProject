import unittest
from functions import (
    split_nodes_delimiter, 
    extract_markdown_images, 
    extract_markdown_links, 
    split_nodes_image, 
    split_nodes_link, 
    text_to_textnode,
    markdown_to_blocks,
    block_to_block_type
)

from textnode import (
    TextNode, 
    text_type_text, 
    text_type_bold,
    text_type_image,
    text_type_link,
    text_type_code, 
    text_type_italic,

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
        #print(match)
        # self.assertEqual(match, 
        #     [  TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), 
        #         TextNode("second image" , text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"), 
        #         TextNode("This is text with an ", text_type_text, None), 
        #         TextNode(" and another ", text_type_text, None),]
        #     )
        
    def test_split_nodes_link(self):
        node = TextNode("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)", text_type_text)
        match = split_nodes_link([node])
        #print(match)
        
    def test_text_to_textnode(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        match = text_to_textnode(text)
        self.assertEqual(match, 
        
        [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        )
        
    def test_markdown_to_blocks(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(markdown)
        #print(blocks)
        self.assertEqual(blocks, ['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', '* This is a list\n* with items'])
        
    def test_block_to_block_paragraph(self):
        block = 'This is a test'

        output = block_to_block_type(block)
        #print(output)
        #self.assertEqual(output, [])

    def test_block_to_block_heading(self):
        block = '### This is a test'

        output = block_to_block_type(block)
        #print(output)
        #self.assertEqual(output, [])
        
    def test_block_to_block_code(self):
        block = '```This is a test```'

        output = block_to_block_type(block)
        #print(output)
        #self.assertEqual(output, [])
        
    def test_block_to_block_quote(self):
        block = '> This is a list/nf testing'

        output = block_to_block_type(block)
        #print(output)
        #self.assertEqual(output, [])
        
    def test_block_to_block_unordered_list(self):
        block = '* This is a list/n- testing'

        output = block_to_block_type(block)
        #print(output)
        #self.assertEqual(output, [])
        
    def test_block_to_block_ordered_list(self):
        block = '1. This is a list/n2. testing'

        output = block_to_block_type(block)
        #print(output)
        #self.assertEqual(output, [])     
    
            
if __name__ == "__main__":
    unittest.main()
