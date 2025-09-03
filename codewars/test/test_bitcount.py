import unittest
from bitcount import count_bit

class TestBits(unittest.TestCase):

    def test_bit_count(self):
        self.number = 1234
        self.assertEqual(5, count_bit(self.number))

if __name__ == "__main__":
    unittest.main()

    #10011010010
    #10011010010