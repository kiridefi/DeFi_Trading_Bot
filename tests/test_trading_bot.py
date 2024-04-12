import unittest
from bot.trading_bot import TradingBot
from config.settings import SETTINGS

class TestTradingBot(unittest.TestCase):
    def setUp(self):
        self.bot = TradingBot(SETTINGS)

    def test_add_wallet(self):
        self.bot.add_wallet("BTC", 1)
        self.assertEqual(self.bot.wallets["BTC"], 1)

    def test_start_stop(self):
        self.bot.start()
        self.assertEqual(self.bot.status, "running")
        self.bot.stop()
        self.assertEqual(self.bot.status, "stopped")

if __name__ == "__main__":
    unittest.main()
