from optibook.synchronous_client import Exchange

# Step 1: Connect to the exchange
e = Exchange()
e.connect()

# Step 2: Pick an instrument (we'll choose the first one from tradable instruments)
tradable_instruments = e.get_tradable_instruments()
instrument_id = list(tradable_instruments.keys())[0]  # pick first available instrument
print(f"Selected instrument: {instrument_id}")

# Step 3: Get the current price book for the instrument
price_book = e.get_last_price_book(instrument_id)
print(f"Price book: {price_book}")

# Step 4: Buy 10 lots using the current best ask price
# If there's an ask price, we buy at that. Otherwise, set a high dummy price.
if price_book and price_book.asks:
    best_ask_price = price_book.asks[0].price
    print(f"Best ask price: {best_ask_price}")
else:
    best_ask_price = 10000.0  # fallback in case no ask exists
    print("No ask price available, using fallback price.")

response = e.insert_order(
    instrument_id=instrument_id,
    price=best_ask_price,
    volume=10,
    side='bid',  # bid = buy
    order_type='ioc'  # immediate or cancel to execute immediately
)

print(f"Insert order response: {response}")

# Step 5: Check and print the updated position
positions = e.get_positions()
position = positions.get(instrument_id, 0)
print(f"Position in {instrument_id}: {position} lots")
