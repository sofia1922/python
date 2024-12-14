import unittest
from reverse_words_package.reverse_words import reverse_text

class TestReverseWords(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(reverse_text("abcd efgh"), "dcba hgfe")

    def test_with_numbers(self):
        self.assertEqual(reverse_text("a1bcd efg!h"), "d1cba hgf!e")

    def test_empty(self):
        self.assertEqual(reverse_text(""), "")

    def test_only_letters(self):
        self.assertEqual(reverse_text("onlyletters"), "srettelylno")

    def test_mixed(self):
        self.assertEqual(reverse_text("word1 and2"), "drow1 dna2")

if __name__ == "__main__":
    unittest.main()
