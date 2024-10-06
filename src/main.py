import os

BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET')
LUNARCRUSH_API_KEY = os.getenv('LUNARCRUSH_API_KEY')
GITHUB_API_KEY = os.getenv('GITHUB_API_KEY')

# Beispiel für die Nutzung der API-Schlüssel
print(f"Binance API Key: {BINANCE_API_KEY}")
print(f"LunarCrush API Key: {LUNARCRUSH_API_KEY}")
