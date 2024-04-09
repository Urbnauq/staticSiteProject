from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text # The text content of the node
        self.text_type = text_type # The type of text this node contains, which is just a string like "bold" or "italic"
        self.url = url # The URL of the link or image, if the text is a link. Default to None is nothing is passed in.
        
    def __eq__(self, other):
        return (self.text == other.text
                and self.text_type == other.text_type
                and self.url == self.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")
            