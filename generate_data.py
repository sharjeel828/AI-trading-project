import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import arrow
import jesse.helpers as jh
# Set env var for sqlite before imports if needed, though we already set it in .env
# But to be safe, we can set it here or rely on .env
# We need to make sure we are in the root of the project to load .env correctly?
# actually jesse imports load .env if we are in a jesse project.

from jesse.services.db import database
from jesse.models import Candle
import random

def generate_db_data(symbol="BTC-USDT", exchange="Binance Perpetual Futures", start_date="2023-01-01", end_date="2025-01-01"):
    print(f"Connecting to database and generating candle data for {exchange} {symbol}...")
    
    # Ensure config is loaded or DB connected
    database.open_connection()
    
    # Create table if not exists (should exist if migration ran, but good to ensure)
    if not Candle.table_exists():
        Candle.create_table()
    
    start = arrow.get(start_date)
    end = arrow.get(end_date)
    
    current = start
    price = 40000.0
    
    candles_batch = []
    total_candles = 0
    
    # 1 minute candles
    while current < end:
        timestamp = current.int_timestamp * 1000
        
        change = random.uniform(-0.001, 0.001)
        open_price = price
        close_price = price * (1 + change)
        high_price = max(open_price, close_price) * (1 + random.uniform(0, 0.0005))
        low_price = min(open_price, close_price) * (1 - random.uniform(0, 0.0005))
        volume = random.uniform(10, 500)
        
        candles_batch.append({
            'id': jh.generate_unique_id(),
            'exchange': exchange,
            'symbol': symbol,
            'timeframe': '1m',
            'timestamp': timestamp,
            'open': open_price,
            'close': close_price,
            'high': high_price,
            'low': low_price,
            'volume': volume
        })
        
        price = close_price
        current = current.shift(minutes=1)
        
        # Batch insert every 500 candles to avoid memory issues and SQLite variable limit
        if len(candles_batch) >= 500:
            Candle.insert_many(candles_batch).on_conflict_ignore().execute()
            total_candles += len(candles_batch)
            print(f"Inserted {total_candles} candles... (Current date: {current.format('YYYY-MM-DD')})")
            candles_batch = []

    # Insert remaining
    if candles_batch:
        Candle.insert_many(candles_batch).on_conflict_ignore().execute()
        total_candles += len(candles_batch)

    print(f"Successfully inserted {total_candles} candles into the database.")
    database.close_connection()

if __name__ == "__main__":
    generate_db_data()
