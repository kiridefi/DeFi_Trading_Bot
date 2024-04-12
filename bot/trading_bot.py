import time
from .strategies import MeanReversionStrategy

class TradingBot:
    def __init__(self, settings):
        self.settings = settings
        self.strategy = MeanReversionStrategy(settings)
        self.wallets = {}

    def add_wallet(self, currency, amount):
        self.wallets[currency] = amount

    def start(self):
        print("Starting trading bot...")
        while True:
            for pair in self.settings["trading_pairs"]:
                base_currency, quote_currency = pair.split("/")
                if base_currency in self.wallets and self.wallets[base_currency] > 0:
                    action = self.strategy.decide(pair, self.wallets[base_currency])
                    if action == "sell":
                        print(f"Selling {self.wallets[base_currency]} {base_currency}")
                        self.wallets[base_currency] = 0
                elif quote_currency in self.wallets and self.wallets[quote_currency] > 0:
                    action = self.strategy.decide(pair, self.wallets[quote_currency])
                    if action == "buy":
                        print(f"Buying {self.wallets[quote_currency]} {quote_currency}")
                        self.wallets[quote_currency] = 0
            time.sleep(60)
