import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    lines = [line.strip() for line in markdown.splitlines()]
    blocks = []
    if len(lines) == 1:
        return lines[0]
    for i in range(len(lines)):
        if not lines[i].strip():
            block_start = i+1
            continue
        if i==0:
            block_start = 0
        if i==len(lines):
            blocks.append(
                    "\n".join(lines[block_start:])
                    )
        if not lines[i+1].strip():
            block_end = i+1
            blocks.append(
                    "\n".join(lines[block_start:block_end])
                    )
            block_start = i+1

    return blocks

def block_to_block_type(markdown):
    lines = markdown.splitlines()
    if re.search(r"^#{1,6} ", markdown):
        return block_type_heading
    if re.search(r"^`{3}.*`{3}$", markdown, flags = re.DOTALL):
        return block_type_code
    quote_lines = re.findall(r"^> ", markdown, flags = re.MULTILINE)
    if len(re.findall(r"^> ", markdown, flags = re.MULTILINE)) == len(lines):
        return block_type_quote
    if len(re.findall(r"^[\*-] ", markdown, flags = re.MULTILINE)) == len(lines):
        return block_type_unordered_list
    numbered_lines = re.findall(r"^(\d)+\.\s+", markdown, flags = re.MULTILINE)
    expected_numbers = list(range(1, len(lines)+1))
    if len(re.findall(r"^(\d)+\.\s+", markdown, flags = re.MULTILINE)) == len(lines) and [int(number) for number in numbered_lines] == expected_numbers:
        return block_type_ordered_list
    else:
        return block_type_paragraph
