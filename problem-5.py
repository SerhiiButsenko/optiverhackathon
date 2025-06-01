from optibook.synchronous_client import Exchange

# Connect to the exchange
e = Exchange()
e.connect()

# Get all tradable instruments
instruments = e.get_tradable_instruments()

# Iterate over each instrument and print public trades
for instrument_id in instruments:
    print(f"\n🔍 Public Trades for Instrument: {instrument_id}")
    ticks = e.get_trade_tick_history(instrument_id)
    if not ticks:
        print("No public trades yet.")
    else:
        for tick in ticks:
            print(f"Timestamp={tick.timestamp}, Price={tick.price}, Volume={tick.volume}, Side={tick.side}")
