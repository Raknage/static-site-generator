import re


def markdown_to_blocks(markdown):
    blocks = [block.strip() for block in markdown.split("\n\n")]
    return [x for x in blocks if x]


def block_to_blocktype(block):
    if re.fullmatch(r"^#{1,6} .{1,}", block):
        return "heading"
    elif re.fullmatch(r"^`{3}.*`{3}$", block, re.DOTALL):
        return "code"
    elif re.fullmatch(r"^>.*(?:\n>.*|)*$", block, re.MULTILINE):
        return "quote"
    elif re.fullmatch(r"^(\*|\+|-) \S+.*(?:\n(\*|\+|-) \S+.*)*$", block, re.MULTILINE):
        return "unordered_list"
    elif re.fullmatch(r"^\d+\. .+\n?(\d+\. .+\n?)*$", block, re.MULTILINE):
        return "ordered_list"
    else:
        return "paragraph"
