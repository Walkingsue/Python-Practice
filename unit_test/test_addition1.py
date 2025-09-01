import unittest
import math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b

class TestUnexpected(unittest.TestCase):
  
  def test_not_a_positive_numb(self):
    with self.assertRaises(ValueError):
      self.assertEqual(12, get_sqrt(-144))

  def test_not_divide_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
      self.assertEqual(12, divide(144, 0))


if __name__ == "__main__":
  unittest.main()