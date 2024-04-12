import unittest
from bot.strategies import MeanReversionStrategy

class TestMeanReversionStrategy(unittest.TestCase):
    def setUp(self):
        self.strategy = MeanReversionStrategy(SETTINGS)

    def test_decide(self):
        decision = self.strategy.decide("BTC/USD", 1)
        self.assertIn(decision, ["buy", "sell"])

if __name__ == "__main__":
    unittest.main()
