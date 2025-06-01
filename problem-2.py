import time
from optibook.synchronous_client import Exchange

# Step 1: Connect to the exchange
e = Exchange()
e.connect()

# Step 2: Select the same instrument used previously
tradable_instruments = e.get_tradable_instruments()
instrument_id = list(tradable_instruments.keys())[0]
print(f"Using instrument: {instrument_id}")

# Step 3: Wait a minute or two (shortened here for demo)
print("Waiting 60 seconds before selling...")
time.sleep(60)

# Step 4: Get current price book and sell at best bid
price_book = e.get_last_price_book(instrument_id)

if price_book and price_book.bids:
    best_bid_price = price_book.bids[0].price
    print(f"Selling at best bid price: {best_bid_price}")
else:
    best_bid_price = 1.0  # fallback
    print("No bid price available, using fallback.")

response = e.insert_order(
    instrument_id=instrument_id,
    price=best_bid_price,
    volume=10,
    side='ask',  # ask = sell
    order_type='ioc'  # immediate execution
)

print(f"Sell order response: {response}")

# Step 5: Check position again
positions = e.get_positions()
position = positions.get(instrument_id, 0)
print(f"Updated position in {instrument_id}: {position} lots")

# Optional: Insert a visible limit order for experimentation
print("\nInserting a visible limit order to watch in the visualizer...")
limit_order_price = best_bid_price + 5.0  # high price to avoid execution
limit_response = e.insert_order(
    instrument_id=instrument_id,
    price=limit_order_price,
    volume=5,
    side='ask',
    order_type='limit'
)

print(f"Limit order response: {limit_response}")
print("Now check the visualizer to see your order live in the book!")

# Reminder: Clean up orders if you're done experimenting
# e.delete_orders(instrument_id)
