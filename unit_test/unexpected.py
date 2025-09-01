import unittest
import math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b

class TestUnexpected(unittest.TestCase):
  def not_a_numb(self):
    with self.assertRaises(ZeroDivisionError):
      self.