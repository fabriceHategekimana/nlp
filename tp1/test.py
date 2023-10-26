import unittest
from app import preprocess, get_word_set, get_neighbours


class Tp1Test(unittest.TestCase):

    def test_preprocess_punctuation(self):
        message = "Should remove the punctuation and Capital letters"
        self.assertEqual(preprocess("Jean-Marc"), ["jeanmarc"], message)

    def test_preprocess_3_words(self):
        message = "Should remove the punctuation and Capital letters"
        self.assertEqual(preprocess("One two three."), ["one", "two", "three"], message)

    def test_get_word_set_T(self):
        message = "Should find a simple list"
        self.assertEqual(get_word_set("T"), ["wood", "practice", "learning"], message)

    # def test_get_neighbours(self):
        # message =  "Should get a list of tuple"


if __name__ == '__main__':
    unittest.main()
