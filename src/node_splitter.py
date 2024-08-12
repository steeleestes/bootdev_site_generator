
from textnode import (
        TextNode, 
        text_type_text, 
        text_type_bold, 
        text_type_italic, 
        text_type_code,
        text_type_link,
        text_type_img
)

from extractors import (
        extract_markdown_links,
        extract_markdown_images
)




def split_nodes_delimiter(old_nodes, delimiter, text_type) -> list:
    out_L = list()
    for node in old_nodes:
        if node.text_type != text_type_text:
            out_L.append(node)
            continue
        temp = node.text.split(delimiter)
        if len(temp) % 2 == 0:
            raise Exception("Attempting to split invalid Markdown: un-paired delimiter.")
        for i in range(len(temp)):
            if temp[i] == "":
                continue
            if i % 2 == 0:
                out_L.append(TextNode(temp[i], text_type_text))
            else:
                out_L.append(TextNode(temp[i], text_type))
            
    return out_L

def split_nodes_image(old_nodes):
    out_L = list()
    for node in old_nodes:
        extracted_L = extract_markdown_images(node.text)
        if len(extracted_L) == 0:
            out_L.append(node)
            continue 
        working_text = node.text
        for i in extracted_L:
            temp = working_text.split(f"![{i[0]}]({i[1]})", 1)
            if len(temp) != 2: 
                raise Exception("Image Splitter Error: bad split section count")
            if temp[0] != "":
                out_L.append(TextNode(temp[0], text_type_text))
            working_text = temp[1]
            out_L.append(TextNode(
                    i[0],
                    text_type_img, 
                    i[1]
                )
            )
        if working_text != "":
            out_L.append(TextNode(working_text, text_type_text))
    return out_L

def split_nodes_link(old_nodes):
    out_L = list()
    for node in old_nodes:
        extracted_L = extract_markdown_links(node.text)
        if len(extracted_L) == 0:
            out_L.append(node)
            continue
        working_text = node.text
        for i in extracted_L:
            temp = working_text.split(f"[{i[0]}]({i[1]})", 1)
            if len(temp) != 2:
                raise Exception("Link Splitter Error: bad split section count")
            if temp[0] != "":
                out_L.append(TextNode(temp[0], text_type_text))
            working_text = temp[1]
            out_L.append(TextNode(
                    i[0],
                    text_type_link,
                    i[1]
                )
            )
        if working_text != "":
            out_L.append(TextNode(working_text, text_type_text))
    return out_L





#def main():
#    node = TextNode("this is text with a `code block` word", text_type_text)
#    new_nodes = split_nodes_delimiter([node], "`", text_type_code)
#    print(new_nodes)
#main()
