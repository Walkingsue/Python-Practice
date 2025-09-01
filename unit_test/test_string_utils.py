import unittest
import test_addition

class TestStringUtils(unittest.TestCase):

    words = ['PERRO', 'gato', 'pajaro']

    cap_word = test_addition.is_capitalized(words)
    cap_letter = test_addition.capitalize_string(words[1])
    is_reverse = test_addition.reverse_string(words[1])


    def test_is_capitalize(self):
        result = True
        self.assertTrue(result, self.cap_word)

    def test_capitalize_string(self):
        result = 'Gato'
        self.assertEqual(result, self.cap_letter)

    def test_reverse_word(self):
        result = 'otag'
        self.assertTrue(result, self.is_reverse)

if __name__ == '__main__':
    unittest.main()