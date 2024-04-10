from textnode import TextNode, text_type_text, text_type_image, text_type_link, text_type_bold, text_type_code, text_type_italic

import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        
        split_nodes = []
        splited = old_node.text.split(delimiter)
        
        if len(splited ) % 2 == 0:
            raise ValueError("Invalid markdown syntax")
        
        for i in range(len(splited)):
            if splited[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(splited[i], text_type_text))
            else:
                split_nodes.append(TextNode(splited[i], text_type))
        
        new_nodes.extend(split_nodes)
    
    return new_nodes

def extract_markdown_images(text):
    match = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return match

def extract_markdown_links(text):
    match = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return match

# def split_nodes_image(old_nodes):
#     new_nodes = []
    
#     for old_node in old_nodes:
#         if old_node.text_type != text_type_text:
#             new_nodes.append(old_node)
#             continue
        
#         old_node.text.split("!")
#         node_text_extract = extract_markdown_images(old_node.text)
        
#         if len(node_text_extract) == 0:
#             new_nodes.append(old_node)
#             continue
        
#         new_nodes.append(TextNode(node_text_extract[0][0], text_type_image, node_text_extract[0][1]))
#         new_nodes.append(TextNode(node_text_extract[1][0], text_type_image, node_text_extract[1][1]))
        
#         before = old_node.text.split(f"![{node_text_extract[0][0]}]({node_text_extract[0][1]})", 1)[0]
#         after = old_node.text.split(f"![{node_text_extract[1][0]}]({node_text_extract[1][1]})", 1)[0][-13:]
    
#         new_nodes.append(TextNode(before, text_type_text))
#         new_nodes.append(TextNode(after, text_type_text))
        
#     return new_nodes
        
        
# def split_nodes_link(old_nodes):
#     new_nodes = []
    
#     for old_node in old_nodes:
#         if old_node.text_type != text_type_text:
#             new_nodes.append(old_node)
#             continue
        
#         old_node.text.split()
#         node_text_extract = extract_markdown_links(old_node.text)
        
#         if len(node_text_extract) == 0:
#             new_nodes.append(old_node)
#             continue
        
#         new_nodes.append(TextNode(node_text_extract[0][0], text_type_link, node_text_extract[0][1]))
#         new_nodes.append(TextNode(node_text_extract[1][0], text_type_link, node_text_extract[1][1]))
        
#         before = old_node.text.split(f"[{node_text_extract[0][0]}]({node_text_extract[0][1]})", 1)[0]
#         after = old_node.text.split(f"[{node_text_extract[1][0]}]({node_text_extract[1][1]})", 1)[0][-5:]
    
#         new_nodes.append(TextNode(before, text_type_text))
#         new_nodes.append(TextNode(after, text_type_text))
        
#     return new_nodes

def text_to_textnode(text):
    nodes = [TextNode(text, text_type_text)]
    
    bold = "**"
    italic = "*"
    code = "`"
    
    nodes = split_nodes_delimiter(nodes, bold, text_type_bold)
    nodes = split_nodes_delimiter(nodes, italic, text_type_italic)
    nodes = split_nodes_delimiter(nodes, code, text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes

def markdown_to_blocks(markdown):
    splited = markdown.split('\n\n')
    
    blocks = []
    for split in splited:
        if split == "":
            continue
        blocks.append(split.strip())
    
    return blocks

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def block_to_block_type(block):
    if (block[:2] == "# "
        or block[:3] == "## "
        or block[:4] == "### "
        or block[:5] == "#### "
        or block[:6] == "##### "
        or block[:7] == "###### "):
        return block_type_heading
        
    if block[:3] == "```" and block[-3:] == "```" :
        return block_type_code
    
    if block[:1] == ">":
        
        block = block.split("\n")
        for line in block:
            if line[:1] != ">":
                return block_type_paragraph
        
        return block_type_quote

    if block[:1] == "*" or block[:1] == "-" :
        
        block = block.split("\n")
        for line in block:
            if line[:1] != "*" or line[:1] != "-":
                return block_type_paragraph
        
        return block_type_unordered_list
    
    if block[:2] == "1.":

        block = block.split("\n")
        num = 1
        for line in range(len(block)):
            if block[line][:2] != f"{num}.":
                return block_type_paragraph
            num += 1
        
        return block_type_ordered_list
    
    return block_type_paragraph
        
def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes
