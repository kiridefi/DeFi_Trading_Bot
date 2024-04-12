import tkinter as tk
from bot.trading_bot import TradingBot
from config.settings import SETTINGS

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.bot = TradingBot(SETTINGS)
        self.title("Cryptocurrency Trading Bot")

        # Start bot button
        start_button = tk.Button(self, text="Start Bot", command=self.bot.start)
        start_button.pack()

        # Stop bot button
        stop_button = tk.Button(self, text="Stop Bot", command=self.bot.stop)
        stop_button.pack()

        # Add wallet label and entry field
        add_wallet_label = tk.Label(self, text="Add Wallet")
        add_wallet_label.pack()
        self.wallet_entry = tk.Entry(self)
        self.wallet_entry.pack()

        # Add wallet button
        add_wallet_button = tk.Button(self, text="Add Wallet", command=self.add_wallet)
        add_wallet_button.pack()

        # Wallets label
        self.wallets_label = tk.Label(self, text="")
        self.wallets_label.pack()

    def add_wallet(self):
        wallet = self.wallet_entry.get()
        if wallet:
            currency, amount = wallet.split()
            self.bot.add_wallet(currency, float(amount))
            self.wallets_label.config(text=f"Wallets: {self.bot.wallets}")

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()
