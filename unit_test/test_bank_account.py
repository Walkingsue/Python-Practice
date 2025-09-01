import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(100)

    def tearDown(self):
        self.account = BankAccount(None)

    def test_is_balance_100(self):
        self.assertEqual(self.account.balance, 100)

    def test_deposit_positive_amount(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

if __name__ == "__main__":
    unittest.main()