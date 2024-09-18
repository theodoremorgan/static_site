import unittest
from block_markdown import (
        markdown_to_blocks,
        block_to_block_type,
        block_type_paragraph,
        block_type_heading,
        block_type_code,
        block_type_quote,
        block_type_unordered_list,
        block_type_ordered_list,
        )

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = "\n# This is a heading\n\n             This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item     \n* This is another list item\n\nand another line \n\n\n\n\n\n"
        actual_blocks = markdown_to_blocks(text)
        expected_block = [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
                "and another line"
                ]
        self.assertEqual(actual_blocks, expected_block)

    def test_block_to_block_type_heading_success(self):
        text = "#### this is a heading"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_heading)

    def test_block_to_block_type_heading_no_hash(self):
        text = "this is not a heading"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_paragraph)

    def test_block_to_block_type_heading_seven_hash(self):
        text = "######## this is not a paragraph"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_paragraph)

    def test_block_to_block_type_code_success(self):
        text = "```This is some code```"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_code)

    def test_block_to_block_type_code_multiline_success(self):
        text = "```This is some\nmultiline code```"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_code)

    def test_block_to_block_type_code_two_backtick(self):
        text = "``This is not code ```"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_paragraph)

    def test_block_to_block_type_quote_success_singleline(self):
        text = "> This is the first quote"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_quote)

    def test_block_to_block_type_quote_fail_singleline(self):
        text = ">This is the first quote"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_paragraph)

    def test_block_to_block_type_quote_success_multiline(self):
        text = "> This is the first quote \n> This is another quote\n> This it the last quote"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_quote)

    def test_block_to_block_type_quote_fail_multiline(self):
        text = "> This is the first quote \nThis is another quote\n This is the last quote"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_paragraph)

    def test_block_to_block_type_ordered_list_success(self):
        text = "1. first element!\n2. second element!  \n3. third element"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_ordered_list)

    def test_block_to_block_type_ordered_list_fail_non_sequence(self):
        text = "1. first element!\n1. second element"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_paragraph)

    def test_block_to_block_type_ordered_list_fail_missing_numbers(self):
        text = "1. first element\n second element"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_paragraph)


    def test_block_to_block_type_unordered_list_success_singleline_star(self):
        text = "* This is the first list item"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_unordered_list)

    def test_block_to_block_type_unordered_list_success_singleline_line(self):
        text = "- This is the first list item"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_unordered_list)
    
    def test_block_to_block_type_unordered_fail_singleline_missing_space(self):
        text = "*This is the first quote"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_paragraph)

    def test_block_to_block_type_unordered_list_success_multiline(self):
        text = "* This is the first quote \n- This is another quote\n- This it the last quote"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_unordered_list)

    def test_block_to_block_type_unordered_list_fail_multiline(self):
        text = "* This is the first quote \nThis is another quote\n This is the last quote"
        result = block_to_block_type(text)
        self.assertEqual(result, block_type_paragraph)

if __name__ == "__main__":
    unittest.main()
