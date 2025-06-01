from optibook.synchronous_client import Exchange

# Connect to exchange
e = Exchange()
e.connect()

# Instrument used earlier
instrument_id = list(e.get_tradable_instruments().keys())[0]
print(f"Using instrument: {instrument_id}")

# Step 1: Get trade history for this instrument
trades = e.get_trade_history(instrument_id)
print("\nTrade History:")
for trade in trades:
    print(trade)

# Step 2: Calculate manual PnL
buy_total = 0.0
buy_lots = 0
sell_total = 0.0
sell_lots = 0

for trade in trades:
    if trade.side == 'bid':  # you bought
        buy_total += trade.price * trade.volume
        buy_lots += trade.volume
    elif trade.side == 'ask':  # you sold
        sell_total += trade.price * trade.volume
        sell_lots += trade.volume

# Manual PnL calculation
manual_pnl = sell_total - buy_total

print(f"\nManual PnL Calculation:")
print(f"Bought {buy_lots} lots for total ${buy_total:.2f}")
print(f"Sold {sell_lots} lots for total ${sell_total:.2f}")
print(f"Manual PnL = ${manual_pnl:.2f}")

# Step 3: Verify with get_pnl()
api_pnl = e.get_pnl()
print(f"\nPnL from e.get_pnl() = ${api_pnl:.2f}")

# Optional sanity check
if abs(api_pnl - manual_pnl) < 0.01:
    print("✅ Manual PnL matches the API PnL!")
else:
    print("❌ Discrepancy between manual and API PnL!")
