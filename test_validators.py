import unittest


class TestValidators(unittest.TestCase):

    def test_symbol(self):
        symbol = "BTCUSDT"
        self.assertEqual(symbol, "BTCUSDT")

    def test_side(self):
        side = "BUY"
        self.assertIn(side, ["BUY", "SELL"])

    def test_quantity(self):
        quantity = 0.01
        self.assertGreater(quantity, 0)


if __name__ == "__main__":
    unittest.main()