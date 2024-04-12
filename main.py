from bot.trading_bot import TradingBot
from config.settings import SETTINGS

def main():
    # Initialize the bot with the settings from settings.py
    bot = TradingBot(SETTINGS)

    # Start the bot
    bot.start()

if __name__ == "__main__":
    main()
